#!/usr/bin/env bash
echo "+++ Running test"

test_home=/Users/nattapol/Documents/Test/github/robotframework-test-template
report_path=${test_home}/tests/reports
robot_env=$1
# robot_test_path=${test_home}/tests/testsuites/login/test_login.robot
robot_test_path=${test_home}/tests/testsuites/backend/test_request_config.robot

pushd tests
robot \
    --outputdir ${report_path} \
    --log log.html \
    --report report.html \
    --variable "env:${robot_env}" \
    ${robot_test_path}
popd
