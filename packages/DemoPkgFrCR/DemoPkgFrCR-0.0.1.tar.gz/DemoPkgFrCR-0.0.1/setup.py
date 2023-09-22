import setuptools

setuptools.setup(
    name="DemoPkgFrCR",
    version="0.0.1",
    author="Ratnakar Kumbhar",
    author_email="ratnakar.kumbhar@crunchyroll.com",
    description="File loading through Package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)