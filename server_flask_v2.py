from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

blocked_ips = []

@app.route('/block', methods=['POST'])
def block_ip():
    data = request.get_json()
    ip = data.get("ip")

    if ip in blocked_ips:
        return jsonify({
            "status": "already_blocked",
            "ip": ip
        })

    url = "http://127.0.0.1:8080/wm/staticflowpusher/json"

    payload = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": f"block-{ip}",
        "priority": "32768",
        "eth_type": "0x0800",
        "ipv4_src": ip,
        "active": "true",
        "actions": "drop"
    }

    response = requests.post(url, json=payload)

    blocked_ips.append(ip)

    return jsonify({
        "status": "blocked",
        "ip": ip,
        "floodlight_response": response.text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
