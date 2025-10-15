from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = []

class PutAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())
    
    def do_PUT(self):
        content_length = int(self.headers.get("Content-Length", 0))
        received_data = self.rfile.read(content_length)
        
        try:
            put_data = json.loads(received_data)  # Parse the JSON from the request
            
            if "name" in put_data:  # Assuming we're using "name" as a unique identifier
                for i, item in enumerate(data):
                    if item.get("name") == put_data.get("name"):  # Check if an item with the same name exists
                        data[i] = put_data  # Update the existing item
                        self.send_data({
                            "Message": "Data Updated",
                            "Updated Data": put_data
                        })
                        return  # Exit after updating
                # If no matching item is found, add a new one
                data.append(put_data)
                self.send_data({
                    "Message": "Data Added (No existing item found)",
                    "Data": put_data
                })
            else:
                self.send_data({"Error": "Missing 'name' field in request"}, status=400)
        except json.JSONDecodeError:
            self.send_data({"Error": "Invalid JSON"}, status=400)
            
def run():
    server_address = ('localhost', 8001)  # Using a different port to avoid conflicts
    httpd = HTTPServer(server_address, PutAPI)
    print("PUT Application is running on http://localhost:8001")
    httpd.serve_forever()
if __name__ == "__main__":
    run()
