import requests
import asyncio
from aiohttp import ClientSession


async def fetch(url,data,session):
    async with session.post(url,data=data) as response:
        return await response.read()

async def run():
    url = "http://localhost:8080/{}"
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in range(1000,9999):
            task = asyncio.ensure_future(fetch(url,data,session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

        # you now have all response bodies in this variable
        print(responses)


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)



#print(OTP())
