from setuptools import find_packages, setup

setup(
    name="cicdservices",
    version="0.0.1",
    description="CI-CD Services",
    package_dir={"": "cicd"},
    packages=find_packages(where="cicd"),
    author="Novateva",
    author_email="novateva@novateva.com",
    license="MIT",
    python_requires=">=3.6",
    include_package_data=True,
    package_data={
        '': ['.env'],
    },
)
