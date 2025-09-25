from flask import *

app = Flask(__name__)

@app.route('/')
def college():
    return "This is college"

@app.route("/admin")
def admin():
    return "This is admin"

@app.route("/student")
def student():
    return "This is student"

@app.route("/staff")
def staff():
    return "This is staff"

def users(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    elif name == 'student':
        return redirect(url_for('student'))
    elif name == 'staff':
        return redirect(url_for('staff'))

if __name__ == '__main__':
    app.run()