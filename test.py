import asyncio
import aiohttp

cnpj_list = [
    "00006486000175",
    "00012377000160",
    "00022244000175",
    "25.533.977/0001-03"
]


async def send_cnpj_request(cnpj):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://localhost:8000/scrape?in_cnpj={cnpj}") as response:
            task_id = await response.text()
            print(f"CNPJ: {cnpj} -> Task ID: {task_id}")


async def main():
    tasks = [send_cnpj_request(cnpj) for cnpj in cnpj_list]
    await asyncio.gather(*tasks)

asyncio.run(main())
