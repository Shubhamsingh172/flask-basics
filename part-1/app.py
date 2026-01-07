"""
Part 1: Hello Flask - Your First Web Server
============================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask  # Import Flask class from the flask package

app = Flask(__name__)  # Create Flask app instance, __name__ tells Flask where to look for templates/static files


@app.route('/')  # Decorator that maps URL '/' (home page) to this function
def home():
    return "Hello Flask! Welcome to my first web server!"  # This text displays in the browser

@app.route('/bold')  # Decorator that maps URL '/' (home page) to this function
def bold():
    return "<h1>Flask! Welcome to my first web server!</h1>"  # This text displays in the browser

@app.route('/about')  # Decorator that maps URL '/' (home page) to this function
def about():
    return "Hello Guys My name is Shubham Singh! Welcome to my first web server!"  # This text displays in the browser


if __name__ == '__main__':
    app.run(debug=True, port= 8000)  # debug=True enables auto-reload and detailed error messages


# =============================================================================
# EXERCISES - Try these after running the basic app:
# =============================================================================
#
# Exercise 1.1: Change the return message
#   - Modify the return statement to say "Hello [Your Name]!"
#   - Save the file and refresh your browser (server auto-reloads!)
#
# Exercise 1.2: Return HTML instead of plain text
#   - Change the return to: return "<h1>Hello Flask!</h1><p>This is HTML</p>"
#   - Notice how the browser renders it as formatted HTML
#
# Exercise 1.3: Add a second route
#   - Add another function with @app.route('/about')
#   - Return something like "This is the about page"
#   - Visit http://localhost:5000/about in your browser
#
# =============================================================================
