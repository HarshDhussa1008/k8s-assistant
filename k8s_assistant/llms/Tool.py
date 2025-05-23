from abc import abstractmethod
from typing import Any


class Params:
    """
    Class to encapsulate parameters for tools.
    """
    def __init__(self, **kwargs):
        self.params = kwargs

    def get(self, key: str, default: Any = None) -> Any:
        return self.params.get(key, default)


class Tool():
    """
    Abstract base class for all tools.
    """
    
    def __init__(self, name):
        
        from k8s_assistant.tools import tool_config
        config = tool_config.tools
        if name not in config:
            raise ValueError(f"Tool '{name}' not found in configuration.")
        config = config[name]
        
        self.name = config["name"]
        self.description = config["description"]
        self.args = config["args"]
    
    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        """
        Implement this method to run the tool.
        This method should contain the logic to execute the tool's functionality.
        """
        pass
    