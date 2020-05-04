import turtle
#turtle.write("SP")

seth = 'e'
w = 50
n = 8

route = [[2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [7, 1]]

def fd(w):
    print("ROBOT MOVES FORWARD BY " + str(w) + " TO POINT" + str(route[i+1]))
    turtle.forward(w)

for i in range(len(route)):
    try:
        x_current = route[i][0]
        y_current = route[i][1]

        x_next = route[i+1][0]
        y_next = route[i+1][1]
    except IndexError:
        turtle.write(route[-1])

    if (x_next > x_current):
        if (seth == 'e'):
            turtle.write(route[i])
            fd(w)
        else:
            seth = 'e'
            print("ROTATE TO SETH E")
            turtle.seth(0)
            turtle.write(route[i])
            fd(w)
    
    elif (x_next < x_current):
        if (seth == 'w'):
            turtle.write(route[i])
            fd(w)
        else:
            seth = 'w'
            print("ROTATE TO SETH W")
            turtle.seth(180)
            turtle.write(route[i])
            fd(w)

    elif (y_next > y_current):
        if (seth == 'n'):
            turtle.write(route[i])
            fd(w)
        else:
            seth = 'n'
            print("ROTATE TO SETH N")
            turtle.seth(90)
            turtle.write(route[i])
            fd(w)

    elif (y_next < y_current):
        if (seth == 's'):
            turtle.write(route[i])
            fd(w)
        else:
            seth = 's'
            print("ROTATE TO SETH S")
            turtle.seth(270)
            turtle.write(route[i])
            fd(w)

