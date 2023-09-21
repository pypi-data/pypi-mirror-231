import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AUDT", # Replace with your own PyPI username(id)
    version="1.1.4",
    author="Juwon Kim",
    author_email="jwkim1094g5@gmail.com",
    description="Auzre Usage Data Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/nicecoding1/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)