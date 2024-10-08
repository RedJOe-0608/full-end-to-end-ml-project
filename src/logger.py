import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #This line of code generates the full path to a log file (named LOG_FILE) located inside the "logs" folder in the current working directory.
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) 
#logs/08_23_2024_11_46_29.log/08_23_2024_11_46_29.log(this is the actual log file)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# for testing if exception.py file is working or not
# if __name__=="__main__":
#     logging.info("Logging has started")