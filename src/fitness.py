import time
import subprocess
import requests
from radon.complexity import cc_visit
from radon.raw import analyze
import coverage 

SERVER_URL = 'http://127.0.0.1:5000'

# --- Time Behavior ---

def measure_send_latency(message):
    """Measures message sending latency."""
    start_time = time.monotonic()
    response = requests.post(f'{SERVER_URL}/messages', json={'message': message})
    end_time = time.monotonic()
    if response.status_code == 201:
        return end_time - start_time
    else:
        raise Exception("Error sending message")

def measure_retrieve_latency():
    """Measures message retrieval latency."""
    start_time = time.monotonic()
    response = requests.get(f'{SERVER_URL}/messages')
    end_time = time.monotonic()
    if response.status_code == 200:
        return end_time - start_time
    else:
        raise Exception("Error retrieving messages")

def measure_count_latency():
    """Measures message count retrieval latency."""
    start_time = time.monotonic()
    response = requests.get(f'{SERVER_URL}/messages/count')
    end_time = time.monotonic()
    if response.status_code == 200:
        return end_time - start_time
    else:
        raise Exception("Error retrieving message count")

# --- Recoverability ---

def check_message_persistence(initial_messages):
    """Checks for message persistence after server restart."""
    try:
        subprocess.run(["python", "app.py"], cwd="server", timeout=5)  # Adjust timeout as needed
        time.sleep(2)  # Wait for server to start
        response = requests.get(f'{SERVER_URL}/messages')
        if response.status_code == 200:
            return len(response.json()) == len(initial_messages)
        else:
            return False 
    except:
        return False
    finally:
        subprocess.run(["pkill", "-f", "app.py"])  # Stop the server

# --- Maintainability ---

def calculate_cyclomatic_complexity(filepath):
    """Calculates cyclomatic complexity of a Python file."""
    with open(filepath, 'r') as file:
        code = file.read()
    return sum([block.complexity for block in cc_visit(code)])


# Example usage: 
if __name__ == "__main__":

    # --- Time Behavior ---
    send_latency = measure_send_latency("Test message") * 1000  # in ms
    retrieve_latency = measure_retrieve_latency() * 1000  # in ms
    count_latency = measure_count_latency() * 1000  # in ms

    print(f"Message Send Latency: {send_latency:.2f} ms")
    print(f"Message Retrieve Latency: {retrieve_latency:.2f} ms")
    print(f"Message Count Latency: {count_latency:.2f} ms")

    # --- Recoverability ---
    initial_msgs = [{'message': 'Msg1'}, {'message': 'Msg2'}]
    persistence = check_message_persistence(initial_msgs) 
    print(f"Message Persistence: {persistence}")

    # --- Maintainability --- 
    complexity = calculate_cyclomatic_complexity("server/app.py")
    print(f"Cyclomatic Complexity: {complexity}") 
