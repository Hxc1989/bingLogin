Feature: Login a website

  Scenario: Login cn.bing.com
    When i open cn.bing.com
    Given input username and password: "*****" "****"
#    change ***** as your username, change **** as your password
    Then login successfully
