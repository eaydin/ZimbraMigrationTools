from subprocess import check_output
import sys
import pickle
import argparse
import os
from VTZM import helpers


def main():
    user = args.user

    try:
        sigs = check_output(["zmprov", "gsig", user])
    except Exception as err:
        print("Error while using zmprov. Probably you're not zimbra user? Error message: {0}".format(str(err)))
        raise SystemExit

    sigs_lines = sigs.split('\n')

    signatures_html = {}
    signatures_plain = {}

    new_sig = True
    html = False

    for line in sigs_lines:
        if new_sig:
            if line.startswith("zimbraPrefMailSignature"):
                new_sig = False
                if "HTML" in line[:28]:
                    html = True
                    temp_sig = line[28:].strip()
                else:
                    html = False
                    temp_sig = line[24:].strip()
                continue
        elif line.startswith("zimbraSignatureId:"):
            continue
        elif line.startswith("zimbraSignatureName:"):
            temp_name = line[20:].strip()
            new_sig = True
            if html:
                signatures_html[temp_name] = temp_sig
            else:
                signatures_plain[temp_name] = temp_sig
        elif line.startswith("#"):
            continue
        else:
            temp_sig += line.strip()

    if args.verbose:
        print("HTML Signatures Exported: ")
        print(signatures_html)
        print("PLAIN Text Signatures Exported: ")
        print(signatures_plain)

    pickle_file_path = os.path.join(args.path, user + ".pickle")

    master_pickle = {'HTML': signatures_html, 'PLAIN': signatures_plain}

    with open(pickle_file_path, 'wb') as fp:
        pickle.dump(master_pickle, fp, protocol=pickle.HIGHEST_PROTOCOL)

    return pickle_file_path


if __name__ == '__main__':

    default_path = helpers.generate_default_path('../data/signatures')

    parser = argparse.ArgumentParser(prog='export_signatures.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--user', '-u', help='Username to export', required=True)
    parser.add_argument('--path', '-p', help='Path to write to', default=default_path)
    parser.add_argument('--verbose', '-v', help='Chatty guy', action='store_true')

    args = parser.parse_args()

    saved = main()

    print("Completed for user: {0} path: {1}".format(args.user, saved))