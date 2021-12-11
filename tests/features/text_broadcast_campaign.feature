
Feature: text broadcast campaign creation and completion 
      
    As a registered user with valid username and password, I want to create a text broadcast campaign and start it to send it to the phonebook contact(s)

  Background:
    Given the CallHub business homepage page is displayed
    And the user logs in using valid "<username>" and "<password>"
    And the user starts text broadcast campaign creation

    Examples:
    |             username                   |    password           |
    |  amber.bestbusinessdeals@gmail.com     |    Sherlock@001       |


  @campaign
  Scenario Outline: text broadcast creation and completion 
    When the user finishes creating text broadcast campaign with a "<phonebook>"
    And user is redirected to overview page
    Then the user clicks on start and campaign completion is verified
    Examples: phonebook
      | phonebook  |
      | Demo Test  |


  @phonebook
  Scenario: phonebook validation
    When user does not select any phonebook
    Then error message "Add atleast 1 phonebook to create this campaign" should be shown on the screen


  @script
  Scenario: script validation
    When user selects phonebook "Demo Test"
    And user does not type any script for text broadcast
    Then error message "Please provide the broadcast message." should be shown on the screen

    

