import io
import base64
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from fastapi import FastAPI
from pydantic import BaseModel
from .agent import agent

app = FastAPI(title="Math First-Principles Tutor API")

class MathRequest(BaseModel):
    problem: str

@app.get("/")
def health():
    return {"status": "online", "monitoring": "langfuse"}

@app.post("/solve")
async def solve_problem(request: MathRequest):
    # Run the agent 
    refined_query = f"{request.problem} (Note: Create any necessary plots but do not call plt.show())"
    result = agent.run(refined_query)
    
    # Extract "Working" 
    working_steps = []
    
    # Each step contains the model's reasoning (model_output)
    if hasattr(agent, 'memory') and hasattr(agent.memory, 'steps'):
        for step in agent.memory.steps:
            # We look for the 'model_output' which contains the 'Thought'
            if hasattr(step, 'model_output') and step.model_output:
                working_steps.append(step.model_output)
            
    steps_text = "\n\n---\n\n".join(working_steps)
    
    # 3. Extract plot if generated
    plot_base64 = None
    if plt.get_fignums():  
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        plot_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)
        
    return {
        "answer": result,
        "working": steps_text,
        "plot": plot_base64
    }