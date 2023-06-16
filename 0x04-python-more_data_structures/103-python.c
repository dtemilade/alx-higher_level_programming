#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
/*introducing variable parameters*/
char *a;
long int size, b, t;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)(p))->ob_size;
a = ((PyBytesObject *)p)->ob_sval;

printf("  size: %ld\n", size);
printf("  trying string: %s\n", a);

if (size >= 10)
b = 10;
else
b = size + 1;

printf("  first %ld bytes:", b);
 
for (t = 0; t < b; t++);
if (a[t] >= 0)
printf(" %02x", a[t]);
else
printf(" %02x", 256 + a[t]);

printf("\n");
}

/**
 * print_python_list - Prints list information
* @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
PyListObject *j;
PyObject *i;
long int x, t;

x = ((PyVarObject *)(p))->ob_size;
j = (PyListObject *)p;

printf("[*] Python list info\n");
printf("[*] X of the Python List = %ld\n", x);
printf("[*] Allocated = %ld\n", j->allocated);

for (t = 0; t < x; t++)
{
i = ((PyListObject *)p)->ob_item[t];
printf("Element %ld: %s\n", t, ((i)->ob_type)->tp_name);
if (PyBytes_Check(i))
print_python_bytes(i);
}
}
