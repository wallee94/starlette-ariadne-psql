import base64


def b64e(value: str) -> str:
    """
    base64 encodes an string. Returns also a string
    """
    return base64.b64encode(value.encode()).decode()


def b64d(value: str) -> str:
    """
    base64 decodes an string. Returns also a string
    """
    return base64.b64decode(value.encode()).decode()
