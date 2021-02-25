"""
Znaleźć wszystkie liczby trzycyfrowe, których suma cyfr jest równa potrojonemi
iloczynowi tych cyfr.
"""

x0 = 100
x1 = 9999


for i in range(x0,x1+1,1):
   valstr = str(i)
   vals = [int(val) for val in valstr]
   val2 = 3 * vals[0] * vals[1] * vals[2]
   if sum(vals) == val2:
       print(i)