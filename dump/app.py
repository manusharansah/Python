from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
from models import load_transactions, save_transactions
import csv, os
from io import StringIO

app = Flask(__name__)
app.secret_key = 'supersecretkey'

USER_DIR = 'users'
os.makedirs(USER_DIR, exist_ok=True)

def user_file(username):
    return os.path.join(USER_DIR, f'{username}_transactions.json')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_path = os.path.join(USER_DIR, f'{username}_auth.json')
        if os.path.exists(user_path):
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        import json
        with open(user_path, 'w') as f:
            json.dump({'username': username, 'password': password}, f)
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        import json
        user_path = os.path.join(USER_DIR, f'{username}_auth.json')
        if not os.path.exists(user_path):
            flash('Invalid username', 'error')
            return redirect(url_for('login'))
        with open(user_path) as f:
            data = json.load(f)
            if data['password'] != password:
                flash('Invalid password', 'error')
                return redirect(url_for('login'))
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

def get_user_transactions():
    if 'username' not in session:
        return []
    return load_transactions(user_file(session['username']))

def save_user_transactions(transactions):
    if 'username' in session:
        save_transactions(user_file(session['username']), transactions)

@app.route('/')
def index():
    transactions = get_user_transactions()
    # Filtering
    category = request.args.get('category')
    type_filter = request.args.get('type')
    filtered = transactions
    if category:
        filtered = [t for t in filtered if t['category'].lower() == category.lower()]
    if type_filter:
        filtered = [t for t in filtered if t['type'].lower() == type_filter.lower()]
    return render_template('index.html', transactions=filtered)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        from datetime import datetime
        transactions = get_user_transactions()
        new_transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "type": request.form['type'],
            "category": request.form['category'],
            "amount": float(request.form['amount'])
        }
        transactions.append(new_transaction)
        save_user_transactions(transactions)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/summary')
def summary():
    transactions = get_user_transactions()
    categories = {}
    for t in transactions:
        if t['type'].lower() == "expense":
            categories[t['category']] = categories.get(t['category'], 0) + t['amount']
    return render_template('summary.html', categories=list(categories.keys()), amounts=list(categories.values()))

@app.route('/export_csv')
def export_csv():
    transactions = get_user_transactions()
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Date','Type','Category','Amount'])
    for t in transactions:
        cw.writerow([t['date'], t['type'], t['category'], t['amount']])
    output = si.getvalue()
    return send_file(
        StringIO(output),
        mimetype='text/csv',
        as_attachment=True,
        download_name='transactions.csv'
    )

if __name__ == '__main__':
    app.run(debug=True)
