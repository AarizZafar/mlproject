import logging
import os
from datetime import datetime

logs_path = os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# IF THE FILE IS RUNNED DIRECTLY THEN THE __name__ VARIABLE WILL BE SET TO __main__ 
if __name__ == "__main__":
    logging.info("Logging has started")     # WE HAVE NOT SPECIFIED A LOGGER LIKE BELOW 
                                            # HENCE WE END UP USIG THE ROOT LOGGER IT RETURNS ROOT


    # ------------------------------ OR ------------------------------------------
# logger1 = logging.getLogger("ML proj Logger")
# logger1.info("test run")
