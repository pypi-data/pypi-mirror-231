from setuptools import setup

setup(
    name='resumer',
    version='0.2.0',
    packages=["resumer", "resumer.gen", "resumer.engines"],
    description="pandoc based generator with advanced filter support",
    author="Zackary W",
    # include .tex and license
    include_package_data=True,
    package_data={'': ['LICENSE.txt', "awesome-cv.cls", "awesome.tex"]},
    license="MIT",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zackaryw/resumer",
    install_requires=[
        "pydantic",
        "click",
    ],

    entry_points={
        'console_scripts': [
            'resumer = resumer.cli:main',
        ]
    }
)