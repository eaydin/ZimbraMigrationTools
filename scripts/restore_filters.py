import subprocess
import argparse
from VTZM import helpers


def main():
    filters = helpers.read_pickle(args.file)
    if filters:

        if args.verbose:
            print("Filters read: ")
            print(filters)

        try:
            ps = subprocess.check_output(["zmprov", "ma", args.user, "zimbraMailSieveScript", filters])
        except Exception as err:
            print("Error while running zmprov command: {0}".format(str(err)))
        else:
            print("Filters for {0} successfully imported.".format(args.user))

    else:
        print("Error while reading filters.")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='restore_filters.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--user', '-u', help='Username to restore', required=True)
    parser.add_argument('--file', '-f', help='File to restore from', required=True)
    parser.add_argument('--verbose', '-v', help='Chatty guy', action='store_true')

    args = parser.parse_args()

    main()