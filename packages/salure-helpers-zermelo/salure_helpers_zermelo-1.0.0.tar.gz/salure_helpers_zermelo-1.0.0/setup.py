from setuptools import setup


setup(
    name='salure_helpers_zermelo',
    version='1.0.0',
    description='Zermelo wrapper from Salure',
    long_description='Zermelo wrapper from Salure',
    author='D&A Salure',
    author_email='support@salureconnnect.com',
    packages=["salure_helpers.zermelo"],
    license='Salure License',
    install_requires=[
        'salure-helpers-salureconnect>=1',
        'pandas>=1,<=1.35',
        'requests>=2,<=3'
    ],
    zip_safe=False,
)