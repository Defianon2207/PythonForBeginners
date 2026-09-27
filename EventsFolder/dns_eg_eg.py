import asyncio
import socket


async def main():
    loop = asyncio.get_running_loop()

    results = await loop.getaddrinfo(
        "example.com",
        443,
        type=socket.SOCK_STREAM,
    )

    for family, socket_type, protocol, canonical_name, address in results:
        print("Family:", family)
        print("Socket type:", socket_type)
        print("Protocol:", protocol)
        print("Canonical name:", canonical_name)
        print("Address:", address)
        print()


asyncio.run(main())