import logging

import azure.functions as func

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(
        "Hello",  # This is the response
        status_code=200
    )
