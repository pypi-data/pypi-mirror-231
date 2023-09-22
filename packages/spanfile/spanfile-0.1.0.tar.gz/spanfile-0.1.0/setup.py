from setuptools import setup, find_packages

setup(
    name="spanfile",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A brief description of your package",
    packages=find_packages(),
    package_data={'mynewtimefile': ['data/*.txt']},
    py_modules=['ntime'],
    license='BSD License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)