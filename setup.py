from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name='fastagi_tools',
    version='1.0.8',
    description='fastagi-tools is a python library specifically designed for developers working with FastAGI. The library offers the BaseToolkit and BaseTool classes, requierd for development of custom tools and toolkits for FastAGI.',
    author='fastagi',
    author_email='info@fastagi.khulnasoft.com',
    packages=find_packages(),
    install_requires=['pydantic==1.10.13', 'PyYAML==6.0'],
    long_description=long_description,  # Include the README.md contents here
    long_description_content_type="text/markdown",  # Specify the content type

)
