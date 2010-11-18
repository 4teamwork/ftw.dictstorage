
from zope.component import queryAdapter
from zope.component import getMultiAdapter

from ftw.dictstorage.interfaces import IDictStorage
from ftw.dictstorage.interfaces import IConfig


class DictStorage(object):

    def __init__(self, context):
        self.context = context
        self._storage = None

    @property
    def storage(self):
        if self._storage is None:
            config = queryAdapter(self.context, IConfig)
            if config is not None:
                self._storage = getMultiAdapter(
                        (self.context, config), IDictStorage)
            else:
                self._storage = dict()
        return self._storage

    def __getitem__(self, key, default=None):
        try:
            return self.storage[key]
        except KeyError:
            return default

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __delitem__(self, key):
        del self.storage[key]

    get = __getitem__
    set = __setitem__
