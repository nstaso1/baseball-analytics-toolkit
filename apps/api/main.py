import antigravity
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class BaseballLiveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/live-stats':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            data = {
                "game_status": "Top 4th",
                "current_batter": "Shohei Ohtani",
                "pitch_velocity": 98.5,
                "exit_velocity": 105.2,
                "launch_angle": 25
            }
            self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), BaseballLiveHandler)
    server.serve_forever()
