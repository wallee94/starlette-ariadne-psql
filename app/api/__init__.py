import os

from ariadne import load_schema_from_path, make_executable_schema
from ariadne.resolvers import snake_case_fallback_resolvers

from .mutations import mutation
from .queries import query

path = os.path.join(os.path.dirname(__file__), 'schema.graphql')
type_defs = load_schema_from_path(path)

resolvers = [query, mutation, snake_case_fallback_resolvers]
schema = make_executable_schema(type_defs, resolvers)
