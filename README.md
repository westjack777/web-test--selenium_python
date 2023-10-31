# Web Automation using Robot Framework + Selenium
Use this guide to:
 * Prepare your machine to run Robot Framework and Selenium tests
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

### 4. Download Chrome Web-driver
Get **chromedriver** from [here](https://sites.google.com/chromium.org/driver/)

### 5. Add Web-drivers to `PATH` environment variable.
 1. After downloading the web-driver, add it to your Python's `SCRIPT` folder

## II. Run example
```
robot -d log TestCases
```

## III. Selenium Library
Please view them at [here](http://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Create%20Webdriver)

## IV. RobotFramework License
Please read at [here](https://github.com/ducdhm/robotframework-selenium-example/blob/master/LICENSE.md)