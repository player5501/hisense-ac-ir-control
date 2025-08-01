from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def send_ir_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {"status": "success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.stderr}

@app.route('/onoff', methods=['GET'])
def onoff():
    command = ["ir-ctl", "--send=onoff.txt"]
    result = send_ir_command(command)
    return jsonify(result)

@app.route('/cooling', methods=['GET'])
def cooling():
    command = ["ir-ctl","--send=61h.txt"]
    result = send_ir_command(command)
    return jsonify(result)

@app.route('/fan', methods=['GET'])
def fan():
    command = ["ir-ctl", "--send=fan.txt"]
    result = send_ir_command(command)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
