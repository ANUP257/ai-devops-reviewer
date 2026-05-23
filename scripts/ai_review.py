import os
import google.generativeai as genai

with open("review.txt", "w") as f:
    f.write("Starting AI Review...")

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")

    with open("diff.txt", "r") as f:
        diff = f.read()

    if not diff.strip():
        review = "No code changes detected."
    else:
        response = model.generate_content(f"""You are a senior DevOps engineer.
Review the following code diff and:
- Identify bugs
- Suggest improvements
- Highlight security risks

Code:
{diff}""")
        review = response.text

except Exception as e:
    review = f"AI Review Error: {str(e)}"

with open("review.txt", "w") as f:
    f.write(review)

print(review)
