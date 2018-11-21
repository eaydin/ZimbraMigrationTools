#!/usr/bin/env bash

source configs.sh

log_line "Beginning Signature Restore"

for user in $(cat ${NEW_ACCOUNTS_PATH}/users.txt); do
    if [[ -f ${NEW_SIGNATURES_PATH}/${user}.pickle ]]; then
        python ${NEW_SCRIPTS_PATH}/restore_signatures.py -u $user -f ${NEW_SIGNATURES_PATH}/${user}.pickle

        if [[ $? -ne 0 ]]; then
            log_line "Error while restoring signature for ${user}"
        fi

    else
        log_line "Error while restoring signature. ${NEW_SIGNATURES_PATH}/${user}.pickle does not exist."
    fi
done

log_line "Signature Restore Complete"