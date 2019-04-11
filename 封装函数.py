class Y:
    def __init__(self,v0,g):
        self.v0=v0
        self.g=g
    def value(self,t):
        return self.v0 * t-0.5 * self.g * t ** 2


y=Y(3,9.81)
print(Y.value(y,1))
print(y.value(1))

class Y:
    def __init__(self,g):
        self.g=g
    def value(self,v0,t):
        return v0 * t-0.5 * self.g * t ** 2

class student:
    def __init__(self):
        self._score=0
    def get_score(self):
        return self._score
    def set_score(self,score):
        if isinstance(score,int):
            self._score=score
    score=property(get_score,set_score)#函数property的参数顺序：读，写，删

y=student()
y.set_score(100)
print(y.get_score())

