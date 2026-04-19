import sys
from client import A2AClient


def main() -> None:
    echo_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    reverse_url = sys.argv[2] if len(sys.argv) > 2 else "http://localhost:8001"
    message = sys.argv[3] if len(sys.argv) > 3 else "Hello from the coordinator"

    with A2AClient(echo_url) as echo_client, A2AClient(reverse_url) as reverse_client:
        # Initialize both agent cards
        echo_card = echo_client.fetch_agent_card()
        reverse_card = reverse_client.fetch_agent_card()

        echo_response = echo_client.send_task(message) # Sends task message to echo client
        echo_text = echo_client.extract_text(echo_response) # Gets echo client response
        print(f"Echo output: {echo_text}")

        reverse_response = reverse_client.send_task(echo_text) # Chains echo client response and feed to the input of reverse client
        reverse_text = reverse_client.extract_text(reverse_response) # Gets reversed text
        print(f"Reverse output: {reverse_text}")


if __name__ == "__main__":
    main()