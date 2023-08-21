import json
import ssl
import socket
import datetime
import requests
import os

def get_ssl_expiry(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as sslsock:
            cert = sslsock.getpeercert()
            return datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")

def main():
    with open('domains.json') as config_file:
        config = json.load(config_file)
        domains = config.get('domains', [])
        
        for domain in domains:
            expiry_date = get_ssl_expiry(domain)
            remaining_days = (expiry_date - datetime.datetime.now()).days
            message = (
                f"SSL Expiry Alert\n"
                f"* Domain : {domain}\n"
                f"* Warning : The SSL certificate for {domain} will expire in {remaining_days} days."
            )
            print(message)

if __name__ == "__main__":
    main()
