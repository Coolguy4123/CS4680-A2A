# CS 4680 - A2A Assignment (Freeman Yiu)

## Questions

---

### Section 3
1. Why does the request use a client-generated id rather than a server-generated one? What problem does this solve in distributed systems?

A client-generated id can be cached to reduce duplicate tasks. In distributed systems, retries often happens because of load balancer and timeouts. Therefore, client-generated id allows the system to recognize previous retries

2. The status.state can be 'working'. Under what circumstances would a server return this state in a non-streaming call, and how should a client react?

This state is returned when the task has been accepted but not finished yet. It is usually returned in long-waiting tasks. In non-streaming call, this state means the process is not ready and the client should not treat this as an error

3. What is the purpose of the sessionId field? Give a concrete example of two related tasks that should share a session.

The sessionId field is used to group related tasks for continous conversation, it allows context to be preserved and lets the server know it is same interaction. Example tasks include "Summarize this doc" and "Turn the summary into presentation slides", both tasks should use the same sessionID

4. The parts array supports types text, file, and data. Describe a realistic multi-agent workflow where all three part types appear in a single conversation.

A realistic example would be: User sends text instructions and URL for a document. Agent A parses the file and turns info into data. Agent B uses those data and previous text instructions to return a detailed summary

---

### Section 4
1. What does the --allow-unautheticated flag does and its security implications

The flag allows the Cloud Run server to run the server publicly without authentication, which means anyone with URL the access. Oberall, this is a dangerous in cloud computing as hackers can esily breach through

2. How Cloud Run scales to zero and what cold start latency means for A2A clients

Cloud run can scale to 0 by shutting down all existing instance. For A2A agents, cold start latency refers to the time for the first request after a fresh start, which is slower than normal requests

---

### Section 5
1. Explain the difference between deploying to Cloud Run vs Agent Engine in terms of operational burden and use-case fit.

Cloud run is a full-on hosting service, while Agent Engine is more specialized for hosting agents in Python. In terms of operational burden, Cloud Run gives more control over the infrasture as it is related to fullstack applications. However, Agent Engine has better convenience for deploying agents. 


2. Why the wrapper class uses a synchronous query() method even though the underlying handler is async?

The synchronous query() is needed because the Agent Engine requires it before deploying the agent. Therefore, it allows components to be reused efficiently for the handler.

---

### Section 6

Log Output: 


GET https://echo-a2a-agent-dl52rreheq-uc.a.run.app/.well-known/agent.json
RESPONSE 200 {'id': 'echo-agent-v1', 'name': 'Echo Agent', 'version': '1.0.0', 'description': 'A simple agent that echoes back any text it receives.', 'url': 'http://localhost:8000', 'contact': {'email': 'fyiu@cpp.edu'}, 'capabilities': {'streaming': False, 'pushNotifications': False}, 'defaultInputModes': ['text/plain'], 'defaultOutputModes': ['text/plain'], 'skills': [{'id': 'echo', 'name': 'Echo', 'description': 'Returns the user message verbatim.', 'inputModes': ['text/plain'], 'outputModes': ['text/plain']}, {'id': 'summarize', 'name': 'Summarize', 'description': 'Summarize the user message verbatim.', 'inputModes': ['text/plain'], 'outputModes': ['text/plain']}]}
Agent: Echo Agent

Skills:
- Echo
- Summarize
  
POST https://echo-a2a-agent-dl52rreheq-uc.a.run.app/tasks/send
PAYLOAD {'id': '66ed91bb-8c8e-4f68-987a-5bbff4834da3', 'sessionId': None, 'message': {'role': 'user', 'parts': [{'type': 'text', 'text': 'Hello from the client!'}]}}
RESPONSE 200 {'id': '66ed91bb-8c8e-4f68-987a-5bbff4834da3', 'status': {'state': 'completed'}, 'artifacts': [{'parts': [{'type': 'text', 'text': 'Hello from the client!'}]}]}
Echoed response: Hello from the client!

UML Diagram: 
<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/74f694f5-b09e-47d5-8033-0e5294ca27e5" />

1. If a client loses the network connection after sending the POST but before receiving the response, how could it safely retry? What field in the A2A protocol helps with idempotency?

It could safely retry by using the same task ID as it is already recognized by the system. Similar to caching, this approach eliminates duplicate steps, allowing faster run time. The field that helps with idempotency is the generated client ID

---

### Section 7
1. How do you add authentication between agents using service account tokens

To add authentication between agents, the system should utilize OAuth 2.0 token attached to the http request, this allows the agents to prove the identity of each other.


2. What changes to the A2A shcema would be needed to pass a sessionID across the chain

Since the sessionID field already exists, the best approach would be passing the same sessionID to the next agent, ensuring that the workflow reuses the same sessionID. 
