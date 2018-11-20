#!/usr/bin/env bash

if [[ -z $1 ]]; then
    echo "Please specify username as argument"
    exit 1
fi

source configs.sh

USER=$1

# Export mailbox
log_line " - Exporting $USER (this will take long)..."

zmmailbox -z -m $USER getRestURL '/?fmt=tgz' > $OLD_MAILBOX_DATA_PATH/${USER}.tgz
check_err "Exporting mailbox of $USER failed."
log_line " - Export mailbox success, proceeding with filters."

# Export filters
python $OLD_SCRIPTS_PATH/export_filters.py -u $USER -p $OLD_FILTER_PATH
check_err "Exporting filters of $USER to $OLD_FILTER_PATH failed."
log_line " - Export filters success. Proceeding to transfer the mailbox (this will take long)"

# Transfer mailbox
scp -P $DEST_PORT -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $OLD_MAILBOX_DATA_PATH/${USER}.tgz ${DEST_SSH_USER}@${DEST_HOST}:${NEW_MAILBOX_DATA_PATH}/
check_err "Transferring mailbox of $USER failed."
log_line " - Transfer of mailbox success. Proceeding to transfer filters."

# Transfer filters
scp -P $DEST_PORT -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $OLD_FILTER_PATH/${USER}.pickle ${DEST_SSH_USER}@${DEST_HOST}:${NEW_FILTER_PATH}/
check_err "Transferring filters of $USER failed."
log_line "- Filter transfer success. Leaving mark on remote"

# Leave mark
COMMAND="ssh -T -p $DEST_PORT -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $DEST_SSH_USER@$DEST_HOST 'echo $USER >> $TRANSFERRED_TXT_PATH'"
eval $COMMAND
check_err "Failed to leave mark."
log_line "Transfer complete successfully for $USER".
