#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object
 * Return: NONE.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = 0, i;
	PyObject *item = NULL;

	if (!PyList_CheckExact(p))
		return;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zu\n", size);

	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zu: %s\n", i, Py_TYPE(item)->tp_name);

	}
}
