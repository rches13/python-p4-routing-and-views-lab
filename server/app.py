#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:hello>")
def print_string(hello):
    print(hello)
    return 'hello'

@app.route("/count/<int:parameter>")
def count(parameter):
    result = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400  # Return a bad request for invalid operations
    
    return str(result)  # Return the result as a string





if __name__ == '__main__':
    app.run(port=5555, debug=True)
