import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'click==6.7',
    'numpy==1.15.0',
    'opencv-python==3.4.2.17'
]

tests_require = [
    'pytest==3.6.1',
    'pytest-cov==2.5.1'
]

setup(
    name='subimage',
    version='0.0',
    description='subimage',
    long_description=README,
    classifiers=[
        'Programming Language :: Python'
    ],
    author='Felipe Godói Rosário',
    author_email='felipe.rosario@gmail.com',
    url='',
    keywords='waldo',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'subimage = subimage.scripts:cli'
        ],
    },
)
