from flask import Blueprint, request
import subprocess
import pickle
import base64

rce_bp = Blueprint('rce', __name__)

@rce_bp.route('/rce')
def rce_page():
    return '''
    <h2>Remote Code Execution (RCE) Vulnerability</h2>
    <form action="/ping" method="GET">
        <input type="text" name="host" placeholder="Host to ping">
        <button type="submit">Ping</button>
    </form>
    <p>Try: 127.0.0.1; ls -la</p>
    <hr>
    <form action="/eval" method="GET">
        <input type="text" name="code" placeholder="Python code">
        <button type="submit">Execute</button>
    </form>
    <p>Try: __import__('os').system('whoami')</p>
    <hr>
    <a href="/file?name=app.py">File Read Test</a> | 
    <a href="/deserialize">Deserialize Test</a>
    '''

@rce_bp.route('/ping')
def ping():
    host = request.args.get('host', '127.0.0.1')
    
    # VULNERABLE: Command injection via shell=True
    try:
        result = subprocess.check_output(f'ping -c 4 {host}', shell=True, stderr=subprocess.STDOUT, timeout=5)
        return f'<h3>Ping Results:</h3><pre>{result.decode()}</pre><a href="/rce">Back</a>'
    except subprocess.TimeoutExpired:
        return '<h3>Timeout</h3><a href="/rce">Back</a>'
    except Exception as e:
        return f'<h3>Error:</h3><pre>{str(e)}</pre><a href="/rce">Back</a>'

@rce_bp.route('/eval')
def eval_code():
    code = request.args.get('code', '')
    
    # VULNERABLE: eval() with user input
    try:
        result = eval(code)
        return f'<h3>Result:</h3><pre>{result}</pre><a href="/rce">Back</a>'
    except Exception as e:
        return f'<h3>Error:</h3><pre>{str(e)}</pre><a href="/rce">Back</a>'

@rce_bp.route('/file')
def read_file():
    filename = request.args.get('name', 'default.txt')
    
    # VULNERABLE: Path traversal
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return f'<h3>File Content:</h3><pre>{content}</pre>'
    except Exception as e:
        return f'<h3>Error:</h3><pre>{str(e)}</pre>'

@rce_bp.route('/deserialize')
def deserialize():
    data = request.args.get('data', '')
    
    if data:
        try:
            # VULNERABLE: Deserializing untrusted data
            decoded = base64.b64decode(data)
            obj = pickle.loads(decoded)
            return f'<h3>Deserialized:</h3><pre>{obj}</pre>'
        except Exception as e:
            return f'<h3>Error:</h3><pre>{str(e)}</pre>'
    
    return '<h3>Provide data parameter with base64 encoded pickle</h3>'
