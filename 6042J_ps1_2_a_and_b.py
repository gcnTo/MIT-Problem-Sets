"""
CHECKS IF THE EQUATIONS ARE EQUALS OR NOT 
EQ FROM: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/assignments/MIT6_042JF10_assn01.pdf
"""

F = False
T = True
p = F
q = F
r = F

equation1 = not (p or (q and r))  
equation2 = (not p) and (not q or not r)
equation1b = not (p and (q or r))
equation2b = not p or (not q or not r)

for i in range(2):
	p = i
	for j in range(2):
		q = j
		for k in range(2):
			r = k
			print(equation1 == equation2)
			print(equation1b == equation2b)
