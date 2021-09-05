from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()


setup(
    name="pantomime",
    version="0.4.2",
    description="MIME type normalisation and labels.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="mime mimetypes file types",
    author="Journalism Development Network, Inc.",
    author_email="data@occrp.org",
    url="http://github.com/alephdata/pantomime",
    license="MIT",
    packages=find_packages(exclude=["ez_setup", "examples", "test"]),
    namespace_packages=[],
    package_data={},
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    install_requires=[
        "six >= 1.11.0",
        "banal >= 0.3.5",
        "normality >= 0.5.6",
    ],
    tests_require=["nose"],
    entry_points={},
    extras_require={
        "dev": [
            "wheel>=0.29.0",
            "twine",
            "mypy",
            "black",
            "flake8>=2.6.0",
            "nose",
            "banal",
            "coverage>=4.1",
        ]
    },
)
