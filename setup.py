from setuptools import setup, find_packages

setup(
    name="image_classification_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "tensorflow",
        "matplotlib",
        "scikit-learn"
    ],
)