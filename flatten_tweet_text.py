import argparse
import json
from normalize_text import normalize_text

def parse_arg():
    args = argparse.ArgumentParser(description="flatten tweet texts.")
    args.add_argument("FILE", type=str, nargs=1, help="specify file.")
    return args.parse_args()


if __name__ == "__main__":
    args = parse_arg()
    tweets = []
    with open(args.FILE[0], "r") as f:
        tweets = json.load(f)
    print("\n".join([normalize_text(t["text"]) for t in tweets]))