"""
Utility File for Pdf generator Project
Errors Implementation
Required Functions Implementation
PDF Options:
1- Otp Pdf
2- Certificate Pdf
3- Result.pdf
"""
import os
import random
import string


def generate_file_path(filename):
    """function to generate random filepath"""
    return os.path.join(f"{os.getcwd()}/PDFs/",
                        "{filename}_{suffix}.pdf".format(filename=filename,
                                                         suffix=''.join(random.choices(string.ascii_letters, k=5))))


def custom_print(msg: str) -> None:
    """
    Function for Print Statement to print in better format
    @param msg: str
    @return: None
    """
    print(f"{msg}".center(50, "-"))
