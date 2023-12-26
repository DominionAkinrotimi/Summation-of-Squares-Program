'''  QUESTION
        n   
  y =    E   (x^2) 
        x=1  

        Note: from the above formula, the letter E is used to represent the summation sign
        Represent the above formula with a program in python
'''
sum = 0
n = int(input("Upper limit: "))
for x in range(1,n):
    print(f"x: {x}")
    y = (x**2)
    sum = sum + y
    print(f"{x}^2 = {y}" )
y = sum
print("")
print(f"y = {y}" )










