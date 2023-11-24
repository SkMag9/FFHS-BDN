import numpy as np
from functools import reduce


def fahrenheit(grad_f):
    return (grad_f - 32) * 5 / 9


def main():
    grad_f = np.linspace(0,1,11)
    grad_c = list(map(fahrenheit,grad_f))
    grad_c_lambda = list((fahrenheit(f) for f in grad_f))
    grad_c_avg = reduce(lambda a, b : a + b, grad_c) / len(grad_c)

    print("2: grad_f list():\n","grad_f: ", grad_f)
    print("3: map():\n","grad_c: ", grad_c)
    print("4: lambda:\n","grad_c: ", grad_c_lambda)
    print("5: avg mit reduce():\n","grad_c_avg: ", grad_c_avg)


if __name__ == '__main__':
    main()
