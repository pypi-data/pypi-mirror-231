# README for AI Library

The AI library is a Python package that allows you to interact with various AI-powered services, including chat with GPT-based models and generate art using the Picasso Diffusion model. This README provides an overview of the library's functionality and usage.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
    - [Initialization](#initialization)
    - [Chat with GPT](#chat-with-gpt)
    - [Generate Art](#generate-art)
3. [Contributing](#contributing)
4. [License](#license)

## Installation <a name="installation"></a>

To use the AI library, you'll need to install it. You can install them using `pip`:

```bash
pip install tools-ai
```

## Usage <a name="usage"></a>

### Initialization <a name="initialization"></a>

To get started with the AI library, you first need to initialize an `AI` object:

```python
from ai_library import AI

ai = AI()
```

### Chat with GPT <a name="chat-with-gpt"></a>

You can use the `send_message` method to chat with GPT-based models. This method sends a message and retrieves a response from the model:

```python
response = ai.send_message("Hello, GPT!")
print(response)
```

The `send_message` method takes a single parameter, `content`, which is the message you want to send to the GPT model.

### Generate Art <a name="generate-art"></a>

The AI library also provides a feature to generate art using the Picasso Diffusion model. You can use the `generate_art` method for this purpose:

```python
art_image = ai.generate_art(
    prompt="A colorful abstract painting",
    steps=30,
    scale=9,
    type="Realistic",
    negative_prompt="",
    disable_auto_prompt=True
)
```

The `generate_art` method takes several parameters, including the art details (`prompt`), the number of steps for art creation (`steps`), the scale of the art (`scale`), the art type (`type`), a negative prompt for art creation (`negative_prompt`), and an option to disable auto prompt correction (`disable_auto_prompt`).

## Contributing <a name="contributing"></a>

Contributions to this library are welcome! If you have any ideas for improvements or new features, please open an issue or submit a pull request on the [GitHub repository](https://github.com/your-repo-url).

## License <a name="license"></a>

This library is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.