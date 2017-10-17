class Fraq:
    def __init__(self, num = 0, den = 0):
        self.num = num
        self.den = den
    
    def add_to(self, fraq):
        return 0
    
    def mul_by(self, fraq):
        fraq1 = self.simplify()
        fraq2 = fraq.simplify()
        temp_frac = Fraq(fraq1[0] * fraq2[0], fraq1[1] * fraq2[1])
        return temp_frac.simplify()
    
    def reciprocal(self):
        return "{}/{}".format(self.num, self.den)
    
    def simplify(self):
        gcd = self.gcd()
        return (self.num//gcd, self.den//gcd)

    def gcd(self):
        x = self.den // self.num
        y = self.num
        z = self.den - y * x

        while not z == 0:
            x = y // z
            d = y
            y = z
            z = d - y * x
    
        return y
            

f = Fraq(1,2)
f2 = Fraq(2,5)
print(f.mul_by(f2))

f = Fraq(312, 845)
print(f.simplify())