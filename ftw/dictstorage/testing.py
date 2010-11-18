
from zope.configuration import xmlconfig

from plone.testing import Layer
from plone.testing.zca import ZCML_DIRECTIVES
from plone.testing.zca import stackConfigurationContext


class DictStorageLayer(Layer):
    defaultBases = (ZCML_DIRECTIVES,)

    def setUp(self):
        self['configurationContext'] = context = \
                stackConfigurationContext(self.get('configurationContext'))

        import ftw.dictstorage
        xmlconfig.file('configure.zcml', ftw.dictstorage, context=context)

        class ExampleContext(object):
            pass
        self['example_context'] = ExampleContext()

    def tearDown(self):
        del self['configurationContext']


DICTSTORAGE_LAYER = DictStorageLayer()
