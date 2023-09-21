n = int(input())
for i in range(n):
	d = int(input())
	l = list(map(int,input().strip().split()))

	def red(m):
		least = 9
		p = 1
		for i in range(d):
			if m[i] <= least:
				least = m[i]
			else:
				continue
		for i in range(d):
			if m[i] == least:
				p = p*(m[i]+1)
				least = 13
			else:
				p = p*m[i]
		return p
	print(red(l))