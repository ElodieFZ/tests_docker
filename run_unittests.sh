#!/bin/bash

##nosetests

# The following is to have it work with codecov, except it doesn't work..
nosetests --with-coverage --cover-package=my_module

#if [[ -n "$CODECOV_TOKEN" ]]; then
#  bash <(curl -s https://codecov.io/bash)
#fi
