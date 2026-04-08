from app.agent import agent
import sympy as sp

def test_calculus_logic():
    print(" Starting First-Principles Math Test...")
    
    # A problem that requires: 1. Symbolic math, 2. Power rule, 3. Verification
    problem = "Find the derivative of f(x) = 3x^3 + 2x^2 + 5. Then verify the result for x=1."
    
    print(f" Student Query: {problem}")
    print("-" * 30)
    
    try:
        # Run the agent
        response = agent.run(problem)
        
        print("\n Agent Response:")
        print(response)
        
        # Check if the response contains common indicators of success
        if "9*x**2 + 4*x" in str(response) or "9x^2 + 4x" in str(response):
            print("\n TEST PASSED: Derivative is correct.")
        else:
            print("\n TEST FAILED: Result does not match expected derivative.")
            
    except Exception as e:
        print(f"\n TEST CRASHED: {str(e)}")

if __name__ == "__main__":
    test_calculus_logic()