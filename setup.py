from setuptools import setup, find_packages

version = '1.1'
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

    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

    keywords='ftw key value storage sqlalchemy dictstorage',
    author='4teamwork GmbH',
    author_email='mailto:info@4teamwork.ch',
    maintainer=maintainer,
    url='https://github.com/4teamwork/ftw.dictstorage/',
    license='GPL2',

    packages = find_packages(exclude=['ez_setup']),
    include_package_data=True,
    namespace_packages=['ftw'],
    zip_safe=False,

    install_requires=[
        'setuptools',
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
