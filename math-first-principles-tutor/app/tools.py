from smolagents import Tool
import sympy as sp

class MathVerificationTool(Tool):
    name = "math_verifier"
    description = "Verifies if two mathematical expressions are algebraically equivalent using symbolic logic."
    inputs = {
        "expression_a": {"type": "string", "description": "The target expression or problem (e.g., 'x**2 - 1')"},
        "expression_b": {"type": "string", "description": "The solution to verify (e.g., '(x-1)*(x+1)')"}
    }
    output_type = "string"

    def forward(self, expression_a: str, expression_b: str) -> str:
        try:
            # First Principles: Use SymPy to simplify and compare
            expr_a = sp.simplify(expression_a)
            expr_b = sp.simplify(expression_b)
            
            if sp.expand(expr_a) == sp.expand(expr_b):
                return "VERIFICATION SUCCESSFUL: The logic is mathematically sound."
            else:
                return f"VERIFICATION FAILED: {expression_a} is NOT equivalent to {expression_b}."
        except Exception as e:
            return f"Error in symbolic verification: {str(e)}"