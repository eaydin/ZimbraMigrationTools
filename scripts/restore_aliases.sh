#!/usr/bin/env bash

source configs.sh

log_line "Processing Alias Restore of User Accounts"

for user in $(cat ${NEW_ACCOUNTS_PATH}/users.txt); do
    if [[ -f ${NEW_ALIASES_PATH}/${user}.txt ]]; then
        for alias in $(grep '@' ${NEW_ALIASES_PATH}/${user}.txt); do
            zmprov aaa ${user} ${alias}
            if [[ $? -eq 0 ]]; then
                log_line "USER ${user} ALIAS ${alias} - Restored"
            else
                log_line "Error while creating USER ${user} ALIAS ${alias}"
            fi
        done
    fi
done

log_line "Processing Alias Restore of Admin Accounts"

for user in $(cat ${NEW_ACCOUNTS_PATH}/admins.txt); do
    if [[ -f ${NEW_ALIASES_PATH}/${user}.txt ]]; then
        for alias in $(grep '@' ${NEW_ALIASES_PATH}/${user}.txt); do
            zmprov aaa ${user} ${alias}
            if [[ $? -eq 0 ]]; then
                log_line "ADMIN ${user} ALIAS ${alias} - Restored"
            else
                log_line "Error while creating ADMIN ${user} ALIAS ${alias}"
            fi
        done
    fi
done

log_line "Restoration of aliases complete"