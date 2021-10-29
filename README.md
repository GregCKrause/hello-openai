# Hello, OpenAI!

## Getting started
To use OpenAI, you will need to create an OpenAI account. OpenAI currently maintains an application [waitlist](https://share.hsforms.com/1Lfc7WtPLRk2ppXhPjcYY-A4sk30), and it may take a few weeks to access.
Once access is granted, it is recommended to check out the [playground](https://beta.openai.com/playground).

## Playground examples:
### [Tweet sentiment (general OpenAI)](https://beta.openai.com/playground/p/default-tweet-classifier)
```txt
This is a tweet sentiment classifier


Tweet: "I loved the new Batman movie!"
Sentiment: Positive
###
Tweet: "I hate it when my phone battery dies."
Sentiment: Negative
###
Tweet: "My day has been 👍"
Sentiment: Positive
###
Tweet: "This is the link to the article"
Sentiment: Neutral
###
Tweet: "This new music video blew my mind"
Sentiment:
```

### [Intelligent Parser](https://beta.openai.com/playground/p/vZSmOrdzgVJ2Bh7SbEafjlDa?model=davinci)
```txt
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

1 cup of butter (softened)
```

### [Function explainer (OpenAI Codex - requires additional Codex access)](https://beta.openai.com/playground/p/7AaExsHVqjQ2TgS6NHvHoSWs?model=davinci-codex)
```txt
def fib(n):
    if n in [0, 1]:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Explain the function
```

## Local examples:
```sh
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Export OpenAI credentials
export OPENAI_API_KEY=<your-api-key>

python ./src/ParseIngredients.py -i "butter (room temp)"
# Butter
```

## Attribution
Special thanks to the following projects:
- [OpenAI](https://openai.com).
- [Recipe1M](http://pic2recipe.csail.mit.edu)
