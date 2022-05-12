from ast import Try
from math import trunc
import random
import string
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    vol = 16
    div_count = 0
    return_arr = []
    alpha_arr = []
    symbol_options = ["@", "$", "!", "&", "%"]
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
    if upper == "True" or upper == "true":
        div_count += 1
    if sym == "True" or sym == "true": 
        div_count += 1
    if nums == "True" or nums == "true":
        div_count += 1
    if lower == "True" or lower == "true":
        div_count += 1
    # generate lowercase letters
    if lower == "True" or lower == "true":
        ln = trunc(vol / div_count)
        vol = vol - ln
        alpha_arr = random.choices(string.ascii_lowercase, k=ln)
        for i in alpha_arr:
            return_arr.append(i)
        div_count -= 1
    # generate uppercase letters
    if upper == "True" or upper == "true":
        ln = trunc(vol / div_count)
        vol = vol - ln
        alpha_arr = random.choices(string.ascii_uppercase, k=ln)
        for i in alpha_arr:
            return_arr.append(i)
        div_count -= 1
    # generate numbers
    print(div_count)
    if nums == "True" or nums == "true":
        ln = trunc(vol / div_count)
        vol = vol - ln
        for i in range(0,ln):
            n = random.randint(0,9)
            return_arr.append(str(n))
        div_count -= 1
    # generate symbols
    if sym == "True" or sym == "true": 
        for i in range(0,vol):
            n = random.randint(0,4)
            return_arr.append(symbol_options[n])
    random.shuffle(return_arr)
    output_string = "".join(return_arr)
    return jsonify({'data': output_string})
app.run()
