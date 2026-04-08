## Mathematics First-Principles Tutor

An Agentic MLOps Pipeline for Mathematical Reasoning & Visualization
This project is a production-grade AI agent designed to teach mathematics through first-principles reasoning. Unlike standard LLM responses, this system uses an Agentic Framework to write, execute, and verify Python code for mathematical proofs, providing both symbolic answers and visual intuition.

###### Live Access

Web Dashboard: https://math-first-principles-tutor-7smkjc9js4xv466mg26sl6.streamlit.app/

Production API: https://math-first-principles-tutor.onrender.com/docs

###### Technical Architecture

The system is built using a decoupled microservices architecture, optimized for bare-metal cloud deployment:

Agentic Core: Built with smolagents and LiteLLM, utilizing the Qwen-2.5-Coder model for high-precision code generation.

Backend: A FastAPI service that manages agent state, tool execution (SymPy, Matplotlib), and mathematical verification.

Frontend: A Streamlit dashboard featuring high-fidelity LaTeX rendering and dynamic plot generation.

Observability: Integrated with Langfuse for full-trace monitoring of agent reasoning and tool usage.

##### Key Features

First-Principles Reasoning: The agent doesn't just "guess" the answer; it derives it using symbolic computation.

Dynamic Visualizations: Automated generation of function plots and geometric representations.

Professional Typesetting: All solutions are rendered in LaTeX for academic-grade clarity.

Production-Ready MLOps: Features a decoupled CI/CD workflow, environment-based configuration, and real-time logging.

###### Tech Stack

Language: Python 3.12+

Frameworks: FastAPI, Streamlit

AI/LLM: smolagents, LiteLLM (Qwen-2.5-Coder), HuggingFace

Math/Stats: SymPy, Matplotlib, NumPy

DevOps: Render (PaaS), GitHub Actions, Langfuse

###### Installation & Local Setup
Clone the repository:

Bash

git clone https://github.com/jameskingsley/math-first-principles-tutor.git

cd math-first-principles-tutor

Setup Virtual Environment:

Bash

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

Environment Variables:

Create a .env file with your credentials:

* Plaintext

HF_TOKEN=your_huggingface_token

LANGFUSE_PUBLIC_KEY=your_key

LANGFUSE_SECRET_KEY=your_key

* Run the Application:

Backend: uvicorn app.main:app --reload

Frontend: streamlit run app/streamlit_app.py

###### Author

James Kingsley Philip, Data Scientist & AI/ML Instructor Specializing in architecting end-to-end MLOps pipelines and translating complex theory into production-ready business solutions.