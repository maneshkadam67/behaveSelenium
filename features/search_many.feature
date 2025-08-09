Feature: Many product search
  @sanity
  Scenario Outline: Search for a valid product
    Given User will navigate to Home Page
    When User enters product name "<product>"
    And User click on search button
    Then Valid <product> should get displayed in search results
  Examples:
  |product|
  |HP     |
  |Mac|
