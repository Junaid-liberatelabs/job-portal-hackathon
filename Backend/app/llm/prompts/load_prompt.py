import yaml

def load_yaml_prompt(path: str, key: str):
    with open(f"app/llm/prompts/{path}.yml", "r") as file:
        return yaml.safe_load(file)[key]
