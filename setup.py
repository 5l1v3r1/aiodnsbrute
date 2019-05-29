"""
Brute force DNS domain names asynchronously
"""
from setuptools import find_packages, setup

dependencies = ['click', 'asyncio', 'uvloop', 'tqdm', 'aiodns']

setup(
    name='aiodnsbrute',
    version='0.2.0',
    url='https://github.com/blark/aiodnsbrute',
    license='BSD',
    author='Mark Baseggio',
    author_email='mark@basegg.io',
    description='Brute force DNS domain names asynchronously',
    long_description=__doc__,
    include_package_data=True,
    package_data={'aiodnsbrute': ['wordlists/*']},
    zip_safe=False,
    platforms='any',
    python_requires='>=3.5',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'aiodnsbrute = aiodnsbrute.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
