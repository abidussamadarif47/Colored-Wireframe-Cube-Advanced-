from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

angle = 0  # rotation angle

def draw_cube():
    glBegin(GL_LINES)
    
    # Front face - Red
    glColor3f(1, 0, 0)
    glVertex3f(-1, -1,  1); glVertex3f( 1, -1,  1)
    glVertex3f( 1, -1,  1); glVertex3f( 1,  1,  1)
    glVertex3f( 1,  1,  1); glVertex3f(-1,  1,  1)
    glVertex3f(-1,  1,  1); glVertex3f(-1, -1,  1)

    # Back face - Green
    glColor3f(0, 1, 0)
    glVertex3f(-1, -1, -1); glVertex3f( 1, -1, -1)
    glVertex3f( 1, -1, -1); glVertex3f( 1,  1, -1)
    glVertex3f( 1,  1, -1); glVertex3f(-1,  1, -1)
    glVertex3f(-1,  1, -1); glVertex3f(-1, -1, -1)

    # Connecting edges - Blue
    glColor3f(0, 0, 1)
    glVertex3f(-1, -1,  1); glVertex3f(-1, -1, -1)
    glVertex3f( 1, -1,  1); glVertex3f( 1, -1, -1)
    glVertex3f( 1,  1,  1); glVertex3f( 1,  1, -1)
    glVertex3f(-1,  1,  1); glVertex3f(-1,  1, -1)

    glEnd()

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)
    
    glRotatef(angle, 1, 1, 1)  # Rotate
    draw_cube()
    
    glutSwapBuffers()
    angle += 1  # Increment rotation

def reshape(width, height):
    if height == 0:
        height = 1
    aspect = width / height
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, aspect, 1, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Rotating 3D Colored Wireframe Cube")
    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
