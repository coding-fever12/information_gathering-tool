import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

try:
    url = sys.argv[1]
    # Ensure the URL is complete and correct
    if not url.startswith("http"):
        url = "https://" + url

    # Get IP address
    hostname = url.split("://")[1]
    ip_address = socket.gethostbyname(hostname)
    print("\nThe IP address of " + hostname + " is " + ip_address + "\n")

    # Get location info from ipinfo.io
    req_two = requests.get("https://ipinfo.io/" + ip_address + "/json")
    resp_ = json.loads(req_two.text)

    print("Location: " + resp_.get("loc", "N/A"))
    print("Region: " + resp_.get("region", "N/A"))
    print("Country: " + resp_.get("country", "N/A"))
    print("City: " + resp_.get("city", "N/A"))

except Exception as e:
    print("An error occurred: " + str(e))
