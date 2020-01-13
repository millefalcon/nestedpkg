import json
import pathlib


def another() -> str:
    datafile = pathlib.Path(__file__).parent / "data.json"
    with open(datafile) as f:
        data = json.load(f)
        data = data["content"]
    return data
