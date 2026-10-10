from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from datetime import datetime, timezone


class PlatformHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "service": "enterprise-platform-engineering",
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
            self.send_response(200)

        elif self.path == "/":
            response = {
                "message": "Enterprise Platform Engineering API",
                "endpoints": ["/", "/health"],
            }
            self.send_response(200)

        else:
            response = {"error": "Not found"}
            self.send_response(404)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))


def main():
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", "8000"))

    server = HTTPServer((host, port), PlatformHandler)
    print(f"Application listening on {host}:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down application.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
