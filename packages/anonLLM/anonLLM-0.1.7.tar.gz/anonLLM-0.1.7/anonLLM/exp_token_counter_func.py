from functools import wraps
from tiktoken import encoding_for_model


def token_counter(input_kwarg, output_var, summary_limit=50):
    encoding = encoding_for_model("gpt-3.5-turbo")

    def count_tokens(text):
        tokens = [encoding.decode_single_token_bytes(token) for token in encoding.encode(text)]
        return len(tokens)

    def summarize_text(text):
        return text[:50] + "..."  # Simple truncation for demonstration

    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            # Count tokens for input
            input_text = kwargs.get(input_kwarg, "")
            input_tokens = count_tokens(input_text)

            # Summarize input if too long
            if input_tokens > summary_limit:
                input_summary = summarize_text(input_text)
                print(f"Input summary: {input_summary}")

            # Call the original function
            output_text = func(*args, **kwargs)

            # Extract output text based on the variable name provided
            output_actual_text = output_text.get(output_var, "")

            # Count tokens for output
            output_tokens = count_tokens(output_actual_text)

            # Print or store token count
            print(f"Input tokens: {input_tokens}, Output tokens: {output_tokens}")

            return output_text
        return inner_wrapper
    return wrapper

# Example usage


@token_counter(input_kwarg="prompt", output_var="response")
def my_function(prompt):
    # Simulate some text generation
    response = f"Hello, {prompt}!"
    return {"response": response}


result = my_function(prompt="How are you?")
