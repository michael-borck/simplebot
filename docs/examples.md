# SimpleBot Examples

Here are some examples of using SimpleBot in educational settings.

## Creating Custom Bot Personalities

You can create custom bot personalities:

```python
from simplebot import get_response

def scientist_bot(prompt):
    """A bot that responds like a scientific researcher."""
    return get_response(
        prompt,
        system="You are a scientific researcher. Provide evidence-based "
               "responses with references to studies when possible. "
               "Be precise and methodical in your explanations."
    )

result = scientist_bot("What happens during photosynthesis?")
print(result)
```

## Building a Simple Quiz System

```python
from simplebot import teacher_bot

quiz_questions = [
    "What is the capital of France?",
    "Who wrote Romeo and Juliet?",
    "What is the chemical symbol for water?"
]

def generate_quiz():
    print("=== Quiz Time! ===")
    for i, question in enumerate(quiz_questions, 1):
        print(f"Question {i}: {question}")
        user_answer = input("Your answer: ")

        # Generate feedback on the answer
        feedback = teacher_bot(
            f"Question: {question}\nStudent answer: {user_answer}\n"
            "Provide brief, encouraging feedback on whether this answer is "
            "correct. If incorrect, provide the correct answer."
        )
        print(f"Feedback: {feedback}\n")

# Run the quiz
generate_quiz()
```

## Simulating a Conversation Between Bots

```python
from simplebot import pirate_bot, shakespeare_bot

def bot_conversation(topic, turns=3):
    """Simulate a conversation between two bots on a given topic."""
    print(f"=== A conversation about {topic} ===")

    # Start with the pirate
    current_message = f"Tell me about {topic}"
    current_bot = "pirate"

    for i in range(turns):
        if current_bot == "pirate":
            response = pirate_bot(current_message)
            print(f"Pirate: {response}")
            current_message = f"Respond to this: {response}"
            current_bot = "shakespeare"
        else:
            response = shakespeare_bot(current_message)
            print(f"Shakespeare: {response}")
            current_message = f"Respond to this: {response}"
            current_bot = "pirate"
        print()

# Run a conversation about the ocean
bot_conversation("the ocean", turns=4)
```
