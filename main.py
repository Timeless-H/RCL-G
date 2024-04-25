import os
from groq import Groq

api_key = os.environ["MY_GROQ_API_KEY"]

client = Groq(api_key=api_key)

chats = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what jobs can a fresh phd in geomatics engineering (with focus on geospatial vision) graduate with no industry work experience get?"
        }
    ],
    model="llama3-70b-8192"
)

print(chats.choices[0].message.content)