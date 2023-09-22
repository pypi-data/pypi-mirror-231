from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'A package for key generation, encrypting and decrypting passwords'
LONG_DESCRIPTION =''' This class initializes the Fernet cipher suite using a key file. The key file path
    should be provided when creating an instance of the class. However if you are using 
    the class for the first time, you should create the key by calling the create key method.
    This key can be saved anywhere on your harddrive, the default location is in the root
    directory of the C: drive. '''

# Setting up
setup(
    name="python_local_passwords",
    version=VERSION,
    author="dave_the_noob",
    author_email="dave.dawson86@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['typing','cryptography'],
    keywords=['python', 'encryption', 'passwords', 'decrypting', 'key generation',],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)