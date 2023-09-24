from xintegrator import Integration
import os
import openai


def get_sentiment(integration: Integration):
    if integration.mentions_tweet_table is None:
        integration.get_tweet_table(100, "mentions")

    if integration.mentions_tweet_table is not None:
        table = integration.mentions_tweet_table

        key = os.environ.get("OPENAI_API_KEY")

        posts = table["tekst"]

        for post in posts:
            prompt = (
                f"Please analyze the sentiment of the following text:{post}"
            )
                response = openai.ChatCompletion.create(
                model="gpt-4"
                prompt=prompt,
                temperature=0,
                max_tokens=128, 
                n=1,
                stop=None,
                timeout=10,
            )

        # response = openai.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=[
        #         {
        #             "role": "system",
        #             "content": "You care a sentiment classification bot,\
        #              print out if the tweet is positive, negative or neutral",
        #         }
        #     ],
        #     temperature=0.5,
        #     max_tokens=150,
        # )

        # response_message = response["choices"][0]["message"]


if __name__ == "__main__":
    mfmorten = Integration("mfmorten")

    get_sentiment(mfmorten)
