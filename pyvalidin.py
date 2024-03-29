import requests

API_BASE_URL = "https://app.validin.com/api/axon"
API_KEY = "ADD_API_KEY_HERE"

# Domain functions
def domain_dns_history(domain, record_type=None):
    url = f"{API_BASE_URL}/domain/dns/history/{domain}"
    if record_type:
        url += f"/{record_type}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def domain_ptr_records(domain):
    url = f"{API_BASE_URL}/domain/dns/hostname/{domain}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def osint_history_domain(domain):
    url = f"{API_BASE_URL}/domain/osint/history/{domain}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def general_osint_context_domain(domain):
    url = f"{API_BASE_URL}/domain/osint/context/{domain}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def domain_pivots(domain):
    url = f"{API_BASE_URL}/domain/pivots/{domain}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

# ip functions
def ip_dns_history(ip):
    url = f"{API_BASE_URL}/ip/dns/history/{ip}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def cidr_dns_history(ip, cidr):
    url = f"{API_BASE_URL}/ip/dns/history/{ip}/{cidr}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def ip_ptr_records(ip):
    url = f"{API_BASE_URL}/ip/dns/hostname/{ip}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def ptr_records_for_cidrs(ip, cidr):
    url = f"{API_BASE_URL}/ip/dns/hostname/{ip}/{cidr}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def osint_history_ip(ip):
    url = f"{API_BASE_URL}/ip/osint/history/{ip}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def osint_history_cidr_ip(ip, cidr):
    url = f"{API_BASE_URL}/ip/osint/history/{ip}/{cidr}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def general_osint_context_ip(ip):
    url = f"{API_BASE_URL}/ip/osint/context/{ip}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

def ip_pivots(ip):
    url = f"{API_BASE_URL}/ip/pivots/{ip}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json()

# results
def display_results(results):
    print(results)


def main():
    print("Welcome to the Domain/IP Tool")
    domain_or_ip = input("Enter a domain name or IP address: ")

    if "." in domain_or_ip:
        # Domain research
        print("Choose an operation:")
        print("1. DNS History")
        print("2. Domain PTR Records")
        print("3. OSINT History (Domain)")
        print("4. General OSINT Context (Domain)")
        print("5. Domain Pivots")

        while True:
            operation_choice = input("Enter operation number: ")
            if operation_choice.isdigit():
                operation_choice = int(operation_choice)
                if 1 <= operation_choice <= 5:
                    break
            print("Invalid choice. Please enter a number between 1 and 5.")

        if operation_choice == 1:
            record_type = input("Enter the record type (A, AAAA, NS, etc.) or press Enter to get all records: ")
            results = domain_dns_history(domain_or_ip, record_type)
        elif operation_choice == 2:
            results = domain_ptr_records(domain_or_ip)
        elif operation_choice == 3:
            results = osint_history_domain(domain_or_ip)
        elif operation_choice == 4:
            results = general_osint_context_domain(domain_or_ip)
        elif operation_choice == 5:
            results = domain_pivots(domain_or_ip)

    else:
        # IP research
        print("Choose an operation:")
        print("1. DNS History (Reverse IP)")
        print("2. CIDR DNS History (Reverse IP)")
        print("3. IP address PTR Records")
        print("4. PTR Records for CIDRs")
        print("5. OSINT History (IP)")
        print("6. OSINT History for CIDR (IP)")
        print("7. General OSINT Context for IP")
        print("8. IP Pivots")

        while True:
            operation_choice = input("Enter operation number: ")
            if operation_choice.isdigit():
                operation_choice = int(operation_choice)
                if 1 <= operation_choice <= 8:
                    break
            print("Invalid choice. Please enter a number between 1 and 8.")

        if operation_choice == 1:
            results = ip_dns_history(domain_or_ip)
        elif operation_choice == 2:
            cidr = input("Enter CIDR: ")
            results = cidr_dns_history(domain_or_ip, cidr)
        elif operation_choice == 3:
            results = ip_ptr_records(domain_or_ip)
        elif operation_choice == 4:
            cidr = input("Enter CIDR: ")
            results = ptr_records_for_cidrs(domain_or_ip, cidr)
        elif operation_choice == 5:
            results = osint_history_ip(domain_or_ip)
        elif operation_choice == 6:
            cidr = input("Enter CIDR: ")
            results = osint_history_cidr_ip(domain_or_ip, cidr)
        elif operation_choice == 7:
            results = general_osint_context_ip(domain_or_ip)
        elif operation_choice == 8:
            results = ip_pivots(domain_or_ip)

    display_results(results)


if __name__ == "__main__":
    main()
