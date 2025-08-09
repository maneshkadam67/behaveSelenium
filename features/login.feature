Feature: Login feature
  Scenario: Login with valid email and valid password
    Given User navigate to login page
    When User enters valid username and valid password
    And Click login button
    Then Proper message should be displayed

  Scenario: Login with valid email and invalid password
    Given User navigate to login page
    When User enters valid username and valid password
    And Click login button
    Then Proper error message should be displayed

  Scenario: Login with empty email and empty password
    Given User navigate to login page
    When User enters valid username and valid password
    And Click login button
    Then Proper error message should be displayed

