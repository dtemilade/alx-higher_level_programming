#include <Python.h>

/**
 * print_python_list_info - C function that prints some basic info about Python lists.
 * @p: parameter for PyObject list.
 */
void print_python_list_info(PyObject *p)
{
/*introducing variable parameter*/
PyObject *obj;
int i, j, k;

k = ((PyListObject *)p)->allocated;
j = Py_SIZE(p);

/*Output result*/
printf("[*] Size of the Python List = %d\n", j);
printf("[*] Allocated = %d\n", k);

/*conditional statement for the function*/
for (i = 0; i < j; i++)
{
/*Output result*/
printf("Element %d: ", i);

obj = PyList_GetItem(p, i);
printf("%s\n", Py_TYPE(obj)->tp_name);
}
}
