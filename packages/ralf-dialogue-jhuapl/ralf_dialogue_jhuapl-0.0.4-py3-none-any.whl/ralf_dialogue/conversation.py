# Copyright (c) 2023 The Johns Hopkins University Applied Physics Laboratory

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Optional, Literal
import ralf.utils as ru

class Turn:
    """
    Represents a conversational turn with a speaker and an utterance.

    :param speaker: The speaker of the turn.
    :type speaker: str
    :param utterance: The utterance made by the speaker.
    :type utterance: str
    """
    def __init__(self, speaker: str, utterance: str) -> None:
        """Constructor method
        """

        self.speaker = speaker
        self.utterance = utterance

    def __str__(self) -> str:
        return f"{self.speaker}: {self.utterance}"

    def __repr__(self) -> str:
        return self.__str__()

class Conversation:
    """
    Represents a conversation with a history of turns.

    :param history: Optional. The history of turns in the conversation.
    :type history: list[Turn] or None
    :param ai_attribution: The attribution for AI speakers (default is 'AI').
    :type ai_attribution: str
    :param human_attribution: The attribution for human speakers 
    (default is 'Human').
    :type human_attribution: str
    """
    def __init__(
        self,
        history: Optional[list[Turn]] = None,
        ai_attribution: str = 'AI',
        human_attribution: str = 'Human',
        trim_method: Literal['tokens', 'turns'] = 'turns',
        max_length: int = 100
    ) -> None:
        """
        Initializes a new Conversation object.

        :param history: Optional. The history of turns in the conversation.
        :param ai_attribution: The attribution for AI speakers.
        :param human_attribution: The attribution for human speakers.
        """
        self.history = history if history else []
        self.ai_attribution = ai_attribution
        self.human_attribution = human_attribution
        self.trim_method = trim_method
        self.max_length = max_length

    def __str__(self) -> str:
        """
        Returns a string representation of the conversation by joining turn 
        strings with newline.

        :return: A string representation of the conversation.
        :rtype: str
        """
        result = []

        for turn in self.history:
            result.append(str(turn))

        return '\n'.join(result)

    def __repr__(self) -> str:
        """
        Returns a string representation of the conversation, which is the same 
        as __str__().

        :return: A string representation of the conversation.
        :rtype: str
        """
        return self.__str__()
    
    def __len__(self) -> int:
        """
        Returns the length of the conversation, which is the number of turns

        :return: number of turns in the conversation
        :rtype: int
        """

        return len(self.history)
    
    def add(self,
            speaker: str,
            utterance: str,
            return_turn: bool = False
        ) -> Optional[Turn]:
        """
        Adds a new turn to the conversation history.

        :param speaker: The speaker of the turn.
        :type speaker: str
        :param utterance: The utterance made by the speaker.
        :type utterance: str
        :param return_turn: Whether to return the turn just added to history
        :type utterance: bool
        :return: The turn object that was just added
        :rtype: Optional[Turn]
        """
        self.history.append(Turn(speaker, utterance))

        # Automatically trim the conversation after adding a turn
        self.trim(method=self.trim_method,
                  max_length=self.max_length,
                  as_messages=True
        )

        return self.history[-1] if return_turn else None

    def add_human_turn(self,
                       utterance: str,
                       return_turn: Optional[bool] = False
        ) -> Optional[Turn]:
        """
        Adds a human turn to the conversation history

        :param utterance: The utterance made by the human
        :type utterance: str
        :param return_turn: Whether to return the turn just added to history
        :type utterance: bool
        """

        return self.add(self.human_attribution, utterance, return_turn=return_turn)

    def add_ai_turn(self,
                    utterance: str,
                    return_turn: Optional[bool] = False
        ) -> Optional[Turn]:
        """
        Adds an AI turn to the conversation history

        :param utterance: The utterance made by the AI
        :type utterance: str
        :param return_turn: Whether to return the turn just added to history
        :type utterance: bool
        """

        return self.add(self.ai_attribution, utterance, return_turn=return_turn)

    def get_last_human_turn(self) -> Optional[Turn]:
        """
        Retrieves the last user turn from the conversation history.

        :return: The last user turn or None if not found.
        :rtype: Optional[Turn]
        """
        for turn in reversed(self.history):
            if turn.speaker == self.human_attribution:
                return turn

    def to_list(self) -> list[str]:
        """
        Converts the conversation history to a list of string representations.

        :return: A list of string representations of turns.
        :rtype: list[str]
        """
        return [str(turn) for turn in self.history]
    
    def to_messages(
            self,
            system_message: str = ru.cfg['default_system_message']
        ) -> list[dict]:
        """
        Converts the conversation into a messages list for use with OpenAI's
        ChatCompletion models.

        :param system_message: system messsage to use for ChatCompletion call
        :type system_message: str

        :return: a list of messages in the conversation
        :rtype: list[dict]
        """

        messages = []
        messages.append({'role': 'system', 'content': system_message})
    
        for turn in self.history:
            if turn.speaker == self.ai_attribution:
                role = 'assistant'
            elif turn.speaker == self.human_attribution:
                role = 'user'
            else:
                raise ValueError(
                    f"Invalid speaker {turn.speaker} provided in conversation."
                )
            messages.append({'role': role, 'content': turn.utterance})

        return messages

    def to_str_double_newline(self) -> str:
        """
        Returns a string representation of the conversation by joining turn 
        strings with double newline.

        :return: A string representation of the conversation with double 
        newlines between turns.
        :rtype: str
        """
        result = []

        for turn in self.history:
            result.append(str(turn))

        return '\n\n'.join(result)
    
    def token_count(self, as_messages: bool = True) -> int:
        """
        Get the current token count of the conversation.

        This method calculates the total number of tokens in the conversation's
        history. You can choose to count tokens from either the conversation's
        messages or string representation.

        :param as_messages: If True, count tokens via messages representation
                            If False, count tokens from raw string representation
        :type as_messages: bool

        :return: The total token count.
        :rtype: int
        """
        if as_messages:
            num_tokens = ru.num_tokens_from_messages(self.to_messages())
        else:
           num_tokens = ru.num_tokens_from_str(str(self)) 

        return num_tokens
    
    def trim(self,
             method: Literal['tokens', 'turns'] = 'turns',
             max_length: int = 100,
             as_messages: bool = True,
             summarize: bool = False
        ) -> None:
        """
        Trim the conversation to maintain a specified maximum length, either
        in terms of tokens or number of turns. Used internally, but can also
        be used externally to manually trim the conversation.

        :param method: Method to use for trimming. Options are 'tokens' or 'turns'.
        :type method: Literal['tokens', 'turns']
        :param max_length: The maximum length to maintain (either tokens or turns).
        :type max_length: int
        :param as_messages: If True, count tokens based on messages.
                            If False, count tokens based on string representation.
        :type as_messages: bool

        :param summarize: If True, perform summarization during trimming (not implemented).
        :type summarize: bool

        :raises NotImplementedError: If summarize is True (summarization not implemented).
        :raises ValueError: If an invalid trim method is specified.
        """

        if summarize:
            raise NotImplementedError(
                "Trimming conversation with summarization not yet implemented.")
        
        if method == 'tokens':
            # Trim based on the number of tokens in the conversation history
            while (
                self.token_count(as_messages=as_messages) > max_length and len(self) > 0):
                # Remove the oldest turn until the token count is within limits
                self.history.pop(0)
    
        elif method == 'turns':
            # Trim based on the number of turns in the conversation history
            while len(self) > max_length:
                # Remove the oldest turn until turn count is within limits
                self.history.pop(0) 
        else:
            raise ValueError(
                f"Invalid trim method '{method}' specified. Use 'tokens' or 'turns'."
            )
