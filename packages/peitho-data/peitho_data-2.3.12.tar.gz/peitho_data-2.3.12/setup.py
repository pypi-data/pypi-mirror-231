from setuptools import setup, find_packages

setup(
    name="peitho_data",
    version="2.3.12",
    description="An opinionated Python package on Big Data Analytics",
    url="https://github.com/QubitPi/peitho-data",
    author="Jiaqi liu",
    author_email="jack20220723@gmail.com",
    license="Apache-2.0",
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        "bs4",
        "opencv-python",
        "numpy",
        "wordcloud",
        "pycodestyle",
        "requests",
        "sphinx-rtd-theme",
        "matplotlib",
        "ebooklib",
        "requests_mock",
    ],
    zip_safe=False,
    include_package_data=True
)
