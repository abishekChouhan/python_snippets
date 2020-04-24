import logging


#############################################
##########      BASIC LOGGING     ###########
#############################################

# Logging levels: DEBUG < INFO < WARNING < ERROR < CRITICAL

# To over write the log file use, filemode='w+'
logging.basicConfig(filename='test.log', level=logging.DEBUG, filemode='w+',
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    return x + y


def divide(x, y):
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))


###############################################
##########      ADVANCED LOGGING     ###########
################################################


# # Create logger object
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# # Format for display log
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# # for writing logs to file
# file_handler = logging.FileHandler('sample.log')
# file_handler.setLevel(logging.ERROR)  # Only error logs are written in file
# file_handler.setFormatter(formatter)  # set formatter

# # To print logs in terminal
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
# # Note:  Level is not set for stream_heldler,
# #        it will take logger object's level i.e. DEBUG


# # Assign different handler
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)


# def add(x, y):
#     return x + y


# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         logger.exception('Tried to divide by zero')
#     else:
#         return result


# num_1 = 10
# num_2 = 12

# add_result = add(num_1, num_2)
# logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))


# div_result = divide(num_1, num_2)
# logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
