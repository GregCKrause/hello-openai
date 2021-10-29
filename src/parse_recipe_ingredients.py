# Third party
import pandas as pd

# Local
from ParseIngredientsBase import parse

# Consts
DATA_DIR = "../data"

# After downloading Recipe1M RECIPES.json file to sibling data directory 
if __name__ == "__main__":
    
    # Filter to first 5 to reduce processing time
    df = pd.read_json(DATA_DIR + "/RECIPES.json").head(5)

    # Use OpenAI to parse each ingredient description
    df["ingredient_list"] = df["ingredients"].apply(
        lambda r: list(map(lambda i: parse(i["text"]), r))
    )

    # Write new dataframe to output JSON file
    df.to_json(DATA_DIR + "/RECIPES_INGREDIENTS.json", orient="records")
