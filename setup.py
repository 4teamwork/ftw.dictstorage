from setuptools import setup, find_packages


version = '0.1'

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
    author='Rok Garbas',
    author_email='rok@garbas.si',
    url='gitolite@git.4teamwork.ch:ftw/ftw.dictstorage.git',
    license='GPL',
    packages = find_packages('src', exclude=['ez_setup']),
    package_dir = {'':'src'},
    namespace_packages=['ftw'],
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.interface',
        'zope.component'
      ],
      extras_require=dict(
        saconfig= [
            'z3c.saconfig',
        ],
        tests = [
            'unittest2',
            'plone.testing',
        ],
    ),
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """
      )
