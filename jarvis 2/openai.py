import openai

# Initialize OpenAI API
openai.api_key = "YOUR_OPENAI_API_KEY"

def ask_openai(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return answer
    except Exception as e:
        return "Sorry, I couldn't process your request."
