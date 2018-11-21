#!/usr/bin/env bash

# This script assumes that you have screenlog.0 in the current directory and that is the log of the screen session
# handling the restore process.

# in order to run such a screen session, simply invoke
# screen -L -D -R migration
# and within the screen session, run the restore_mailbox_and_filters.sh script
# then CTRL+A CTRL+D to detach from the session
# you'll have a screenlog.0 file in the current directory. Now here, run this script

watch "tail -n 50 screenlog.0 | grep 'Restore success for';
echo '';
grep 'Restoring mailbox for' screenlog.0 | tail -n1;
echo '';
echo -n 'Total Completed Restores: ';
grep 'Restore success for' screenlog.0 | wc -l;
echo -n 'Total Errors: ';
grep 'ERROR: Failed to restore' screenlog.0 | wc -l"