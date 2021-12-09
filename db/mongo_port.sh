#!/bin/bash

export passwd="emailfilter"
export db="emailFilterDB"
export collect="subscriptions"
export key="subscription_name_date"

python3 mongo_port.py $db $collect $key $passwd
