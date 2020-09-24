## happy path
* greet
  - utter_greet
  - form_get_client_message  
  - form{"name": "form_get_client_message"}
  - slot{"client_name": "Rohit Sharma"}
  - slot{"client_email": "max@gmail.com"}
  - slot{"client_message": "An example of a message is a speech mae An example of a message inbox"}
  - form{"name": null}



## Name entry
* client_name_entry{"client_name": "Rohit Sharma"}
  - slot{"client_name": "Rohit Sharma"}
  ## Name entry
  * client_name_entry{"client_name": "Rohit"}
    - slot{"client_name": "Rohit"}

## Email entry
* client_email_entry{"client_email": "max@gmail.com"}
- slot{"client_email": "max@gmail.com"}

## Message Entrey
* client_message_entry
- slot{"client_message": "An example of a message is a speech mae An example of a message inbox"}
