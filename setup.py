from setuptools import setup, find_packages


def get_git_version(abbrev=4):
    from subprocess import Popen, PIPE
    try:
        p = Popen(['git', 'rev-parse', 'HEAD'],
                  stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        line = p.stdout.readlines()[0]
        return '-' + line.strip()[:abbrev]
    except:
        return ''

version = '2.1.8.dev0' + get_git_version()

setup(name='plone.app.iterate',
      version=version,
      description="check-out/check-in staging for Plone",
      long_description=\
          open("README.txt").read() + "\n" + \
          open("CHANGES.txt").read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.app.iterate',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages = ['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'Products.PloneTestCase',
        ]
      ),
      install_requires=[
          'setuptools',
          'plone.locking',
          'plone.memoize',
          'zope.annotation',
          'zope.component',
          'zope.event',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.lifecycleevent',
          'zope.schema',
          'zope.viewlet',
          'Acquisition',
          'DateTime',
          'Products.Archetypes',
          'Products.CMFCore',
          'Products.CMFEditions',
          'Products.CMFPlacefulWorkflow',
          'Products.DCWorkflow',
          'Products.statusmessages',
          'ZODB3',
          'Zope2',
      ],
      entry_points = '''
          [z3c.autoinclude.plugin]
          target = plone
      ''',
      )
