webssh_embedded
-----------------

This release provides approximate execution time(as opposed to the previous versions which gave exact time). This change allows us to execute commands like cd which changes the directory of the embedded terminal and also retain environment variables of the terminal session. An additional feature for local storage clearance(only in case of error) has been provided. Logging has been improved. Also, a special treatment of script command has been made so that the system does not await the status of script command and hence only execute the command and not provide the status. This means that the script command can now be executed from the input. 
