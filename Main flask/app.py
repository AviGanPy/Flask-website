from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/switch', methods = ["POST"])
def switch():
    return render_template('new_page.html')

@app.route('/switchnew', methods = ["POST"])
def switch_new():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)