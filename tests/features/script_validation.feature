@script

Feature: script validation while campaign creation
      
    Background:
    Given the CallHub login page is displayed

  Scenario: Successful user log in and script validation
    When the user logs in using valid "amber.bestbusinessdeals@gmail.com" and "Sherlock@001" 
    And user starts creating campaign using phonebook "Demo Test"
    And user does not type any script for text broadcast
    Then error message "Please provide the broadcast message." should be shown on the screen

