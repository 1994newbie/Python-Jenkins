import unittest


def ADD(x,y):
    return x+y


def ADD_TesT():
    assert ADD(3,4) == 7, "sum should be 7"

if __name__=="__main__":
    ADD_TesT()
    print("Everthing Passed")