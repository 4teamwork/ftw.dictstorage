Introduction
============

This package provides a layer for storing key/value pairs. The storage
can be configured dynamically by providing a ``IConfig`` adapter of the
context on which the dict storage is used.


Examples
========

The adapter defaults to using a non-persistent dict:

.. code-block:: python

    >>> from ftw.dictstorage.interfaces import IDictStorage

    >>> context = layer['example_context']
    >>> print context
    <ftw.dictstorage.testing.ExampleContext object at ...>

    >>> storage = IDictStorage(context)
    >>> storage['key'] = 'value'
    >>> print storage['key']
    value

    >>> print storage.storage
    {'key': 'value'}

    >>> print IDictStorage(context).storage
    {}


For configuring a custom storage, implement your own ``IConfig`` which uses
custom ``IDictStorage``:

.. code-block:: python

    >>> from ftw.dictstorage.interfaces import IConfig
    >>> from ftw.dictstorage.base import DictStorage
    >>> from zope.component import provideAdapter, adapts
    >>> from zope.interface import Interface, alsoProvides, implements

    >>> context = layer['example_context']
    >>> class IMyContext(Interface):
    ...     pass
    >>> alsoProvides(context, IMyContext)

    >>> class ContextStorageConfig(object):
    ...     implements(IConfig)
    ...     adapts(IMyContext)
    ...
    ...     def __init__(self, context):
    ...         self.context = context
    ...
    ...     def get_storage(self):
    ...         if not hasattr(self.context, '_dictstorage'):
    ...             self.context._dictstorage = {}
    ...         return self.context._dictstorage
    >>> provideAdapter(ContextStorageConfig)

    >>> class ContextDictStorage(DictStorage):
    ...     implements(IDictStorage)
    ...     adapts(IMyContext, IConfig)
    ...
    ...     def __init__(self, context, config):
    ...         self.context = context
    ...         self.config = config
    ...         self._storage = config.get_storage()
    ...
    ...     @property
    ...     def storage(self):
    ...         return self._storage
    ...
    >>> provideAdapter(ContextDictStorage)

    >>> storage = IDictStorage(context)
    >>> storage['foo'] = 'bar'
    >>> print storage['foo']
    bar

    >>> print context._dictstorage
    {'foo': 'bar'}

    >>> print IDictStorage(context)['foo']
    bar


Compatibility
=============

Runs with `Plone <http://www.plone.org/>`_ `4.2`, `4.3`, `5.1`.


Links
=====

- Github: https://github.com/4teamwork/ftw.dictstorage
- Issues: https://github.com/4teamwork/ftw.dictstorage/issues
- Pypi: http://pypi.python.org/pypi/ftw.dictstorage
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.dictstorage


Copyright
---------

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.dictstorage`` is licensed under GNU General Public License, version 2.
