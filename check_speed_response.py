import requests
import time
import concurrent.futures

# Download the proxy list
url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt"
response = requests.get(url)
proxy_list = response.text.split("\n")


# Function to test a single proxy
def test_proxy(proxy):
    try:
        # Test the proxy by making a request to a website
        start_time = time.time()
        response = requests.get("https://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        end_time = time.time()

        if response.status_code == 200:
            return (proxy, end_time - start_time)
    except:
        pass


# Filter out the working and fast proxies using concurrent requests
working_proxies = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(test_proxy, proxy_list)
    for result in results:
        if result:
            working_proxies.append(result)

# Sort the working proxies by response time (fastest first)
working_proxies.sort(key=lambda x: x[1])

# Print the working and fast proxies with their response times
for proxy, response_time in working_proxies:
    print(f"Proxy: {proxy}, Response Time: {response_time:.2f} seconds")
