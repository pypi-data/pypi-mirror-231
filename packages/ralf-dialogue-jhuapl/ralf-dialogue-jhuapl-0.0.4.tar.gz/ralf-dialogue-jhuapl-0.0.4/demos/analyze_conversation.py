
"""
Example of performing analysis on a given covnersation
"""

from ralf.dispatcher import Action
from ralf_dialogue import Conversation
import ralf_dialogue as rd
from termcolor import colored

# Create the conversation object
conversation = Conversation()

# Simulate a conversation between a human and an AI
print(colored("Simulating conversation...", 'grey'))
conversation.add_human_turn("Hey! I have a question for you.")
conversation.add_ai_turn(Action(messages=conversation.to_messages())()['output'])
conversation.add_human_turn("In a few sentences, can you tell me about Julius Caesar's leadership style?")
conversation.add_ai_turn(Action(messages=conversation.to_messages())()['output'])
conversation.add_human_turn("And can you tell me what year he was born in?")

print('\nConversation:')
print('"""', conversation, '"""', sep='\n')

# Disambiguate the last thing the user said, using conversational context
disambiguated_utt = rd.dialogue.disambiguate(conversation)
print('')
print("Last human utterance was disambiguated as: "
      f"{colored(disambiguated_utt, 'yellow')}"
)

# Perform intent classification/recognition
intents = { # define the intents
    'factual question': [
        "What's the capital of Zimbabwe?",
        "Tell me which team won the world series in 2006"
    ],
    'opinion question': [
        "Who's the greatest NBA player of all time?"
    ],
    'other': []
}

# Create the intent classifier and run it on the disambiguated human utterance
ic = rd.planners.IntentClassifier(intents=intents) 
label, _ = ic(disambiguated_utt)

print(f"Human utterance classified as {colored(label, 'green')}")