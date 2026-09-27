import asyncio
import socket


async def main():
    loop = asyncio.get_running_loop()

    # Forward lookup
    results = await loop.getaddrinfo(
        "localhost",
        8000,
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
    )

    address = results[0][4]

    print("Forward lookup:")
    print("localhost →", address)

    # Reverse lookup
    hostname, service = await loop.getnameinfo(
        address,
        flags=socket.NI_NUMERICSERV,
    )

    print("\nReverse lookup:")
    print(address, "→", hostname, service)


asyncio.run(main())