from setuptools import setup, find_packages


setup(
    name='biosimulators-simularium',
    version='0.2.1',
    packages=find_packages(),
    url='https://github.com/biosimulators/Biosimulators_simularium',
    author='Alexander Patrie/BioSimulators Team',
    author_email='info@biosimulators.org',
    install_requires=[
        'zarr',
        'simulariumio[tutorial]',
        'smoldyn==2.72',
    ],
    entry_points={
            'console_scripts': [
                'biosimulators-simularium = biosimulators_simularium.__main__:main',
            ],
    },
)
