from setuptools import setup, find_packages

setup(
    name="parallel-podcast-parser",  # pip install parallel-podcast-parser
    description="High performance parallel podcast RSS feed parser written in Rust. Platform independent.",
    # long_description=open('README.md', 'rt').read(),
    version="0.3.3",
    author="Filip Alexandrov",
    author_email="filipalexandrov28@gmail.com",
    url="https://github.com/impactfactor-app/parallel-podcast-parser",
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
