import sys
from client import A2AClient


def main() -> None:
    echo_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    reverse_url = sys.argv[2] if len(sys.argv) > 2 else "http://localhost:8001"
    message = sys.argv[3] if len(sys.argv) > 3 else "Hello from the coordinator"

    with A2AClient(echo_url) as echo_client, A2AClient(reverse_url) as reverse_client:
        echo_client.fetch_agent_card()
        reverse_client.fetch_agent_card()

        echo_response = echo_client.send_task(message)
        echo_text = echo_client.extract_text(echo_response)
        print(f"Echo output: {echo_text}")

        reverse_response = reverse_client.send_task(echo_text)
        reverse_text = reverse_client.extract_text(reverse_response)
        print(f"Reverse output: {reverse_text}")


if __name__ == "__main__":
    main()
