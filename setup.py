from os.path import join, dirname, abspath

from setuptools import setup, find_packages

from prettypy import __version__

curdir = abspath(dirname(__file__))
readme = open(join(curdir, 'README.rst')).read()

setup(
    name             = 'prettypy',
    packages         = find_packages(),
    version          = __version__,
    description      = 'Python Pretty Printer',
    long_description = readme,
    keywords         = ['testing', 'logging', 'debugging'],
    url              = 'https://github.com/louis-riviere-xyz/prettypy',
    author           = 'Louis RIVIERE',
    author_email     = 'louis@riviere.xyz',
    license          = 'MIT',
    classifiers      = [
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Testing',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3',
    ],
)
