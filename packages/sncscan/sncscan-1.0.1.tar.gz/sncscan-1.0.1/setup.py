from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='sncscan',
    version='1.0.1',
    packages=[''],
    url='https://github.com/usdAG/sncscan',
    license='GPLv3',
    author='Jonas Wamsler, Nicolas Schickert',
    author_email='jonas.wamsler@usd.de',
    description='sncscan: Tool for analyzing SAP Secure Network Communications (SNC).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points = {
        'console_scripts': [
            'sncscan = sncscan:main'
        ]
    }
    )

