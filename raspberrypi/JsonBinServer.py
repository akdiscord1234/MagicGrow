from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith(".html"):
                # Serve static HTML content
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                with open("index.html", "rb") as f:
                    self.wfile.write(f.read())
            elif self.path.endswith(".json"):
                # Serve JSON data
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                data = {"message": "Hello from the server!"}
                self.wfile.write(json.dumps(data).encode("utf-8"))
            else:
                # Handle other paths (e.g., root)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h1>Welcome to the server!</h1>")
        except IOError:
            self.send_error(404, "File Not Found: %s" % self.path)

def run_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

run_server()