tools = {
    "KubectlTool": {
        "name": "kubectl",
        "description": "Execute a kubectl command against the Kubernetes cluster.",
        "args": {
            "command": {
                "type": str,
                "description": "The kubectl command to execute.",
                "required": True
            },
            "namespace": {
                "type": str,
                "description": "The namespace to use for the kubectl command.",
                "required": False,
                "default": "default"
            },
        }
    }
}