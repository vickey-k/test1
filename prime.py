num = 7 
for i in range(2,int(num*0.5)+1):
    if num % i == 0:
		break
else:
    print("given num is prime")
