Domain/IP Tool

The Domain/IP Tool is a Python script that allows users to retrieve various information related to domain names and IP addresses using the Validin API. This tool provides functionalities such as DNS history lookup, PTR records retrieval, OSINT (Open Source Intelligence) history, and more.
Requirements

    Python 3.x
    Requests library (can be installed via pip install requests)

Setup

    Clone the repository or download the domain_ip_tool.py file.
    Install the required dependencies using pip: pip install requests.
    Replace YOUR_API_KEY with your Validin API key in the API_KEY variable within the script.

Usage

    Run the script: python domain_ip_tool.py.
    Enter a domain name or an IP address when prompted.
    Choose an operation from the provided options based on the type of input:
        For domain names: select from DNS history, domain PTR records, OSINT history, general OSINT context, or domain pivots.
        For IP addresses: select from DNS history (reverse IP), CIDR DNS history (reverse IP), IP address PTR records, PTR records for CIDRs, OSINT history (IP), OSINT history for CIDR (IP), general OSINT context for IP, or IP pivots.
    Follow any additional prompts for operation-specific input (e.g., record types, CIDR).
    View the results displayed by the tool.

Input Validation

The script includes input validation to ensure that users provide valid inputs for selecting operations and entering additional parameters (e.g., record types, CIDR).
Notes

    Ensure that you have a valid API key from Validin to access the API endpoints used by this tool.
    This tool relies on the Validin API for retrieving domain and IP-related information. Any changes to the Validin API may affect the functionality of this tool.
