import os
import requests
import operator
import re
import pickle
from flask import Flask, render_template, request
from collections import Counter
from bs4 import BeautifulSoup
import pyopencc_pure
import regex

tang_poetrys = pickle.load( open( "tang_poetrys.p", 'rb') )
s2t_config = pyopencc_pure.load_config('s2t.json')

def query_poetry(query_string='^绿树', fisrt_n = 40):
    results = []
    para_count = 0
    reg_obj = regex.compile(query_string)
    for peotry in tang_poetrys:
        content = None
        if 'paragraphs' in peotry.keys() and len(peotry['paragraphs'])>0:
            content = peotry['paragraphs']
        if 'content' in peotry.keys() and len(peotry['content'])>0:
            content = peotry['content']
        if content:
            for para in content:
                ma = reg_obj.search(para)
                if ma is not None:
                    if 'title' in peotry:
                        results.append([peotry['title'], peotry['author'], para])
                    elif 'rhythmic' in peotry:
                        results.append([peotry['rhythmic'], peotry['author'], para])
                    para_count = para_count +1
            if para_count>fisrt_n:
                break
    return para_count, results

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/', methods=['GET', 'POST'])
def hello():
    errors = []
    results = []
    word = None
    if request.method == "POST":
        word = request.form['regex']
        para_count, results = query_poetry(word, 40)
        if para_count < 40:
            word_t = pyopencc_pure.convert(s2t_config, word)
            para_count_t, results_t = query_poetry(word_t, 40-para_count)
            results.extend(results_t)

    return render_template('index.html', query_word=word,errors=errors, results=results)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
