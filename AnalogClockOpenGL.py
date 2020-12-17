from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys
import time

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def addDate():
    t = time.localtime()
    current_time = str(time.strftime("%H:%M:%S", t))
    glWindowPos2f(0.0, 0.0)
    # for i in current_time:
    glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_10, current_time)

def drawClock():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    # addDate()
    glPointSize(3.5)

    # TITIK TENGAH
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)
    glEnd()
    
    # MENGGAMBAR LINGKARAN
    for t in arange(0.0, 6.28, 0.01):
        glPointSize(2.5)
        glBegin(GL_POINTS)
        glVertex2f(sin(t), cos(t))
        glEnd()
        glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(int((glutGet(GLUT_SCREEN_WIDTH)-640)/2),int((glutGet(GLUT_SCREEN_HEIGHT)-480)/2))
    glutCreateWindow("CLOCK ANALOG")
    glutDisplayFunc(drawClock)

    init()
    glutMainLoop()

main()

