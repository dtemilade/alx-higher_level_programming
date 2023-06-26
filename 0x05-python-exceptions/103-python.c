#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prototype that print some basic info on Python lists.
 * @p: parameter for ‘list’ object.
 */
void print_python_list(PyObject *p)
{
/*introducing parameters variables*/
	Py_ssize_t tstval, size, memval;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	memval = list->allocated;
	size = var->ob_size;

	fflush(stdout);

	/*output as example given*/
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		/*output as example given*/
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	/*output as example given*/
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", memval);

	for (tstval = 0; tstval < size; tstval++)
	{
		type = list->ob_item[tstval]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[tstval]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[tstval]);
	}
}

/**
 * print_python_bytes - Prototype fncs that print basic info on Python byte.
 * output as the example provided
 * @p: parameter for ‘byte’ object.
 */
void print_python_bytes(PyObject *p)
{
	/*introducing parameters variables*/
	Py_ssize_t tstval, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (tstval = 0; tstval < size; tstval++)
	{
		printf("%02hhx", bytes->ob_sval[tstval]);
		if (tstval == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prototype fncs that print basic info on Python float.
 * output as the example provided
 * @p: parameter for ‘float’ object.
 */
void print_python_float(PyObject *p)
{
	/*introducing variable parameter*/
	char *retval = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	retval = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
	Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", retval);
	PyMem_Free(retval);
}
