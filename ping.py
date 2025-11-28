import requests
import time

url = "https://www.smartplay.lcsd.gov.hk/facilities/search-result?district=WTS&startDate=&typeCode=TENC&venueCode=&sportCode=BAGM&typeName=%E7%B6%B2%E7%90%83&frmFilterType=&venueSportCode=&isFree=false"

latencies = []
for i in range(10):  # Do it 10 times for a good average
    start = time.time()
    try:
        response = requests.get(url, timeout=5)
        latency = (time.time() - start) * 1000  # in ms
        latencies.append(latency)
        print(f"Try {i+1}: {latency:.2f} ms")
    except Exception as e:
        print(f"Request failed: {e}")

if latencies:
    print(f"\nAverage HTTP latency: {sum(latencies)/len(latencies):.2f} ms")
else:
    print("All requests failed.")