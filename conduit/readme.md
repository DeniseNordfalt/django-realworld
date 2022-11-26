`pip install -r requirements.txt`

`docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=superhemligt -d mysql:8`
kan jag starta docker med namnet på databasen jag vill använda? eller måste jag skapa en ny databas i mysql?
kolla upp

`docker run -p 8080:8080 --name mysqladmin -d phpmyadmin/phpmyadmin`
