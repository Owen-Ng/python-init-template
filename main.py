from sortedcontainers import SortedList
import requests
import main

def arg1():
    res = input("Arg1")
    return res
def arg2():
    res = input("Arg2")
    return res
def main():
    arg = input("Input something\n")
    argg1 = arg1()
    argg2 = arg2()
    return arg + argg1 + argg2
if __name__ == '__main__':
    response = main()
    print(response)