#Claude Peon

time = 0

def setup():
    size(800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)

def draw():
    global time
    time += .01

    background (255, 255, 255)
    camera (0, 0, 70, 0, 0, 0, 0,  1, 0)

    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    directionalLight (100, 100, 100, -0.3, 0.5, 1)
    
    noStroke()
    shininess(15)

    pushMatrix()
    rotateY(-time)
    pikachu()
    popMatrix()
    

def pikachu():
    head()
    body()
    arms()
    tail()
    nose()
    eyes()
    feet()
    bulge()
    cheeks()
    ears()
    smile()

# cone with radius = 1, z range in [-1,1]
def cone(sides = 64):
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex(x,  y, 1)
    endShape(CLOSE)
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal(x1, y1, 0)
        vertex(x1, y1, 1)
        vertex(0, 0, -1)
        normal(x2, y2, 0)
        vertex(x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2

def nose():
    #nose
    fill(0, 0, 0)
    pushMatrix()
    translate(0, -3, 13.9)
    rotateZ(radians(180))
    scale(.6, .2, .1)
    triangularPrism()
    popMatrix()

def body():
    #body
    fill(229, 218, 42)
    pushMatrix()
    translate(0, 0, 0)
    scale(2.9, 4.3, 2)
    sphereDetail(60)
    sphere(5)
    popMatrix()

def arms():
    #right arm
    fill(229, 218, 42)
    pushMatrix()
    translate(10, 5, 6)
    rotateY(radians(-105))
    rotateZ(radians(55))
    scale(1.5, .5, .5)
    sphereDetail(60)
    sphere(5)
    popMatrix()

    #left arm
    pushMatrix()
    translate(-10, 5, 6)
    rotateY(radians(105))
    rotateZ(radians(-55))
    scale(1.5, .5, .5)
    sphereDetail(60)
    sphere(5)
    popMatrix()

def head():
    #head
    fill(229, 218, 42)
    pushMatrix()
    translate(0, -8, 0)
    scale(2.85, 2.6, 3)
    sphereDetail(60)
    sphere(5)
    popMatrix()

def bulge():
    #right bulge
    fill(229, 218, 42)
    pushMatrix()
    translate(4, 15, 0)
    rotateZ(radians(90))
    scale(1.4, 1.5, 1)
    sphereDetail(60)
    sphere(5)
    popMatrix()

    #left bulge
    pushMatrix()
    translate(-4, 15, 0)
    rotateZ(radians(90))
    scale(1.4, 1.5, 1)
    sphereDetail(60)
    sphere(5)
    popMatrix()

def cheeks():
    # left cheek
    fill(255, 0, 0)
    pushMatrix()
    translate(-6, -4, 8.4)
    scale(.8, .8, .8)
    sphereDetail(60)
    sphere(5)
    popMatrix()

    #right cheek
    fill(255, 0, 0)
    pushMatrix()
    translate(6, -4, 8.4)
    scale(.8, .8, .8)
    sphereDetail(60)
    sphere(5)
    popMatrix()

def eyes():
    #left eye
    fill(0, 0, 0)
    pushMatrix()
    translate(-4, -6, 12.2)
    scale(.5, .5, .5)
    sphereDetail(60)
    sphere(5)
    popMatrix()

    #right eye
    fill(0, 0, 0)
    pushMatrix()
    translate(4, -6, 12.2)
    scale(.5, .5, .5)
    sphereDetail(60)
    sphere(5)
    popMatrix()

def feet():
    #left foot
    fill(229, 218, 42)
    pushMatrix()
    translate(-6, 22, 1)
    rotateY(radians(-25))
    scale(3, 1.7, 5)
    box(1)
    popMatrix()

    #right foot
    fill(229, 218, 42)
    pushMatrix()
    translate(6, 22, 1)
    rotateY(radians(25))
    scale(3, 1.7, 5)
    box(1)
    popMatrix()

def ears():
    #left ear
    fill(229, 218, 42)
    pushMatrix()
    translate(-14.45, -20, 3)
    rotateZ(radians(-55))
    rotateX(radians(-90))
    scale(3, 3, 7)
    cone()
    popMatrix()

    #left ear cap
    fill(0, 0, 0)
    pushMatrix()
    translate(-14.45, -20, 3)
    rotateZ(radians(-55))
    rotateX(radians(-90))
    scale(3, 3, 10)
    cone()
    popMatrix()

    #right ear
    fill(229, 218, 42)
    pushMatrix()
    translate(14.45, -20, 3)
    rotateZ(radians(55))
    rotateX(radians(-90))
    scale(3, 3, 7)
    cone()
    popMatrix()

    #right ear cap
    fill(0, 0, 0)
    pushMatrix()
    translate(14.45, -20, 3)
    rotateZ(radians(55))
    rotateX(radians(-90))
    scale(3, 3, 10)
    cone()
    popMatrix()


def triangularPrism():
    beginShape()
    #bot left to bot right to top
    vertex(-1, 1, 0)
    vertex(1, 1, 0)
    vertex(0, -1, 0)
    endShape(CLOSE)

    beginShape()
    #bot right to top to out
    vertex(1, 1, 0)
    vertex(0, -1, 0)
    vertex(0, 0, -1)
    endShape(CLOSE)

    beginShape()
    #top to bot left to out
    vertex(0, -1, 0)
    vertex(-1, 1, 0)
    vertex(0, 0, -1)
    endShape(CLOSE)

    beginShape()
    #bot left to out to bot right
    vertex(-1, 1, 0)
    vertex(0, 0, -1)
    vertex(1, 1, 0)
    endShape(CLOSE)


def tail():

    fill(139,69,19)
    pushMatrix()
    translate(0, 14, -9)
    rotateX(radians(120))
    scale(5, .2, 2)
    box(1)
    popMatrix()

    # fill(139,69,19)
    pushMatrix()
    translate(2, 12.5, -9)
    rotateX(radians(120))
    rotateY(radians(90))
    scale(5, .5, 3)
    box(1)
    popMatrix()

    # fill(139,69,19)
    pushMatrix()
    translate(3, 11, -9)
    rotateX(radians(120))
    # rotateY(radians(-45))
    scale(5, .5, 4)
    box(1)
    popMatrix()

    fill(229, 218, 42)
    pushMatrix()
    translate(5, 10, -9)
    rotateX(radians(120))
    rotateY(radians(90))
    scale(5, .5, 5)
    box(1)
    popMatrix()

    pushMatrix()
    translate(6, 8, -9)
    rotateX(radians(120))
    # rotateY(radians(90))
    scale(5, .5, 6)
    box(1)
    popMatrix()

    pushMatrix()
    translate(8, 6, -9)
    rotateX(radians(120))
    rotateY(radians(90))
    scale(5, .5, 7)
    box(1)
    popMatrix()

    pushMatrix()
    translate(10, 4, -9)
    rotateX(radians(120))
    # rotateY(radians(90))
    scale(6, .5, 9)
    box(1)
    popMatrix()

    pushMatrix()
    translate(12, 2, -9)
    rotateX(radians(120))
    rotateY(radians(90))
    scale(6, .5, 10)
    box(1)
    popMatrix()

    pushMatrix()
    translate(13, 0, -9)
    rotateX(radians(120))
    # rotateY(radians(90))
    scale(6, .5, 10)
    box(1)
    popMatrix()

    pushMatrix()
    translate(15, -2, -9)
    rotateX(radians(120))
    rotateY(radians(90))
    scale(10, .5, 18)
    box(1)
    popMatrix()

def smile():
    pushMatrix()
    stroke(0, 0, 0)
    translate(0, -2, 13.4)
    scale(.2, .2, .2)
    rotateX(radians(-30))
    curve(-10, -2, -6, 5, 0, 0, 0, 0)
    curve(0, 0, 0, 0, 6, 5, 10, -2)
    popMatrix()
