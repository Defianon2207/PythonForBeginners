from concurrent.futures import ProcessPoolExecutor


def count_primes(limit):
    count = 0

    for number in range(2, limit):
        is_prime = True

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

    return count


if __name__ == "__main__":
    limits = [50_000, 60_000, 70_000, 80_000]

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(count_primes, limits)

        print(list(results))