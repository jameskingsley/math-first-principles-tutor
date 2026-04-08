import os
import litellm
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel
from .tools import MathVerificationTool

load_dotenv()

# Enable Langfuse Tracing via LiteLLM
litellm.success_callback = ["langfuse"]
litellm.failure_callback = ["langfuse"]

# Set the project name for the dashboard
os.environ["LANGFUSE_PROJECT_NAME"] = "Math Tutor Monitoring"

model = LiteLLMModel(
    model_id="huggingface/Qwen/Qwen2.5-Coder-32B-Instruct",
    api_key=os.getenv("HF_TOKEN")
)

verification_tool = MathVerificationTool()

agent = CodeAgent(
    tools=[verification_tool],
    model=model,
    additional_authorized_imports=["sympy", "matplotlib.pyplot", "numpy", "pandas"],
    name="MathFirstPrinciplesTutor"
    
)