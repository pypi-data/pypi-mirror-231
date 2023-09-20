from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()


VERSION = '0.1.1'


setup(
    name='patch-aiohttp-requests',
    zip_safe=False,
    version=VERSION,
    description=('Simple patching of `aiohttp` requests'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[],
    keywords=['aiohttp', 'requests', 'tests', 'mock', 'patch'],
    author='Teemu Husso',
    author_email='teemu.husso@gmail.com',
    url='https://github.com/Raekkeri/patch-aiohttp-requests',
    py_modules=['patch_aiohttp_requests'],
    install_requires=['setuptools'],
)
