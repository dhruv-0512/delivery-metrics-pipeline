import unittest
import app

class MetricsTest(unittest.TestCase):

    def test_metrics_exist(self):
        self.assertIsNotNone(app.total_deliveries)
        self.assertIsNotNone(app.pending_deliveries)
        self.assertIsNotNone(app.on_the_way_deliveries)
        self.assertIsNotNone(app.average_delivery_time)

if __name__ == "__main__":
    unittest.main()