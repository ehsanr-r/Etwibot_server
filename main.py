
import asyncio
import websockets


async def hello(websocket):

    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"
    await websocket.send(greeting)
    print(f">>> {greeting}")

    user_name = input("Enter username: ")
    await websocket.send(user_name)
    print(f">>> Username: {user_name}")

    tweet_text = input("Enter text to tweet: ")
    await websocket.send(tweet_text)
    print(f">>> Tweet text: {tweet_text}")

    tweet_id = input("Enter tweet id: ")
    await websocket.send(tweet_id)
    print(f">>> Tweet id: {tweet_id}")

    url = await websocket.recv()
    print(f"<<< {url}")

    pin = input("Enter pin: ")
    await websocket.send(pin)
    print(f">>> Pin: {pin}")

    auth = await websocket.recv()
    print(f"<<< {auth}")

    user_info = await websocket.recv()
    print(f"<<< {user_info}")

    timeline = await websocket.recv()
    print(f"<<< {timeline}")

    status = await websocket.recv()
    print(f"<<< {status}")

    update = await websocket.recv()
    print(f"<<< {update}")


async def main():

    async with websockets.serve(hello, "localhost", 8766):

        await asyncio.Future()  # run forever


if __name__ == "__main__":

    asyncio.run(main())
