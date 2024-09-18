import requests

SERVER_URL = 'http://127.0.0.1:5000'

def send_message(message):
    """Sends a message to the server."""
    response = requests.post(f'{SERVER_URL}/messages', json={'message': message})
    if response.status_code == 201:
        print("Message sent successfully")
    else:
        print(f"Error sending message: {response.text}")

def get_messages():
    """Retrieves all messages from the server."""
    response = requests.get(f'{SERVER_URL}/messages')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching messages: {response.text}")
        return []

def get_message_count():
    """Retrieves the total message count from the server."""
    response = requests.get(f'{SERVER_URL}/messages/count')
    if response.status_code == 200:
        return response.json()['count']
    else:
        print(f"Error fetching message count: {response.text}")
        return None

if __name__ == '__main__':
    while True:
        print("\nChoose an action:")
        print("1. Send message")
        print("2. View messages")
        print("3. Get message count")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            message = input("Enter your message: ")
            send_message(message)
        elif choice == '2':
            messages = get_messages()
            for msg in messages:
                print(f"{msg['timestamp']} - {msg['message']}")
        elif choice == '3':
            count = get_message_count()
            print(f"Total messages: {count}")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
