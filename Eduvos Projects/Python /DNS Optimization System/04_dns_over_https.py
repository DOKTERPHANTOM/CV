import requests
import json


def resolve_with_doh(domain):
    # Cloudflare DoH endpoint
    doh_url = "https://cloudflare-dns.com/dns-query"

    # DoH request headers and parameters
    headers = {
        "accept": "application/dns-json"
    }
    params = {
        "name": domain,  # Domain to resolve
        "type": "A",  # Type A for IPv4 address
        "do": "true"  # Enable DNSSEC (optional)
    }

    try:
        # Send the DoH request
        response = requests.get(doh_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the JSON response
        result = response.json()

        # Extract the IP address from the response
        if "Answer" in result and len(result["Answer"]) > 0:
            ip_address = result["Answer"][0]["data"]
            print(f"Resolved {domain} to {ip_address} via DoH")
            print(f"DNSSEC Status: {'Secure' if result.get('AD') else 'Insecure'}")
            return ip_address
        else:
            print(f"No A record found for {domain}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error during DoH query for {domain}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing DoH response for {domain}: {e}")
        return None


# Test the script
if __name__ == "__main__":
    domain_to_resolve = "google.com"
    ip_address = resolve_with_doh(domain_to_resolve)
    if ip_address:
        print(f"Successfully resolved to: {ip_address}")