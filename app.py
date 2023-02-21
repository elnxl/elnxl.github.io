from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return redirect(url_for('profile'))

@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')

@app.route("/static/<path:file_path>")
def files(file_path):
    return url_for('static', filename=file_path)

if __name__ == "__main__":
    app.run(debug=False)