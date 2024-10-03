from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

openai_client = OpenAI()


def chat_completion(user_input):
    # Call OpenAI API
    completion = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You're an expert in motivating people. It the user shares what's wrong, address it. Otherwise give general motivation",
            },
            {"role": "user", "content": user_input},
        ],
    )
    response = completion.choices[0].message.content
    return response
