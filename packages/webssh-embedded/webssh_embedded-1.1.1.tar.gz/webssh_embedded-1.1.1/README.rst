webssh_embedded
-----------------

This release is simplified compared to the previous versions. No database connection is made. Instead a REST call is made to a server dealing with the database. This represents a standard Microservice architecture where webssh_embedded takes care of only the SSH connections and not the database. A separate database handling server would take care of the CRUD ops. Hence the implementation of such a server and also the database is completely left to the developer. Also this release removes the pending command handling feature. The logging has been improved. A separate logs directory will be created. One log per terminal session will be created in the logs directory.
