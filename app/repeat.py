from .db_api import get_crawl_by_id

from .utils import run_proc
import argparse

from . import db


def parse_args():
    parser = argparse.ArgumentParser(description="Nutch Repeater")

    parser.add_argument("--crawl_id", type=int, required=True,
                        help="ID of crawl instance")
    parser.add_argument("--seed_dir", type=str, required=True,
                        help="Seed directory")
    parser.add_argument("--crawl_dir", type=str, required=True,
                        help="Crawl directory")

    return parser.parse_args()

def keep_going(crawl):
	db.session.refresh(crawl)
	return crawl.status is not "stop requested"

if __name__ == "__main__":

    args = parse_args()
	crawl = get_crawl_by_id(args.crawl_id)

    while keep_going(crawl):
	    run_proc("crawl {} {} 1".format(args.seed_dir, args.crawl_dir))
