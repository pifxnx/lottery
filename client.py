from httpx import AsyncClient
from asyncio import TaskGroup, run


random_names_url = "https://randomapi.dev/api/names?count=100&fields=fullname"


async def get_random_names():
    async with AsyncClient() as client:
        r = await client.get(random_names_url)
        names = [x["fullName"] for x in r.json()["data"]]
        return names


async def add_one_name(client: AsyncClient, name: str):
    await client.post("http://localhost:8000/add", json={"name": name})


async def add_all_names():
    names = await get_random_names()
    async with AsyncClient() as client:
        async with TaskGroup() as tg:
            tasks = [tg.create_task(add_one_name(client, name)) for name in names]
        return [task.result() for task in tasks]


if __name__ == "__main__":
    run(add_all_names())
