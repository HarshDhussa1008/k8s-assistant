from openai import OpenAI
from k8s_assistant.llms.LLM import LLM

class GPT(LLM):
    """GPT class for interacting with the OpenAI GPT model."""
    
    def __init__(self):
        
        self.api_key = os.getenv("GPT_API_KEY")
        if not self.api_key:
            raise ValueError("GPT_API_KEY environment variable not set")
        self.user_history = []
        self.gpt_client = self._initialize_client()
        
        
    def _initialize_client(self) -> OpenAI:
        """Initialize and return the Anthropic client."""
        
        if not self.api_key:
            raise ValueError("GPT_API_KEY environment variable not set")
        return OpenAI(api_key=self.api_key)
        

    def get_response(self, max_tokens: int, model: str, prompt: str, tools: list=[]) -> dict:
        """Get a response from the GPT model."""
        
        # print(f"Prompt: {prompt}")
        # print(f"Model: {model}")
        # print(f"Max Tokens: {max_tokens}")
        # print(f"Tools: {tools}")
        # print(f"User History: {self.user_history}")
        
        # Call the GPT API to get a response
        response = self.gpt_client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                *self.user_history,
                {"role": "developer", "content": prompt}
            ],
            tools=tools
        )
        
        # Append the user history to the GPT model
        # self.update_llm_history(
        #     role="assistant",
        #     content=response.choices[0].message.content if len(response.choices) > 0 else ""
        # )
        
        return response
    
    
    def update_llm_history(self, role: str, content: str|list) -> None:
        """Update the user history with the latest user input."""
        
        if isinstance(content, list) and role == "assistant":
            # Try to extract text content from choices if it's a list
            try:
                formatted_content = content[0].message.content if len(content) > 0 else ""
            except (AttributeError, IndexError):
                formatted_content = str(content)
        else:
            formatted_content = content
        
        self.user_history.append(
            {
                "role": role,
                "content": formatted_content
            }
        )
