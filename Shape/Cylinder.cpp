/*
 * Cylinder.cpp
 *
 *  Created on: 2015年5月28日
 *      Author: lc4t
 */

#include "Cylinder.h"

Cylinder::Cylinder() {
	// TODO Auto-generated constructor stub
	this->x = 0;
	this->y = 0;
	this->r = 0;
	this->h = 0;
}

Cylinder::Cylinder(double x, double y, double r, double h)
{
	this->x = x;
	this->y = y;
	this->r = r;
	this->h = h;
}

Cylinder::Cylinder(Circle &circle, double h)
{
	this->x = circle.getCenterX();
	this->y = circle.getCenterY();
	this->r = circle.getRadius();
	this->h = h;
}


double Cylinder::getVolume()
{
	return pi * r * r *h;
}

Cylinder::~Cylinder() {
	// TODO Auto-generated destructor stub
}

