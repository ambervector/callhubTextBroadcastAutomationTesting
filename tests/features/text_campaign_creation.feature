@campaign

Feature: the working of campaign creation (Text Broadcast), starting of campaign and validate the count of successful messages sent from the campaign overview page
      
      I want to test the text broadcast campaign 


  Background:
    Given the CallHub homepage page is displayed

  Scenario: Successful user log in for Text Broadcast campaign creation and campaign validation
    When the user logs in using valid "amber.bestbusinessdeals@gmail.com" and "Sherlock@001" 
    Then the user is redirected to the guide page

    # Examples:
    #   | username | password |
    #   | amber.bestbusinessdeals@gmail.com | Sherlock@001 |
    
    When the user finishes creating text broadcast campaign with a phonebook called "Demo Test"
    Then user is redirected to overview page

    When the user clicks on start
    Then validate the count of successful messages sent from the campaign overview page 

    

