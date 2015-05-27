/*
 * Circle.cpp
 *
 *  Created on: 2015年5月28日
 *      Author: lc4t
 */

#include "Circle.h"

Circle::Circle() {
	// TODO Auto-generated constructor stub
	this->x = 0;
	this->y = 0;
	this->r = 0;
}

Circle::Circle(double x, double y, double r)
{
	this->x = x;
	this->y = y;
	this->r =r;
}

void Circle::setCenterX(double x)
{
	this->x = x;
}

void Circle::setCenterY(double y)
{
	this->y = y;
}

void Circle::setRadius(double r)
{
	this->r = r;
}

double Circle::getCenterX()
{
	return this->x;
}


double Circle::getCenterY()
{
	return this->y;
}

double Circle::getRadius()
{
	return this->r;
}

double Circle::getArea()
{
	return pi * r * r;
}



Circle::~Circle() {
	// TODO Auto-generated destructor stub
}

