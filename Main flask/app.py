from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        if operation == 'add':
            answer = num1 + num2
        elif operation == 'subtract':
            answer = num1 - num2
        elif operation == 'multiply':
            answer = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return render_template('index.html', answer="Error: Division by zero")
            else:
                answer = num1 / num2
    except (ValueError, ZeroDivisionError):
        return render_template('index.html', answer="Error: Invalid input or division by zero")

    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)