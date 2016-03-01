/**
 * @File Name: 1_1_a_simple_om.cpp
 * @Author: Joshua Liu
 * @Email: liuchaozhen@neusoft.com
 * @Create Date: 2016-02-18 16:02:30
 * @Last Modified: 2016-02-18 19:02:15
 * @Description:
 */

class Point {
public:
    Point(float xval);
    virtual ~Point();
    float x() const;
    static int PointCount();
protected:
    virtual ostream& print(ostream& os) const;
    float _x;
    static int _point_count;
};
