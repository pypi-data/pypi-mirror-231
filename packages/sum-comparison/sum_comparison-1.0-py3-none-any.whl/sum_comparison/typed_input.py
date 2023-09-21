#!/bin/python3

'''Deprecated'''
def input_float(text=""):
    while True:
        try:
            return (float(input(text)))
        except ValueError:
            print("Error: not a number :(")

'''Deprecated'''
def input_int(text=""):
    while True:
        try:
            return (int(input(text)))
        except ValueError:
            print("Error: not an integer :(")
            
def input_type(input_type, text=""):
    if input_type == int:
        while True:
            try:
                return (int(input(text)))
            except ValueError:
                print("Error: not an integer :(")
    elif input_type == float:
        while True:
            try:
                return (float(input(text)))
            except ValueError:
                print("Error: not a number :(")
    elif input_type == complex:
        while True:
            try:
                return (complex(input(text)))
            except ValueError:
                print("Error: not a complex number :(")
    elif input_type == str:
        while True:
            try:
                return (str(input(text)))
            except ValueError:
                print("Error: cannot convert to string :(")
    elif input_type == bool:
        while True:
            try:
                return (bool(input(text)))
            except ValueError:
                print("Error: not a boolean :(")
    elif input_type == set:
        while True:
            try:
                return (set(input(text)))
            except ValueError:
                print("Error: not a set :(")
    elif input_type == dict:
        while True:
            try:
                return (dict(input(text)))
            except ValueError:
                print("Error: not a dictionary :(")
    elif input_type == list:
        while True:
            try:
                return (set(input(text)))
            except ValueError:
                print("Error: not a set :(")
    elif input_type == tuple:
        while True:
            try:
                return (tuple(input(text)))
            except ValueError:
                print("Error: not a tuple :(")
    else:
        print("Error: bad type :(")
        return ""

if __name__ == '__main__':
    input_float()
