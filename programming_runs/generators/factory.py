from .py_generate import PyGenerator
from .rs_generate import RsGenerator
from .generator_types import Generator
from .rewriter import ReWriter
from .model import CodeLlama, ModelBase, GPT4, GPT35, StarChat, GPTDavinci, OpenChat


def generator_factory(lang: str) -> Generator:
    if lang == "py" or lang == "python":
        return PyGenerator()
    elif lang == "rs" or lang == "rust":
        return RsGenerator()
    elif lang == "text":
        return ReWriter()
    else:
        raise ValueError(f"Invalid language for generator: {lang}")


def model_factory(model_name: str) -> ModelBase:
    if model_name in {"gpt-4", "gpt4-turbo-128k"}:
        return GPT4(name=model_name)
    elif model_name == "gpt-35-turbo-0301":
        return GPT35()
    elif model_name == "starchat":
        return StarChat()
    elif model_name in {"mistralai/Mixtral-8x7B-Instruct-v0.1", "codellama/CodeLlama-70b-Instruct-hf",
                        "meta-llama/Llama-2-70b-chat-hf", "01-ai/Yi-34B-Chat"}:
        return OpenChat(name=model_name)
    elif model_name.startswith("codellama"):
        # if it has `-` in the name, version was specified
        kwargs = {}
        if "-" in model_name:
            kwargs["version"] = model_name.split("-")[1]
        return CodeLlama(**kwargs)
    elif model_name.startswith("text-davinci"):
        return GPTDavinci(model_name)
    else:
        raise ValueError(f"Invalid model name: {model_name}")
