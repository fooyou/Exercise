/**
 * @File Name: currentcondationsdisplay.h
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-04-10 14:04:55
 * @Last Modified: 2016-04-10 22:04:15
 * @Description:
 */
#include <observer.h>
#include <display.h>
#include "subject.h"

class CurrentConditionsDisplay : public IObserver, IDisplayElement
{
    public:
        CurrentConditionsDisplay(ISubject* isj);
        virtual ~CurrentConditionsDisplay();
    public:
        virtual void update(float temp, float humidity, float pressure);
        virtual void display();
    private:
        float _temprature;
        float _humidity;
        ISubject* _pWeatherData;
};
