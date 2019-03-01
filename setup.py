from setuptools import setup

# Get the version from the scheduler.py file itself (not imported)
with open('scheduler.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            _, _, sch_version = line.replace("'", '').split()
            break

setup(name='scheduler',
      version=sch_version,
      description='Job Manager for CTMO System',
      author='TOROS Dev Team',
      author_email='ctmo@utrgv.edu',
      url='https://toros.utrgv.edu',
      py_modules=['scheduler', ],
      install_requires=[],
      entry_points={
        'console_scripts': [
            'epimetheus = scheduler:serve',
        ],
      },
      test_suite='tests',
      )
