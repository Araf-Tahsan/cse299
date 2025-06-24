import argparse
from runner import run_pipeline

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', required=True)
parser.add_argument('--model', required=True)
parser.add_argument('--otherOptions', required=False, default=None)

args = parser.parse_args()

if __name__ == "main":
    run_pipeline(args.model, args.dataset, args.otherOptions)
