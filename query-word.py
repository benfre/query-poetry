# query-poetry: query all tang and song poetry / ci using regex
# Copyright (C) 2018  benfre
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


import pickle
import regex
import argparse
import pyopencc_pure

tang_poetrys = pickle.load( open( "tang_poetrys.p", 'rb') )

def query_tang_poetry(word):
    para_count = 0
    query_string = word
    reg_obj = regex.compile(query_string)
    for peotry in tang_poetrys:
        # print(peotry['paragraphs'][0])
        if len(peotry['paragraphs'])>0:
            for para in peotry['paragraphs']:
                ma = reg_obj.search(para)
                if ma is not None:
                    if 'title' in peotry:
                        print(para +': ' + peotry['title']+'--'+peotry['author'] )
                    elif 'rhythmic' in peotry:
                        print(para +': ' + peotry['rhythmic']+'--'+peotry['author'] )
                    para_count = para_count +1
    print(str(para_count) + ' paragraphs found.' )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='query poetry from word')
    parser.add_argument('word', help='word for query')
    args = parser.parse_args()
    query_tang_poetry(args.word)
    config = pyopencc_pure.load_config('s2t.json')
    word_t = pyopencc_pure.convert(config, args.word)
    if word_t != args.word:
        query_tang_poetry(word_t)