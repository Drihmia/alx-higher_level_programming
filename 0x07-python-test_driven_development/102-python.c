#include <Python.h>

/**
 * print_python_string - prints information about Python strings.
 * @p: PyObject string.
 * Return: None
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	const char *type;
	const char *value;

	printf("[.] string object info\n");

	if (PyUnicode_Check(p))
	{
		if (PyUnicode_IS_COMPACT_ASCII(p))
			type = "compact ascii";
		else if (PyUnicode_IS_COMPACT(p))
			type = "compact unicode object";
		else
			type = "unknown unicode object";

		length = PyUnicode_GET_LENGTH(p);
		value = PyUnicode_AsUTF8(p);

		printf("  type: %s\n", type);
		printf("  length: %ld\n", length);
		printf("  value: %s\n", value);
	}
	else if (PyBytes_Check(p))
	{
		type = "compact ascii";
		length = PyBytes_GET_SIZE(p);
		value = PyBytes_AsString(p);

		printf("  type: %s\n", type);
		printf("  length: %ld\n", length);
		printf("  value: %s\n", value);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}

