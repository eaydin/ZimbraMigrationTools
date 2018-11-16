import subprocess
import pickle
import argparse
import os


def get_filters(user, verbose=False):
    try:
        ps = subprocess.Popen(["zmprov", "ga", user, "zimbraMailSieveScript"], stdout=subprocess.PIPE)
        ps2 = subprocess.Popen(["sed", "-e", "1d"], stdin=ps.stdout, stdout=subprocess.PIPE)
        ps3 = subprocess.check_output(["sed", "s/zimbraMailSieveScript: //g"], stdin=ps2.stdout)
        return ps3
    except Exception as err:
        print("Error while getting filters: {0}".format(str(err)))
        return False


def save_file(filters, user, path, verbose=False):
    file_path = os.path.join(path, user + ".pickle")
    try:
        with open(file_path, 'wb') as fp:
            pickle.dump(filters, fp, protocol=pickle.HIGHEST_PROTOCOL)
        return True
    except Exception as err:
        print("Error while dumping pickle: {0}".format(str(err)))
        return False


def main():
    filters = get_filters(args.user, args.verbose)
    if filters:
        save_file(filters, args.user, args.path, args.verbose)
        print("Filter save success for user {user} to {path}".format(path=args.path, user=args.user))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='export_filters.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--user', '-u', help='Username to export', required=True)
    parser.add_argument('--path', '-p', help='Path to write to', default='.')
    parser.add_argument('--verbose', '-v', help='Chatty guy', action='store_true')

    args = parser.parse_args()

    main()
