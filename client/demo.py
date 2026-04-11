import sys
from client import A2AClient


def main() -> None:
    # Instantiates A2A client
    agent_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"

    with A2AClient(agent_url) as client:
        card = client.fetch_agent_card() # Fetches card
        print(f"Agent: {card.get('name', 'Not known')}")  # Prints agent name

        # Print skills
        print("Skills:")
        for skill in client.get_skills():
            print(f"* {skill.get('name', skill.get('id', 'Unknown'))}")

        response = client.send_task("Hello from the client!") # Sends text
        print(f"Echoed response: {client.extract_text(response)}") # Prints echoed response


if __name__ == "__main__":
    main()
