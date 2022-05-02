import random
import string

def randomgen(upper = True, lower = True, nums = True, sym = True):
    return_arr = []
    alpha_arr = []
    symbol_options = ["@", "$", "!", "&", "%"]
    cases = [string.ascii_lowercase, string.ascii_uppercase]
    output_string = ""
    # generate letters
    if (upper or lower):
        alpha_arr = random.choices(cases[0], k=5)
        for i in alpha_arr:
            return_arr.append(i)
    # generate numbers
    if nums:
        for i in range(0,5):
            n = random.randint(0,9)
            return_arr.append(str(n))
    # generate symbols
    if sym: 
        for i in range(0,3):
            n = random.randint(0,4)
            return_arr.append(symbol_options[n])
    random.shuffle(return_arr)
    output_string = "".join(return_arr)
    print(output_string)
    

randomgen(True, False, False, True)
