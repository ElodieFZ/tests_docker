![Test Status](https://github.com/ElodieFZ/tests_docker/workflows/tests/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ElodieFZ/tests_docker/badge.svg?branch=master)](https://coveralls.io/github/ElodieFZ/tests_docker?branch=master)
![Coverage Status](https://codecov.io/gh/ElodieFZ/tests_docker/branch/master/graph/badge.svg)

# Github workflow using Docker 

## For a random action

Uses:
- GitHub workflow file: `.github/workflows/main.yml`
- an action file in the root directory of the repo: `action.yaml`
- a Dockerfile in the root directory of the repo: `Dockerfile`
- the script to run within a Docker container, when the GitHub workflow is called: `entrypoint.sh`

Hints:
 - `uses: ./` in the GitHub workflow file means to use an action in the root directory of the repo. An action is a file named `action.yaml`.
 
## To perform unittests

Uses:
- GitHub workflow file: `.github/workflows/tests.yml`
- a Dockerfile in the root directory of the repo: `Dockerfile.unittests`
- a Docker Compose in the root directory of the repo: `docker-compose.unittests.yml`
  (to describe the environment where the Docker container will run?)
