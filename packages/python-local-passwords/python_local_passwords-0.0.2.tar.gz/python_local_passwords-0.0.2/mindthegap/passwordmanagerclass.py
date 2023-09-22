from cryptography.fernet import Fernet
from typing import Optional

class PythonPasswords:
    """
    A class for encrypting and decrypting passwords using the Fernet encryption algorithm.

    This class initializes the Fernet cipher suite using a key file. The key file path
    should be provided when creating an instance of the class. However if you are using 
    the class for the first time, you should create the key by calling the create key method.
    This key can be saved anywhere on your harddrive, the default location is in the root
    directory of the C: drive. 

    Attributes:
        cipher_suite (Fernet): The Fernet cipher suite for encryption and decryption.

    Args:
        path_to_key (str, optional): The file path to the key file. Defaults to 'C:/password_key.txt'.

    Note:
        The key file should contain a valid Fernet key in bytes format.
    """

    def __init__(self, path_to_key: Optional[str] = 'C:/password_key.txt'):
        """
        Initializes an instance of the PythonPasswords class.

        Args:
            path_to_key (str, optional): The file path to the key file. Defaults to 'C:/password_key.txt'.

        Initializes the Fernet cipher suite using the key from the specified file.
        """

        with open(path_to_key, 'rb') as file:
            for key in file:
                self.cipher_suite = Fernet(key)

    def encrypt(self, password):
        """
        Encrypts the given password.

        Args:
            password (str): The password to be encrypted.

        Returns:
            str: The encrypted password as a string.

        Note:
            The password must be in string format before encrypting.
        """

        password = bytes(password, 'utf-8')
        return self.cipher_suite.encrypt(password).decode('utf-8')

    def decrypt(self, password):
        """
        Decrypts the given password.

        Args:
            password (str): The password to be decrypted.

        Returns:
            str: The decrypted password as a string.

        Note:
            The password must be in string format before decrypting.
        """
        password = bytes(password, 'utf-8')
        return self.cipher_suite.decrypt(password).decode('utf-8')

    def create_key(self):
        """
        Generates a new Fernet key and returns it as a string.

        Returns:
            str: The generated Fernet key as a string.
        """
        return Fernet.generate_key().decode('utf-8')
