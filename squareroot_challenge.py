"""There is a video that I saw that a person was able to solve big square roots
like sqrt(25) is 5 right? So the way they find is by adding 2+5 = 7 and that 7
you subtract it by 2 because its a square root. If it were a cubic root you would
subtract by 3.
"""
x = 1 #starting number
max = 10000 #the last number to search for
a = 0
check = []
#here is a list of all the square root all the way to
sq = []
while a < max:
	a = x*x
	sq.append(a)
	x+=1


for i in sq:
	if i == 1:
		check.append(1)

	else:
		x = True
		while x:
			sum = 0
			num = i % 10
			sum = num
			num = int(i/10)
			if num == 0:
				sum = i - 2
				check.append(sum)
				x = False
			else:
				sum += num
				sum-=2
				check.append(sum)


print(check)

print("The amount of square roots from 1 to",max,":",x)
	

