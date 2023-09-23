import sys

def error_message_detail(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info                 # .exc_info PROVIDES INFORMATION ABOUT THE EXCEPTION
                                                        # THE exe_tb -> FILE PROVIDES THE INFORMATIO ABOUT WHERE THE ERROR HAS OCCURED IN THE FILE, LINE WHERE THE ERROR OCCURED
    
    file_name = exc_tb.tb_frame.f_code.co_filename      # USED TO TRACK BACK OBJECT 
                                                        # tb_frame    -> FRAME IN WHICH THE ERROR OCCURED
                                                        # f_code      -> REPRESENTS THE CODE OBJECT FRAME
                                                        # co_filename -> STORES THE NAME OF THE PYTHON CODE FILE IN WHICH THE ERROR OCCURES

    error_message = "error occured in python \nscript name [{0}] \nline number [{1}] error message [{2}]".format(
                                                                                                                    file_name,
                                                                                                                    exc_tb.tb_lineno,
                                                                                                                    str(error)
                                                                                                                )
    return error_message
    
# Exception it's a built-in base class for all exceptions.
class Customexception(Exception):
    def __init__(self,error_message,error_detail:sys):
        # SUPER IS USED TO CALL THE PARENT CLASS THAT IS Exception class
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self) -> str:
        return self.error_message
