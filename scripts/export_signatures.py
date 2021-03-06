from subprocess import check_output
import argparse
from VTZM import helpers


def get_signatures(user):
    """Get signatures of user


    Parameters
    ----------
    user : str
        The username to export. Ex: billgates@microsoft.com

    Returns
    -------
    dictionary
        Returns a dictionary with two dictionaries nested.
        { 'HTML': { signature_name1: signature1,
                    signature_name2: signature2
                    },
          'PLAIN': { signature_name1: signature1,
                     signature_name2: signature2
                   }
        }

    Raises
    ------
    Exception: Raises a generic exception when the zmprov command fails. When the exception occurs,
        will return False.
    """

    try:
        sigs = check_output(["zmprov", "gsig", user])
    except Exception as err:
        print("Error while using zmprov. Probably you're not zimbra user? Error message: {0}".format(str(err)))
        return False

    sigs_lines = sigs.split('\n')

    signatures_html = {}
    signatures_plain = {}

    new_sig = True
    html = False
    temp_sig = ''

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

    all_signatures = {'HTML': signatures_html, 'PLAIN': signatures_plain}

    return all_signatures


def main():
    all_signatures = get_signatures(args.user)
    if all_signatures:
        try:
            helpers.save_pickle(all_signatures, args.user, args.path, args.verbose)
            print("Signatures file successfully saved for user {0} to pickle file {1}".format(args.user, args.path))
        except IOError as err:
            print("IOError while saving signatures file: {0}".format(str(err)))
        except Exception as err:
            print("Unknown exception while saving signatures file: {0}".format(str(err)))


if __name__ == '__main__':

    default_path = helpers.generate_default_path('data/signatures')

    parser = argparse.ArgumentParser(prog='export_signatures.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--user', '-u', help='Username to export', required=True)
    parser.add_argument('--path', '-p', help='Path to write to', default=default_path)
    parser.add_argument('--verbose', '-v', help='Chatty guy', action='store_true')

    args = parser.parse_args()

    main()