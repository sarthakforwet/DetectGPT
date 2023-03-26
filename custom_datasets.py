import random
import datasets
from bs4 import BeautifulSoup
import os


SEPARATOR = '<<<SEP>>>'


DATASETS = ['medquad']

def load_medquad(cache_dir):
    path = "S:/NLP/Project/MedQuadDataset"
    questions = []
    answers = []
    print("Loading MedQuad Data....")
    for dir in os.listdir(path):
        print(f"working with {dir}")
        print(dir)
        for file in os.listdir(os.path.join(path, dir)):
            with open(os.path.join(path, dir, file), "r", encoding="utf-8") as f:
                data = f.read()

            page = BeautifulSoup(data, "xml")
            qa_pairs = page.find_all("QAPair")
            for e in qa_pairs:
                ques = e.find("Question")
                ans = e.find("Answer")
                if len(ans.text)==0:
                    continue

                questions.append(ques.text)
                answers.append(ans.text)
    
    data = [f"Question: {q} Answer:{SEPARATOR}{a}" for q, a in zip(questions, answers)]

    return data

def process_prompt(prompt):
    return prompt.replace('[ WP ]', '').replace('[ OT ]', '')

def process_spaces(story):
    return story.replace(
        ' ,', ',').replace(
        ' .', '.').replace(
        ' ?', '?').replace(
        ' !', '!').replace(
        ' ;', ';').replace(
        ' \'', '\'').replace(
        ' ’ ', '\'').replace(
        ' :', ':').replace(
        '<newline>', '\n').replace(
        '`` ', '"').replace(
        ' \'\'', '"').replace(
        '\'\'', '"').replace(
        '.. ', '... ').replace(
        ' )', ')').replace(
        '( ', '(').replace(
        ' n\'t', 'n\'t').replace(
        ' i ', ' I ').replace(
        ' i\'', ' I\'').replace(
        '\\\'', '\'').replace(
        '\n ', '\n').strip()

def load(name, cache_dir, **kwargs):
    if name in DATASETS:
        load_fn = globals()[f'load_{name}']
        return load_fn(cache_dir=cache_dir, **kwargs)
    else:
        raise ValueError(f'Unknown dataset {name}')