Application URL to work with: https://www.google.com/ 

Test Scenario:
                        Navigate to https://www.google.com/
                        search 'qwallity' word and Enter
                        Create universal locator which will select all searched links
                        Go to page by page, take all linkes
                        filter only those which has 'qwallity' word inside the link
                        Create txt file and add only those links which is filtered by point - 5, 6

TODO:                   pip install selenium webdriver

Impotred Libraries:     selenium.webdriver.common.keys, selenium.webdriver.common.by,
                        selenium, logging, time, registered

Run result files:       google_log.txt
                        qwallity_links.txt (stores search results)