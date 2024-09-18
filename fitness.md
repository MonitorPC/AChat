## Fitness Functions for Anonymous Chat Application

Here are fitness functions to assess the quality of the application based on time behavior, recoverability, and maintainability:

**1. Time Behavior:**

- **Message Sending Latency (ms):**
   - Send a message from the client and measure the time taken for the server to acknowledge successful receipt.
   - **Ideal:** < 200ms
   - **Acceptable:** < 500ms
   - **Penalty:** Linearly increasing penalty for latency beyond acceptable range. 

- **Message Retrieval Latency (ms):**
   - Retrieve all messages from the server and measure the time taken.
   - **Ideal:** < 300ms 
   - **Acceptable:** < 700ms
   - **Penalty:** Linearly increasing penalty for latency beyond acceptable range. Consider additional penalties based on the number of messages being retrieved.

- **Message Count Retrieval Latency (ms):**
   - Retrieve the total message count from the server and measure the time taken.
   - **Ideal:** < 100ms
   - **Acceptable:** < 300ms
   - **Penalty:** Linearly increasing penalty for latency beyond acceptable range.

**2. Recoverability:**

- **Message Persistence After Restart:** 
   - Send a set of messages.
   - Restart the server.
   - Check if the previously sent messages are still available.
   - **Ideal:** All messages persist.
   - **Penalty:**  Significant penalty for each lost message.

- **Graceful Degradation under Load:** 
   - Simulate a large number of concurrent users sending messages (using a load testing tool like Locust).
   - Monitor error rates and response times.
   - **Ideal:** Minimal degradation in performance (e.g., response times within an acceptable range even under high load).
   - **Penalty:**  Increasing penalty for higher error rates or significant increases in response times.

**3. Maintainability:**

- **Code Complexity (Cyclomatic Complexity):** 
    - Analyze the codebase (especially server-side) using a static analysis tool to measure cyclomatic complexity of functions.
    - **Ideal:**  Functions with complexity below 10.
    - **Penalty:** Increasing penalty for functions with higher complexity (more prone to errors and difficult to modify).



