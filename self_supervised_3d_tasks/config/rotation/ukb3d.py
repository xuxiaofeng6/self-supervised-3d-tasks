from pathlib import Path

import json
from self_supervised_3d_tasks.train_and_eval import train_and_eval


def main():

    with open(Path(__file__).parent / "ukb3d.json", 'r') as f:
        args = json.load(f)
    train_and_eval(args)


if __name__ == "__main__":
    main()