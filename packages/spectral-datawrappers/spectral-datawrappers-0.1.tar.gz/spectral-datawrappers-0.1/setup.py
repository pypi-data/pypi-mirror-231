from setuptools import setup, find_packages

setup(
    name='spectral-datawrappers',  # Name of your package
    version='0.1',  # Version number
    # Automatically discover all packages and subpackages. Alternatively, you can specify the package names.
    packages=find_packages(),
    install_requires=[
    ],
    author='Spectral Finance',
    author_email='maciej@spectral.finance',
    description='Datawrappers for Spectral Finance',
    # You can use a README file to provide a longer description
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # If using a markdown README file
    # Link to the source code or the project website
    url='https://github.com/Spectral-Finance/spectral-datawrappers',
    classifiers=[
        'License :: OSI Approved :: MIT License',  # Example license
        # Specify which python versions your package works on
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    # Optionally include package data
    # This will include any non-python files specified in your MANIFEST.in
    include_package_data=True,
    keywords='machine learning ai data science web3',
    entry_points={
        'console_scripts': [  # This allows creating command-line scripts from your package's functions
            # This will create a command-line script named 'myscript' which will execute 'myfunction' from 'mymodule' in 'mypackage'
            'myscript=mypackage.mymodule:myfunction',
        ],
    },
    python_requires='>=3.7',  # Minimum python version
)
