
from zope.interface import Interface


class IDictStorage(Interface):
    """ funcionality that dictstorage is providing
        like ordinary dictionary
        TODO: maybe __iter__, values, keys, etc ... should also be implemented
    """

    def __getitem__(key):
        """
        """

    def __setitem__(key, value):
        """
        """

    def __delitem__(key):
        """
        """


class IConfig(Interface):
    """ marker for configuration
    """


class ISQLAlchemy(Interface):
    """ marker for sqlalchemy storage
    """
