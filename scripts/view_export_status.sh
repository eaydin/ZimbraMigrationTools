#!/usr/bin/env bash

# This script assumes that you have screenlog.0 in the current directory and that is the log of the screen session
# handling the export process.

# in order to run such a screen session, simply invoke
# screen -L -D -R migration
# and within the screen session, run the export_mailbox_and_filters.sh script
# then CTRL+A CTRL+D to detach from the session
# you'll have a screenlog.0 file in the current directory. Now here, run this script

watch "tail -n 50 screenlog.0 | grep 'Transfer complete';
echo '';
grep 'Exporting' screenlog.0 | tail -n 1;
echo '';
echo -n 'Total Completed Transfers: ';
grep 'Transfer complete' screenlog.0 | wc -l;
echo -n 'Total Errors: ';
grep -iP 'ERROR.*failed' screenlog.0 | wc -l"