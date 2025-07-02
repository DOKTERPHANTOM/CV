import dns.resolver
import time


class DNSCache:
    def __init__(self, ttl=60):  # Default TTL of 60 seconds
        self.cache = {}  # Cache storage: {domain: (ip, timestamp, ttl)}
        self.ttl = ttl  # Time-to-live in seconds

    def is_expired(self, timestamp):
        """Check if a cache entry has expired based on its timestamp."""
        return (time.time() - timestamp) > self.ttl

    def get_cached_result(self, domain):
        """Check if the domain is in the cache and not expired."""
        if domain in self.cache:
            ip, timestamp, ttl = self.cache[domain]
            if not self.is_expired(timestamp):
                print(f"Cache hit for {domain}: {ip}")
                return ip
            else:
                print(f"Cache expired for {domain}")
                del self.cache[domain]  # Remove expired entry
        return None

    def cache_result(self, domain, ip):
        """Store a new result in the cache with the current timestamp."""
        self.cache[domain] = (ip, time.time(), self.ttl)
        print(f"Cached {domain}: {ip} (TTL: {self.ttl} seconds)")

    def resolve(self, domain):
        """Resolve a domain, using the cache if possible."""
        # Check cache first
        cached_ip = self.get_cached_result(domain)
        if cached_ip:
            return cached_ip

        # If not in cache or expired, query the DNS server
        print(f"Cache miss for {domain}, querying DNS...")
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8']  # Use Google DNS
        try:
            answer = resolver.resolve(domain, 'A')
            ip_address = answer[0].to_text()
            # Cache the result
            self.cache_result(domain, ip_address)
            return ip_address
        except Exception as e:
            print(f"Error resolving {domain}: {e}")
            return None


# Test the script
if __name__ == "__main__":
    # Create a DNS cache with a TTL of 5 seconds for testing
    dns_cache = DNSCache(ttl=5)

    # Test with multiple queries
    domains = ["google.com", "example.com", "google.com", "cloudflare.com", "google.com"]

    for domain in domains:
        print(f"\nQuerying {domain}...")
        ip = dns_cache.resolve(domain)
        if ip:
            print(f"Resolved to: {ip}")
        else:
            print(f"Failed to resolve {domain}")

        # Simulate some delay between queries
        time.sleep(2)

    # Wait longer than TTL to see expiration
    print("\nWaiting for cache to expire...")
    time.sleep(6)

    # Query again to see cache miss
    print(f"\nQuerying {domains[0]} after expiration...")
    ip = dns_cache.resolve(domains[0])
    if ip:
        print(f"Resolved to: {ip}")