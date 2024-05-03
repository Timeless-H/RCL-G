import os
from groq import Groq


def main(user_input):
    api_key = os.getenv("API_KEY")

    client = Groq(api_key=api_key)

    chats = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Parse the following into (job title/position, responsibiliities/duties, company vision/mission, job qualifications/experience, knowledge/skill) sections. Parsed content should be verbatim as possible. No list limits. '{}'".format(user_input)
            }
        ],
        model="llama3-70b-8192"
    )

    job_description = chats.choices[0].message.content
    print(job_description)

    # load master resume
    master_resume = open("master_resume.txt", "r") # pdf, docx, txt

    # create a new 'chats' with content from master resume and job description
    chats = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": master_resume.read()
            },
            {
                "role": "system",
                "content": job_description
            }
        ],
        model="llama3-70b-8192"
    ) #TODO: figure out what the different roles mean


if __name__ == '__main__':
    main()