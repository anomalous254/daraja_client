from setuptools import setup, find_packages

setup(
    name="daraja_client",  # Replace with your package name
    version="0.1.3",    # Initial version
    author="Peter Nyando",
    author_email="peternyando2@gmail.com",
    description=(
        "This python module provides a simple way to integrate the Safaricom MPESA Daraja 2.0 API "
        "into your Python projects. It is designed to handle common operations like generating access "
        "tokens, formatting phone numbers, and sending STK Push requests."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anomalous254/daraja_client",  # Replace with your repo URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "idna==3.10",
        "requests==2.32.3",
        "urllib3==2.2.3",
        "python-decouple==3.8",
    ],
)
