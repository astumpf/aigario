try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='aigario',
      packages=['aigario'],
      py_modules=['aigario'],
      version='0.0.1',
      description='Artificial intelligence experiment living in Agario',
      author='astumpf',
      author_email='stumpf@sim.tu-darmstadt.de',
      url='https://github.com/astumpf/aigario',
      license='GPLv3',
      install_requires=[
          'agarnet >= 0.1.3',
          'gagar >= 0.1',
      ],
      entry_points={'gui_scripts': ['gagar = gagar.main:main']},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: X11 Applications :: GTK',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Education',
          'Topic :: Games/Entertainment',
          'Topic :: Games/Entertainment :: Simulation',
      ],
)
