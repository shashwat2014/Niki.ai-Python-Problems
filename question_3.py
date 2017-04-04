def factors(n):
	count = 0
	print("1")
	for i in range(2,n//2+1):
		if(n%i==0):
			print(i)
			count = count +1
	print(n)
	if count == 0:
		print("Prime")
        
def main():
    var = input("Enter the number : ")
    factors(var)
   
main()
