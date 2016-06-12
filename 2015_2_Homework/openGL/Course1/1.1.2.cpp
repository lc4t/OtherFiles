#include <GL/glut.h>
#include <math.h>
#define PI 3.14
void drawMyLines()
{
    float t;
    float x,y,z;
    float a = 2, b = 3, c = 18;
    glColor3f(1.0, 0.5, 0.5);
    glBegin(GL_LINE_STRIP);   
        for(t = 0.0; t <= 2 * PI; t += 0.0002)
        {
            x = (a * sin(c * t) + b) * cos(t);
            y = (a * sin(c * t) + b) * sin(t);
            z = a * cos(c * t);
            glVertex3f(x, y, z);
        }
    glEnd();

    glColor3f(1.0, 1.0, 1.0);
    glBegin(GL_LINES);   
        glVertex3f(0, 0, 0);
        glVertex3f(12, 0, 0);
    glEnd();
    glBegin(GL_LINES);  
         glVertex3f(0, 0, 0);
        glVertex3f(0, 0, 12);
    glEnd();
    glBegin(GL_LINES);   
        glVertex3f(0, 0, 0);
        glVertex3f(0, 12, 0);
    glEnd();
}
void display()
{
    glClear(GL_COLOR_BUFFER_BIT);
    drawMyLines();
            
    glFlush();
}

void init()
{
    glClearColor(0.0, 0.0, 0.0, 0.0);

    glColor3f(1.0, 1.0, 1.0);

    gluLookAt(1, 1, 1,
        3, 3, 3,
        -1, -1, 1
        );

    glMatrixMode(GL_PROJECTION); 
    glLoadIdentity();         
    glOrtho(-12.0, 12.0, -12.0, 12.0, -12, 12);

}


int main(int argc, char* argv[])
{
     
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(0, 0);
    glutCreateWindow("1-1-2");

    glutDisplayFunc(display);
    
    init();

    glutMainLoop();
        
   
    return 0;
}