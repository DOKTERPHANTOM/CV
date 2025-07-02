import dns.resolver
from concurrent.futures import ThreadPoolExecutor
import time

# List of DNS servers to query
dns_servers = [
    '8.8.8.8',  # Google DNS
    '1.1.1.1',  # Cloudflare DNS
    '8.8.4.4',  # Google DNS (secondary)
    '208.67.222.222'  # OpenDNS
]

def query_dns(server, domain):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [server]
    start_time = time.time()
    try:
        answer = resolver.resolve(domain, 'A')  # 'A' record for IP address
        latency = time.time() - start_time
        return server, answer[0].to_text(), latency
    except Exception as e:
        return server, None, float('inf')  # Return infinite latency if query fails

def get_fastest_dns(domain='example.com'):
    with ThreadPoolExecutor(max_workers=len(dns_servers)) as executor:
        # Run queries in parallel
        future_to_server = {executor.submit(query_dns, server, domain): server for server in dns_servers}
        results = []

        for future in future_to_server:
            server, ip, latency = future.result()
            results.append((server, ip, latency))

    # Find the fastest response
    fastest = min(results, key=lambda x: x[2] if x[2] != float('inf') else float('inf'))
    return fastest

# Test the script
if __name__ == "__main__":
    domain_to_resolve = "google.com"
    server, ip, latency = get_fastest_dns(domain_to_resolve)
    print(f"Fastest DNS Server: {server}")
    print(f"Resolved IP: {ip}")
    print(f"Latency: {latency:.4f} seconds")