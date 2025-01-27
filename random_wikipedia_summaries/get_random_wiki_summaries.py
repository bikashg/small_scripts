# Based on https://pypi.org/project/wikipedia/
import wikipedia
from tqdm import tqdm
import random
import json

def get_intro_text(article_name):
    try:
        return {"article_title": article_name, "intro_text": wikipedia.page(article_name, auto_suggest=False, ).summary.strip()}
    except wikipedia.DisambiguationError as e:
        # print(f'e.options = {e.options}')
        s = random.choice(e.options)
        return get_intro_text(s)

def get_random_articles_summaries(count_articles, min_characters):
    print(f'Retrieving names for random {count_articles} wiki articles ... ')
    article_names = [wikipedia.random(pages=1) for i in range(count_articles)]
    print(f'done')
    print(f'Proceed to summary text retrieval ... ')
    outfile = open('random_wikipedia_summaries.txt', 'w')
    for article_summary_text in tqdm(article_names):
        result_dict = get_intro_text(article_summary_text)
        result_text = result_dict['intro_text']
        if len(result_text)>min_characters:
            json.dump(result_dict, outfile, indent=2)
            outfile.write('\n')
    outfile.close()

get_random_articles_summaries(count_articles=20, min_characters=100)
