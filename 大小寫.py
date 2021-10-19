N = int(input("N = "))
max = ord('A')
min = ord('a')


for j in range(min, min+N, 1):
    print("%c"%j,end=",")
    
for i in range(max, max+N, 1):
 
    print("%c"%i, end=",")
