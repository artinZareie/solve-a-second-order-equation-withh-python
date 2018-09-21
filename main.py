import math

print(u"Hi , We want to solve a second-order equation with this program. \n")
print(u"OK , Now our equation is (ax^2+bx+c=0) , you should give me ordered a , b and c \n")
a = float(input(u"a : "))
b = float(input(u"b : "))
c = float(input(u"c : "))
roots = [0,0]
delta = (b ** 2) - (4 * a * c)
print(u"delta :: " + str(delta))
print(u'\n\n\n\n\n\n\n\n\n\n\n\n')
if delta < 0:
    print(u"error : delta must be more than -1 \n")
elif delta == 0:
    roots[0] = (-b + math.sqrt(delta) / (2 * a))
    print(u"Two similar answers were found : " + str(roots[0]) + u"\n")
else:
    roots[0] = (-b + math.sqrt(delta) / (2 * a))
    roots[1] = (-b - math.sqrt(delta) / (2 * a))
    print(u"\tFirst answer : " + str(roots[0]) + u'\n')
    print(u"\tSecond answer : " + str(roots[1]) + u'\n')
