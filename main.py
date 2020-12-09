from app.repositories import PsqlRepository
from setup import bootstrap

app = bootstrap(repository=PsqlRepository())
