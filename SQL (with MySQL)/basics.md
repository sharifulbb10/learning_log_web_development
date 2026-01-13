##### Database
- collection of data in easily accessible format

##### Database Management System (DBMS)
- a software; two types:
	- relational
	- non-relational

##### SQL
- Structured Query Language
- language to interact with RDBMS
- used to do CRUD operation:
	- create
	- read
	- update
	- delete

##### Intalling MySQL:
- downloaded and installed MySQL community version
```bash
# downloaded apt from mysql official website
sudo apt update
sudo apt upgrage
sudo apt install mysql-server

# check whether installed or not
mysql --version
```
- downloaded and installed Work bench
- But the problem I faced:
	- I couldn't configure a new connection from the workbench, error message: `access denied for user 'root'@'localhos'`
	- **ADDITIONAL -** The reason of this issue is: from terminal command, we add `sudo` for any operation with root access, but the GUI cannot add sudo, that's why it is displaying this access-error message.
- To mitigate this,
(from terminal)
```bash
sudo mysql
# enter password for 'sudo' operation

# create a new user
CREATE USER 'devuser'@'localhost' IDENTIFIED BY 'strongpassword';

# grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'devuser'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```
- Now I configured a new connection with the username and password from MySQL Workbench.

**ADDTIONAL:**
##### How to delete a mysql user from terminal?
```bash
sudo mysql

# verify if the user exists
SELECT 'devuser', 'localhost' FROM mysql.user;
# 'devuser' - user name
# 'localhost' - host

DROP USER 'devuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# verify deletion
mysql -u devuser -p

# We should see:
# ERROR 1045 (28000): Access denied
```

**ADDTIONAL:**
##### How to change the password from terminal?
```bash
sudo mysql
# provide authentication password
ALTER USER 'devuser'@'localhost' IDENTIFIED BY 'NewStrongPass123!';
FLUSH PRIVILEGES;
EXIT;
mysql -u devuser -p
# provide new password, see if it connects.
```

##### First database creation with sql
```sql
CREATE DATABASE db_name;
DROP DATABASE db_name;
```
