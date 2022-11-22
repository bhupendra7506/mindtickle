from configurations import genericConfig, serverConfig
from services.utils.commonUtils import loggerUtils

if __name__ == "__main__":
    genericConfig.ENVIRONMENT = "prod"
    logger = loggerUtils.Logger()

