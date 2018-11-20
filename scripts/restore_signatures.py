from subprocess import check_output
import argparse
from VTZM import helpers
import sys


def main():

    errors = False
    master_signatures = helpers.read_pickle(args.file)
    if master_signatures:

        signatures_html = master_signatures['HTML']
        signatures_plain = master_signatures['PLAIN']

        for signame in signatures_html:

            try:
                create_sigs = check_output(["zmprov", "csig", args.user, signame, "zimbraPrefMailSignatureHTML", signatures_html[signame]])
            except Exception as err:
                print("Error while running zmprov csig command for HTML Signature: {0}".format(str(err)))
                errors = True
            else:
                if args.verbose:
                    print(create_sigs)

        for signame in signatures_plain:

            try:
                create_sigs = check_output(["zmprov", "csig", args.user, signame, "zimbraPrefMailSignature", signatures_plain[signame]])
            except Exception as err:
                print("Error while running zmprov csig command for Plain Text Signature: {0}".format(str(err)))
                errors = True
            else:
                if args.verbose:
                    print(create_sigs)

    else:
        print("Error while reading signatures.")
        sys.exit(1)

    return errors


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='restore_signatures.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--user', '-u', help='Username to restore', required=True)
    parser.add_argument('--file', '-f', help='Path to the pickle file', required=True)
    parser.add_argument('--verbose', '-v', help='Chatty guy', action='store_true')

    args = parser.parse_args()

    errors = main()

    if errors:
        print("Signature restore for user {0} completed with errors!".format(args.user))
        sys.exit(1)
    else:
        print("Signature restore completed for user: {0} pickle: {1}".format(args.user, args.file))
        sys.exit(0)