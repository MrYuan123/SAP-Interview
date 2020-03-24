from flask import Flask, json, jsonify, redirect, url_for
import math

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<int:number>')
def display(number):
    result = [m for m in range(1, number + 1)]
    return jsonify({"result": result})

# @app.route('/<int:number>/<string:type>')
# def display_with_type(number, type):
#     if type == 'odd':
#         return display_odd(number)
#     elif type == 'even':
#         return display_even(number)
#     elif type == 'prime':
#         return display_prime(number)
#     else:
#         return jsonify({'Error': 'Invalid type'})

@app.route('/<int:number>/odd')
def display_odd(number):
    result = [m for m in range(number + 1) if m % 2 == 1]
    return jsonify({"result": result})


@app.route('/<int:number>/even')
def display_even(number):
    result = [m for m in range(number + 1) if m % 2 == 0]
    return jsonify({"result": result})


@app.route('/<int:number>/prime')
def display_prime(number):
    result = []
    for i in range(2, number + 1):
        if isPrime(i):
            result.append(i)
    return jsonify({"result": result})


def isPrime(number):
    if number == 2 or number == 3:
        return True

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
