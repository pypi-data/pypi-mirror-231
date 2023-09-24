from setuptools import setup, find_packages

setup(
    name='msdataviewer',\
    version='1.0.0',\
    description='A package for handling SQT format ProLucid search files',\
    author='Prashanth Ciryam',\
    author_email='psciryam@gmail.com',\
    url='https://github.com/prashanthciryam/DataViewer', # Replace with your GitHub URL\
    packages=find_packages(),\
    install_requires=[
        'pandas>=1.0.0',  # Replace with your desired version
        'biopython>=1.78',  # Replace with your desired version
        'pyteomics>=4.4',  # Replace with your desired version
        'PyQt5>=5.15',  # Replace with your desired version
        'numpy>=1.18',  # Replace with your desired version
        'sqtIO>=0.1.1'  # Replace with your desired version, if it's a package from PyPI or another source
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',\
        'Intended Audience :: Science/Research',\
        'License :: OSI Approved :: MIT License',\
        'Programming Language :: Python :: 3',\
        'Programming Language :: Python :: 3.6',\
        'Programming Language :: Python :: 3.7',\
        'Programming Language :: Python :: 3.8',\
        'Programming Language :: Python :: 3.9',\
        'Programming Language :: Python :: 3.10',\
        'Programming Language :: Python :: 3.11'
    ],
    entry_points = {
    'console_scripts': [
        'msdataviewer=msdataviewer.__main__:run_msdataviewer'
    ]
}
)
