import code
import math

def square_code():
    code_len = 0
    
    while code_len == 0:
        print("Your input does not contain any alphanumeric characters! Try again!")
        a = input("Put your message to be encoded here! ")
        new_input = ''.join(e for e in a if e.isalnum())
        new_input = new_input.lower()
        print(new_input)
        code_len= len(new_input)
    else:
        pass    

    while code_len != 0:
        if code_len <=81:
            sqr_len = int(math.sqrt(code_len))
            print("Message Square:")
            for i in range(0, code_len +1, sqr_len):
                print(new_input[i:i+sqr_len])
            '''
            print("Coded message:")
            for letter in new_input:
                for i in range(0, code_len +1, sqr_len):
            '''
        else:
            print("Message too long, can not be encoded. Try again!")
        a = input("Put your message to be encoded here! ")
        new_input = ''.join(e for e in a if e.isalnum())
        new_input = new_input.lower()
        code_len = len(new_input)
        print(code_len)


square_code()