# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openbrain', 'openbrain.agents', 'openbrain.orm']

package_data = \
{'': ['*']}

install_requires = \
['aws-lambda-powertools>=2.25.0,<3.0.0',
 'aws-xray-sdk>=2.12.0,<3.0.0',
 'black>=23.9.1,<24.0.0',
 'boto3>=1.28.51,<2.0.0',
 'gradio>=3.44.4,<4.0.0',
 'langchain>=0.0.295,<0.0.296',
 'openai>=0.28.0,<0.29.0',
 'pre-commit>=3.4.0,<4.0.0',
 'promptlayer>=0.2.9,<0.3.0',
 'pydantic>=2.3.0,<3.0.0',
 'python-dotenv>=1.0.0,<2.0.0',
 'python-ulid>=1.1.0,<2.0.0',
 'requests>=2.31.0,<3.0.0',
 'tiktoken>=0.5.1,<0.6.0']

entry_points = \
{'console_scripts': ['ob = openbrain.agents.gpt_agent:cli',
                     'ob-chat = openbrain.agent.gpt_agent:chat',
                     'ob-tuner = openbrain.app:main']}

setup_kwargs = {
    'name': 'openbrain',
    'version': '0.4.11',
    'description': 'A package to interact with generative AI and build specialized generative AI workflows. This project is dual-licensed under AGPL-3.0 and a separate commercial license.',
    'long_description': '# OpenBrain\n\n![Main Build Status](https://github.com/svange/openbrain/actions/workflows/main.yml/badge.svg?event=push)\n\n🚧 **Under active development. Not ready for use.** 🚧\n\nOpenBrain is a chat platform backed by Large Language Model (LLM) agents. It provides APIs and tools to configure, store, and retrieve chat agents, making your chat sessions more versatile and context-aware. \n\nOpenBrain agents are stateful, so they can remember things about you and your conversation. They can also use tools, so you can use the same agent to chat and to perform actions. \n\nInteractions with the agent can be injected into any application easily by constructing a query, choosing an agent configuration, and pre-processing your data through that agent before sending it of for further processing.\n\n## Features\n\n- **Interactive Agent Tuner**: A GUI to modify and test agent configurations.\n- **Command-Line Interface**: Use `ob` for quick completions and `ob-chat` for an interactive session.\n- **Flexible Configuration**: Customizable agents through DynamoDB backed ORM.\n- **Event-Driven Architecture**: Extensible through cloud-based event handling.\n\n## Quick Start\n### Installation\n\n\n```bash\npip install openbrain\n```\n\n### Setup .env file\n```bash\ncp .env.example .env  # Edit this file with your own values\n```\n### Deploy Supporting Infrastructure\n```bash\npython ci_cd.py -I\n```\n\n## Using OpenBrain\n\n### OpenBrain Gradio Tuner\nTo facilitate tuning agent parameters and experimenting with prompts, OpenBrain provides a GUI interface using Gradio. To launch the GUI.\n\n![img.png](img.png)\n\n```bash\n$ ob-tuner\nRunning on local URL:  http://0.0.0.0:7861\n\nTo create a public link, set `share=True` in `launch()`.\nTip: You can show or hide the button for flagging with the `allow_flagging=` kwarg; for example: gr.Interface(..., allow_flagging=False)\n```\n\n### Command Line Completions\n\n```bash\n$ ob "What is the air speed velocity of an unladen swallow?" -v\n\n> Entering new AgentExecutor chain...\nAh, the famous question about the air speed velocity of an unladen swallow. Are you referring to an African or European swallow?\n\n> Finished chain.\nAh, the famous question about the air speed velocity of an unladen swallow. Are you referring to an African or European swallow?\n```\n\n### Command Line Interactive Session\n\n```bash\n$ ob-chat\n---------- Begin Chat Session ----------\n> OpenBrain: What… is your name?\nUser: It is Arthur – King of the Britons.\n> OpenBrain: What… is your quest?\nUser: To seek the Holy Grail.\n> OpenBrain: What… is the air-speed velocity of an unladen swallow?\nUser: What do you mean? An African or a European swallow?\n> OpenBrain: I don’t know that. Aaaaaaaaagh!\n```\n\n## Architecture Overview\n\n### Data Model\n\n```mermaid\nclassDiagram\n    class ChatMessage {\n        User provided*\n        + str: sessionId\n        + str: clientId\n        + str: message\n        + AgentConfig: agentConfigOverrides\n        + str: agentConfig\n        + bool: reset\n    }\n\n    class AgentConfig {\n        + str: profileName\n        + str: clientId\n        + str: iceBreaker\n        + Decimal: temperature\n        + ...\n        + save()\n        + refresh()\n        + load()\n        + delete()\n        + get_all()\n    }\n\n    class ChatSession {\n        + str: sessionId\n        + str: clientId\n        + byte: agentMemory\n        + AgentConfig: agentConfig\n        + Lead: lead\n        + save()\n        + load()\n    }\n\n    class Lead {\n        + str: sessionId\n        + str: clientId\n        + str: fullName\n        + str: firstName\n        + str: middleName\n        + str: lastName\n        + List[str]: medications\n        + str: email\n        + ...\n        + save()\n        + refresh()\n        + delete()\n        + load()\n        + get_all()\n    }\n\n    ChatSession "1" *-- "1" Lead: contains\n    ChatSession "1" *-- "1" AgentConfig: contains\n%%    ChatMessage "1" *-- "1" AgentConfig: contains\n%%    ChatSession "1" *-- "*" ChatMessage: contains\n    ChatSession "1" *-- "1" langchain_ChatMemory: from langchain, serialized\n```\n\n# Data Flow diagram\nOpenBrain uses an event driven architecture. The agent sends events to event bus and then the developer can simply write rules and targets for the incoming events once the targets are ready. The following diagram shows the data flow in two parts.\n1. The user interaction with the agent and the agent interaction with an event bus.\n2. The event bus and the targets that are triggered by the events.\n```mermaid\nsequenceDiagram\n    title Agent Data Flow\n    participant User\n    create participant GPT Agent\n    participant AgentConfigTable\n    participant OpenAI\n    participant Tool\n    participant EventBus\n\n    User ->> GPT Agent: (AgentConfig, AgentMemory), ChatMessage\n        GPT Agent -->> AgentConfigTable: profileName\n        AgentConfigTable -->> GPT Agent: AgentConfig\n        GPT Agent -->> OpenAI: ChatMessage\n        OpenAI -->> GPT Agent: ChatMessage\n%%        GPT Agent ->> GPT Agent: Create/Update Object\n        GPT Agent -->> Tool: Tool(Object, clientId)\n        Tool -->> EventBus: (Object, clientId, session_id, object_id)\n        Tool -->> GPT Agent: ChatMessage\n    destroy GPT Agent\n    GPT Agent ->> User: ChatMessage, (AgentConfig, AgentMemory), Object\n\n  box blue Databases\n      participant AgentConfigTable\n  end\n  box purple Tool\n      participant Tool\n  end\n\n  box gray EventBus\n      participant EventBus\n  end\n\n  box red Provider\n      participant OpenAI\n  end\n```\n\n```mermaid\nsequenceDiagram\n    title Agent Data Flow\n    participant SQS\n    participant EventBus\n    participant Lambda\n    participant ObjectTable\n    participant AgentConfigTable\n    participant ChatHistoryTable\n    participant ExternalSite\n\n    EventBus ->> Lambda: (Object, clientId, sessionId, objectId)\n    Lambda -->> ObjectTable: (clientId, objectId)\n    ObjectTable -->> Lambda: Object\n\n    Lambda -->> AgentConfigTable: (profileName, clientId)\n    ChatHistoryTable -->> Lambda: AgentConfig\n\n    Lambda --> ChatHistoryTable: (clientId, sessionId)\n    ChatHistoryTable -->> Lambda: (AgentMemory, AgentConfig)\n\n    Lambda ->> ExternalSite: ...\n    ExternalSite --x Lambda: ERROR\n    Lambda ->> SQS: <DETAILS NEEDED TO RETRY>\n    ExternalSite ->> Lambda: ...\n\n    Lambda -> EventBus: <POTENTIAL NEW EVENT>\n\n    box maroon DeadLetterQueue\n        participant SQS\n    end\n\n    box blue Databases\n        participant ObjectTable\n        participant AgentConfigTable\n        participant ChatHistoryTable\n    end\n\n    box gray EventBus\n        participant EventBus\n    end\n\n    box brown EventTargets\n        participant Lambda\n    end\n\n    box green Internet\n        participant ExternalSite\n    end\n\n\n\n```\n\n## Contributing\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.\n\n## License\n\n- **Open Source**: AGPL-3.0, see [LICENSE](LICENSE)\n- **Commercial**: See [COMMERCIAL_LICENSE](COMMERCIAL_LICENSE) and contact us for inquiries.\n',
    'author': 'Samuel Vange',
    'author_email': '7166607+svange@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
