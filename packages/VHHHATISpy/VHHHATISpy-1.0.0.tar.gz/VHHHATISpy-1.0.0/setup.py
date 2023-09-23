from setuptools import setup, find_packages

with open("README.md", "r") as f:
  long_description = f.read()

setup(
    name='VHHHATISpy',
    version='1.0.0',
    description='Fetch ATIS data for Hong Kong International Airport.',
    author='William NG',
    author_email='Williamntw.Website@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4==4.12.2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ]
)