from ast import Try
from math import trunc
import random
import string
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Method to Generate Random Numbers, takes in a Length, and the array to pass numbers back to
def gen_nums(ln, return_arr):
    for i in range(0,ln):
        n = random.randint(0,9)
        return_arr.append(str(n))

# Method to Generate Random Symbols, takes in a Length, and the array to pass symbols back to
def gen_sym(vol, return_arr):
    symbol_options = ["@", "$", "!", "&", "%"]
    for i in range(0,vol):
        n = random.randint(0,4)
        return_arr.append(symbol_options[n])

# Method to Generate Random Letters, takes in a Length, the case of the letters, and the array to pass letters back to
def gen_letters(case, ln, return_arr):
    alpha_arr = random.choices(case, k=ln)
    for i in alpha_arr:
        return_arr.append(i)

# Method to calculate how many different char types will be in the string (max:4 upper, lower, symbols, numbers)
def update_div_count(upper, lower, sym, nums, div_count):
    if upper == "True" or upper == "true":
        div_count += 1
    if sym == "True" or sym == "true": 
        div_count += 1
    if nums == "True" or nums == "true":
        div_count += 1
    if lower == "True" or lower == "true":
        div_count += 1
    return div_count

@app.route('/')
def index():
    vol = 16
    div_count = 0
    return_arr = []
    output_string = ""
    # parameters
    upper = "True"
    lower = "True"
    nums = "True"
    sym = "True"
    if request.args:
        if request.args.get('upper'):
            upper = request.args.get('upper')
        if request.args.get('lower'): 
            lower = request.args.get('lower')
        if request.args.get('nums'):
            nums = request.args.get('nums')
        if request.args.get('sym'): 
            sym = request.args.get('sym')
        if request.args.get('length'):
            vol = int(request.args.get('length')) 
    div_count = update_div_count(upper, lower, sym, nums, div_count)
    # generate lowercase letters
    if lower == "True" or lower == "true":
        ln = trunc(vol / div_count)
        vol = vol - ln
        gen_letters(string.ascii_lowercase, ln, return_arr)
        div_count -= 1
    # generate uppercase letters
    if upper == "True" or upper == "true":
        ln = trunc(vol / div_count)
        vol = vol - ln
        gen_letters(string.ascii_uppercase, ln, return_arr)
        div_count -= 1
    # generate numbers
    if nums == "True" or nums == "true":
        ln = trunc(vol / div_count)
        vol = vol - ln
        gen_nums(ln, return_arr)
        div_count -= 1
    # generate symbols
    if sym == "True" or sym == "true": 
        gen_sym(vol, return_arr)
    random.shuffle(return_arr)
    output_string = "".join(return_arr)
    return jsonify({'data': output_string})
app.run()
