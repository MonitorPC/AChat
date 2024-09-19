from flask import Flask, request, jsonify
from datetime import datetime
import threading

app = Flask(__name__)

messages = []
message_lock = threading.Lock()

@app.route('/messages', methods=['POST'])
def send_message():
    """Endpoint to send anonymous messages."""
    message = request.get_json().get('message')
    if not message:
        return jsonify({'error': 'Message is required'}), 400

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with message_lock:
        messages.append({'message': message, 'timestamp': timestamp})

    return jsonify({'status': 'Message sent'}), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    """Endpoint to retrieve all messages."""
    return jsonify(messages)

@app.route('/messages/count', methods=['GET'])
def get_message_count():
    """Endpoint to get the total message count."""
    with message_lock:
        count = len(messages)
    return jsonify({'count': count})

if __name__ == '__main__':
    app.run()
