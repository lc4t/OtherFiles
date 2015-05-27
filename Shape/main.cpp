#include <iostream>
#include "Length.h"
#include "Circle.h"
#include "Cylinder.h"

//基类:长度派生园,再圆柱,输出圆面积和圆柱体积
//Complex * 和 <<
int main(int argc, const char *argv[])
{
	Circle circle(0, 0, 5);	// x, y, r
	std::cout<<circle.getArea()<<std::endl;

	Cylinder cylinder(0, 0, 5, 10); 	//x, y, r, h
	std::cout<<cylinder.getVolume()<<std::endl;
}
