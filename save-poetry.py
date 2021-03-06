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
        fi.close()
        tang_poetrys.extend(poetryi)
    if "poet.tang." in filename:
        fi = open(poetry_directory+"\\"+filename, 'r', encoding='utf-8')
        poetryi = json.load(fi, encoding='utf-8')
        fi.close()
        tang_poetrys.extend(poetryi)
ci_directory = "..\\chinese-poetry\\ci"
for filename in os.listdir(ci_directory):
    if "ci.song." in filename:
        fi = open(ci_directory+"\\"+filename, 'r', encoding='utf-8')
        poetryi = json.load(fi, encoding='utf-8')
        fi.close()
        tang_poetrys.extend(poetryi)
lunyu_directory = "..\\chinese-poetry\\lunyu"
for filename in os.listdir(lunyu_directory):
    if ".json" in filename:
        fi = open(lunyu_directory+"\\"+filename, 'r', encoding='utf-8')
        poetryi = json.load(fi, encoding='utf-8')
        fi.close()
        tang_poetrys.extend(poetryi)  
shijing_directory = "..\\chinese-poetry\\shijing"
for filename in os.listdir(shijing_directory):
    if ".json" in filename:
        fi = open(shijing_directory+"\\"+filename, 'r', encoding='utf-8')
        poetryi = json.load(fi, encoding='utf-8')
        fi.close()
        tang_poetrys.extend(poetryi)   

wudai_directory = "..\\chinese-poetry\\wudai\\huajianji\\"
for filename in os.listdir(wudai_directory):
    if ".json" in filename:
        fi = open(wudai_directory+"\\"+filename, 'r', encoding='utf-8')
        poetryi = json.load(fi, encoding='utf-8')
        fi.close()
        tang_poetrys.extend(poetryi)

nantang_filename ="..\\chinese-poetry\\wudai\\nantang\\poetrys.json"
fi = open(nantang_filename, 'r', encoding='utf-8')
poetryi = json.load(fi, encoding='utf-8')
fi.close()
tang_poetrys.extend(poetryi)

print(len(tang_poetrys))

pickle.dump( tang_poetrys, open( "tang_poetrys.p", "wb" ) )
