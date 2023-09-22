"""
A simple chat interface built using ralf and ralf-dialogue.
"""

from ralf.dispatcher import Action
from ralf_dialogue import Conversation
from termcolor import colored

# Provide a system message that will condition the AI's responses
system_msg = "You are a helpful assistant that speaks with a pirate accent."

# Create the conversation object
conversation = Conversation(trim_method='tokens', max_length=4097)

while True:
    # Get input from the user and add it to the conversation
    user_utterance = input(colored('Human: ', 'blue', attrs=['bold']))
    if user_utterance == 'exit':
        break
    conversation.add_human_turn(user_utterance)

    # Generate the AI response using the current conversation history
    response = Action(messages=conversation.to_messages(system_msg))()
    ai_utterance = response['output']

    # Add and display the AI turn
    ai_turn = conversation.add_ai_turn(ai_utterance, return_turn=True)
    print(f"{colored(ai_turn.speaker+':', 'green', attrs=['bold'])} {ai_turn.utterance}")

print('')
print('='*20, 'Conversation History', '='*20)
print(conversation)