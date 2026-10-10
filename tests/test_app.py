import json
import threading
import unittest
from http.server import HTTPServer
from urllib.request import urlopen
from urllib.error import HTTPError

from app.main import PlatformHandler


class PlatformAPITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), PlatformHandler)
        cls.port = cls.server.server_address[1]

        cls.thread = threading.Thread(
            target=cls.server.serve_forever,
            daemon=True,
        )
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_home_endpoint(self):
        with urlopen(f"http://127.0.0.1:{self.port}/") as response:
            data = json.loads(response.read().decode("utf-8"))

        self.assertEqual(response.status, 200)
        self.assertEqual(
            data["message"],
            "Enterprise Platform Engineering API",
        )

    def test_health_endpoint(self):
        with urlopen(
            f"http://127.0.0.1:{self.port}/health"
        ) as response:
            data = json.loads(response.read().decode("utf-8"))

        self.assertEqual(response.status, 200)
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(
            data["service"],
            "enterprise-platform-engineering",
        )
        self.assertIn("timestamp", data)

    def test_unknown_endpoint(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(f"http://127.0.0.1:{self.port}/unknown")

        self.assertEqual(error.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
