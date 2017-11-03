/**
 * @File Name: subject.h
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-04-02 11:04:04
 * @Last Modified: 2016-04-10 22:04:35
 * @Description:
 */
#ifndef __SUBJECT_H__
#define __SUBJECT_H__

#include "observer.h"

class ISubject {
public:
    virtual void RegisterObserver(IObserver* obs) = 0;
    virtual void RemoveObserver(IObserver* obs) = 0;
    virtual void NotifyObservers() = 0;
};

#endif /*__OBSERVER_H__*/
