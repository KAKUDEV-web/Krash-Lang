"""Setup script for Krash Programming Language."""

from setuptools import setup, find_packages

setup(
    name="krash",
    version="1.0.0",
    description="Krash Programming Language - An interpreted language with clear, readable syntax",
    author="Krash Community",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'krash': ['stdlib/*.py'],
    },
    entry_points={
        'console_scripts': [
            'krsh=krash.cli:main',
        ],
    },
    python_requires='>=3.7',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Interpreters',
    ],
)
