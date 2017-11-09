/**
 * @File Name: weatherdata.h
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-04-02 12:04:04
 * @Last Modified: 2016-04-10 22:04:50
 * @Description:
 */
#include <list>
#include "subject.h"
#include "observer.h"

typedef std::list<IObserver*> ArrayList;
typedef std::list<IObserver*>::iterator ArrayList_Iter;

class WeatherData : public ISubject {
public:
    WeatherData();
    virtual void RegisterObserver(IObserver* obs);
    virtual void RemoveObserver(IObserver* obs);
    virtual void NotifyObservers(); 
public:
    void MeasurementsChanged();
    void SetMeasurements(float temprature, float humidity, float pressure);
private:
    float _temprature;
    float _humidity;
    float _pressure;
    ArrayList _observers;
};
