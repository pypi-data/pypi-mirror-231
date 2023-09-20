from setuptools import setup, find_packages


setup(
    name='biosimulators-simularium',
    version='0.2.3',
    packages=find_packages(),
    url='https://github.com/biosimulators/Biosimulators_simularium',
    author='Alexander Patrie/BioSimulators Team',
    author_email='info@biosimulators.org',
    install_requires=[
        'zarr',
        'simulariumio[tutorial]',
        'smoldyn',
        'biosimulators-utils'
    ],
    entry_points={
            'console_scripts': [
                'biosimulators-simularium = biosimulators_simularium.__main__:main',
            ],
    },
)
