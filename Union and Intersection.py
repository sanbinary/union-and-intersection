import itertools
from typing import Union

class Input():
    def a(a):
        global A
        A = a
    def b(b):
        global B
        B = b
    def c(c):
        global C
        C = c
    print("Enter the value of A")
    a(list(map(int,input("A = ").split(","))))
    print("Enter the value of B")
    b(list(map(int,input("B = ").split(","))))
    print("Enter the value of C")
    c(list(map(int,input("C = ").split(","))))

class Choices():
    @staticmethod
    def Cho():
        global Choice
        print("i - (i) | ii - (ii) | cv - (change values) | e - (exit)")
        Choice = str(input("Enter your choice: "))
        if Choice ==("i"):
            Output.I()
        elif Choice == ("ii"):
            if list(set(B) & set(C)) == []:
                print("{} - Empty set")
            else:
                Output.II()
        elif Choice == ("cv"):
            print("a - (A) or b - (B) or c - (C)")
            cv = str(input("Enter your choice: "))
            if cv == ("a"):
                print("Enter the value of A")
                Input.a(list(map(int,input("A = ").split(","))))
                assign()
                Loop.loop()
            elif cv == ("b"):
                print("Enter the value of B")
                Input.b(list(map(int,input("B = ").split(","))))
                assign()
                Loop.loop()
            elif cv == ("c"):
                print("Enter the value of C")
                Input.c(list(map(int,input("C = ").split(","))))
                assign()
                Loop.loop()
            else:
                print("Please enter a valid input")
        elif Choice == ("e"):
            exit
        else:
            print("Please enter a valid input")

