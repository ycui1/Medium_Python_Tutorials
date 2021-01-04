import time

def authenticate_user():
    # mimic a network request lasting 2 seconds
    print("***Begin authenticating", time.asctime())
    time.sleep(2)
    print("***End authenticating", time.asctime())

def get_posts_remotely():
    # mimic a network request lasting 2 seconds
    print("###Begin fetching", time.asctime())
    time.sleep(3)
    print("###End fetching", time.asctime())

def load_data_for_user():
    print("@@@Start loading", time.asctime())
    authenticate_user()
    get_posts_remotely()
    print("@@@End loading", time.asctime())

load_data_for_user()

import asyncio
async def authenticate_user_a():
    # mimic a network request lasting 2 seconds
    print("***Begin authenticating", time.asctime())
    await asyncio.sleep(2)
    print("***End authenticating", time.asctime())

async def get_posts_remotely_a():
    # mimic a network request lasting 2 seconds
    print("###Begin fetching", time.asctime())
    await asyncio.sleep(3)
    print("###End fetching", time.asctime())

async def load_data_for_user_a():
    print("@@@Start loading", time.asctime())
    await asyncio.gather(
        authenticate_user_a(),
        get_posts_remotely_a()
    )
    print("@@@End loading", time.asctime())

asyncio.run(load_data_for_user_a())

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

say_hello()

# Create the coroutine
say_hello_coroutine0 = say_hello()
say_hello_coroutine0
# Run the coroutine
asyncio.run(say_hello_coroutine0)

# Create an async function
async def say_hello_caller():
    print("###Start calling say_hello_caller")
    say_hello_coroutine1 = say_hello()
    print("say_hello_coroutine1:", say_hello_coroutine1)
    await say_hello_coroutine1
    print("###End calling say_hello_caller")

# Execute the function
asyncio.run(say_hello_caller())

asyncio.sleep(1)


# Create an async function
async def say_hello_scheduler():
    print("###Start calling say_hello_scheduler")
    say_hello_task = asyncio.create_task(say_hello())
    await say_hello_task
    print("###End calling say_hello_scheduler")

asyncio.run(say_hello_scheduler())


async def get_posts():
    await asyncio.sleep(3)
    print("Getting posts")
    return "Posts"

async def authenticate_user():
    await asyncio.sleep(2)
    print("Authenticating user")
    return True

async def fetch_data_for_user():
    print("Fetching data")
    await asyncio.gather(
        get_posts(),
        authenticate_user()
    )
    print("Fetched data")

asyncio.run(fetch_data_for_user())


async def fetch_data_for_user_results():
    print("Fetching data")
    gathered_task = asyncio.gather(
        get_posts(),
        authenticate_user()
    )
    print("Gathered task:", gathered_task)
    result = await gathered_task
    print("Fetched data:", result)


asyncio.run(fetch_data_for_user_results())

