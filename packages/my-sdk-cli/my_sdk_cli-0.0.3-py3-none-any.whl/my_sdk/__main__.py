#!/usr/bin/env python
import argparse
from my_sdk.module1 import Module1
from my_sdk.module2 import Module2
import sys


def main():
    parser = argparse.ArgumentParser(description="My SDK CLI")
    parser.add_argument("--action", choices=["action1", "action2"], required=True, help="Choose an action")

    args = parser.parse_args()

    if args.action == "action1":
        module1 = Module1()
        result = module1.do_something()
        print(result)
    elif args.action == "action2":
        module2 = Module2()
        result = module2.do_something_else()
        print(result)

if __name__ == "__main__":
  sys.exit(main())
