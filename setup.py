from setuptools import setup, find_packages

version = open('src/ftw/dictstorage/version.txt').read().strip()
maintainer = 'Rok Garbas'

tests_require = [
            'unittest2',
            'plone.testing',
            ]

setup(
    name='ftw.dictstorage',
    version=version,
    description="",
    long_description=open("README.rst").read(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='fwt 4teamwork key value storage sqlalchemy',
    author='%s, 4teamwork GmbH' % maintainer,
    author_email='rok@garbas.si',
    url='gitolite@git.4teamwork.ch:ftw/ftw.dictstorage.git',
    license='GPL',
    packages = find_packages('src', exclude=['ez_setup']),
    package_dir = {'':'src'},
    namespace_packages=['ftw'],
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.component'
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
