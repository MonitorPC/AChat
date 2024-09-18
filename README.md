## Anonymous Chat Application

This application allows users to send anonymous messages and retrieve the total count of messages.

### Requirements:

- Python 3.6 or higher
- Flask 
- requests

### Starting the Server:

1. **Navigate to the server directory:** 
   ```bash
   cd server
   ```
2. **Run the server:**
   ```bash
   python app.py
   ```
   This will start the Flask server on `http://127.0.0.1:5000/`.

### Using the Client:

1. **Open a terminal or command prompt in the client directory:**
   ```bash
   cd client
   ```
2. **Run the client:**
   ```bash
   python client.py
   ```

3. **Follow the menu options:**
   - **Send message:** Choose option `1` and type your message.
   - **View messages:** Choose option `2` to see all messages with timestamps.
   - **Get message count:** Choose option `3` to display the total number of messages sent.
   - **Exit:** Choose option `4` to quit the client.

### API Endpoints:

- **POST /messages**: Send an anonymous message.
  - **Request body:**
    ```json
    {
      "message": "Your message here"
    }
    ```
- **GET /messages**: Retrieve all messages.
- **GET /messages/count**: Get the total message count.

### Notes:

- The current implementation stores messages in memory, so they will be lost if the server restarts. For persistent storage, consider using a database.
- This application is for demonstration purposes only and does not include user authentication or advanced security features. 
