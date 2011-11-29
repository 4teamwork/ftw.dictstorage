from setuptools import setup, find_packages

version = '1.1dev'
maintainer = 'Rok Garbas'

tests_require = [
            'unittest2',
            'plone.testing',
            ]

setup(
    name='ftw.dictstorage',
    version=version,
    description="Ftw dictstorage package used in OpenGever (Maintainer: %s)" % maintainer,
    long_description=open("README.rst").read() + "\n" + \
              open("docs/HISTORY.txt").read(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='fwt 4teamwork key value storage sqlalchemy',
    author='%s, 4teamwork GmbH' % maintainer,
    author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
    url='http://psc.4teamwork.ch/dist/ftw-dictstorage/',
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
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """
    )
