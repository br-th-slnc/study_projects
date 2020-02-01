import random

class Box:

    def __init__(self, h, w, l, mass):
        self._h = h
        self._w = w
        self._l = l
        self._mass = mass
        self._v = h * l * w

    @property
    def h(self):
        return self._h

    @property
    def l(self):
        return self._l

    @property
    def w(self):
        return self._w

    @property
    def mass(self):
        return self._mass

    @l.setter
    def l(self, l1):
        self._l = l1

    @h.setter
    def h(self, h1):
        self._h = h1

    @mass.setter
    def mass(self, mass1):
        self._mass = mass1

    @w.setter
    def w(self, w1):
        self._w = w1

    def __str__(self):
        return f"Box with parameters:\n " \
               f"Height: {self.h} cm\n " \
               f"Length: {self.l} cm\n " \
               f"Width: {self.w} cm\n " \
               f"Mass: {self.mass} kg "

    @classmethod
    def creating(cls):
        h1 = random.randint(100, 500)
        l1 = random.randint(100, 2000)
        mass1 = random.randint(50, 1000)
        w1 = random.randint(100, 500)
        return cls(h1,w1,l1,mass1)

new_box = Box.creating() #working check
print(new_box) #check


# class Carriage:
#    cargo_list = []
#    def __init__(self,h,w,l,currmass,mass):
#       self._h = h
#       self._w = w
#       self._l = l
#       self._v = h * w * l
#       self._mass = mass
#       self._currmass = currmass

#    @l.setter
#    def l(self, l1):
#        self._l = l1

#    @h.setter
#    def h(self, h1):
#        self._h = h1

 #   @mass.setter
 #   def mass(self, mass1):
#        self._mass = mass1

 #   @w.setter
 #   def w(self, w1):
 #       self._w = w1

 #   def check(self, cargo):
 #       if (cargo.h <= self._h) ||  (cargo.w <= self._w) || (self.h <= self._h)

 #   @classmethod
 #   def creating(cls):
 #       h1 = random.randint(100, 500)
 #       l1 = random.randint(500, 2000)
 #       mass1 = random.randint(40000, 80000)
 #       w1 = random.randint(100, 500)
 #       currmass1 = mass1
#        return cls(h1,w1,l1,currmass1, mass1)

# test_carriage = Carriage(300,500,600,1000,5000)
# print(test_carriage)