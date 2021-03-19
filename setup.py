import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="validpy",
    version="0.0.2",
    author="Tegan Hakim",
    author_email="tegan.hakim@gmail.com",
    license="MIT",
    description="A simple validation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeganHakim/validpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
)