class Output():
    @staticmethod
    def I():
        print("(i)   A x (B U C) = (A x B) U (A x C)\n            B U C = {{{}}} U {{{}}} = {{{}}}".format(str(B)[1:-1],str(C)[1:-1],str(sorted(list(set().union(B,C))))[1:-1]))
        print("      A x (B U C) = {{{}}} x {{{}}} = {{{}}}   ...(1)".format(str(A)[1:-1],str(sorted(list(set().union(B,C))))[1:-1],",".join(repr(_) for _ in list(itertools.product(A,sorted(list(set().union(B,C))))))))
        print("            A x B = {{{}}} x {{{}}} = {{{}}}".format(str(A)[1:-1],str(B)[1:-1],",".join(repr(_) for _ in list(itertools.product(A,B)))))
        print("            A x C = {{{}}} x {{{}}} = {{{}}}".format(str(A)[1:-1],str(C)[1:-1],",".join(repr(_) for _ in list(itertools.product(A,C)))))
        print("(A x B) U (A x C) = {{{}}} U {{{}}}".format(",".join(repr(_) for _ in list(itertools.product(A,B))),",".join(repr(_) for _ in list(itertools.product(A,C)))))
        print("                  = {{{}}}   ...(2)".format(str(sorted(list(set().union(list(itertools.product(A,B)),list(itertools.product(A,C))))))[1:-1]))
        if list(itertools.product(A,sorted(list(set().union(B,C))))) == sorted(list(set().union(list(itertools.product(A,B)),list(itertools.product(A,C))))):
            print("From (1) and (2) we observe that, A x (B U C) = (A x B) U (A x C) as {} = {} and {} = {},etc.".format(list(itertools.product(A,sorted(list(set().union(B,C)))))[0],sorted(list(set().union(list(itertools.product(A,B)),list(itertools.product(A,C)))))[0],list(itertools.product(A,sorted(list(set().union(B,C)))))[1],sorted(list(set().union(list(itertools.product(A,B)),list(itertools.product(A,C)))))[1]))
        else:
            print("From (1) and (2) we observe that, A x (B U C) ≠ (A x B) U (A x C) as {} ≠ {} and {} ≠ {},etc.".format(list(itertools.product(A,sorted(list(set().union(B,C)))))[0],sorted(list(set().union(list(itertools.product(A,B)),list(itertools.product(A,C)))))[0],list(itertools.product(A,sorted(list(set().union(B,C)))))[1],sorted(list(set().union(list(itertools.product(A,B)),list(itertools.product(A,C)))))[1]))
    @staticmethod
    def II():
        print("(ii)  A x (B ∩ C) = (A x B) ∩ (A x C)\n            B ∩ C = {{{}}}".format(str(list(set(B) & set(C)))[1:-1]))
        print("      A x (B ∩ C) = {{{}}} x {{{}}} = {{{}}}   ...(3)".format(str(A)[1:-1],str(list(set(B) & set(C)))[1:-1],str(list(itertools.product(A,list(set(B) & set(C)))))[1:-1]))
        print("            A x B = {{{}}} x {{{}}} = {{{}}}".format(str(A)[1:-1],str(B)[1:-1],",".join(repr(_) for _ in list(itertools.product(A,B)))))
        print("            A x C = {{{}}} x {{{}}} = {{{}}}".format(str(A)[1:-1],str(C)[1:-1],",".join(repr(_) for _ in list(itertools.product(A,C)))))
        print("(A x B) ∩ (A x C) = {{{}}} ∩ {{{}}}".format(",".join(repr(_) for _ in list(itertools.product(A,B))),",".join(repr(_) for _ in list(itertools.product(A,C)))))
        print("                  = {{{}}}   ...(4)".format(str(sorted(list(set(list(itertools.product(A,B))) & set(list(itertools.product(A,C))))))[1:-1]))
        if 1<len(list(set(list(itertools.product(A,B))) & set(list(itertools.product(A,C))))):
            if list(itertools.product(A,list(set(B) & set(C)))) == sorted(list(set(list(itertools.product(A,B))) & set(list(itertools.product(A,C))))):
                print("From (3) and (4) we observe that, A x (B ∩ C) = (A x B) ∩ (A x C) as {} = {} and {} = {},etc.".format(list(itertools.product(A,list(set(B) & set(C))))[0],sorted(list(set(list(itertools.product(A,B))) & set(list(itertools.product(A,C)))))[0],list(itertools.product(A,list(set(B) & set(C))))[1],sorted(list(set(list(itertools.product(A,B))) & set(list(itertools.product(A,C)))))[1]))
            else:
                print("From (3) and (4) we observe that, A x (B ∩ C) ≠ (A x B) ∩ (A x C) as {} ≠ {} and {} ≠ {},etc.".format(list(itertools.product(A,list(set(B) & set(C))))[0],sorted(list(set(list(itertools.product(A,B))) & set(list(itertools.product(A,C)))))[0],list(itertools.product(A,list(set(B) & set(C))))[1],sorted(list(set(list(itertools.product(A,B))) & set(list(itertools.product(A,C)))))[1]))
        else:
            if list(itertools.product(A,list(set(B) & set(C)))) == sorted(list(set(list(itertools.product(A,B))) & set(list(itertools.product(A,C))))):
                print("From (3) and (4) we observe that, A x (B ∩ C) = (A x B) ∩ (A x C) as {} = {}.".format(list(itertools.product(A,list(set(B) & set(C))))[0],sorted(list(set(list(itertools.product(A,B))) & set(list(itertools.product(A,C)))))[0]))
            else:
                print("From (3) and (4) we observe that, A x (B ∩ C) ≠ (A x B) ∩ (A x C) as {} ≠ {}.".format(list(itertools.product(A,list(set(B) & set(C))))[0],sorted(list(set(list(itertools.product(A,B))) & set(list(itertools.product(A,C)))))[0]))
def assign():
    print("A = {{{}}}, B = {{{}}}, C = {{{}}}".format(str(A)[1:-1],str(B)[1:-1],str(C)[1:-1]))
    print("(i) A x (B U C) = (A x C) (ii) A x (B ∩ C) = (A x B) ∩ (A x C)")
assign()

class Loop(Choices):
    @staticmethod
    def loop():
        __Loop = 0
        while __Loop != -1:
            Choices.Cho()
            __Loop = Loop =+ 1
            if Choice == ("e"):
                break
Loop.loop()
