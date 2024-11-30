import pgzrun
WIDTH = 800
HEIGHT = 600
 
def draw():
    screen.clear()
    screen.fill("yellow")

    rectangle = Rect((150,150),(150,100))
    screen.draw.rect(rectangle,"red")
    rectangle2 = Rect((50,100),(150,100))
    screen.draw.filled_rect(rectangle2,"blue")
    screen.draw.circle((300,125),(40),"green")
    screen.draw.filled_circle((300,350),(40),"green")
    screen.draw.line((10,10),(190,190),"purple")


pgzrun.go()