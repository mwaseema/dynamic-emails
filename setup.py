import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynamic-emails-mwaseema",
    version="0.0.1",
    author="M. Waseem Ashraf",
    author_email="mohammadwaseem043@gmail.com",
    description="A small package for sending emails dynamically",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mwaseema/dynamic-emails",
    project_urls={
        "Bug Tracker": "https://github.com/mwaseema/dynamic-emails/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'tqdm'
    ],
)
