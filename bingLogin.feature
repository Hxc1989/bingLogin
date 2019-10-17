Feature: Login a website

  Scenario: Login cn.bing.com
    When i open cn.bing.com
    Given input username and password: "1018615857@qq.com" "xiaoNa*1989"
    Then login successfully