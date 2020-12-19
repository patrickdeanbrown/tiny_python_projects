#!/usr/bin/env python3
"""Purpose: say hello"""

import argparse


def get_args():
    """Returns command line arguments via argparse module"""

    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("-n",
                        "--name",
                        metavar="name",
                        default="World",
                        help="Name to greet")
    return parser.parse_args()


def main():
    """Main program executable"""

    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == "__main__":
    main()
