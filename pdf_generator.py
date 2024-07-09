"""
Python File to Generate PDF
"""
import pdfkit

from constants import UNKNOWN_ERROR, OS_ERROR, OTP_PDF_HTML, CERTIFICATE_PDF_HTML, RESULT_PDF_HTML
from utils import custom_print, generate_file_path


class PdfGenerator:
    """
    Class to Implement PDF Generation Process
    """

    def __init__(self, filename):
        self.filename = filename

    def otp_pdf_generate(self) -> None:
        """
        method for process of otp pdf generation
        @return: None
        """
        try:
            custom_print("OTP PDF Generator")
            print("Required Data: otp: Number")
            otp = int(input("Enter the OTP: "))
            pdfkit.from_string(OTP_PDF_HTML.format(otp=otp),
                               generate_file_path(self.filename))
        except ValueError as ve:
            print("OTP Should be Number", ve)
            return
        except Exception as err:
            print(UNKNOWN_ERROR, err)
            return

    def certificate_pdf_generate(self) -> None:
        """
        method for process of certificate pdf generation
        @return: None
        """
        try:
            custom_print("Certificate PDF Generator")
            print("Required Data: Name: Text, Rank: Text")
            name = input("Enter the Name: ")
            rank = input("Enter the Rank: ")
            pdfkit.from_string(CERTIFICATE_PDF_HTML.format(name=name, rank=rank),
                               generate_file_path(self.filename))
        except Exception as err:
            print(UNKNOWN_ERROR, err)
            return

    def result_pdf_generate(self) -> None:
        """
        method for process of result pdf generation
        @return: None
        """
        try:
            custom_print("Result PDF Generator")
            print("Required Data: "
                  "Name: Text, "
                  "Marks(Subject(Hindi: Number, English: Number, Science: Number, Maths: Number))")
            name = input("Enter Student Name: ")
            hindi = int(input("Enter Hindi Marks"))
            english = int(input("Enter English Marks"))
            science = int(input("Enter Science Marks"))
            maths = int(input("Enter Maths Marks"))
            if 0 < hindi < 101 and 0 < english < 101 and 0 < science < 100 and 0 < maths < 100:
                pdfkit.from_string(RESULT_PDF_HTML.format(name=name,
                                                          hindi=hindi,
                                                          english=english,
                                                          science=science,
                                                          maths=maths),
                                   generate_file_path(self.filename))
        except ValueError as ve:
            print("OTP Should be Number", ve)
            return
        except Exception as err:
            print(UNKNOWN_ERROR, err)
            return
