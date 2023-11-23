from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Dummy user data for demonstration purposes
users = {
    'user1': {
        'username': 'user1',
        'password': generate_password_hash('password123', method='sha256'),  # Hashed password
    },
    # Add more users as needed
}

@app.route('/')
def home():
    return 'Welcome to Samyak event registration and login!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists. Please choose a different one.', 'danger')
        else:
            users[username] = {
                'username': username,
                'password': generate_password_hash(password, method='sha256'),
            }
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))

        flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        return f'Welcome to your Samyak event profile, {username}!'
    else:
        flash('You must log in to access your profile.', 'warning')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)