import sys
import logging

def get_exception_details(exc, exc_details:sys)->str:
    _, _, exc_tab = exc_details.exc_info()
    file_name = exc_tab.tb_frame.f_code.co_filename
    line_no = exc_tab.tb_lineno
    exc_message = f"""Exception occured in a python script 
        Filename: {file_name}
        Line no: {line_no} 
        Exception message: {exc_message}"""
    return exc_message

class CustomException(Exception):
    def __init__(self, exc_details:sys, exc_msg):
        super().__init__(exc_msg)
        self.exc_msg = get_exception_details(exc_msg, exc_details)
     
    def __str__(self):
        return self.exc_msg