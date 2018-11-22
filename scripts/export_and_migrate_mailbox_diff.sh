#!/usr/bin/env bash

if [[ -z $1 ]]; then
    echo "Please specify username as argument"
    exit 1
fi

if [[ -z $2 ]]; then
    echo "Please specify start date in MM/DD/YY format"
    exit 1
fi

source configs.sh

USER=$1
STARTDATE=$2

# Export mailbox diff
log_line " - Exporting $USER diff after $STARTDATE"

EXPORT_COMMAND="zmmailbox -z -m $USER getRestURL '//?fmt=tgz&query=under:/ after:\"$STARTDATE\"'  > $OLD_MAILBOX_DATA_DIFF_PATH/${USER}.tgz"
eval $EXPORT_COMMAND
check_err "Exporting mailbox diff of $USER failed."
log_line " - Export mailbox diff success. Proceeding to transfer file"

# Transfer mailbox diff
scp -P $DEST_PORT -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $OLD_MAILBOX_DATA_DIFF_PATH/${USER}.tgz ${DEST_SSH_USER}@${DEST_HOST}:${NEW_MAILBOX_DATA_DIFF_PATH}/
check_err "Transferring mailbox diff of $USER failed."
log_line " - Transfer of mailbox diff success. Leaving mark on remote."

# Leave mark
COMMAND="ssh -T -p $DEST_PORT -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $DEST_SSH_USER@$DEST_HOST 'echo $USER >> $TRANSFERRED_DIFF_TXT_PATH'"
eval $COMMAND
check_err "Failed to leave mark."
log_line "Transfer of diff complete successfully for $USER".
