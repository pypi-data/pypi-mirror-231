from setuptools import setup
setup(
    name = 'mphatoday',          # name of your package
    package = ['mphatoday'],     # same as name of your package
    version = '1.0.0',
    licence = 'MIT',
    description = 'weather app, pulls data from api',
    author = 'Mpatisi',
    author_email = 'mphatomnz@gmail.com',
    keywords =['weather', 'forecast'],
    install_requires=[          # other packages pip needs to install
        'requests',
        ],
classifiers= [
    'Development Status :: 3 - Alpha', # Choose either 3 alpah or Beta
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    ],
)
 
    
    
    
    
