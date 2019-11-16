import asyncio
import time

#
# async def write_to_db(seconds):
#     await asyncio.sleep(seconds)
#
#
# async def main():
#     print('hello')
#     num_objects = await write_to_db(3)
#     print('world')
#
# asyncio.run(main())


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(5, 'hello'))

    task2 = asyncio.create_task(
        say_after(10, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
