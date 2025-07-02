import dns.resolver
import threading
import time
import random
from collections import defaultdict

# List of DNS servers (resolvers)
dns_servers = [
    '8.8.8.8',   # Google DNS
    '1.1.1.1',   # Cloudflare DNS
    '8.8.4.4',   # Google DNS (secondary)
    '208.67.222.222'  # OpenDNS
]

# Track the load (number of active queries) for each server
server_load = defaultdict(int)
load_lock = threading.Lock()  # To safely update server_load in a multi-threaded environment

def resolve_dns(domain, resolver_address):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [resolver_address]
    try:
        answer = resolver.resolve(domain, 'A')
        return answer[0].to_text()
    except Exception as e:
        print(f"Error resolving {domain} with {resolver_address}: {e}")
        return None

def query_with_load_balancing(domain):
    # Find the server with the least load
    with load_lock:
        selected_server = min(dns_servers, key=lambda server: server_load[server])
        server_load[selected_server] += 1  # Increment load for the selected server
        print(f"Routing query for {domain} to {selected_server} (Load: {server_load[selected_server]})")

    # Perform the DNS query
    result = resolve_dns(domain, selected_server)

    # Decrease the load after the query is done
    with load_lock:
        server_load[selected_server] -= 1
        print(f"Finished query for {domain} on {selected_server} (Load: {server_load[selected_server]})")

    return result

def simulate_query(domain):
    # Simulate a query with some delay (to mimic real-world latency)
    time.sleep(random.uniform(0.1, 1.0))  # Random delay between 0.1 and 1 second
    result = query_with_load_balancing(domain)
    if result:
        print(f"Resolved {domain} to {result}")

# Test the load balancer with multiple queries
if __name__ == "__main__":
    domains = ["google.com", "example.com", "cloudflare.com", "microsoft.com", "apple.com"]
    threads = []

    # Simulate multiple queries concurrently
    for domain in domains:
        thread = threading.Thread(target=simulate_query, args=(domain,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("\nFinal Load on Servers:")
    for server in dns_servers:
        print(f"{server}: {server_load[server]} queries")