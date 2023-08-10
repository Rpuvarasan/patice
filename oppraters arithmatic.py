##rectangle
l=int(input('enter the rectangular length'))
b=int(input('enter the rectangular breath'))
area=l*b
print('area of the rectangle',area)


##square
a=int(input('enter the area of square='))
area=a**2
print('area of the square=',area)


##right angle triangle

b=int(input('enter the triangle base='))
h=int(input('enter the triangle height='))
area=1/2*b*h
print('area of the triangle=',area)


##parallelogram
b=float(input('enter the paralleloram base='))
h=float(input('enter the paralleloram hight='))
a=b*h
perimeter=2*a+b
print('area of the parallelogram=',a)
print('perimeter of the parallelogram=',perimeter)


##circle
pie=3.14
r=int(input('enter the radious value='))
area=pie*r**2
perimeter=2*pie*r
print('area of the circle=',area)
print('perimeter of the circle=',perimeter) 

##student mark sheet
eng=int(input('enter english mark'))
tam=int(input('enter tamil mark'))
math=int(input('enter matchs mark'))
sci=int(input('enter science mark'))
soc=int(input('enter social mark'))
print('english=',eng,'\ntamil=',tam,'\nmatchs=',math,'\nscience=',sci,'\nsocial',soc)
total=eng+tam+math+sci+soc
pre=(total/500)*100
print("total=",total,'\nprecentage=',pre)

