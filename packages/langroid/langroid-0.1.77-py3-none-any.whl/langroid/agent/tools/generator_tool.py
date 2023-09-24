"""
A tool to generate a message from the current pending message.
The idea is that when an LLM is generating text that is a deterministic transformation
of known text, then specifying the transformation can be much cheaper than actually
generating the transformation.
"""

from langroid.agent.tool_message import ToolMessage

class GeneratorTool(ToolMessage):
    request: str = "generate"
    purpose: str = """
            To generate a message where the parts within curly braces  
            are derived from previous previous messages in the conversation,
            using  
            message are 
            obtained from a previous message numbered <n>, 
            using the <rules>.
            """
    rules: str


    def handle(self) -> str:
        pass

