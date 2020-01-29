import os
import requests
import pickle
from flask import Flask, render_template, request
import pyopencc_pure
import regex

tang_poetrys = pickle.load( open( "tang_poetrys.p", 'rb') )
s2t_config = pyopencc_pure.load_config('s2t.json')

def query_poetry(query_string='^绿树', fisrt_n = 40, start = 0):
    results = []
    para_count = 0
    more = False
    reg_obj = regex.compile(query_string)
    poetrys_size = len(tang_poetrys)
    end = poetrys_size

    if poetrys_size > start:
        for i in range(start, poetrys_size):
            peotry = tang_poetrys[i]
            content = None
            if 'paragraphs' in peotry.keys() and len(peotry['paragraphs'])>0:
                content = peotry['paragraphs']
            if 'content' in peotry.keys() and len(peotry['content'])>0:
                content = peotry['content']
            if content:
                for para in content:
                    ma = reg_obj.search(para)
                    if 'author' in peotry.keys():
                        author = peotry['author']
                    elif "section" in peotry.keys():
                        author = peotry['section']
                    else:
                        author = "unkown"
                    if ma is not None:
                        if 'title' in peotry:
                            results.append([peotry['title'], author, para])
                        elif 'rhythmic' in peotry:
                            results.append([peotry['rhythmic'], author, para])
                        elif 'chapter' in peotry:
                            results.append([peotry['chapter'], '孔丘', para])
                        para_count = para_count +1
                if para_count>=fisrt_n:
                    more = True
                    end = i + 1
                    break
    return para_count, results, more, end

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/', methods=['GET', 'POST'])
def main_query():
    errors = []
    results = []
    word = None
    end = 0
    more = False
    if request.method == "POST":
        word = request.form['regex']
        para_count, results, more, end = query_poetry(word, 40, start = 0)
        if para_count < 40:
            word_t = pyopencc_pure.convert(s2t_config, word)
            if word_t != word: 
                para_count_t, results_t, more, end = query_poetry(word_t, 40-para_count, start = 0)
                results.extend(results_t)
    if request.method == "GET":
        word = request.args.get('regex')
        if word is not None:
            start = int(request.args.get('start', default = 0))
            para_count, results, more, end = query_poetry(word, 40, start = start)

    return render_template('index.html', query_word=word,errors=errors, results=results, more =more, stop =end)


if __name__ == '__main__':
    app.run()
