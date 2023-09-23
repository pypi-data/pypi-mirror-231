from setuptools import setup, find_packages

requirements = [
    "requests",
    "websocket-client",
    "bs4",
    "setuptools"
]

long_description ="""Made by nxSlayer"""

setup(
    name="tools_ai",
    license="MIT",
    author="nxSlayer",
    version="1.1.0",
    author_email="princediscordslay@gmail.com",
    description="Library for ai tools",
    url="https://github.com/nxSlayer/tools_ai",
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    install_requires=requirements,
    keywords=[
        'tools_ai',
        'toolsai',
    ],
    python_requires='>=3.8',
)