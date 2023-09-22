<div align="center">
<img alt="ralf-dialogue_logo" src="https://github.com/jhuapl-fomo/ralf-dialogue/blob/main/assets/ralf-dialogue_logo_v1.png" width="200">
  
# ralf-dialogue

[![Documentation](https://readthedocs.org/projects/ralf-jhuapl/badge/?version=latest)](https://ralf-jhuapl.readthedocs.io/en/latest/)
[![PyPI version](https://badge.fury.io/py/ralf-dialogue-jhuapl.svg)](https://badge.fury.io/py/ralf-dialogue-jhuapl)
[![License](https://img.shields.io/github/license/jhuapl-fomo/ralf.svg)](https://github.com/jhuapl-fomo/ralf/blob/main/LICENSE)
</div>

**ralf-dialogue** is a Python framework for quickly prototyping dialogue agents that leverage large language models (LLMs),
like ChatGPT or GPT-4. It lives in the broader RALF ecosystem, and assumes the use of the **ralf** library, which
provides primitives, constructs, and other utilities for building complex systems around large language models
using a desingn paradigm that some parts of the community have begun to call *composability*.

## A word on the broader RALF ecosystem

**ralf** is a Python library intended to assist developers in creating applications
that involve calls to Large Language Models (LLMs). A core concept in **ralf** is the idea of *composability*,
which allows chaining together LLM calls such that the output of one call can be
used to form the prompt of another. **ralf** makes it easy to chain together both
LLM-based and Python-based actions&mdash; enabling developers to construct complex 
information processing pipelines composed of simpler building blocks. Using LLMs
in this way can lead to more capable, robust, steerable and inspectable applications.

A general framework for building applications -- including conversational AIs -- that rely
on a mix of prompted large language models (LLMs) and conventional Python code and services.
This can be considered a powerful form of neuro-symbolic AI. Other frameworks -- such as this
one, `ralf-dialogue` -- build on the core `ralf` library, adding primatives and components for
building conversational agents (or "chatbots") that can interact with users in natural language,
leveraging context and accessing external knowledge stores or reasoning engines. Many of these
components are still under active construction, and we're always looking for talented contributors.

## Quickstart Guide
This quickstart guide is intended to get you up and running with **ralf** within
a few minutes.
### Installation

We recommend creating a Conda environment before installing the package:

    conda create -n ralf python=3.10
    conda activate ralf

#### Install from PyPI

You may install **ralf-dialogue** from PyPI using ``pip``:

    pip install ralf-dialogue-jhuapl

#### Install from Source

Alternatively, you can build the package from source. First, clone the Github repository:

    git clone https://github.com/jhuapl-fomo/ralf-dialogue.git

Next, install the requirements using ``pip``:
    
    cd ralf-dialogue
    pip install -r requirements.txt

Then, build the package using ``flit`` and install it using ``pip``:

    flit build
    pip install .

Or if you would like an editable installation, you can instead use:

    pip install -e .

### OpenAI Configuration
**ralf** currently relies on language models provided by OpenAI. 
In order to access the models, you must store your OpenAI API key as an 
environment variable by executing the following in bash:

    echo "export OPENAI_API_KEY='yourkey'" >> ~/.bashrc
    source ~/.bashrc

### Running the Demos
To test if installation was successful, try running the demo scripts:

    cd demos
    python simple_chat.py

This demo script will allow you to converse with a chatbot created using **ralf-dialogue**. Next, you can delve deeper and explore other features of the library:

    python analyze_conversation.py

If the scripts execute successfully, you are good to go!

