#include <GL/glut.h>
#include <math.h>
#include <stdio.h>

void init()
{
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glOrtho(-100, 100, -100, 100, -100, 100); 
}

int D_top = 10, D_bottom = 20, H = 20;
float PI = 3.14159;

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);
    int i = 0;
    float angle = 0.0f;
    glBegin(GL_TRIANGLES);
        for(; i < 32; angle += PI / 32.0f, i++)
        {
            glColor3f(0.9, 0.9, 0.9);
            glVertex3f(D_bottom * cos(angle),D_bottom * sin(angle), 0);
            glVertex3f(D_bottom * cos(angle + PI / 16.0),D_bottom * sin(angle + PI / 16.0), 0);
            glVertex3f(D_top * cos(angle), D_top * sin(angle), H);
            glColor3f(0.1, 0.1, 0.2);
            glVertex3f(D_top *cos(angle), D_top * sin(angle), H);
            glVertex3f(D_top * cos(angle + PI / 16.0), D_top * sin(angle + PI / 16.0), H);
            glVertex3f(D_bottom * cos(angle + PI / 16.0), D_bottom * sin(angle + PI / 16.0), 0);
        }
    glEnd();
    glBegin(GL_TRIANGLE_FAN);
        glVertex3f(0, 0, 0);
        for(i = 0; i < 33; angle += PI /16.0f, i++)
        {
            glColor3f(1.0, 1.0, 1.0);
            glVertex3f(D_bottom * cos(angle), D_bottom * sin(angle), 0);
            glColor3f(0.1, 0.1, 0.2);
            glVertex3f(D_bottom * cos(angle + PI / 32.0), D_bottom * sin(angle + PI / 32.0), 0);
        }
    glEnd();
    glBegin(GL_TRIANGLE_FAN);
        glVertex3f(0, 0, H);
        for(i = 0; i < 32; angle += PI / 32.0f, i++)
        {
            glColor3f(1.0, 1.0, 1.0);
            glVertex3f(D_top * cos(angle), D_top * sin(angle), H);
            glColor3f(0.1, 0.1, 0.1);
            glVertex3f(D_top * cos(angle + PI / 32.0), D_top * sin(angle + PI / 32.0), H);
        }
    glEnd();
    glFlush();
}
void keyboard(unsigned char key, int x, int y)    
{
    switch(key)
    {
    case 'x':
        printf("x");
        glRotatef(10, 1.0, 0.0, 0.0);
        break;
    case 'y':
        printf("y");
        glRotatef(10, 0.0, 1.0, 0.0);
        break;
    case 'z':
        printf("z");
        glRotatef(10, 0.0, 0.0, 1.0);
        break;
    case 'D':
        D_top += 2;
        break;
    case 'd':
        D_top -= 2;
        break;
    case 'R':
        D_bottom += 2;
        break;
    case 'r':
        D_bottom -= 2;
        break;
    case 'H':
        H += 2;
        break;
    case 'h':
        H -= 2;
        break;
    }
    display();

}

int main(int argc,char* argv[])
{
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutInitWindowPosition(0,0); 
    glutInitWindowSize(500,500);   
    glutCreateWindow("1-2-2");
    init();
    glutDisplayFunc(display);    
    glutKeyboardFunc(keyboard);   
    glutMainLoop();
    return 0;
}