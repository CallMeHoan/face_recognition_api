
def response(status: int, message: str, payload: object):
    return {
        "status": status,
        "message": message,
        "payload": payload
    }
