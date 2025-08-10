from flask import Flask, request, render_template_string

app = Flask(__name__)

users = {}

html_form = '''
<!doctype html>
<html>
  <head>
    <title>Login/Signup</title>
    <link rel="stylesheet" href="/static/styles.css">
  </head>
  <body>
    <h2>User Login / Signup for Conditional</h2>
    <form method="POST" action="/login">
      <label>Username:</label><br>
      <input type="text" name="username" required><br><br>
      <label>Password:</label><br>
      <input type="password" name="password" required><br><br>
      <button type="submit" name="action" value="Login">Login</button>
      <button type="submit" name="action" value="Signup">Signup</button>
    </form>
  </body>
</html>
'''

# Add the missing route decorator
@app.route('/')
def index():
    return render_template_string(html_form)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    action = request.form['action']

    if action == "Signup":
        if username in users:
            return f"<h2 style='color:red;'>Username '{username}' already exists. Try logging in.</h2>"
        users[username] = password
        return f"<h3>Signup successful for user: {username}</h3>"

    elif action == "Login":
        if username not in users:
            return f"<h3 style='color:red;'>Username '{username}' not found. Please sign up first.</h3>"
        if users[username] != password:
            return f"<h3 style='color:red;'>Incorrect password for user: {username}</h3>"
        return f"<h3>Welcome back, {username}!</h3>"

    else:
        return "<h3>Unknown action.</h3>"

if __name__ == '__main__':
    app.run(debug=True)