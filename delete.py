from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = []  # Global list to store data for DELETE operations

class DeleteAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())
    
    def do_DELETE(self):
        content_length = int(self.headers.get("Content-Length", 0))
        received_data = self.rfile.read(content_length)
        
        try:
            delete_data = json.loads(received_data)  # Parse the JSON from the request
            
            if "name" in delete_data:  # Assuming we're using "name" as the identifier
                name_to_delete = delete_data.get("name")
                global data  # Access the global data list
                for i, item in enumerate(data):
                    if item.get("name") == name_to_delete:  # Find the item by name
                        deleted_item = data.pop(i)  # Remove the item
                        self.send_data({
                            "Message": "Data Deleted",
                            "Deleted Data": deleted_item
                        })
                        return  # Exit after deleting
                self.send_data({"Error": "Item not found"}, status=404)  # If no item matches
            else:
                self.send_data({"Error": "Missing 'name' field in request"}, status=400)
        except json.JSONDecodeError:
            self.send_data({"Error": "Invalid JSON"}, status=400)
    
    # Note: This class only handles DELETE requests. Other methods will return a 405 Method Not Allowed by default.

def run():
    server_address = ('localhost', 8002)  # Using a different port to avoid conflicts
    httpd = HTTPServer(server_address, DeleteAPI)
    print("DELETE Application is running on http://localhost:8002")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
