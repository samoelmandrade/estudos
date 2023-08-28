#install docker my sql

docker run --name samoelmaciel -e MYSQL_ROOT_PASSWORD=samoca123 -d mysql:5.7


#Connect to MySQL from the MySQL command line client

docker run -it --network some-network --rm mysql mysql -hsome-mysql -uexample-user -p

docker run --name samoelmaciel -e MYSQL_ROOT_PASSWORD=samoca123 -d mysql:8.0 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci


 docker run --name samoelmysql -e MYSQL_ROOT_PASSWORD=samoca123 -v D:\curso\mysql:/var/lib/mysql -d mysql:5.7

 docker exec -it 8aeeb02be081 bash 

  docker container inspect 8aeeb02be081


  mysql -u samoelmysql -p EnterPassword:samoca123