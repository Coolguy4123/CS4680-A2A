# server/reverse_agent_wrapper.py
import uuid


class ReverseAgent:
    """Agent Engine wrapper for a simple reverse-word agent."""

    def set_up(self):
        print('ReverseAgent.set_up() called')

    def query(self, *, task_id: str = None, message_text: str) -> dict:
        words = message_text.split()
        reversed_text = ' '.join(reversed(words))

        return {
            'id': task_id or str(uuid.uuid4()),
            'status': {'state': 'completed'},
            'artifacts': [{'parts': [{'type': 'text', 'text': reversed_text}]}]
        }
