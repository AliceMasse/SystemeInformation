from Cours.TP2.duck import Canard

class DuckSimulator:

    @classmethod
    def simulate(cls, duck: Canard):
       for i in range(2):
           duck.fly()
           duck.quack()
           for i in range(3):
               duck.fly()

if  __name__ == "_main_":
   DuckSimulator.simulate(CouRouge('jojo'))