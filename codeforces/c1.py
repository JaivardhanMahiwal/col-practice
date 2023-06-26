import math
def fnc(n):
	a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	t = 1
	q = 0
	while q < n:
		rev = ''
		for i in range(t):
			if q<n:
				if rev == '':
					rev = rev + a[q]
					q = q + 1
				else:
					rev = rev + ' ' + a[q]
					q = q+1
			else:
				break
		print(rev)
		t = t + 1
n = int(input("enter a number:"))
fnc(n)
