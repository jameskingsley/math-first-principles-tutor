import streamlit as st
import requests
import base64
from io import BytesIO
from PIL import Image

# --- UI SETUP ---
st.set_page_config(
    page_title="First-Principles Math Tutor",
    page_icon="",
    layout="centered"
)

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    .reasoning-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #FF4B4B;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("First-Principles Math Tutor")
st.markdown("""
This AI agent doesn't just calculate; it **reasons**, **writes code**, and **symbolically verifies** its own logic.
""")

# Sidebar for Project Context
with st.sidebar:
    st.header("Project Info")
    st.info("""
    **Stack:**
    - Agent: smolagents (Qwen-2.5-Coder)
    - Backend: FastAPI
    - Observability: Langfuse
    - Math: SymPy
    """)
    st.divider()
    st.write("Developer: James Kingsley ")
    st.write("Location: Nigeria")

# User Input
problem = st.text_area(
    "Enter your Math Problem:", 
    placeholder="e.g., Find the area under y=x^2 from 0 to 3 and plot the result.",
    height=150
)

# EXECUTION LOGIC 
if st.button("Solve & Verify"):
    if problem:
        with st.spinner("Agent is thinking, coding, and verifying..."):
            try:
                # Send request to FastAPI backend
                response = requests.post(
                    "https://math-first-principles-tutor.onrender.com/solve", 
                    json={"problem": problem}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Display Agent's Working/Reasoning (The "How")
                    if data.get("working"):
                        with st.expander("View Agent's Reasoning & Working", expanded=True):
                            st.markdown("### Internal Thought Process")
                            st.code(data["working"], language="python")
                    
                    # Display the Final Answer
                    st.subheader("Final Answer")
                    st.success(data["answer"])
                    
                    # Render the Plot if returned by the backend
                    if data.get("plot"):
                        st.divider()
                        st.subheader("Visual Representation")
                        image_bytes = base64.b64decode(data["plot"])
                        img = Image.open(BytesIO(image_bytes))
                        st.image(img, use_container_width=True)
                    
                else:
                    st.error(f"Server Error ({response.status_code}): {response.text}")
            except Exception as e:
                st.error("Connection Failed: Ensure the FastAPI server is running at http://localhost:8000")
                st.exception(e)
    else:
        st.warning("Please enter a mathematical query to proceed.")

# Footer
st.divider()
st.caption("Built for AI/ML Project Portfolio - MLOps Grade")