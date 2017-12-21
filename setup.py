from setuptools import setup, find_packages

version = '1.3.dev0'
maintainer = 'Rok Garbas'

tests_require = [
    'unittest2',
    'plone.testing',
    ]

setup(
    name='ftw.dictstorage',
    version=version,
    description='Provides a layer for storing key / value paires.',
    long_description=open('README.rst').read() + '\n' + \
        open('docs/HISTORY.txt').read(),

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers

      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.1',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

    keywords='ftw key value storage sqlalchemy dictstorage',
    author='4teamwork AG',
    author_email='mailto:info@4teamwork.ch',
    maintainer=maintainer,
    url='https://github.com/4teamwork/ftw.dictstorage',
    license='GPL2',

    packages = find_packages(exclude=['ez_setup']),
    include_package_data=True,
    namespace_packages=['ftw'],
    zip_safe=False,

    install_requires=[
        'setuptools',
        'zope.component',
        'zope.configuration',
        'zope.security',
        ],

    extras_require=dict(
        sqlalchemy = [
            'SQLAlchemy',
            ],
        tests = tests_require,
        ),

    tests_require=tests_require,

    entry_points='''
    [z3c.autoinclude.plugin]
    target = plone
    ''')
