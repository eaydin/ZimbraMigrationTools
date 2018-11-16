import sys
import os


def generate_default_path(custom_folder):
    """Catch the path where the script lives.
    Not from where it is called. So if the script lives in /opt/zimbra/ZimbraMigrationTools/scripts and
    you call it from /opt as

    $ python zimbra/ZimbraMigrationTools/scripts/some_script.py <args>

    then the path catched will be /opt/zimbra/ZimbraMigrationTools/scripts

    The script will check if /opt/zimbra/ZimbraMigrationTools/scripts/../<custom_folder> exists, if it does, returns it.
    If the path does not exist, will return the current path, '.', which in such as a case, the path will be relative to
    the caller, not where the script lives. In our example, it will return '/opt/.' as the default path.

    If for some reason this argument was not called from a shell (i.e. called from Python interpreter) or
    the input was piped in such a way, it will still default to '.'

    Parameters
    ----------
    custom_folder : str
        Folder name to check for one upper level to the scripts home path

    Returns
    -------
    str
        Full path of the generated default path
    """

    if sys.path[0] != '':
        default_path = os.path.join(sys.path[0], '..', custom_folder)
        if not os.path.exists(default_path):
            default_path = '.'
    else:
        default_path = '.'

    return default_path