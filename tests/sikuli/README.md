# How We QA Maps Demo

## Sikuli

Sikuli tests are designed to walkthrough the entire Maps demo workflow
and test the application from a fully integrated and functional standpoint.

Sikuli tests are designed to be run specifically on 1. Windows 7 environments
and 2. Mac OSX environments.

* Both enviroments can be virtualized, but Sikuli must be installed in the
virtual environment.

## Browsers

Sikuli tests are designed to test specific browser combinations.

In Windows environments:
1. Chrome
2. Firefox

In Mac environments:
1. Safari
2. Firefox

**More to be added**

**NB: Sikuli relies on image recognition. If the browser UI or application UI changes,
tests must be updated**

## Setup

* Ensure that all required browsers are installed.
* Ensure that Sikuli IDE is installed (http://www.sikuli.org/)
* Test cases are located in demos/maps/tests/sikuli/

## Configuration

* All browsers should be on the same screen
  - Doesn't matter if they overlap each other.
* The Sikuli IDE should be located on the same screen as the test browsers.
* Before starting the test take each browser to https://www.gotesters.com/lib/qa-supported-files/sikuli-calibration.html
  - Make the neccessary adjustments.

## Running tests

Simply click the ```Run``` button in the Sikuli IDE.
