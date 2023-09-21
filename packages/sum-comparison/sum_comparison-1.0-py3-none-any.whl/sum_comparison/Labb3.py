#!/bin/python3

import typed_input

def sum_arithmetic(first_a1, difference, seq_len):

    '''
    The last element is calculated as: an = a1 + d * (n-1)
    Where an = last element, a1 = first element, d = difference, n = number of elements(seq_len)
    '''
    last = first_a1 + difference * (seq_len - 1)

    '''
    Arithmetic sequence formula: s = n * (a1 + an) /2 
    Where s = sum
    '''
    a_sum = seq_len * (first_a1 + last) / 2
    return a_sum

def sum_geometric(first_g1, ratio, seq_len):

    '''
    The last element is calculated as: gn = g1 * g ** (n-1)
    Where gn = last element, g1 = first element, q = quotient, n = sequence length
    '''
    last = first_g1 * ratio ** (seq_len - 1)

    '''
    Geometric sequence formula: s = g1 * (q ** n - 1) / (q -1 )
    Where s = sum
    '''
    g_sum = first_g1 * (ratio ** (seq_len - 1)) / (ratio - 1)
    return g_sum

def main():

    '''Input for the arithemtic sequence'''
    print("Data for arithmetic sum: ")
    ari_first = typed_input.input_type(float, "Enter the value of a1 (float): ")
    ari_diff = typed_input.input_type(float, "Enter the value of d (float): ")
    
    print("")

    '''Input for the geometric seqeunce'''
    print("Data for geometric sum: ")
    geo_first = typed_input.input_type(float, "Enter the value of g1 (float): ")
    geo_ratio = 1
    while geo_ratio == 1:
        geo_ratio = typed_input.input_type(float, "Enter the value of q (float): ")
        if geo_ratio == 1:
            print("Error: division by zero :(")

    '''Input for the sequence length'''
    seq_len = typed_input.input_type(int, "Enter the value of n (int): ")

    arithmetic = sum_arithmetic(ari_first, ari_diff, seq_len)
    geometric = sum_geometric(geo_first, geo_ratio, seq_len)

    if arithmetic != None and geometric != None:
        if arithmetic > geometric:
            print("The arithmetic sum (" + str(arithmetic) + ") is greater!")
        elif arithmetic < geometric:
            print("The geometric sum (" + str(geometric) + ") is greater!")
        else:
            print("Equal sums!")

main()
