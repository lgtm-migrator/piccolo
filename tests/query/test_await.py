import asyncio

from tests.example_apps.music.tables import Band

from ..base import DBTestCase


class TestAwait(DBTestCase):
    def test_await(self):
        """
        Test awaiting a query directly - it should proxy to Query.run().
        """

        async def get_all():
            return await Band.select()

        response = asyncio.run(get_all())

        self.assertIsInstance(response, list)
