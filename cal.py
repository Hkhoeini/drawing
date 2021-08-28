# mavaredi ke bayad  ezafe  gardad ro comment birai ke dar nazar begirim:
#
import turtle
metraj , zirbana , otagha = input('metraj koli va zibana va tedade otag ra vared konid : ').split()
params =[metraj,zirbana,otagha]



def diagnosis(i):
        if i.isdigit():
            return True
        else:
            return False



number = 0
while number != 3:
    number = 0
    for i in range(len(params)):
        if diagnosis(params[i]):
            number += 1
        else:
            print('parametre mord nazar ra dorost vard konid')
            metraj , zirbana , otagha = input('metraj koli va zirbana va tedade otag ra vared konid : ').split()
            params =[metraj,zirbana,otagha]
params = [int(i) for i in params]



drawer = turtle.Turtle()
drawer.penup()
drawer.setposition(-400, 100)
drawer.pendown()
drawer.pencolor("red")
win = turtle.Screen()
win.bgcolor("black")
win.setup(width=1000, height=1000)


def build_metrag(metraj):
    if metraj * (2.4/4) < 200:
        metraj *= 4

    elif metraj * (2.4/4) < 500:
        metraj *= 2

    length = metraj * (2.4/4)
    Width = metraj * (1.6/4)
    drawer.forward(length)
    drawer.right(90)
    drawer.forward(Width)
    drawer.right(90)
    drawer.forward(length)
    drawer.right(90)
    drawer.forward(Width)




def build_zirbana(zirbana,metraj):
    if zirbana * (2.4/4) < 150:
        zirbana *= 4
    elif zirbana * (2.4/4) < 400:
        zirbana *= 2
        
    if metraj * (2.4/4) < 200:
        metraj *= 4

    elif metraj * (2.4/4) < 500:
        metraj *= 2

    length = zirbana * (2.4/4)
    Width = metraj * (1.6/4)
    drawer.right(90)
    drawer.forward(length)
    drawer.right(90)
    drawer.forward(Width)
    drawer.right(90)
    drawer.forward(length)
    drawer.right(90)
    drawer.forward(Width)
    


def build_otagha(otagha):
    return False








build_metrag(params[0])
build_zirbana(params[1],params[0])
build_otagha(params[2])
win.mainloop()




