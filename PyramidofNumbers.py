# A python code that requests the user to enter a number and displays a pyramid having number of raws equal to this number

x = int(input(" Enter a number x to display a pyramid: "))

for x in range(1, x + 1, 1):
     for i in range(1, x + 1, 1):
          print(i, end="")
     print()    
          
          
    
          
