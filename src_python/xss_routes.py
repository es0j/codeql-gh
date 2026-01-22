from flask import Blueprint, request, render_template_string

xss_bp = Blueprint('xss', __name__)

@xss_bp.route('/xss')
def xss_page():
    return '''
    <h2>Cross-Site Scripting (XSS) Vulnerability</h2>
    <form action="/search" method="GET">
        <input type="text" name="q" placeholder="Search query">
        <button type="submit">Search</button>
    </form>
    <p>Try: &lt;script&gt;alert('XSS')&lt;/script&gt;</p>
    <br>
    <a href="/comment">Leave a comment</a>
    '''

@xss_bp.route('/search')
def search():
    query = request.args.get('q', '')
    
    # VULNERABLE: Directly rendering user input without escaping
    return f'''
    <h2>Search Results</h2>
    <p>You searched for: {query}</p>
    <p>No results found for your query.</p>
    <a href="/xss">Back to search</a>
    '''

@xss_bp.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        comment_text = request.form.get('comment', '')
        # VULNERABLE: Reflected XSS
        return render_template_string(f'''
        <h2>Your Comment</h2>
        <div>{comment_text}</div>
        <a href="/xss">Back</a>
        ''')
    
    return '''
    <h2>Leave a Comment</h2>
    <form method="POST">
        <textarea name="comment" placeholder="Enter your comment"></textarea>
        <button type="submit">Submit</button>
    </form>
    '''
