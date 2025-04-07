from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

feedback_data = []

coffee_menu = [
    {
        'id': 1,
        'name': 'Coffee Latte',
        'description': 'Smooth espresso with steamed milk and light foam.',
        'image': '/static/images/latte.jpg'
    },
    {
        'id': 2,
        'name': 'Irish Coffee',
        'description': 'A bold mix of coffee, Irish whiskey, sugar, and cream.',
        'image': '/static/images/irish.jpg'
    },
    {
        'id': 3,
        'name': 'Dark Mocha',
        'description': 'Rich espresso with dark chocolate and steamed milk.',
        'image': '/static/images/mocha.jpg'
    },
    {
        'id': 4,
        'name': 'Caramel Frappuccino',
        'description': 'Blended ice, espresso, caramel syrup, and whipped cream.',
        'image': '/static/images/frappuccino.jpg'
    },
    {
        'id': 5,
        'name': 'Affogato',
        'description': 'Vanilla ice cream drowned in a shot of hot espresso.',
        'image': '/static/images/affogato.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', coffees=coffee_menu)

@app.route('/feedback', methods=['POST'])
def feedback():
    coffee_id = int(request.form['coffee_id'])
    coffee_name = next((c['name'] for c in coffee_menu if c['id'] == coffee_id), 'Unknown')
    rating = request.form['rating']
    comment = request.form['comment']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')

    feedback_data.append({
        'coffee_name': coffee_name,
        'rating': rating,
        'comment': comment,
        'timestamp': timestamp
    })

    return redirect(url_for('menu'))

@app.route('/view-feedback')
def view_feedback():
    return render_template('feedback.html', feedback=feedback_data)

if __name__ == '__main__':
    app.run(debug=True)