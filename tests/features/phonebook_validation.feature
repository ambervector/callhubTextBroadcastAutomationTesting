@phonebook

Feature: phonebook validation while campaign creation
      
    Background:
    Given the CallHub login page is displayed

  Scenario: Successful user log in and phonebook validation
    When the user logs in using valid "amber.bestbusinessdeals@gmail.com" and "Sherlock@001" 
    And user starts creating campaign
    And user does not select any phonebook
    Then error message "Add atleast 1 phonebook to create this campaign" should be shown on the screen

