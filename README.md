# Web Automation using Python + Selenium
Use this guide to:
 * Prepare your machine to run Python and Selenium tests
 * Run a test case

## I. Pre-requirement
### 1. Python
Get **Python** from [here](https://www.python.org/downloads/)
**Note**: Don't forget to add Python to your environment variable's `PATH` 

### 2. PIP
Get **pip** from [here](https://pip.pypa.io/en/stable/installation/)


### 3. Required Packages
```
pip install -r requirements.txt
```

### 4. Web-drivers
Use thw WebdriverManager to get the proper drivers.

### 5. Add Web-drivers to `PATH` environment variable.
 1. After downloading the web-driver, add it to your Python's `SCRIPT` folder

## II. Run test
```
 python -m pytest @vacancies
```
