from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    # Get the client's IP address
    client_ip = request.remote_addr
    # Log the IP address
    print(f"IP Address: {client_ip}")
    # Return a response
    return f"Your IP address is: {client_ip}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
