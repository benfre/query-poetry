import json
import os
import pickle

# tang_author_file = "..\\chinese-poetry\\json\\authors.tang.json"

# with open(tang_author_file, 'r', encoding='utf-8') as f:
#     tang_author = json.load(f, encoding='utf-8')

tang_poetrys = list()
poetry_directory = "..\\chinese-poetry\\json"
for filename in os.listdir(poetry_directory):
    if "poet.song." in filename:
        fi = open(poetry_directory+"\\"+filename, 'r', encoding='utf-8')
        poetryi = json.load(fi, encoding='utf-8')
        tang_poetrys = tang_poetrys + poetryi
    if "poet.tang." in filename:
        fi = open(poetry_directory+"\\"+filename, 'r', encoding='utf-8')
        poetryi = json.load(fi, encoding='utf-8')
        tang_poetrys = tang_poetrys + poetryi
ci_directory = "..\\chinese-poetry\\ci"
for filename in os.listdir(ci_directory):
    if "ci.song." in filename:
        fi = open(ci_directory+"\\"+filename, 'r', encoding='utf-8')
        poetryi = json.load(fi, encoding='utf-8')
        tang_poetrys = tang_poetrys + poetryi      
print(len(tang_poetrys))

pickle.dump( tang_poetrys, open( "tang_poetrys.p", "wb" ) )

# print(tang_poetrys[123456]['title']+'--'+tang_poetrys[123456]['author'])
# print(tang_poetrys[123456]['paragraphs'])

