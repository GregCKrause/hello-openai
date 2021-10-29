# Standard library
import argparse
import os

# Third party
import openai

# Consts
FINE_TUNED_MODEL = "curie:ft-user-ch5mio4xqj0cnvlo2zmn7ir6-2021-10-29-04-31-36"

def parse(ingredient_description):
    try:
        openai.api_key = os.environ["OPENAI_API_KEY"]
        response = openai.Completion.create(
            model=FINE_TUNED_MODEL,
            prompt=ingredient_description,
            top_p=1,
            stop=["\n"]
        )
        return response.choices[0].text.split("-> ")[1]
    except:
        return ingredient_description


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Parse ingredients using OpenAI")
    parser.add_argument("-i", "--ingredient", help="Ingredient description to parse")
    args = parser.parse_args()

    print(parse(args.ingredient))
