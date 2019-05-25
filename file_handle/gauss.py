import matplotlib.pyplot as plt
import math
import sys
import time
from subprocess import Popen, PIPE
class GaussSolver():
    def __init__(self, func, a, b, n):
        self.func = func
        self.a = a
        self.b = b
        self.n = n
        self.result = 0
    def legendre(self, n, x):
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return ((2*n-1) * x * self.legendre(n-1,x) - (n-1) * self.legendre(n-2,x))/n
        
    def dLegendre(self, n, x):
        return (n * (x* self.legendre(n, x)- self.legendre(n-1,x)))/(x*x-1)

    def weight(self, n, x):
        return 2/((1-x*x)*(self.dLegendre(n,x)**2))

    def legendreZeros(self, n, i):
        xold = math.cos(math.pi*(i-.25)/(n+ .5))
        xnew = 0
        iteration = 1
        while ((1+abs(xnew - xold)) > 1):
            if iteration != 1:
                xold = xnew
            xnew = xold - self.legendre(n, xold)/ self.dLegendre(n, xold)
            iteration +=1
        
        return xnew
    
    def execute(self):
        integral = 0
        iteration = 2
        for i in range(1,self.n+1):
            integral = integral + self.func(self.legendreZeros(self.n, i)) * self.weight(self.n, self.legendreZeros(self.n, i))
        self.result = ((self.b - self.a)/2) * integral

    def get_result(self):
        return self.result


def func(x):
    xn = x*.5 + .5
    return (xn**3/(xn+1))* math.cos(xn*xn)
def func2(x):
    xn = x*.5 + .5
    return (xn**3)



# g = GaussSolver(func, 0, 1, n)
# start = time.time()
# g.execute()
# end = time.time()
# python_time = end-start
# print("Result of python code (n = {}): {}".format(n, g.get_result()))
# start = time.time()
# p = Popen(['./q1 {}'.format(n)], shell=True, stdout=PIPE, stdin=PIPE)
# result = p.stdout.readline().strip()
# end =  time.time()
# cpp_time = end - start
# print(result.decode())
# print('python time: '+ str(python_time) + '  ,  c++ time: '+ str(cpp_time))


python_dict = {}
cpp_dict = {}
for i in range(1,24):
    g = GaussSolver(func, 0, 1, i)
    start = time.time()
    g.execute()
    end = time.time()
    python_time = end-start
    python_dict[i] = python_time
    start = time.time()
    p = Popen(['./q1 {}'.format(i)], shell=True, stdout=PIPE, stdin=PIPE)
    result = p.stdout.readline().strip()
    end =  time.time()
    cpp_time = end - start
    cpp_dict[i] = cpp_time

plt.figure(1)
# plt.subplot(211)
plt.plot(list(python_dict.keys()), list(python_dict.values()), label='Python')

# plt.subplot(212)
plt.plot(list(cpp_dict.keys()), list(cpp_dict.values()), label = 'C++')
plt.show()
