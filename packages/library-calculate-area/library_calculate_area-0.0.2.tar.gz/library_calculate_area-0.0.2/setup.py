import setuptools

setuptools.setup(
    name="library_calculate_area",
    version="0.0.2",
    author="Yana",
    description="A library that can calculate the area of a circle by radius and a triangle on three sides.",
    url="https://github.com/Yana-K38/library_calculate_area/tree/main",
    readme = "README.md",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)