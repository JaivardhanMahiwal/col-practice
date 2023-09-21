n = int(input())
for i in range(n):
	l1 = list(map(int, input().strip().split()))
	length = l1[0]
	wp = l1[1]
	l = list(input().strip().split())
	def clean(m):
		count = 0
		tempc = 0
		print(length)
		print(wp)
		for i in range(length):
			if m[i] == "B" and tempc < wp and count == 0:
				count = count + 1
				tempc = 0
			elif m[i] == "B" and tempc < wp and count > 0:
				tempc = 0
			elif m[i] == "B" and tempc >= wp:
				count = count + 1
				tempc = 0
			elif m[i] == "W" and count == 0:
				continue
			elif m[i] == "W" and count > 0:
				tempc = tempc + 1
			else:
				continue
		return count
	print(clean(l))

