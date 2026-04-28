import http.server
import os

port = int(os.environ.get("DATABRICKS_APP_PORT", os.environ.get("PORT", 8000)))
handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(("0.0.0.0", port), handler) as httpd:
    httpd.serve_forever()
