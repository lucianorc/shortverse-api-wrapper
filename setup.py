import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shortverse_api_wrapper",
    author="Luciano Costa",
    author_email="lcosta_96@hotmail.com.br",
    description="API Wrapper written in Python for Shortverse API",
    keywords="shortverse, wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucianorc/shortverse-api-wrapper",
    project_urls={},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        # see https://pypi.org/classifiers/
    ],
    python_requires=">=3.10",
    install_requires=["requests"],
    extras_require={
        "dev": ["black", "ipython"],
        "test": ["pytest", "pytest-cov", "vcrpy"],
    },
)
