#!/usr/bin/env bash

source configs.sh

log_line "Starting Distribution List Member Restoration"

for list in $(cat ${NEW_DIST_LISTS_PATH}/dist_lists.txt); do
    for member in $(grep -v '#' ${NEW_DIST_LISTS_PATH}/${list}.txt | grep '@'); do
        zmprov adlm ${list} ${member}
        if [[ $? -eq 0 ]]; then
            log_line "Restore ${member} on ${list} done"
        else
            log_line "Error restoring ${member} on ${list}"
        fi
    done
done

log_line "Restoring distribution list members done"
