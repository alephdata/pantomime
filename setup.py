from setuptools import setup, find_packages


setup(
    name='celestial',
    version='0.2.0',
    description="MIME type processing tools.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='names countries phones domains email country',
    author='Journalism Development Network, Inc.',
    author_email='data@occrp.org',
    url='http://github.com/alephdata/celestial',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    package_data={},
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        'six >= 1.11.0',
        'normality >= 0.5.6',
    ],
    tests_require=['nose'],
    entry_points={}
)
