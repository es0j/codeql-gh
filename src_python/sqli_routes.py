from flask import Blueprint, request
import sqlite3

sqli_bp = Blueprint('sqli', __name__)

@sqli_bp.route('/sqli')
def sqli_page():
    return '''
    <h2>SQL Injection Vulnerability</h2>
    <form action="/login" method="GET">
        <input type="text" name="username" placeholder="Username">
        <input type="text" name="password" placeholder="Password">
        <button type="submit">Login</button>
    </form>
    <p>Try: username=' OR '1'='1 </p>
    '''

@sqli_bp.route('/login')
def login():
    username = request.args.get('username', '')
    password = request.args.get('password', '')
    
    # VULNERABLE: Direct string concatenation in SQL query
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        
        if result:
            return f"<h3>Login Successful!</h3><p>User data: {result}</p>"
        else:
            return "<h3>Login Failed</h3><p>Invalid credentials</p>"
    except Exception as e:
        return f"<h3>Error:</h3><p>{str(e)}</p>"
