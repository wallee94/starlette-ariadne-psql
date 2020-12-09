from ariadne.asgi import GraphQL
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route

from app import api
from middlewares import encode_id_middleware, request_state_middleware
from settings import DEBUG, ALLOW_ORIGINS


def bootstrap(**dependencies) -> Starlette:
    """
    Boostraps a starlette app setting context_value in the GraphQL config
    """
    def context_value(request):
        return {**dependencies, 'request': request}

    gql_app = GraphQL(
        api.schema, debug=DEBUG, context_value=context_value,
        middleware=[encode_id_middleware]
    )
    routes = [
        Route("/graphql", gql_app)
    ]

    middleware = [
        Middleware(
            CORSMiddleware, allow_origins=ALLOW_ORIGINS,
            allow_methods=['*'], allow_headers=['*']
        ),
        Middleware(request_state_middleware(**dependencies)),
    ]
    return Starlette(routes=routes, debug=DEBUG, middleware=middleware)
