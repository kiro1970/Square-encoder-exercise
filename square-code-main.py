import code
import math
import numpy as np
np.__verion__
def sqr_encoder(input_string, input_len):
    sqr_len = int(math.sqrt(input_len))
    print("Message Square:")
    for i in range(0, input_len +1, sqr_len):
        print(input_string[i:i+sqr_len])


def square_code():
    sqr_validator = False

    while sqr_validator == False:
        code_len = 0
        a = input("Put your message to be encoded here! ")
        new_input = ''.join(e for e in a if e.isalnum())
        new_input = new_input.lower()
        code_len= len(new_input)
        if code_len <=81:
            sqr_encoder(new_input,code_len)
            sqr_validator = True
        elif code_len == 0:
            print("Can not code this message, try again!")
        else:
            print("Message too long, can not be encoded. Try again!")



square_code()