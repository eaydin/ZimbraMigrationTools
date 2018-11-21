#!/usr/bin/env bash

source configs.sh

log_line "Restore script started..."

while true; do

    log_line "Checking differences"
    mapfile -t NEW_BOXES < <(diff <(sort $TRANSFERRED_TXT_PATH | uniq | sort) <(sort $RESTORED_TXT_PATH | uniq | sort) | grep @ | cut -d ' ' -f2)

    for account in "${NEW_BOXES[@]}"; do
        # Restore mailbox
        log_line "Restoring mailbox for ${account} (this will take long)..."
        zmmailbox -z -m ${account} postRestURL "/?fmt=tgz&resolve=skip" ${NEW_MAILBOX_DATA_PATH}/${account}.tgz
        check_err_cont "Failed to restore ${account} from ${NEW_MAILBOX_DATA_PATH}/${account}.tgz"

        # Restore filters
        log_line "Mailbox restore success, proceeding on filter restore"
        python ${NEW_SCRIPTS_PATH}/restore_filters.py -u ${account} -f ${NEW_FILTER_PATH}/${account}.pickle
        check_err_cont "Failed to restore filters for ${account} from ${NEW_FILTER_PATH}/${account}.pickle"

        # Leave mark
        log_line "Filter restore success, leaving mark on restore file."
        echo ${account} >> ${RESTORED_TXT_PATH}
        check_err_cont "Failed to leave mark on restore file"

        log_line "Restore success for ${account}"

    done

    log_line "Waiting for new input"
    sleep 5
done

