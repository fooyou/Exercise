/**
 * @File Name: currentcondationsdisplay.cpp
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-04-10 14:04:52
 * @Last Modified: 2016-04-10 22:04:22
 * @Description:
 */
#include "currentcondationsdisplay.h"
#include<iostream>

CurrentConditionsDisplay::CurrentConditionsDisplay(ISubject* isj) :
_temprature(0.0f),
_humidity(0.0f),
_pWeatherData(isj)
{
    if (NULL != _pWeatherData)
    {
        _pWeatherData->RegisterObserver(this);
    }
}

CurrentConditionsDisplay::~CurrentConditionsDisplay()
{
    _pWeatherData = NULL;
}

void CurrentConditionsDisplay::update(float temp, float humidity, float pressure)
{
    _temprature = temp;
    _humidity = humidity;
    display();
}

void CurrentConditionsDisplay::display()
{
    std::cout << "当前温度：" << _temprature << "; 湿度: " << _humidity << std::endl;
}
