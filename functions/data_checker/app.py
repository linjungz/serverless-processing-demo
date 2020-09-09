from datetime import datetime
from random import randint
from uuid import uuid4

class DataNotReadyError(Exception):
    pass



def lambda_handler(event, context):
    """Sample Lambda function which mocks the operation of buying a random number
    of shares for a stock.

    For demonstration purposes, this Lambda function does not actually perform any 
    actual transactions. It simply returns a mocked result.

    Parameters
    ----------
    event: dict, required
        Input event to the Lambda function

    context: object, required
        Lambda Context runtime methods and attributes

    """

    print(event)

    is_data_ready = randint(1,100) % 2

    if not is_data_ready :
        print("data is not ready")
        raise DataNotReadyError

    status = {
        'id' : event['id'],
        'status' : 'Data Ready'
    }
    return status

