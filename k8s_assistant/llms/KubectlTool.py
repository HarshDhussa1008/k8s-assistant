import subprocess
from typing import Any, Dict
from k8s_assistant.tools.Tool import Tool


class KubectlTool(Tool):
    """
    Class to interact with Kubernetes using kubectl.
    """

    def __init__(self):
        super().__init__("KubectlTool")
    
    def run(
        self,
        command: str, 
        namespace: str = "default"
    ) -> Dict[str, Any]:
        """
        Execute a kubectl command against the Kubernetes cluster.
        """
        
        forbidden_keywords = ["delete", "apply", "patch", "scale", "edit", "rollout restart", "cordon", "uncordon", "drain"]
        if any(keyword in command for keyword in forbidden_keywords):
            return {
                "stderr": "This command is not allowed for security reasons.",
                "stdout": "",
                "code": 403,
                "status": "forbidden"
            }
        
        cmd = f"kubectl {command}"
        
        if namespace and '-n' not in command:
            cmd += f" -n {namespace}"
        print(f"Executing command: {cmd}")
        
        try:
            result = subprocess.run(
                cmd.split(), 
                capture_output=True, 
                text=True,
                check=False,
                timeout=10  # Timeout after 10 seconds
            )
            
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "status": "success" if result.returncode == 0 else "error",
                "code": result.returncode
            }
        
        except subprocess.TimeoutExpired:
            return {"error": "Command timed out", "status": "timeout"}
        except Exception as e:
            return {"error": str(e), "status": "exception"}
