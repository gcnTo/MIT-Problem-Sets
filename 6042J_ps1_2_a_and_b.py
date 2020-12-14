F = False
T = True
p = F
q = F
r = F

equation1 = not (p or (q and r))  
equation2 = (not p) and (not q or not r)

for i in range(2):
	p = i
	for j in range(2):
		q = j
		for k in range(2):
			r = k
			print(equation1 == equation2)
