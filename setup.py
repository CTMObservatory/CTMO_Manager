from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='ctmomanager',
      version='1.0a1',
      description='CTMO Automation System',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='GAIA Dev Team',
      author_email='ctmo@utrgv.edu',
      url='https://github.com/CTMObservatory',
      py_modules=['scheduler', 'telescope'],
      install_requires=['pyyaml'],
      entry_points={
        'console_scripts': [
            'scheduler = scheduler:serve',
            'telescope = telescope:serve',
        ],
      },
      test_suite='tests',
      )
