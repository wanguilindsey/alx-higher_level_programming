#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: Python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned long size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		size = PyBytes_GET_SIZE(p);
		str = bytes->ob_sval;

		printf("  size: %lu\n", size);
		printf("  trying string: %s\n", str);

		printf("  first %lu bytes: ", (size < 10) ? size : 10);
		for (i = 0; i < size && i < 10; i++)
		{
			printf("%02x", (unsigned char)str[i]);
			if (i < size - 1 && i < 9)
				printf(" ");
		}
		printf("\n");
	} else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - Print information about Python lists
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	long size, allocated, i;

	printf("[*] Python list info\n");

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		allocated = list->allocated;

		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", allocated);

		for (i = 0; i < size; i++)
		{
			PyObject *item = PyList_GetItem(p, i);

			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
			if (PyBytes_Check(item))
			{
				print_python_bytes(item);
			}
		}
	}
}
