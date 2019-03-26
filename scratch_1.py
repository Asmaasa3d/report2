from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np
from math import *
angle=0
x=0
d=1
def myInit():
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluPerspective(60,1,0.1,50)
   gluLookAt(8,9,10,
             0,0,0,
             0,1,0)
   glClearColor(0.2,0.8,0.8,1)
   glClear(GL_COLOR_BUFFER_BIT)

def xyAxis ()  :
    glLineWidth(1)
    glColor(1, 0, 0)
    glBegin(GL_LINES)
    glVertex(0, 1000,0)
    glVertex(0, 0,0)
    glEnd()
    glColor(0, 1, 0)
    glBegin(GL_LINES)
    glVertex(1000, 0,0)
    glVertex(0, 0,0)
    glEnd()
    glColor(0, 0, 1)
    glBegin(GL_LINES)
    glVertex(0,0,0)
    glVertex(0,0,1000)
    glEnd()

def background():
    glBegin(GL_POLYGON)

    glColor(0.1,0.9,0.1)
    glVertex(10, -2.5 * 0.25, -4)
    glVertex(-40, -2.5 * 0.25,-4)
    glVertex(10, -2.5 * 0.25, 10)
    glVertex(-10, -2.5 * 0.25, 10)
    glEnd()
    #glScale(3,1,3)
    glColor(0.2, 0.2, 0.2)
    glBegin(GL_QUADS)
    glVertex(-40, -2.5 * 0.25, -4)
    glVertex(-40, -2.5 * 0.25, 4)
    glVertex(10, -2.5 * 0.25, 4)
    glVertex(10, -2.5 * 0.25, -4)
    glEnd()

    glColor(1, 1, 1)
    glLoadIdentity()
    glTranslate(0, 0, .5)
    glTranslate(0, 5.5, -5)
    glutSolidSphere(.5, 100, 100)
    glLoadIdentity()
    glTranslate(0, .5, 0)
    glTranslate(0, 5.5, -5)
    glutSolidSphere(.5, 100, 100)
    glLoadIdentity()
    glTranslate(.5, 0, 0)
    glTranslate(0, 5.5, -5)
    glutSolidSphere(.5, 100, 100)
    glLoadIdentity()

    glColor(1, 1, 1)
    glLoadIdentity()
    glTranslate(0, 0, 1)
    glTranslate(3.5, 5.5, -5)
    glutSolidSphere(1, 100, 100)
    glLoadIdentity()
    glTranslate(0, 1, 0)
    glTranslate(3.5, 5.5, -5)
    glutSolidSphere(1, 100, 100)
    glLoadIdentity()
    glTranslate(1, 0, 0)
    glTranslate(3.5, 5.5, -5)
    glutSolidSphere(1, 100, 100)
    glLoadIdentity()

    glBegin(GL_QUADS)
    glVertex(-5, -2.5 * 0.25, 0)
    glVertex(-5, -2.5 * 0.25, 1.5)
    glVertex(0, -2.5 * 0.25, 1.5)
    glVertex(0, -2.5 * 0.25, 0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex(7, -2.5 * 0.25, 0)
    glVertex(7, -2.5 * 0.25, 1.5)
    glVertex(2, -2.5 * 0.25, 1.5)
    glVertex(2, -2.5 * 0.25, 0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex(-8, -2.5 * 0.25, 0)
    glVertex(-8, -2.5 * 0.25, 1.5)
    glVertex(-40, -2.5 * 0.25, 1.5)
    glVertex(-40, -2.5 * 0.25, 0)
    glEnd()

    glColor(0.1,0.4,0.1)
    glBegin(GL_QUADS)
    glVertex(-40, 4, -4)
    glVertex(-40,4, 4)
    glVertex(10, 4, 4)
    glVertex(10, 4, -4)
    glEnd()
    glTranslate(5,4,0)
    glutSolidSphere(2,100,100)
    glLoadIdentity()
    glTranslate(3, 4.6, 0)
    glutSolidSphere(2, 100, 100)
    glLoadIdentity()
    glTranslate(1, 4, 0)
    glutSolidSphere(2, 100, 100)
    glLoadIdentity()
    glTranslate(-2, 4, 0)
    glutSolidSphere(2, 100, 100)
    glLoadIdentity()
    glTranslate(-3, 4.5, 0)
    glutSolidSphere(3, 100, 100)
    glLoadIdentity()
    glTranslate(-7, 4.5, 0)
    glutSolidSphere(2, 100, 100)
    glLoadIdentity()
    glTranslate(-10, 4, 0)
    glutSolidSphere(2, 100, 100)
    glLoadIdentity()

    glBegin(GL_QUADS)
    glColor(0.6,0.7,0.5)
    glVertex(-5, -2.5 * 0.25, -1)
    glVertex(-6, -2.5 * 0.25, -1)
    glVertex(-6, 2.5, -1)
    glVertex(-5, 2.5, -1)
    glEnd()


    glTranslate(-5.5,4,-1)
    glColor(0.6,0.7,0.5)
    glScale(1, 1.5, .25)
    glutSolidCube(2)
    glColor(0.9,0.9,0)
    glutSolidSphere(.25, 50, 50)

    glColor(1,0,0)
    glTranslate(0,.75,0)
    glutSolidSphere(.25, 50, 50)
    glLoadIdentity()
    glTranslate(-5.5, 4, -1)
    glScale(1, 1.5, .25)
    glColor(0.5,0.9,0.2)
    glTranslate(0, -.75, 0)
    glutSolidSphere(.25, 50, 50)
    glLoadIdentity()


def draw():
    global angle
    global x
    global  d
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    background()


    glLoadIdentity()
    glColor(0,0,1)

    glTranslate(2.5+x,-2.5*0.25,1.25)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.25,0.5,13,14)

    glLoadIdentity()
    glColor(0,0,1)
    glTranslate(-2.5+x,-2.5*0.25,1.25)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.25,0.5,13,14)

    glLoadIdentity()
    glColor(0,0,1)
    glTranslate(2.5+x,-2.5*0.25,-1.25)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.25,0.5,12,8)
    #xyAxis()
    glLoadIdentity()
    glColor(0,0,1)
    glTranslate(-2.5+x,-2.5*0.25,-1.25)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.25,0.5,12,8)

    glLoadIdentity()
    glColor(0, 0, 0)
    glTranslate(x, 0, 0)
    glScale(1, 0.25, 0.5)
    glColor(0.9, 0.6, 1)
    glutSolidCube(5)
    glLoadIdentity()
    glTranslate(x, 1.25, 0)
    glScale(0.5, 0.25, 0.5)
    glColor(0.9,0.8,0.9)
    glutSolidCube(5)

    glColor(1,1,0)
    glLoadIdentity()
    glTranslate(2.5+x,0,-0.6)
    glutWireSphere(0.3,100,100)

    glLoadIdentity()
    glTranslate(2.5+x, 0, 0.6)
    glutWireSphere(0.3,100,100)

    if x>5:
        d=-1
    if x<-5:
        d=1
    if d==1:
        x+=0.1
    if d==-1:
        x-=0.1


    angle = (angle + 1) % 1000000
    glLoadIdentity()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"moving car")

glutDisplayFunc(draw)
glutIdleFunc(draw)

myInit()

glutIdleFunc(draw)
glutMainLoop()