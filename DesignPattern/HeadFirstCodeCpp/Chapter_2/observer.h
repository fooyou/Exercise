/**
 * @File Name: observer.h
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-04-02 11:04:52
 * @Last Modified: 2016-04-10 22:04:34
 * @Description:
 */
#ifndef __OBSERVER_H__
#define __OBSERVER_H__

class IObserver {
public:
    virtual void update(float temp, float humidity, float pressure) = 0;
};

#endif // __OBSERVER_H__
