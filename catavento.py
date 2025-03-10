import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


pygame.init()
largura, altura = 500, 500
pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)
gluOrtho2D(0, largura, 0, altura)


angle = 0.0


def drawTriangle(cx, cy, size, angle):

    glPushMatrix()
    glTranslatef(cx, cy, 0)
    glRotatef(angle, 0, 0, 1)

    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, size)
    glVertex2f(-size / 1.5, -size)
    glVertex2f(size / 1.5, -size)
    glEnd()

    glPopMatrix()


def desenharCatavento():

    global angle
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex2f(245, 100)
    glVertex2f(255, 100)
    glVertex2f(255, 300)
    glVertex2f(245, 300)
    glEnd()

    cores = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]
    for i in range(4):
        glColor3fv(cores[i])
        drawTriangle(250, 320, 40, angle + (i * 90))

    pygame.display.flip()


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        if evento.type == KEYDOWN:
            if evento.key == K_a:
                angle += 10
            elif evento.key == K_d:
                angle -= 10

    desenharCatavento()
    pygame.time.wait(50)
pygame.quit()
