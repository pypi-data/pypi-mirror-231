from setuptools import setup, find_packages

setup(
    name='nikeidproductscraper',
    version='0.3',
    description='A Python package for scraping Nike Indonesia website.',
    author='hasan ash ',
    author_email='hasan40p30m@gmail.com',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas>=2.1',
        'httpx>=0.25.0',
        'playwright>=1.38.0',
        'selectolax>=0.3.16',
    ],
    setup_requires=['setuptools>=44'],
)
