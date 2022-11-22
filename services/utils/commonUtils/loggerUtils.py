import logging, os, sys
import time
import datetime

import mindtickle.configurations.genericConfig as genericConfig

class Logger():
    logSaveLocationDir = None
    logFile = None
    logFileSaveLocation = None
            
    def __init__(self):
        '''
        Initialize Logger Instance
        '''
        
        self.logSaveLocationDir = os.path.dirname(__file__)
        
        if not os.path.exists(self.logSaveLocationDir):
            os.makedirs(self.logSaveLocationDir)
    
        self.logFile = self.logSaveLocationDir + os.sep + 'automation.log'
        logger = logging.getLogger('')    
        
        hdlr = logging.FileHandler(self.logFile)
        formatter = logging.Formatter('%(asctime)s - %(filename)s  - %(lineno)d - %(levelname)s - %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr) 
        logger.setLevel(logging.INFO)
        
        ''' Printing logs to console as well'''
        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)

        genericConfig.logObj = logger
         
    def getTimeStamp(self):
        '''
        Get current Timestamp
                
        '''
        timestampInSecs = time.time()
        timestamp = datetime.datetime.fromtimestamp(timestampInSecs).strftime('%Y-%m-%d-%H-%M-%S-%f')
        return timestamp