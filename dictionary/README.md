# Jbovlaste

This Python module allows to search for words in the official Jbovlaste ("dictionary" in Lojban).

Words include a type, definition, and optional glosswords in the target language of the dictionary.

## Usage

Module can either be imported in other python files

```
from dictionary.jbovlaste import Jbovlaste

dict_instance = Jbovlaste()

print(dict_instance.get_word('blanu'))
# OR
print(dict_instance.get_word_pretty('blanu'))

```

or run as-is

`python dictionary/jbovlaste.py <word to search>`

(will run the function `get_word_pretty()` by default)

## TODO LIST

- [ ] Error Handling

## Citation / External sources

File `jbovlaste-en.xml` is a XML export of the Lojban dictionary found [here](https://jbovlaste.lojban.org/).

Github repository of the project: https://github.com/lojban/jbovlaste
