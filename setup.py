from setuptools import setup

setup(name='scheduler',
      version='0.0',
      description='Job Manager for CTMO System',
      author='TOROS Dev Team',
      author_email='ctmo@utrgv.edu',
      url='https://toros.utrgv.edu',
      py_modules=['scheduler', ],
      install_requires=[],
      entry_points={
        'console_scripts': [
            'epimetheus = scheduler:service',
        ],
      },
      test_suite='tests',
      )
