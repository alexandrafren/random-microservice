from ast import Try
import random
import string
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return_arr = []
    alpha_arr = []
    symbol_options = ["@", "$", "!", "&", "%"]
    cases = [string.ascii_lowercase, string.ascii_uppercase]
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
    # generate letters
    if (upper == "True" or lower == "True" or upper == "true" or lower == "true"):
        alpha_arr = random.choices(cases[0], k=5)
        for i in alpha_arr:
            return_arr.append(i)
    # generate numbers
    if nums == "True" or nums == "true":
        print("we should be adding numbers")
        for i in range(0,5):
            n = random.randint(0,9)
            return_arr.append(str(n))
    # generate symbols
    if sym == "True" or sym == "true": 
        for i in range(0,3):
            n = random.randint(0,4)
            return_arr.append(symbol_options[n])
    random.shuffle(return_arr)
    output_string = "".join(return_arr)
    return jsonify({'ran': output_string})
app.run()
