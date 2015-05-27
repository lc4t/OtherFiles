/*
 * Cylinder.h
 *
 *  Created on: 2015年5月28日
 *      Author: lc4t
 */

#ifndef CYLINDER_H_
#define CYLINDER_H_
#include "Circle.h"
class Cylinder:public Circle {
public:
	Cylinder();
	Cylinder(double x, double y, double r, double h);
	Cylinder(Circle &circle, double h);
	double getVolume();
	virtual ~Cylinder();
private:
	double x,y,r,h;
};

#endif /* CYLINDER_H_ */
