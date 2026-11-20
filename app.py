from prometheus_client import start_http_server, Counter, Gauge, Summary
import time
import random

total_deliveries = Counter(
    'total_deliveries', 'Total number of deliveries'
)

pending_deliveries = Gauge(
    'pending_deliveries', 'Number of pending deliveries'
)

on_the_way_deliveries = Gauge(
    'on_the_way_deliveries', 'Deliveries currently on the way'
)

average_delivery_time = Summary(
    'average_delivery_time', 'Delivery processing time'
)

if __name__ == '__main__':
    start_http_server(8000)
    print("Metrics exporter running on port 8000")

    while True:
        total_deliveries.inc()
        pending_deliveries.set(random.randint(1, 15))
        on_the_way_deliveries.set(random.randint(1, 10))

        average_delivery_time.observe(random.uniform(10, 40))

        time.sleep(5)