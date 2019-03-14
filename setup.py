from setuptools import setup

with open('ctmomanager/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            _, _, _version = line.replace("'", '').split()
            break

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='ctmomanager',
      version=_version,
      description='CTMO Automation System',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='GAIA Dev Team',
      author_email='ctmo@utrgv.edu',
      url='https://github.com/CTMObservatory',
      packages=['ctmomanager', ],
      install_requires=['pyyaml'],
      entry_points={
        'console_scripts': [
            'scheduler = ctmomanager.scheduler:serve',
            'telescope = ctmomanager.telescope:serve',
        ],
      },
      test_suite='tests',
      )
