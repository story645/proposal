import setuptools

setuptools.setup(
    packages=setuptools.find_packages(
        include = ["matplottoy.*"], exclude=['notebooks']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)