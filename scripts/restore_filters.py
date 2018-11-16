import subprocess
import pickle
import argparse
import os


def read_filters(filepath, verbose=False):
    with open(filepath, 'rb') as fp:
        filters = pickle.load(fp)
    if verbose:
        print("Filters read:")
        print(filters)

    return filters


def restore_filters(filters, user, verbose=False):
    ps = subprocess.check_output(["zmprov", "ma", user, "zimbraMailSieveScript", filters])

    if verbose:
        print("Filters restored.")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='restore_filters.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--user', '-u', help='Username to restore', required=True)
    parser.add_argument('--file', '-f', help='File to restore from', required=True)
    parser.add_argument('--verbose', '-v', help='Chatty guy', action='store_true')

    args = parser.parse_args()

    filters = read_filters(args.file, args.verbose)
    try:
        restore_filters(filters, args.user, args.verbose)
    except Exception as err:
        print("Error while restoring filters: {0}".format(str(err)))
        raise SystemExit

    if not args.verbose:
        print("Filters restored for user: {0} from file: {1}".format(args.user, args.file))