import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nstdpkg",
    version="0.0.1",
    author="han-solo",
    author_email="han-solo@fatcatsbbs.com",
    description="A sample nested package example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="",
    #packages=setuptools.find_packages(),
    packages=['nstdpkg', 'nstdpkg.inner'],
    package_data = {'nstdpkg': ["data.json"]},
    install_requires=[
        'attrs',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
