import subprocess
import pickle
import argparse
import os
import sys

def get_filters(user, verbose=False):
    """Function to extract filters.

    Parameters
    ----------
    user : str
        The username to extract. Ex: billgates@microsoft.com

    verbose : bool
        Should we get verbose?

    Returns
    -------
    str
        Returns the string of filters if succeeded. Yet returns a boolean False if an exception occurs.

    """
    if verbose:
        print("Getting filters for user: {0}".format(user))
    try:
        ps = subprocess.Popen(["zmprov", "ga", user, "zimbraMailSieveScript"], stdout=subprocess.PIPE)
        ps2 = subprocess.Popen(["sed", "-e", "1d"], stdin=ps.stdout, stdout=subprocess.PIPE)
        ps3 = subprocess.check_output(["sed", "s/zimbraMailSieveScript: //g"], stdin=ps2.stdout)
        if verbose:
            print("Got filters from zmprov for user: {0}".format(user))
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

    # Catch the path where the script lives
    # NOT FROM WHERE IT IS CALLED
    # so if the script lives in /opt/zimbra/ZimbraMigrationTools/scripts and you call it from /opt as
    # python zimbra/ZimbraMigrationTools/scripts/export_filters.py billgates@microsoft.com
    # then the path catched will be /opt/zimbra/ZimbraMigrationTools/scripts
    # The script wil check if /opt/zimbra/ZimbraMigrationTools/data/filters exists
    # If it does, that will be the default path
    # If it doesn't, then the script from where it is called (in our example /opt) will be the default path

    if sys.path[0] != '':
        default_path = os.path.join(sys.path[0], '../data/filters')
        if not os.path.exists(default_path):
            default_path = '.'
    else:
        default_path = '.'

    parser = argparse.ArgumentParser(prog='export_filters.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--user', '-u', help='Username to export', required=True)
    parser.add_argument('--path', '-p', help='Path to write to. Default value is ../data/filters relative to the '
                    'scripts true position, not relative to the position you call the scripts from!'
                    'If that path does not exist, then the default path is the current location of '
                                             'whoever calls the script.' , default=default_path)
    parser.add_argument('--verbose', '-v', help='Chatty guy', action='store_true')

    args = parser.parse_args()

    main()
