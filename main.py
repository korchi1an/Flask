from flask import Flask, request, jsonify
import openai

API_KEY = "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"

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = API_KEY

@app.route('/generate_text', methods=['POST'])
def generate_text():
    # Get the input data from the Postman request
    data = request.get_json()
    prompt = data.get('prompt')
    max_tokens = data.get('max_tokens')

    # Use the OpenAI API to generate text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens
    )

    # Extract the generated text
    generated_text = response.choices[0].text

    # Return the generated text as JSON
    return jsonify({"result": generated_text})

if __name__ == '__main__':
    app.run(debug=True)


