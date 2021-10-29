# Third party
import pandas as pd

# Local
from ParseIngredients import parse

if __name__ == "__main__":
    df = pd.read_json("../data/RECIPES.json")

    # Filter to just AllRecipes to reduce processing time
    ar = df[df.url.str.contains("allrecipes.com")].head(400)

    ar["ingredient_list"] = ar["ingredients"].apply(
        lambda r: list(map(lambda i: parse(i["text"]), r))
    )

    ar.to_json("../data/RECIPES_INGREDIENTS.json", orient="records")
