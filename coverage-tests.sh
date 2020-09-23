#!/bin/bash

coverage run --omit=test/* --source my_module -m my_module.examples || exit 1
coverage report

echo

if [[ -n "$COVERALLS_REPO_TOKEN" ]]
then
  coveralls
else
  echo %%
  echo %% Do you want code coverage generated on https://coveralls.io with GitHub Actions.
  echo %%
  echo "%%   1. Add repository to coveralls.io."
  echo "%%   2. Add a repository secret in [ Setting > Secrets ]."
  echo "%%      Name it COVERALLS_REPO_TOKEN, and use the token from coveralls.io as value."
  echo %%
fi
