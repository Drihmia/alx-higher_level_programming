#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists.
 * @p: python object
 * Return: NONE.
 */
void print_python_list(PyObject *p)
{
	PyListObject *cast = (PyListObject *)p;
	Py_ssize_t listSize = ((PyVarObject *)p)->ob_size;

	printf("[*] Allocated = %zd\n", cast->allocated);
	printf("[*] Size of the Python List = %zd\n", cast->ob_base.ob_size);

	for (Py_ssize_t i = 0; i < listSize; i++)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i];

		if (item == NULL)
			printf("Element %zd is NULL\n", i);
		else
			printf("Element %zd: %s\n", i, ((PyTypeObject *)(item->ob_type))->tp_name);
	}
}


