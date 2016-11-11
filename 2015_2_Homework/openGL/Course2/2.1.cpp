#include <GL/glut.h>
#include <math.h>
#include <time.h>

void init()
{
	glClearColor (1.0, 1.0, 1.0, 1.0);
	gluOrtho2D(-100, 100, -100, 100);
}


void createHourhand(float angle)
{
	glRotatef(angle, 0,0, 1.0);
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
	glColor3f(0.9, 0.9, 0.9);
	glBegin(GL_POLYGON);
		glVertex3f(-10, 0, 0);
		glVertex3f(0, 4, 0);
		glVertex3f(25, 0, 0);
		glVertex3f(0, -4, 0);
	glEnd();
	glRotatef(-angle, 0, 0, 1.0);
}

void createMinutehand(float angle)
{
	glRotatef(angle, 0, 0, 1.0);
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
	glColor3f(0.9, 0.9, 0.9);
	glBegin(GL_POLYGON);
		glVertex3f(-10, 0, 0);
		glVertex3f(0, 3, 0);
		glVertex3f(30, 0, 0);
		glVertex3f(0, -3, 0);
	glEnd();
	glRotatef(-angle, 0, 0, 1.0);
}

void createSecondhand(float angle)
{

	glRotatef(angle, 0, 0, 1.0);
	glColor3f(0.9, 0.9, 0.9);
	glLineWidth(2.0);
	glBegin(GL_LINES);
		glVertex3f(-6, 0, 0);
		glVertex3f(35, 0, 0);
	glEnd();
	glRotatef(-angle, 0, 0, 1.0);
}

int KDx = 10, KDy = 2;

void createDial_kedu(float angle, float offset_x, float offset_y)
{

	glRotatef(angle, 0.0, 0.0, 1.0);
	glTranslatef(offset_x - KDx / 2,offset_y, 0);
	glBegin(GL_POLYGON);
	glVertex3f(KDx / 2, KDy / 2 , 0);
	glVertex3f(-KDx / 2, KDy / 2, 0);
	glVertex3f(-KDx / 2 , -KDy / 2,0);
	glVertex3f(KDx / 2,-KDy / 2, 0);
	glEnd();
	glTranslatef(-offset_x + KDx / 2, -offset_y , 0);
	glRotatef(-angle, 0.0, 0.0, 1.0);
}


int D = 50;
float PI = 3.14159;
void createDial()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.0, 0.0, 0.0);
	int i = 0;
	glBegin(GL_POLYGON);
	for(; i < 24; i++)
	{
    glColor3f(i * 0.03,i * 0.03,i * 0.03);
		glVertex3f(D * cos(i * PI / 12.0), D * sin(i * PI / 12.0), 0);
	}
	glEnd();

	glLineWidth(3.0);
	glColor3f(0.0, 0.0, 0.0);
	glBegin(GL_LINE_LOOP);
	for(i = 0; i < 24; i++)
	{
		glVertex3f(D * cos(i * PI / 12.0), D * sin(i * PI / 12.0), 0);
	}
	glEnd();
	glLineWidth(1.0);
	glColor3f(0.0, 0.0, 0.0);
	glPointSize(8.0);
	glBegin(GL_POINTS);
		glVertex3f(0, D - 2.5, 0);
		glVertex3f(0,-D + 2.5, 0);
		glVertex3f(D - 2.5, 0, 0);
		glVertex3f(-D + 2.5, 0, 0);
	glEnd();
	glPointSize(1.0);
	glBegin(GL_LINES);
		glVertex3f(-D, 0, 0);
		glVertex3f(D, 0, 0);
		glVertex3f(0, D, 0);
		glVertex3f(0, -D, 0);
	glEnd();
	createDial_kedu(30, D, 0);
	createDial_kedu(60, D, 0);
	createDial_kedu(120, D, 0);
	createDial_kedu(150, D, 0);
	createDial_kedu(-30, D, 0);
	createDial_kedu(-60, D, 0);
	createDial_kedu(-120, D, 0);
	createDial_kedu(-150, D, 0);

}

void createWatch(float hour, float minute, float second)
{
	createDial();
	glRotatef(90, 0.0, 0.0, 1.0);
	createHourhand(-hour / 12 * 360 - minute / 60 * 30);
	createMinutehand(-minute / 60 * 360);
	createSecondhand(-second / 60 * 360);
	glRotatef(-90, 0.0, 0.0, 1.0);


	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
	glColor3f(0.5, 0.5, 0.5);
	glBegin(GL_POLYGON);
		for(int i = 0; i < 12; i++)
			glVertex3f(3 * cos(PI / 6 * i), 3 * sin(PI / 6 * i), 0);
	glEnd();
}

GLuint Hour, Minute, Second;
void processWatch()
{
	struct tm* localTime;
	time_t curTime;
	time(&curTime);
	localTime = localtime(&curTime);
	if(Second != localTime->tm_sec)
	{
		Hour=localTime->tm_hour;
		Minute=localTime->tm_min;
		Second=localTime->tm_sec;
		glutPostRedisplay();
	}
}

void display()
{
	createWatch(Hour, Minute, Second);
	glFlush();
}

void timerProc(int id)
{
	processWatch();
	glutTimerFunc(1000, timerProc, 1);
}

int main(int argc,char** argv)
{
	glutInit(&argc,argv);
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);

	glutInitWindowSize (500, 500);
	glutInitWindowPosition (0, 0);
	glutCreateWindow ("2-1");
	processWatch();
	glutDisplayFunc(display);
	glutTimerFunc(1000,timerProc,1);
	processWatch();
	init();
	glutMainLoop();
	return 0;
}
