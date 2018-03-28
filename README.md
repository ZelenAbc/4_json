# Prettify JSON

Script restructures JSON string with key sorting and 4-space indentation.

# Quickstart

```bash
$ cat test.json
```
```json
["foo", {"bar":["baz", null, 1.0, 2]}]
```
Example of script launch on Linux, Python 3.5:
```bash
$ python pprint_json.py test.json
```
```json
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
