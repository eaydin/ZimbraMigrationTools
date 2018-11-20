#!/usr/bin/env bash

# Root path to the data directory. You don't have to follow this convention, but it keeps things simple.
DATA_ROOT_PATH="/opt/zimbra/ZimbraMigrationTools/data/"

# Specific Paths under the data directory. If your specific paths are not under a single data directory, edit every
# single one of the accordingly.

FILTER_PATH="$DATA_ROOT_PATH/filters/"
MAILBOX_DATA_PATH="$DATA_ROOT_PATH/mailbox_data/"
MAILBOX_DATA_DIFF_PATH="$DATA_ROOT_PATH/mailbox_data_diff/"
SIGNATURES_PATH="$DATA_ROOT_PATH/signatures/"
DOMAINS_PATH="$DATA_ROOT_PATH/domains/"
DIST_LISTS_PATH="$DATA_ROOT_PATH/dist_lists/"
ACCOUNT_DETAILS_PATH="$DATA_ROOT_PATH/account_details/"
ACCOUNTS_PATH="$DATA_ROOT_PATH/accounts/"
PASSWORDS_PATH="$DATA_ROOT_PATH/passwords/"

# Lists to append and read from when migrating mailboxes
TRANSFERRED_TXT_PATH="$DATA_ROOT_PATH/transferred.txt"
RESTORED_TXT_PATH="$DATA_ROOT_PATH/restored.txt"