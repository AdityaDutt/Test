import setuptools
from setuptools import find_packages
from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Test',
    author = 'Aditya Dutt',
    author_email = 'aditya.dutt@ufl.edu',
    license='MIT',
    description="Testing...",
    long_description=long_description,    
    long_description_content_type="text/markdown",    
    version='0.0.1',
    requires = ["setuptools", "wheel"],
    include_package_data=True,

    install_requires=['numpy'],
    python_requires='>=3.7.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        "Operating System :: OS Independent",
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

    ]
)