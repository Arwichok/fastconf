import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastconf",
    version="1.0.0",
    author="Arwichok",
    keywords="config",
    license="MIT",
    author_email="arwichok@gmail.com",
    description="A simple config lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arwichok/fastconf",
    packages=setuptools.find_packages(),
    install_requires=[
        'pyyaml',
    ]
)