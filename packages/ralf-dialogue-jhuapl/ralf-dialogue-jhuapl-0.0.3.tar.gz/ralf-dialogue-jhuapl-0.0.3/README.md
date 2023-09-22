# `ralf-dialogue`

[![Documentation](https://readthedocs.org/projects/ralf-jhuapl/badge/?version=latest)](https://ralf-jhuapl.readthedocs.io/en/latest/)
[![PyPI version](https://badge.fury.io/py/ralf-jhuapl.svg)](https://badge.fury.io/py/ralf-jhuapl)
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

## Getting started

Create a new Conda environment (or equivalent) containing Python 3.9 and switch to it:
```bash
conda create -n [ralf-env-name] python=3.9
conda activate [ralf-env-name]
```

Make sure you have the RALF library cloned and installed:
```bash
git clone git@github.com:jhuapl-fomo/ralf.git
cd ralf
pip install -r requirements.txt
flit build
pip install -e .
```

Next, make sure you have this repo (the RALF Dialogue repo) cloned into a local directory, and then navigate into
it and repeat the same steps you followed above:
```bash
git clone git@github.com:jhuapl-fomo/ralf-dialogue.git
cd ralf-dialogue
pip install -r requirements.txt
flit build
pip install -e .
```


<!-- ## Tutorial -->
<!-- [**TODO**] -->

<!-- ### Setting up the configuration -->
<!-- [**TODO**: explain] -->

<!-- [**TODO**: models.yml] -->

<!-- [**TODO**: prompts.yml] -->

<!-- ### Actions Pipelines and The Action Dispatcher -->
<!-- [**TODO**] -->

<!-- ### Zero-shot Classifier -->
<!-- [**TODO**] -->

<!-- ## Read the Docs -->
<!-- [**TODO**] -->

<!-- ## Further Reading -->
<!-- [**TODO**] -->
