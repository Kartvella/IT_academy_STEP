import asyncio
import random
from datetime import datetime

#Exercise N1
async def delay_two_seconds():
    await asyncio.sleep(2)
    print('2 second delayed function is done')

async def delay_five_seconds():
    await asyncio.sleep(5)
    print('5 second delayed function is done')

async def main():
    task1 = asyncio.create_task(delay_two_seconds())
    task2 = asyncio.create_task(delay_five_seconds())

    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())

#Exercise N2

async def print_numbers_with_delay():

    delay = random.randrange(1, 5)
    print(f"delaying for {delay} seconds...")
    await asyncio.sleep(delay)

    
    for i in range(1, 11):
        print(i)

async def main():
    await print_numbers_with_delay()

asyncio.run(main())

#Exericse N3

async def is_even(number):
    return number % 2 == 0

async def get_square_if_even(number):
    if await is_even(number):
        return number ** 2
    else:
        return f"{number} is not even"

async def main():
    starttime = datetime.now()
    tasks = [get_square_if_even(num) for num in range(1, 10000)]
    
    results = await asyncio.gather(*tasks)
    
    for number, result in zip(range(1, 10000), results):
        print(f"number: {number}, result: {result}")
    endt = datetime.now()
    print(f'{endt-starttime}')

if __name__ == "__main__":
    asyncio.run(main())

#Exericse N4

async def write_to_file(filename, content):
    print(f"starting to write to {filename}")
    await asyncio.sleep(3)
    with open(filename, 'w') as file:
        file.write(content)
    print(f"finished writing to {filename}")

async def main():
    tasks = [
        write_to_file('Lecture 22 - Async/file1.txt', 'content for file 1'),
        write_to_file('Lecture 22 - Async/file2.txt', 'content for file 2'),
        write_to_file('Lecture 22 - Async/file3.txt', 'content for file 3')
    ]
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
