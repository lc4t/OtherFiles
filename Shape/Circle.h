/*
 * Circle.h
 *
 *  Created on: 2015年5月28日
 *      Author: lc4t
 */

#ifndef CIRCLE_H_
#define CIRCLE_H_
#include "Length.h"
class Circle:public Length
{
public:
	Circle();
	Circle(double x, double y, double r);
	void setCenterX(double x);
	void setCenterY(double y);
	void setRadius(double r);
	double getCenterX();
	double getCenterY();
	double getRadius();
	double getArea();
	virtual ~Circle();
	const double pi = 3.14159;
private:
	double x,y,r;
};

#endif /* CIRCLE_H_ */
