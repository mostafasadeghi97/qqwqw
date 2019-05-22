
import math
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



g = GaussSolver(func, 0, 1, 10)
g.execute()
print(g.get_result())
