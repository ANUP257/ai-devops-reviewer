import os
import google.generativeai as genai

# Always create review.txt first
with open("review.txt", "w") as f:
    f.write("Starting AI Review...")

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")

    with open("diff.txt", "r") as f:
        diff = f.read()

    if not diff.strip():
        review = "No code changes detected."
    else:
        prompt = f"""You are a senior DevOps engineer.
Review the following code diff and:
- Identify bugs
- Suggest improvements
- Highlight security risks

Code:
{diff}"""

        response = model.generate_content(prompt)
        review = response.text

except Exception as e:
    review = f"AI Review Error: {str(e)}"

# Always update review.txt with final result
with open("review.txt", "w") as f:
    f.write(review)

print(review)
