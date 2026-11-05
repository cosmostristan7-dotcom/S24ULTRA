##This following script is designed to run a light A.I. nested inside a USB device.

# A basic script using a lightweight library like llama-cpp-python.
from llama_cpp import Llama


# Load a small, quantized model stored on your USB.
llm = Llama(model_path="./models/gema-model.gguf", n_ctx=2048)


# Prompt the lightweight local A.I.
output = llm("Write a short, encouraging note for a programmer:", max_tokens=100)
print(output['choices'][0]['text'])

