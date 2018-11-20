import sys
import os
import pickle


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


def save_pickle(data, filename, path, verbose=False):
    """Saves a pickle file.

    Parameters
    ----------
    data: object
        Whatever Python object we pass that want it to be written as a Pickle file.

    filename: str
        Filename to write. Do not include the .pickle extension.

    path: str
        Path to write the file to. If this path does not exist, will raise an IO Error.

    verbose: bool
        Self explanatory.

    Returns
    -------
    bool
        True if succeeds, False or Exception if fails.

    Raises
    ------
    IOError
        If filepath does not exist.

    Exception
        A generic exception when opening the file in write mode, or dump ping fails.

    """

    if not os.path.exists(path):
        raise IOError("Pickle not dumped since path does not exist: {0}".format(path))

    file_path = os.path.join(path, filename + ".pickle")

    try:
        with open(file_path, 'wb') as fp:
            pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
        if verbose:
            print("Successfully dumped to {0}".format(file_path))
        return True
    except Exception as err:
        raise Exception("Error while dumping pickle: {0}".format(str(err)))


def read_pickle(filepath):
    """Read pickle file

    Parameters
    ----------
    filepath: str
        Filepath of pickle file to read.

    Returns
    -------
    Object: Returns the Python object in the pickle file. If an error occurs, returns False

    Raises
    ------
    FileNotFound: If the file does not exist.
    IOError: When an IOError occurs.
    Exception: Broad exception when arises.

    """

    if not os.path.isfile(filepath):
        raise FileNotFoundError("File not found. Please check if file exists: {0}".format(filepath))
    try:
        with open(filepath, 'rb') as fp:
            dumplings = pickle.load(fp)
    except IOError:
        print("IOError while reading pickle file: {0}".format(filepath))
        return False
    except Exception as err:
        print("Unknown error while reading pickle file {0} error: {1}".format(filepath, str(err)))
        return False
    else:
        return dumplings



