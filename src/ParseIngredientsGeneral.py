# Standard library
import argparse
import os

# Third party
import pandas as pd
import openai

# Consts
PROMPT = """
Given a cooking ingredient and quantity, return only the ingredient name

2 cups flour
Flour
Cinnamon ~1 tablespoon
Cinnamon
About one tsp salt
Salt
1.5-2 cups grated raw zucchini
Raw zucchini
1c walnuts (optional)
Walnuts
%s
"""

def parse(ingredient_description):
    try:
        openai.api_key = os.environ["OPENAI_API_KEY"]
        response = openai.Completion.create(
            engine="davinci",
            prompt=PROMPT % (ingredient_description),
            temperature=0,
            max_tokens=64,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        return response.choices[0].text
    except:
        return ingredient_description


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Parse ingredients using OpenAI")
    parser.add_argument("-i", "--ingredient", help="Ingredient description to parse")
    args = parser.parse_args()

    print(parse(args.ingredient))
