import logging

#%%
logger = logging.getLogger("my_app")
id(logger)

another_logger = logging.getLogger("my_app")
id(another_logger)

id(logging.Logger("my_app"))

#%%
logging_levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
for logging_level in logging_levels:
    print(f"Logging Level {logging._levelToName[logging_level]}: {logging_level}")

#%%
logger = logging.getLogger("my_app")
logger.setLevel(logging.WARNING)

#%%
# Add a file handler
fh = logging.FileHandler("my_app_logging.log")
logger.addHandler(fh)

# Send some log events
logger.error("This is an error message.")
logger.critical("This is a critical message.")
logger.info("This is an info message.")

# Check the log
with open("my_app_logging.log") as file:
    print(file.read())

#%%
# for handler in logger.handlers:
#     logger.removeHandler(handler)

# Add a stream handler
sh = logging.StreamHandler()
logger.addHandler(sh)

logger.critical("Just a random critical event.")

#%%
logger.critical("This is a critical message.")
logger.error("This is an error message.")
logger.warning("This is a warning message.")
logger.info("This is an info message.")
logger.debug("This is a debug message.")

#%%
logger.removeHandler(sh)

# Create a new file handler with formatting
fh = logging.FileHandler("formatted_log.log")
fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(fh_formatter)
logger.addHandler(fh)

# Logging events
logger.warning("Warning message with formatting")
logger.error("Error message with formatting")
logger.critical("Critical message with formatting")

# Check the log
with open("formatted_log.log") as file:
    print(file.read())
