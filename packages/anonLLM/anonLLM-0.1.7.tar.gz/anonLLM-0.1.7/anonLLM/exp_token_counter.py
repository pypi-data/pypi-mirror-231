from functools import wraps
from tiktoken import encoding_for_model


class TokenCounter:
    def __init__(self, input_kwarg, output_var, summary_limit=50):
        self.input_kwarg = input_kwarg
        self.output_var = output_var
        self.summary_limit = summary_limit
        self.encoding = encoding_for_model("gpt-3.5-turbo")

    def count_tokens(self, text):
        tokens = [self.encoding.decode_single_token_bytes(token) for token in self.encoding.encode(text)]
        return len(tokens)

    def summarize_text(self, text):
        return text[:50] + "..."  # Simple truncation for demonstration

    def token_counter_decorator(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Count tokens for input
            input_text = kwargs.get(self.input_kwarg, "")
            input_tokens = self.count_tokens(input_text)

            # Summarize input if too long
            if input_tokens > self.summary_limit:
                input_summary = self.summarize_text(input_text)
                print(f"Input summary: {input_summary}")

            # Call the original function
            output_text = func(*args, **kwargs)

            # Extract output text based on the variable name provided
            output_actual_text = output_text.get(self.output_var, "")

            # Count tokens for output
            output_tokens = self.count_tokens(output_actual_text)

            # Print or store token count
            print(f"Input tokens: {input_tokens}, Output tokens: {output_tokens}")

            return output_text
        return wrapper

# Example usage
token_counter = TokenCounter(input_kwarg="prompt", output_var="response")

@token_counter.token_counter_decorator
def my_function(prompt):
    # Simulate some text generation
    response = f"Hello, {prompt}!"
    return {"response": response}

result = my_function(prompt="How are you?")
