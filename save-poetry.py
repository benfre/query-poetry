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


