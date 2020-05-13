# snbank
This a python console banking program built using Python filesystem. 
### Features
* Bank staffs can login into the system, because the program can validate user input from data stored in a file.
* After login, a session file is generated that stores the details of the logged in staff.
* Logged in staff can choose among different operations to perform (Opening an account, Checking Bank Details or Logging out)
* To open an account, the program asks for customer details, generate a unique account number for the customer and then saves the customer details to the customer file 
* To check for bank details, the program asks for customer account number and checks the customer file to retrieve the customer account details
* Finally, the staff can logout and the session file is deleted
