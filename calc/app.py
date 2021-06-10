# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """ Add a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = add(a,b)

    return str(results)

@app.route("/sub")
def do_sub():
    """ Subtract a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = sub(a,b)

    return str(results)

@app.route("/mult")
def do_mult():
    """ Multiply a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = mult(a,b)

    return str(results)

@app.route("/div")
def do_div():
    """ Divide a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = div(a,b)

    return str(results)

# Further Study

OPERATORS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<operator>")
def do_math(operator):
    """ Do math operations with a and b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = OPERATORS[operator](a,b)

    return str(results)