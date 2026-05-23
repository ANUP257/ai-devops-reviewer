import os

# Always create review.txt first thing
with open("review.txt", "w") as f:
    f.write("Starting AI Review...")

try:
    import openai
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    with open("diff.txt", "r") as f:
        diff = f.read()

    if not diff.strip():
        review = "No code changes detected."
    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert DevOps reviewer"},
                {"role": "user", "content": f"Review this code diff:\n{diff}"}
            ],
            temperature=0.3
        )
        review = response.choices[0].message.content

except Exception as e:
    review = f"AI Review Error: {str(e)}"

# Update review.txt with actual result
with open("review.txt", "w") as f:
    f.write(review)

print(review)
