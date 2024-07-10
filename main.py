"""
Main File for the Process of PDF Generator
"""

from constants import PDF_OPTIONS, CERTIFICATE_SUCCESS, OTP_SUCCESS, RESULT_SUCCESS
from pdf_generator import PdfGenerator
from utils import custom_print


def main() -> None:
    """
    Driver Code
    @return: None
    """
    try:
        custom_print("Welcome to PDF Generator")
        filename = input("Please Enter Result filename: ")
        pdf_obj = PdfGenerator(filename)
        print(
            f"Choose Options of PDF Generator"
            f"\n{PDF_OPTIONS}\n"
            f"Must be in Number Format From Valid Options"
        )
        while True:
            option = input("Choose: ")
            if option.lower() == "c":
                custom_print("Thank you For Using")
                return
            elif int(option) == PDF_OPTIONS.get("OTP_GENERATE_PDF"):
                custom_print("OTP PDF")
                pdf_obj.otp_pdf_generate()
                custom_print(OTP_SUCCESS)
                break
            elif int(option) == PDF_OPTIONS.get("CERTIFICATE_PDF"):
                custom_print("Certificate  PDF")
                pdf_obj.certificate_pdf_generate()
                custom_print(CERTIFICATE_SUCCESS)
                break
            elif int(option) == PDF_OPTIONS.get("RESULT_PDF"):
                custom_print("Result PDF")
                pdf_obj.result_pdf_generate()
                custom_print(RESULT_SUCCESS)
                break
            else:
                print("Choose Valid Option Else Press C/c to Cancel")
    except ValueError as ve:
        print(ve)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
