#!/usr/bin/env bash

source configs.sh

log_line "Restore script started..."

while true; do

    log_line "Checking differences"
    mapfile -t NEW_BOXES < <(diff <(sort $TRANSFERRED_DIFF_TXT_PATH | uniq | sort) <(sort $RESTORED_DIFF_TXT_PATH | uniq | sort) | grep @ | cut -d ' ' -f2)

    for account in "${NEW_BOXES[@]}"; do
        # Restore mailbox
        log_line "Restoring mailbox diff for ${account}"
        zmmailbox -z -m ${account} postRestURL "/?fmt=tgz&resolve=skip" ${NEW_MAILBOX_DATA_DIFF_PATH}/${account}.tgz
        check_err_cont "Failed to restore ${account} from ${NEW_MAILBOX_DATA_DIFF_PATH}/${account}.tgz"

        # Leave mark
        log_line "Mailbox diff restore success, leaving mark on restore file."

        echo ${account} >> ${RESTORED_DIFF_TXT_PATH}
        check_err_cont "Failed to leave mark on restore diff file"

        log_line "Restore mailbox diff success for ${account}"

    done

    log_line "Waiting for new input"
    sleep 5
done

