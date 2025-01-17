import argparse
import config

from add_entry import add_entry
from generate import generate_html

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="nanopage")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser(
        "add_entry", help="Add / Update entry data to page from demozoo id"
    )
    parser_add.add_argument(
        "category",
        type=str,
        help="Category",
        choices=[c["id"] for c in config.CATEGORIES],
    )
    parser_add.add_argument(
        "flavor", type=str, help="Flavor", choices=[c["id"] for c in config.FLAVORS]
    )
    parser_add.add_argument("demozoo_id", type=str, help="demozoo_id")

    parser_add = subparsers.add_parser("generate", help="Generate HTML")

    args = parser.parse_args()
    if args.command == "add_entry":
        add_entry(args.category, args.flavor, args.demozoo_id)
    elif args.command == "generate":
        generate_html()
