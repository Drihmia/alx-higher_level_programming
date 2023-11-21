#include <Python.h>
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - prints some basic info about Python lists.
 * @p: python object
 * Return: NONE.
 */
void print_python_list(PyObject *p)
{
	PyListObject *cast = (PyListObject *)p;
	Py_ssize_t listSize = ((PyVarObject *)p)->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", cast->ob_base.ob_size);
	printf("[*] Allocated = %zd\n", cast->allocated);

	for (Py_ssize_t i = 0; i < listSize; i++)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i];

		if (item)
		{
			printf("Element %zd: %s\n", i, ((PyTypeObject *)(item->ob_type))->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
		}
	}
}


/**
 * print_python_bytes - prints some basic info about Python bytes objects.
 * @p: python object
 * Return: NONE.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	const char *data;
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		size = ((PyVarObject *)p)->ob_size;
		data = ((PyBytesObject *)p)->ob_sval;

		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", data);
		size++;
		printf("  first %zd bytes:", (size < 10) ? size : 10);


		for (i = 0; i < ((size < 10) ? size : 10); i++)
		{
			printf(" %02x", (unsigned char)data[i]);
		}
		printf("\n");
	}
	else
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
}

void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (PyFloat_Check(p))
	{
		value = ((PyFloatObject *)p)->ob_fval;

		printf("  value: %f\n", value);
	}
	else
		fprintf(stderr, "  [ERROR] Invalid Float Object\n");
}
