# Jbovlaste

This Python module allows the user to search for words in (an export of) the official Jbovlaste ("dictionary" in Lojban). Words include a type, definition, and optional glosswords in the target language of the dictionary.

## Usage

Module can either be imported and used in other python files

```
from dictionary import Jbovlaste

dict_instance = Jbovlaste()

print(dict_instance.get_word_struct('blanu'))
# OR
print(dict_instance.get_word_pretty('blanu'))
```

or run as-is

`python3 dictionary/jbovlaste.py "<word to search>"`

(this will run the `get_word_pretty()` function by default, double quotes are recommended as Lojban has many words with single quotes in them)

## Citation / External sources

File `jbovlaste-en.xml` is a XML export of the Lojban dictionary found [here](https://jbovlaste.lojban.org/).

Github repository of the project: https://github.com/lojban/jbovlaste