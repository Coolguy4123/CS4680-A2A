# CS 4680 - A2A Assignment (Freeman Yiu)

### Questions
1. Why does the request use a client-generated id rather than a server-generated one? What problem does this solve in distributed systems?

A client-generated id can be cached to reduce duplicate tasks. In distributed systems, retries often happens because of load balancer and timeouts. Therefore, client-generated id allows the system to recognize previous retries

2. The status.state can be 'working'. Under what circumstances would a server return this state in a non-streaming call, and how should a client react?

This state is returned when the task has been accepted but not finished yet. It is usually returned in long-waiting tasks. In non-streaming call, this state means the process is not ready and the client should not treat this as an error

3. What is the purpose of the sessionId field? Give a concrete example of two related tasks that should share a session.

The sessionId field is used to group related tasks for continous conversation, it allows context to be preserved and lets the server know it is same interaction. Example tasks include "Summarize this doc" and "Turn the summary into presentation slides", both tasks should use the same sessionID

4. The parts array supports types text, file, and data. Describe a realistic multi-agent workflow where all three part types appear in a single conversation.

A realistic example would be: User sends text instructions and URL for a document. Agent A parses the file and turns info into data. Agent B uses those data and previous text instructions to return a detailed summary

5. What does the --allow-unautheticated flag does and its security implications

The flag allows the Cloud Run server to run the server publicly without authentication, which means anyone with URL the access. Oberall, this is a dangerous in cloud computing as hackers can esily breach through

6. How Cloud Run scales to zero and what cold start latency means for A2A clients

Cloud run can scale to 0 byy shutting down all existing instance. For A2A agents, cold start latency refers to the time for the first request after a fresh start, which is slower than normal requests