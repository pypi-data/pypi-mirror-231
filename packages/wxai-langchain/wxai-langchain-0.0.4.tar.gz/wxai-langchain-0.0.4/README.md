# IBM watsonx.ai LangChain interface

This is a Python library to add a LangChain interface to IBM watsonx.ai. This is not an IBM project and is not supported by IBM.

GitHub repo: https://github.com/rampadc/wxai-langchain

```shell
pip install wxai-langchain==0.0.4
```

## v0.0.4

Version 0.0.4 is a breaking change and uses ibm-watson-machine-learning SDK to use the syntatic sugars that comes with the SDK.

```shell
pip install -e '.[dev]'
```

Examples:

1. Create a new `.env` file `examples/0.0.4` with contents

```
API_KEY=
PROJECT_ID=
```

2. Run the examples with 

```shell
python examples/0.0.4/<example-file>.py
```

## v0.0.2

Version 0.0.2 does not use ibm-watson-machine-learning SDK.

To install,

```shell
pip install wxai-langchain==0.0.2
```

To use, see the examples folder. This LangChain interface is not compatible with IBM's GenAI GenerateParams schema object.
Always use a JSON for the model's parameters as shown in the examples.