#include <GL/glut.h>
#include <stdio.h>

void init()
{
	glClearColor(1.0, 0.0, 0.0, 0.0);
	glOrtho(-1, 1, -1, 1, -10, 10);
}

GLdouble eyex=0.0, eyey=0.0, eyez=0.8;
GLdouble upx=0.0, upy=1.0, upz=0.0;

int flag = 0;

float angel1 = 0, angel2 = 0, angel3 = 0;
float depth = 0;
float change = 5;

void change_look_point(unsigned char key, int x, int y)
{
	switch(key)
	{
	case 'x':
		angel1 -= change;
		break;
	case 'X':
		angel1 += change;
		break;
	case 'y':
		angel2 -= change;
		break;
	case 'Y':
		angel2 += change;
		break;
	case 'z':
		angel3 -= change;
		break;
	case 'Z':
		angel3 += change;
		break;
	case 'd':
		depth -= 0.1;
		break;
	case 'D':
		depth += 0.1;
		break;
	default:
		return;
	}

	glutPostRedisplay();
}

void display()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glRotatef(angel1, 1, 0, 0);
	glRotatef(angel2, 0, 1, 0);
	glRotatef(angel3, 0, 0, 1);

	glTranslatef(0, 0, depth);
	glTranslatef(-0.4, 0, 0.0);
	glutWireTeapot(0.3);
	glTranslatef(0.8, 0, 0.0);
	glutWireTeapot(0.3);
	glTranslatef(-0.4, 0, 0.0);
	glFlush();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutCreateWindow("2-2");
	glutInitWindowSize(400,  400);
	glutDisplayFunc(display);
	glutKeyboardFunc(change_look_point);
	init();
	glutMainLoop();
	return 0;
}
