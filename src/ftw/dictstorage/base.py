
from zope.interface import implements
from zope.component import queryAdapter
from zope.component import getMultiAdapter

from ftw.dictstorage.interfaces import IDictStorage
from ftw.dictstorage.interfaces import IDictStorageConfig


class DictStorage(dict):
    """
    """

    def __init__(self, context):
        self.context = context
        self._storage = None

    @property
    def storage(self):
        if self._storage is None:
            config = queryAdapter(self.context, IDictStorageConfig)
            if config is not None:
                self._storage = getMultiAdapter((context, config), IDictStorage)
            else:
                self._storage = dict()
        return self._storage

    def __getitem__(self, key):
        return self.storage[key]

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __delitem__(self, key):
        raise
