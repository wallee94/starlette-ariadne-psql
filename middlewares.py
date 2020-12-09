from starlette.middleware.base import BaseHTTPMiddleware

from app.utils import b64e


def request_state_middleware(**dependencies):
    """
    Sets dependencies in the request.state attribute
    """
    class RequestStateMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request, call_next):
            for k, v in dependencies.items():
                setattr(request.state, k, v)
            return await call_next(request)

    return RequestStateMiddleware


def encode_id_middleware(resolver, obj, info, **args):
    """
    b64 encodes every ID field before returning the response
    """
    value = resolver(obj, info, **args)
    if info.parent_type and getattr(info.return_type, 'name', None) == 'ID':
        value = b64e(f"{info.parent_type.name}:{value}")

    return value
