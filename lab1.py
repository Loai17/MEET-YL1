#Problem1
print("Loai")

#Problem2
##Part1
number1=6
print(number1)

##Part2
number2=number1/2
print(number2)

#Problem3
list=[1,2,3]
for num in range(3):
	print(list[num])

for num in range(3):
	print(list[num]*2)

print(list[0]+list[1]+list[2])

#Problem4
import turtle

turtle.begin_fill()
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(100,100)
turtle.end_fill()
turtle.mainloop()