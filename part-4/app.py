"""
Part 4: Dynamic Routes - URL Parameters
========================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Try different URLs like /user/YourName or /post/123
"""

from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user/<username>')  # <username> captures any text from URL, visit: /user/Alice, /user/Bob
def user_profile(username):
    return render_template('user.html', username=username)


@app.route('/post/<int:post_id>')  # <int:post_id> captures only integers, /post/abc returns 404
def show_post(post_id):
    posts = {  # Simulated post data (in real apps, this comes from a database)
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }
    post = posts.get(post_id)  # Get the post or None if not found
    return render_template('post.html', post_id=post_id, post=post)


@app.route('/user/<username>/post/<int:post_id>')  # Multiple dynamic segments, visit: /user/Alice/post/1
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)


@app.route('/about/')  # Trailing slash means both /about and /about/ work
def about():
    return render_template('about.html')


@app.route('/links')  # Demonstrates url_for() - generates URLs dynamically (better than hardcoding!)
def show_links():
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
    }
    return render_template('links.html', links=links)

@app.route('/product/<int:product_id>')
def product_page(product_id):
    products = {
        1: {'name': 'Laptop', 'price': 999.99},
        2: {'name': 'Smartphone', 'price': 499.99},
        3: {'name': 'Tablet', 'price': 299.99},
    }
    product = products.get(product_id)
    return render_template('product.html', product_id=product_id, product=product)

@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):

    # Step 1: Data structure (Category → Products)
    data = {
    'electronics': {
        1: {'name': 'Mouse', 'price': 500},
        2: {'name': 'Keyboard', 'price': 1200},
        3: {'name': 'Headphones', 'price': 1800}
    },

    'books': {
        1: {'name': 'Python Basics', 'price': 350},
        2: {'name': 'Flask Guide', 'price': 450},
        3: {'name': 'Data Structures', 'price': 600}
    },

    'cosmetics': {
        1: {'name': 'Face Wash', 'price': 250},
        2: {'name': 'Lipstick', 'price': 499},
        3: {'name': 'Perfume', 'price': 1200}
    },

    'music': {
        1: {'name': 'Guitar', 'price': 3500},
        2: {'name': 'Keyboard Piano', 'price': 5200},
        3: {'name': 'Headphones', 'price': 2000}
    },

    'clothes': {
        1: {'name': 'T-Shirt', 'price': 699},
        2: {'name': 'Jeans', 'price': 1499},
        3: {'name': 'Jacket', 'price': 2999}
    },

    'cleaning': {
        1: {'name': 'Floor Cleaner', 'price': 299},
        2: {'name': 'Dish Wash', 'price': 199},
        3: {'name': 'Detergent', 'price': 399}
    }
}
    # Step 2: Check if category exists
    category = data.get(category_name)

    # Step 3: If category exists, check product
    if category:
        product = category.get(product_id)
    else:
        product = None

    # Step 4: Send everything to template
    return render_template(
        'product_category.html',
        category_name=category_name,
        product=product,
        product_id=product_id
    )

products = [
    {'id': 1, 'name': 'Mouse', 'category': 'electronics', 'price': 500},
    {'id': 2, 'name': 'Keyboard', 'category': 'electronics', 'price': 1200},
    {'id': 3, 'name': 'Python Basics Book', 'category': 'books', 'price': 350},
    {'id': 4, 'name': 'Flask Guide Book', 'category': 'books', 'price': 450},
    {'id': 5, 'name': 'T-Shirt', 'category': 'clothes', 'price': 800},
]

@app.route('/search')
def search():
    query = request.args.get('q')

    results = []

    if query:   # 🔑 MOST IMPORTANT LINE
        for product in products:
            if query.lower() in product['name'].lower():
                results.append(product)

    return render_template('search.html', query=query, results=results)



if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# URL PARAMETER TYPES:
# =============================================================================
#
# <variable>         - String (default), accepts any text without slashes
# <int:variable>     - Integer, accepts only positive integers
# <float:variable>   - Float, accepts floating point numbers
# <path:variable>    - String, but also accepts slashes
# <uuid:variable>    - UUID strings
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 4.1: Create a product page
#   - Add route /product/<int:product_id>
#   - Create a products dictionary with id, name, price
#   - Display product details or "Not Found" message
#
# Exercise 4.2: Category and product route
#   - Add route /category/<category_name>/product/<int:product_id>
#   - Display both the category and product information
#
# Exercise 4.3: Search route
#   - Add route /search/<query>
#   - Display "Search results for: [query]"
#   - Bonus: Add a simple search form that redirects to this route
#
# =============================================================================
