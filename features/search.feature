Feature: Search feature
  @smoke
  Scenario: Search for a valid product
    Given User will navigate to Home Page
    When When User enters product name "HP"
    And User click on search button
    Then Valid product should get displayed in search results
  @smoke
  Scenario: Search for a invalid product
    Given User will navigate to Home Page
    When When User enters invalid product name "HP43423432"
    And User click on search button
    Then Proper message should be displayed on screen

  Scenario: Search for a invalid product
    Given User will navigate to Home Page
    When User enter valid valid product
    And User click on search button
    Then Proper message should be displayed on screen



