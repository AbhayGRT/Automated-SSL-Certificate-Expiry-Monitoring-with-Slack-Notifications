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
            
            payload = {"text": message}
            slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
            if slack_webhook_url:
                response = requests.post(slack_webhook_url, json=payload)
                print("Response content:", response.content)
                print("Response status code:", response.status_code)
                if response.status_code == 200:
                    print(f"Alert sent for {domain}")
                else:
                    print(f"Failed to send alert for {domain}: {response.status_code}")
            else:
                print("No Slack webhook URL provided. Skipping alert.")

if __name__ == "__main__":
    main()
