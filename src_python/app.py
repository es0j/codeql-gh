from flask import Flask
from database import init_db
from sqli_routes import sqli_bp
from xss_routes import xss_bp
from rce_routes import rce_bp

app = Flask(__name__)

# Initialize database
init_db()

# Register blueprints
app.register_blueprint(sqli_bp)
app.register_blueprint(xss_bp)
app.register_blueprint(rce_bp)

@app.route('/')
def index():
    return '''
    <h1>Vulnerable Flask App - SAST Benchmark</h1>
    <ul>
        <li><a href="/sqli">SQL Injection Test</a></li>
        <li><a href="/xss">XSS Test</a></li>
        <li><a href="/rce">RCE Test</a></li>
    </ul>
    '''

if __name__ == '__main__':
    # VULNERABLE: Debug mode in production, all interfaces
    app.run(debug=True, host='0.0.0.0', port=5000)
