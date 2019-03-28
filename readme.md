# mrs-marc

```
Usage: mrs-marc.py [--no-highlight] <file.mrc> [--output <output.mrc>]

Options:
    -n --no-highlight   do not highlight console output
    -o --output <file>  output identified records to file
    -h --help           show this text
    -v --version        print program version
```

Inspired by Noah Geraci's talk at Code4Lib 2019, _[Programmatic approaches to bias in descriptive metadata](https://www.youtube.com/watch?v=7mdMtukvtxc&t=3965)_, here's a case study in using the [mrs](https://github.com/ngeraci/mrs) tool to analyze MARC metadata. The script looks for instances of personal names with the structure "Mrs. [male first name] [last name]," such as "Mrs. Ralph Mayer", then prints the MARC field with the name highlighted.

The scripts runs really slowly because it runs every MARC field through analysis so that potential problems can be highlight in context of the field where they occur. It'd be much quicker to concatenate the text of all fields and then parse that record-level text.

## Setup

Requires Python 3.

```sh
> pip install -r requirements.txt
> python -m spacy download en_core_web_sm # https://spacy.io/models/en
```
