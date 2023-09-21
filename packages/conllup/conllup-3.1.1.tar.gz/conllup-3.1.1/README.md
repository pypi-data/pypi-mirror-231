# CONLLUP Python (conllup-py)

Convert .conlly dependency graph to/from JSON format (supported by arboratorgrew)\*

## Usefull links

- [conllup-js](https://github.com/kirianguiller/conllup-js) : Javascript version of this library
- [ArboratorGrew](https://arboratorgrew.elizia.net/#/) : An online collaborative annotation tools, that use the same JSON format for the dependency trees

## sentenceJson interface

```json
{
    "metaJson": {
        "sent_id": "corpusA_sent1",
        "text": "I eat an apple",
    },
    "treeJson": {
        "nodesJson": {
            "1": {
                "ID": "1",
                "FORM": "I",
                "LEMMA": "_",
                "UPOS": "_",
                "XPOS": "_",
                "FEATS": {},
                "HEAD": 4,
                "DEPREL": "_",
                "DEPS": {},
                "MISC": {},
            },
            "2": {
                "ID": "2",
                "FORM": "eat",
                "LEMMA": "_",
                "UPOS": "_",
                "XPOS": "_",
                "FEATS": {},
                "HEAD": 0,
                "DEPREL": "_",
                "DEPS": {},
                "MISC": {},
            },
            "3": {
                "ID": "3",
                "FORM": "an",
                "LEMMA": "a",
                "UPOS": "DET",
                "XPOS": "_",
                "FEATS": {},
                "HEAD": 4,
                "DEPREL": "_",
                "DEPS": {},
                "MISC": {},
            },
            "4": {
                "ID": "4",
                "FORM": "apple",
                "LEMMA": "apple",
                "UPOS": "NOUN",
                "XPOS": "_",
                "FEATS": {},
                "HEAD": 2,
                "DEPREL": "_",
                "DEPS": {},
                "MISC": {},
            }
        },
        "groupsJson": {}
    }
}

```

## Deploy new release

Require to have `pip install twine setuptools build` before doing any build 0) check all tests are passing `python3 -m pytest`

1. change versions in pyproject.toml
2. build new package `python3 -m build`
3. upload to pypi `python3 -m twine upload --repository pypi dist/*`
4. Optional : if you want to try the testpypi version of the package `pip install --index-url https://test.pypi.org/simple/ --no-deps conllup`

## Changelog
### 3.1.1
- accept empty conll column (it will automatically convert to a "_" if it's for lines other than ID, FORM and LEMMA)
### 3.1.0 (big jump in version to be coherent with [conllup-js](https://github.com/kirianguiller/conllup-js), the Javascript implementation)
- add support to Enhanced UD specifications ([link here](https://universaldependencies.org/u/overview/enhanced-syntax.html#ellipsis))
### 0.4.9
- indicate conll sent_id for raised errors
### 0.4.8
- raise errors for empty tokens
### 0.4.7
- modify _featuresConllToJson() so it order features in the order [specified by UD](https://universaldependencies.org/format.html) (thank you @bguil): 
> In sorting, uppercase letters are considered identical to their lowercase counterparts.
### 0.4.6
- add order in place in replaceArrayOfTokens() outputted treeJson (thanks to the new _sortTokensJson())
### 0.4.4:
- minor fix
### 0.4.3:
- optimized for speed (reduced by half the time of loading and serializing conllus)
### 0.4.2:
- add optional parameter `keepEmptyTrees` in `readConlluFile()`. If True, Empty trees in conll will be discarded (some malformed conll trees could have some empty tokens)
### 0.4.0:
- add `writeConlluFile()` and `readConlluFile()` to handle file reading and writing
### 0.3.1: 
- sorting of feature json when converted to conll string
### 0.3.0: add `replaceArrayOfTokens()` in `processing.py`
### 0.2.1
- fixed : `_metaConllLinesToJson() `when wrong formatting of meta line when missing part after equal sign (`# meta without right part = `)
### 0.2.0
- added `constructTextFromTreeJson` method (in `processing.py` file)
- added `emptySentenceConllu` method (in `processing.py` file)
- added `changeMetaFieldInSentenceConllu` method (in `processing.py` file)
- minor: some more typing annotations
### 0.1.0
First release, with the core methods : `sentenceConllToJson` and `sentenceJsonToConll`