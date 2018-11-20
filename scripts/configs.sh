#!/usr/bin/env bash

# Root path to the data directory. You don't have to follow this convention, but it keeps things simple.
OLD_DATA_ROOT_PATH="/opt/zimbra/ZimbraMigrationTools/data/"
NEW_DATA_ROOT_PATH=$OLD_DATA_ROOT_PATH

# Specific Paths under the data directory. If your specific paths are not under a single data directory, edit every
# single one of the accordingly.

# Paths below are for the OLD Server
OLD_FILTER_PATH="$OLD_DATA_ROOT_PATH/filters/"
OLD_MAILBOX_DATA_PATH="$OLD_DATA_ROOT_PATH/mailbox_data/"
OLD_MAILBOX_DATA_DIFF_PATH="$OLD_DATA_ROOT_PATH/mailbox_data_diff/"
OLD_SIGNATURES_PATH="$OLD_DATA_ROOT_PATH/signatures/"
OLD_DOMAINS_PATH="$OLD_DATA_ROOT_PATH/domains/"
OLD_DIST_LISTS_PATH="$OLD_DATA_ROOT_PATH/dist_lists/"
OLD_ACCOUNT_DETAILS_PATH="$OLD_DATA_ROOT_PATH/account_details/"
OLD_ACCOUNTS_PATH="$OLD_DATA_ROOT_PATH/accounts/"
OLD_PASSWORDS_PATH="$OLD_DATA_ROOT_PATH/passwords/"

# Paths below are for the NEW Server. We use identical paths but you don't have to
NEW_FILTER_PATH="$NEW_DATA_ROOT_PATH/filters/"
NEW_MAILBOX_DATA_PATH="$NEW_DATA_ROOT_PATH/mailbox_data/"
NEW_MAILBOX_DATA_DIFF_PATH="$NEW_DATA_ROOT_PATH/mailbox_data_diff/"
NEW_SIGNATURES_PATH="$NEW_DATA_ROOT_PATH/signatures/"
NEW_DOMAINS_PATH="$NEW_DATA_ROOT_PATH/domains/"
NEW_DIST_LISTS_PATH="$NEW_DATA_ROOT_PATH/dist_lists/"
NEW_ACCOUNT_DETAILS_PATH="$NEW_DATA_ROOT_PATH/account_details/"
NEW_ACCOUNTS_PATH="$NEW_DATA_ROOT_PATH/accounts/"
NEW_PASSWORDS_PATH="$NEW_DATA_ROOT_PATH/passwords/"

# Lists to append and read from when migrating mailboxes
TRANSFERRED_TXT_PATH="$NEW_DATA_ROOT_PATH/transferred.txt"
RESTORED_TXT_PATH="$NEW_DATA_ROOT_PATH/restored.txt"

# Parameters of the new server to connect while transferring data

# Write destination host IP address and SSH Port
DEST_HOST=10.10.10.10
DEST_PORT=22

