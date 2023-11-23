from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration purposes
users = {
    'faculty1': 'Faculty',

    'student1': 'Student',
}

# Routes
@app.route('/')
def index():
    return 'Welcome to the User Profile System!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect(url_for('profile', user_type=users[username]))

        return 'Invalid credentials. Please try again.'

    return '''
        <form method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/profile/<user_type>')
def profile(user_type):
    if user_type == 'Faculty':
        # Render Faculty profile template
        return render_template('faculty_profile.html')
    elif user_type == 'Student':
        # Render Student profile template
        return render_template('student_profile.html')
    else:
        return 'Invalid user type.'

if __name__ == '__main__':
    app.run(debug=True)
