#!/usr/bin/env bash

source configs.sh

check_err_cont () {
    if [[ $? -ne 0 ]]; then
        log_line " -- ERROR: $1"
        log_line "Continuing to next element"
        continue
    fi
}

log_line "Restoring accounts and passwords"

for i in $(cat ${NEW_ACCOUNTS_PATH}/users.txt); do
    givenName=$(grep givenName: ${NEW_ACCOUNT_DETAILS_PATH}/$i.txt | cut -d ":" -f2)
    check_err_cont "Could not get givenName for ${i}"
    displayName=$(grep displayName: ${NEW_ACCOUNT_DETAILS_PATH}/$i.txt | cut -d ":" -f2)
    check_err_cont "Could not get displayName for ${i}"
    shadowpass=$(cat ${NEW_PASSWORDS_PATH}/${i}.shadow)
    check_err_cont "Could not read password for ${i}"

    zmprov ca $i "TeMpPa55^()" cn "$givenName" displayName "$displayName" givenName "$givenName"
    check_err_cont "Failed to run zmprov ca for ${i}"
    zmprov ma $i userPassword "$shadowpass"
    check_err_cont "Failed to change password for ${i}"

    log_line "Restored user ${i}"
done
log_line "Restoration complete"

