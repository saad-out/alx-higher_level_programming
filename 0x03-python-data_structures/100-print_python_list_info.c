#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	PyObject *obj;
	Py_ssize_t size, i;
	struct _typeobject *type;

	if (strcmp(p->ob_type->tp_name, "list") != 0)
		return;

	list = (PyListObject *)p;
	size = list->ob_base.ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		obj = list->ob_item[i];
		type = obj->ob_type;
		printf("Element [%ld]: %s\n", i, type->tp_name);
	}
}
