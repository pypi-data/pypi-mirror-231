from setuptools import setup, find_packages

setup(
    name='nanomotif',
    version='0.0.1',
    description='Identifying methlyation motifs in nanopore data',
    author='AAU_DarkScience',
    author_email='shei@bio.aau.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    entry_points={
            'console_scripts': [
                  'nanomotif = nanomotif.main:main'
            ]
    }
)