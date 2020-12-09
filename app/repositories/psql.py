import asyncpg

from settings import POSTGRES_DSN


class PsqlRepository:
    """PsqlRepository implements the Repository interface used in this app"""
    _pool: asyncpg.pool.Pool = None

    async def get_pool(self) -> asyncpg.pool.Pool:
        """
        Pool has to be created inside the event loop, so we cannot create it from main
        or setup. It will be created with the first request to db.
        https://magicstack.github.io/asyncpg/current/api/index.html#connection-pools
        """
        if self._pool is None:
            self._pool = await asyncpg.create_pool(POSTGRES_DSN)
        return self._pool

    async def power(self, power):
        """
        TODO: This is just an EXAMPLE. Can be removed
        """
        pool = await self.get_pool()
        async with pool.acquire() as connection:
            async with connection.transaction():
                # Run the query passing the request argument.
                return await connection.fetchval('select 2 ^ $1', power)
