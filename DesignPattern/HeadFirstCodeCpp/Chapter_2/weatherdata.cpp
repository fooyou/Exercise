/**
 * @File Name: weatherdata.cpp
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-04-02 12:04:08
 * @Last Modified: 2016-04-10 16:04:50
 * @Description:
 */
#include "weatherdata.h"

WeatherData::WeatherData()
: _temprature(0.0f)
, _humidity(0.0f)
, _pressure(0.0f)
{
}

void WeatherData::RegisterObserver(IObserver* obs)
{
    _observers.push_back(obs);    
}

void WeatherData::RemoveObserver(IObserver* obs)
{
    ArrayList_Iter itr = _observers.begin();
    for (;itr != _observers.end(); ++itr)
    {
        if (*itr == obs)
        {
            _observers.remove(*itr);
            break;
        }
    }
}

void WeatherData::NotifyObservers()
{
    ArrayList_Iter itr = _observers.begin();
    for (;itr != _observers.end(); ++itr)
    {
        (*itr)->update(_temprature,
                _humidity,
                _pressure);
    }
}

void WeatherData::MeasurementsChanged()
{
    NotifyObservers();
}

void WeatherData::SetMeasurements(float temprature,
        float humidity,
        float pressure)
{
    _temprature = temprature;
    _humidity = humidity;
    _pressure = pressure;
    MeasurementsChanged();
}
