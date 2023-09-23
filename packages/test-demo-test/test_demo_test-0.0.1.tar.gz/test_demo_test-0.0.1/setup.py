import setuptools

setuptools.setup(
    # packages=['test_demo'],
    name="test_demo_test",
    version="0.0.1",
    author="xxxxxx",
    author_email="admin@baidu.com",
    description="A test package",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",

)









