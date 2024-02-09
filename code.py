import openai
import json

# Load your OpenAI API Key
openai.api_key = 'your_api_key_here'

def analyze_customer_journey(journey_data):
    """
    Analyze customer journey data using OpenAI to detect potential anomalies.
    """
    prompt = f"Detect any anomalies or potential issues in this customer journey: {journey_data}"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5
        )
        print("Analysis Results:", response.choices[0].text.strip())
    except Exception as e:
        print("An error occurred:", str(e))

# Example journey data
example_journey = """
Customer starts at HomePage, clicks on Product XYZ, adds to cart, attempts to checkout, 
receives error 'Payment Gateway Timeout', tries again with a different card, completes purchase.
"""

# Analyze the provided example customer journey
analyze_customer_journey(example_journey)
