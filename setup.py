from setuptools import setup

long_description = """
Python bindings for Nutritionix API.

See the repo home for usage instructions at
 https://github.com/leetrout/python-nutritionix/
"""

setup(
    name='nutritionix',
    version='0.2',
    description='Nutritionix Python API wrapper',
    long_description=long_description,
    author='Lee Trout',
    author_email='leetrout@gmail.com',
    url='https://github.com/leetrout/python-nutritionix/',
    py_modules=['nutritionix'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
)
