Description
===========

    >>> from ftw.dictstorage.interfaces import IDictStorage

    >>> context = layer['example_context']
    >>> print context
    <ftw.dictstorage.testing.ExampleContext object at ...>

    >>> storage = IDictStorage(context)
    >>> storage['key'] = 'value'
    >>> print storage['key']
    value

    >>> print storage._storage
    {'key': 'value'}


#    >>> storage = IDictStorage(context)
#    >>> storage['key'] = 'value'
#    >>> print storage['key']
#    'value'
