from subprocess import check_output
import pickle
import argparse


def main():

    with open(args.file, 'rb') as fp:
        master_signatures = pickle.load(fp)

    signatures_html = master_signatures['HTML']
    signatures_plain = master_signatures['PLAIN']

    for signame in signatures_html:

        create_sigs = check_output(["zmprov", "csig", args.user, signame, "zimbraPrefMailSignatureHTML", signatures_html[signame]])

        if args.verbose:
            print(create_sigs)

    for signame in signatures_plain:

        create_sigs = check_output(["zmprov", "csig", args.user, signame, "zimbraPrefMailSignature", signatures_plain[signame]])

        if args.verbose:
            print(create_sigs)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='restore_signatures.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--user', '-u', help='Username to restore', required=True)
    parser.add_argument('--file', '-f', help='Path to the pickle file', required=True)
    parser.add_argument('--verbose', '-v', help='Chatty guy', action='store_true')

    args = parser.parse_args()

    main()

    print("Completed for user: {0} pickle: {1}".format(args.user, args.file))