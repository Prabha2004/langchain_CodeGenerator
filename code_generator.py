from transformers import pipeline

def get_user_input():
    """Prompt the user to input a Python code requirement."""
    print("Enter the Python code requirement (e.g., 'A function to calculate Fibonacci numbers'):")
    return input("Requirement: ")

def generate_code(requirement):
    """
    Generates Python code based on the provided requirement using Hugging Face's text-generation pipeline.

    Args:
        requirement (str): A description of the code to be generated.

    Returns:
        str: Generated Python code or an error message.
    """
    try:
        # Load a text generation pipeline using GPT-2
        generator = pipeline("text-generation", model="gpt2")
        
        # Generate code using the pipeline
        result = generator(
            f"You are a Python programmer. Write Python code for the following requirement:\n{requirement}",
            max_length=200,
            num_return_sequences=1,
            pad_token_id=50256  # Ensure compatibility with GPT-2's tokenizer
        )
        
        return result[0]["generated_text"]
    except Exception as e:
        return f"An error occurred during code generation: {e}"

if __name__ == "__main__":
    try:
        user_requirement = get_user_input()
        print("\nProcessing your request...\n")
        
        # Generate Python code based on the user input
        generated_code = generate_code(user_requirement)
        
        print("\nGenerated Python Code:\n")
        print(generated_code)
    except Exception as e:
        print(f"An error occurred: {e}")

