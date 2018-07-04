# query all tang and song peotry / ci

## requirement

'regex' for better unicode support (not the buildin 're' package), 

'pyopencc_pure' for chinese convert (https://github.com/benfre/OpenCC/tree/benfre_master/python/pyopencc_pure)

Other opencc wrapper could replace pyopencc_pure, the cnverting code need be changed.

## convert json to pickle for fast read

The following command takes about 10 seconds:

`python .\save-poetry.py`

## query using regular expression

query string is in simplified chinese, automatically convert to traditional chinese for search in poetries.

Examples:

- For a word: `python .\query-word.py 乱花` > 26 + 101 results
- For beginning of paragraph: `python .\query-word.py ^乱花` ==> 8 + 20 results
- For 7 word in a paragraph: `python .\query-word.py "[眼乱人日花欲迷渐西]{7}"` ==> 1 results
```
0 paragraphs found.
亂花漸欲迷人眼，淺草纔能沒馬蹄。: 錢唐湖春行--白居易
1 paragraphs found.
```
