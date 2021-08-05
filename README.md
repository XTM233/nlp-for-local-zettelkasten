# NLP for local zettelkasten

A collection of scripts that might be useful for followers of zettelkasten who use local plain text files to manage their notes.

## Features

Currently we have the following functionalities:

1. (Inspired by [Flomo](flomoapp.com)) suggest a list of high-frequency words (splited by jieba) in your note directory and allow the user to browse notes containing these "keywords" for further processing, such as tagging or making connections between these notes
2. (Inspired by [Obsidian](obsidian.md)) print a randomly selected note from your note directory

## Installation

1. Download the python scripts and move them to your note directory.
2. Ensure you have installed python. You may get it from [Microsoft Store](https://www.microsoft.com/store/productId/9MSSZTT1N39L). The scripts are tested with Python 3.8
3. For word-frequency.py, the NLP package jieba is required. Get it through `$pip install jieba`.

## Usage

1. Open terminal and navigate to your note directory.
2. Run the script through `$python random-walk.py` or `$python word-frequency.py`
3. Follow the command prompt and enjoy.

### User case

It is found that these two scripts are particularly useful when you have:

1. massive notes migrated from other software/platform, losing metadata
2. a large amount of notes related to similar topics
3. some potentially duplicate notes
4. obsolete notes which should be archived
5. useful notes which you "forget" you've written

## Future work

Future improvement will be mainly focused on these aspects:

- make it a command line application
- customization in terms of parameters and stopwords
- improvemen on efficiency of indexing
- improvement on accuracy and precision of model, for example, to include aliases and synonyms.

Welcome to raise issues or contribute to these project! 

## Thanks

A big thanks to [jieba](https://pypi.org/project/jieba/), zettelkasten.de, [Obsidian](obsidian.md) and [Flomo](flomoapp.com)).
