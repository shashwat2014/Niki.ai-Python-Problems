def helperConvert(A):
	ans = []
	arr = []
	num = A
	rem = 0
	while num!=0 :
		rem = int(num%26)
		quo = num//26
		if rem == 0:
			rem = 26
			quo = quo - 1
		ans.append(rem)
		num = quo
	s = len(ans) - 1
	ret = ''
	for i in range(s+1):
		#arr.append(chr(ans[s-i]+64))
		ret = ret + chr(ans[s-i]+64)
	return ret

def convert(m ,n ):
	if m < n:
		small = m
		big = n
	else:
		small = n
		big = m
	for i in range(big-small+1):
		print(helperConvert(small+i))

def start():
    var1=input("first number : ")
    var2=input("second number : ")
    convert(var1,var2)
    
start()
