import dns.resolver
import dns.exception


def resolve_with_dnssec(domain):
    # Create a resolver instance
    resolver = dns.resolver.Resolver()

    # Enable DNSSEC by setting the DO (DNSSEC OK) bit
    resolver.use_edns(0, dns.flags.DO)

    # Set timeouts to avoid hanging
    resolver.timeout = 2
    resolver.lifetime = 2

    try:
        # Perform the DNS query with validation
        answer = resolver.resolve(domain, 'A')  # 'A' record for IP address
        print(f"Resolved IP for {domain}: {answer[0]}")
        print("DNSSEC Validation: Passed")
        return answer[0].to_text()  # Return the IP address
    except dns.exception.DNSSECValidationError as e:
        print(f"DNSSEC Validation Failed for {domain} - Possible cache poisoning! Error: {e}")
        return None
    except Exception as e:
        print(f"Error resolving {domain}: {e}")
        return None


# Test the script
if __name__ == "__main__":
    domain_to_resolve = "google.com"  # Use a domain that supports DNSSEC
    ip_address = resolve_with_dnssec(domain_to_resolve)
    if ip_address:
        print(f"Successfully resolved to: {ip_address}")