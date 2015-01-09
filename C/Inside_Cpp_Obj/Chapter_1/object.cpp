
class Point {
public:
    Point(float x = 0.0): _x(x) { }
    float x() { return _x; }
    void x(float xval) { _x = xval; }
    ~Point();
protected:
    float _x;
};

class Point2d : public Point {
public:
    Point2d(float x = 0.0, float y = 0.0): Point(x), _y(y) { }
    float y() { return _y; }
    void y(float yval) { _y = yval; }
    ~Point2d();
protected:
    float _y;
};

class Point3d: public Point2d {
public:
    Point3d(float x = 0.0, float y = 0.0, float z = 0.0): Point2d(x, y), _z(z) { }
    float z() { return _z; }
    void z(float zval) { _z = zval; }
    ~Point3d();
private:
    float _z;
};

int main() {
    return 0;
}