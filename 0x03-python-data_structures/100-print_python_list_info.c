#include <Python.h>

/**
 * print_python_list_info - will print basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, ui;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (ui = 0; ui < size; ui++)
	{
		printf("Element %d: ", ui);

		obj = PyList_GetItem(p, ui);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
