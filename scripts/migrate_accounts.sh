#!/usr/bin/env bash

source configs.sh

send_file () {
scp -P $DEST_PORT -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $1/$2 ${DEST_SSH_USER}@${DEST_HOST}:$3/
}

log_line "Migrating domains.txt"
send_file ${OLD_DOMAINS_PATH} domains.txt ${NEW_DOMAINS_PATH}
check_err "Error while migrating domains.txt"

log_line "Migrating admins.txt"
send_file ${OLD_ACCOUNTS_PATH} admins.txt ${NEW_ACCOUNTS_PATH}
check_err "Error while migrating admins.txt"

log_line "Migrating users.txt"
send_file ${OLD_ACCOUNTS_PATH} users.txt ${NEW_ACCOUNTS_PATH}

log_line "Migrating account details"
send_file ${OLD_ACCOUNT_DETAILS_PATH} \* ${NEW_ACCOUNT_DETAILS_PATH}
check_err "Error while migrating account details"

log_line "Migrating account passwords"
send_file ${OLD_PASSWORDS_PATH} \* ${NEW_PASSWORDS_PATH}
check_err "Error while migrating account passwords"

log_line "Migrating distribution lists"
send_file ${OLD_DIST_LISTS_PATH} dist_lists.txt ${NEW_DIST_LISTS_PATH}
check_err "Error while migrating dist_lists.txt"

log_line "Migrating alises"
send_file ${OLD_ALIASES_PATH} \* ${NEW_ALIASES_PATH}
check_err "Error while migrating account aliases"

log_line "Migrating Signatures"
send_file ${OLD_SIGNATURES_PATH} \* ${NEW_SIGNATURES_PATH}
check_err "Error while sending signatures"

log_line "File based migrations complete"