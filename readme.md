

___________________________________________________________
Problem statement: 

Develop automated test system using pytest-bdd (https://github.com/pytest-dev/pytest-bdd) that will test the working of campaign creation (Text Broadcast), starting of campaign and validate the count of successful messages sent from the campaign overview page.
____________________________________________________________


___________________________________________________________
Test Cases: 

1. Create text broadcast campaign successfully, start the campaign and validate it's completion
  	COMMAND: pytest -m campaign -v -s 

2. Phonebook validation while campaign creation : creating campaign without any selected phonebook > gives error message

	COMMAND: pytest -m phonebook -v -s

3. Script validation: creating campaign without typing any script text > gives error message
	COMMAND: pytest -m script -v -s 
____________________________________________________________


___________________________________________________________

COMMAND for creating report for all the test cases (saves it in callhub_text_broadcast_test_report.html) : 


  	COMMAND: pytest --html=callhub_text_broadcast_test_report.html -v -s 

____________________________________________________________




