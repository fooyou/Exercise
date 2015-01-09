/* 
* @Author: joshua
* @Date:   2014-11-13 14:50:07
* @Last Modified by:   joshua
* @Last Modified time: 2014-11-17 13:16:15
*/

#include "Python.h" 

static PyObject *ex_foo(PyObject *self, PyObject *args)
{
    printf("Hello, world \n");
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef example_methods[] = {
    {"foo", ex_foo, METH_VARARGS, "foo() doc string"},
    {NULL, NULL }
};

static struct PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "example" ,
    "example module doc string" ,
    -1 ,
    example_methods,
    NULL ,
    NULL ,
    NULL ,
    NULL 
};

PyMODINIT_FUNC PyInit_example(void )
{
    return PyModule_Create(&examplemodule);
}
