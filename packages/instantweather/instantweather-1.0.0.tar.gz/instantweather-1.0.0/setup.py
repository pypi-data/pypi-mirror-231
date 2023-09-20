from setuptools import setup
setup(
    name='instantweather',
    packages=['instantweather'],
    version='1.0.0',
    license='MIT',    
    description='weather forecast data',
    author='Anuj Pandey',    
    url='https://github.com/newguy7/instantweather',
    keywords=['weather','forecast','openweather'],    
    install_requires=[
        'requests',
        'os',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)