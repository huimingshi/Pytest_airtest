cd  ./testCases
pytest  -s  --alluredir  ../outFiles/reports/tmp  --clean-alluredir
allure serve ../outFiles/reports/tmp