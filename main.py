from turtle import*

user = int(input("Rows: ")) # if rgb values are expanded by 15 maximum number of rows is 18

rectangleHeight = 500/user # counting height of each rectangle
r,g,b = 0, 0, 0 # default black color rgb value is (0,0,0)

colormode(255) # setting colormode to 255 so I can use int insted of float

up()

goto(-200,200) # setting up start cordinations
down()

for i in range(2): # drawing basic square
    forward(400)
    right(90)
    forward(500)
    right(90)
up()

for i in range(user):
    color((r,g,b)) # setting color of fillament

    begin_fill()
    forward(400)
    right(90)
    forward(rectangleHeight)
    right(90)
    forward(400)
    right(180)
    end_fill()

    r,g,b = r + 15, g + 15, b + 15 # adding rgb value, so it makes shades of black

done()