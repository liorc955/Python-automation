
# Python Automation - nopCommerce Website & API testing

In this project, I built UI automation test cases on NopCommerce Website and API automation test cases on reqres.in with Selenium & Pytest as framework.



## Attached resources
- allure-results folder - contains all the test reports.
- TestData - contains the CSV file for the data-driven testing
- Configuration - contains an ini file that configures the browser, timeout, etc.. for the automation framework.


## Run Locally

Install pipenv:

```bash
 install pipenv --upgrade
 ```

Clone the project

```bash
  git clone https://github.com/liorc955/Python-automation.git
```

Go to the project directory

```bash
  cd Python-automation
```

Install dependencies

```bash
  pipenv install --system
```

Run the web tests

```bash
  pytest .\testCases\test_nopcommerce.py --browser chrome --platform web
```
Run the API tests

```bash
  pytest .\testCases\test_api.py
```


## Allure Tests Report

You can see the Allure Report [here]()

