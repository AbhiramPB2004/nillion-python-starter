from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the maximum of my_int1 and my_int2
    result = If(my_int1 > my_int2, my_int1, my_int2)

    # Return the output with the computed result
    return [Output(result, "max_output", party1)]
