from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

FLOODLIGHT_URL = "http://127.0.0.1:8080/wm/staticflowpusher/json"

@app.route('/block', methods=['POST'])
def block_ip():

    ip = request.json['ip']

    flow = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "block_"+ip,
        "priority": "32768",
        "eth_type": "0x0800",
        "ipv4_src": ip,
        "actions": "drop",
        "active": "true"
    }

    r = requests.post(FLOODLIGHT_URL, data=json.dumps(flow))

    return jsonify({"status": "blocked", "ip": ip})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
