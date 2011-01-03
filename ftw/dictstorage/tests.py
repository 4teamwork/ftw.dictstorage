import os
import unittest2 as unittest
import doctest

from plone.testing import layered
from ftw.dictstorage.testing import DICTSTORAGE_LAYER


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite(
                    os.path.join('..', '..', 'README.rst'),
                    package='ftw.dictstorage',
                    optionflags=doctest.ELLIPSIS),
                layer = DICTSTORAGE_LAYER),
    ])
    return suite
