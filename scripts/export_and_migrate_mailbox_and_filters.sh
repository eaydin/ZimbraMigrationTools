#!/usr/bin/env bash

if [[ -z $1 ]]; then
    echo "Please specify username as argument"
    exit 1
fi

source configs.sh

USER=$1

log_line "Username is $USER"
log_line "The filters path on the new server is $NEW_FILTER_PATH"

