/**
 * @File Name: main.cpp
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-04-10 14:04:38
 * @Last Modified: 2016-04-10 22:04:03
 * @Description:
 */
#include "./weatherdata.h"
#include "./currentcondationsdisplay.h"
#include <iostream>

int main(int argc, char* argv[])
{
    WeatherData weatherData;
    CurrentConditionsDisplay* pDisplay = new CurrentConditionsDisplay(&weatherData);
    weatherData.SetMeasurements(80, 65, 30.4f);
    delete pDisplay;
    return 0;
}
