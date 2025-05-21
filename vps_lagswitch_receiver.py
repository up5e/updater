from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/launch', methods=['POST'])
def launch():
    data = request.get_json()
    key = data.get("key")
    ip = data.get("ip")
    duration = data.get("duration", 3)

    if not key or not ip:
        return jsonify({"error": "Missing key or IP"}), 400

    # Trusting external validation
    subprocess.Popen(['python3', 'w_temp.py', ip, str(duration)])
    return jsonify({"status": "launched", "ip": ip, "duration": duration}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
