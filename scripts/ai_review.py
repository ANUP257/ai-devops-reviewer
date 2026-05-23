import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def review_code(diff):
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert DevOps reviewer"},
                {"role": "user", "content": f"""
You are a senior DevOps engineer.
Review the following code diff and:
- Identify bugs
- Suggest improvements
- Highlight security risks

Code:
{diff}
"""}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Review could not be completed. Error: {str(e)}"

if __name__ == "__main__":
    # Create empty diff if file doesn't exist
    if not os.path.exists("diff.txt"):
        with open("diff.txt", "w") as f:
            f.write("")

    with open("diff.txt", "r") as f:
        diff = f.read()

    if not diff.strip():
        review = "No code changes detected to review."
    else:
        review = review_code(diff)

    # Always write review.txt even if API fails
    with open("review.txt", "w") as f:
        f.write(review)

    print(review)
