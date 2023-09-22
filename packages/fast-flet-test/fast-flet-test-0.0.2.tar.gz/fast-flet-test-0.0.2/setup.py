from setuptools import setup,find_packages

with open("./README.md", "r", encoding="utf-8") as e:
    long_description = e.read()

VERSION = "0.0.2"
DESCRIPCION = "Fast-Flet is a package built as a complement to Flet, which makes it easier to handle flet events, designed to work with numerous pages of your app built with. It also provides a better MVC construction of your code, which can be scalable and easy to read. but it not only limits the MVC model but you can adapt it according to your preferences."


setup(
    name="fast-flet-test", 
    version=VERSION,
    author='Jrxvx',
    description=DESCRIPCION,
    long_description=long_description,
    url='https://github.com/Jrxvx/Fast-Flet',
    long_description_content_type="text/markdown",
    download_url='https://github.com/Jrxvx/Fast-Flet',
    project_urls = {
        "Bug Tracker":"https://github.com/Jrxvx/Fast-Flet/issues"
    },
    packages=find_packages(),
    package_data={
        "commands": [
            "templates/*",
            "templates/*/*",
            "templates/*/*/*",
            "templates/*/*/*/*",
            "templates/*/*/*/*/*",
        ],
    },
    install_requires=[
        "typer[all]",
        "flet",
        "flet_fastapi",
        "uvicorn",
        ],
    classifiers={
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: Apache License 2.0",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    },
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "fast-flet=commands.cli:cli",
        ],
    },
    keywords=[
        "python web template",
        "flet",
        "app python",
        "flet mvc",
        "fast flet mvc",
        "fast flet",
        "flet-fastapi",
        "flutter python",
        "flet personalized",
        "web application",
        "development"
        ],
    
)