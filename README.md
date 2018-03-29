# Prettify JSON

Script restructures JSON string with key sorting and 4-space indentation.

# Quickstart

```bash
$ cat test.json
```
```json
["foo", {"bar":["baz", null, 1.0, 2]}]
```
Usage :

```bash
$ int_json.py -h
usage: pprint_json.py [-h] [-f DATA_FILE]

Convert JSON data to human-readable form

optional arguments:
  -h, --help            show this help message and exit
  -f DATA_FILE, --data_file DATA_FILE
                        path to file with JSON string, default: ./test.json
```
Example of script launch on Linux, Python 3.5:


```json
$ python pprint_json.py 
[
    "foo",
    {
        "bar": [
            "baz",
            null,
            1.0,
            2
        ]
    }
]


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
