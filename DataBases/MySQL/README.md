# MySQL

## Instalación en Fedora

```shell
sudo dnf install python3-devel mysql-devel community-mysql community-mysql-server
```

## Configurando servidor

> Improve MySQL installation security.  manual

```shell
mysql_secure_installation
```


## Iniciar y habilitar servicio mysqld

```shell
sudo systemctl enable mysqld.service
sudo systemctl start mysqld.service
```

## Ingresar a MySQL

```sql
mysql -h localhost -P 3306 -u root -p
```

## Crear usuario

```sql

SELECT VALIDATE_PASSWORD_STRENGTH('contraseña_segura');

CREATE USER 'nombre_usuario'@'%' IDENTIFIED BY 'contraseña_segura';

```

## Crear tabla e ingresar VALIDATE_PASSWORD_STRENGTH

```sql
CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    url_image VARCHAR(255),
    price FLOAT,
    discount INT,
    category INT,
    FOREIGN KEY (category) REFERENCES category(id)
);

CREATE TABLE category (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NULL
);
```


```sql
INSERT INTO product(name, url_image, price, discount, category) VALUES
  ('ENERGETICA MR BIG', 'https://dojiw2m9tvv09.cloudfront.net/11132/product/misterbig3308256.jpg', 1490, 20, 1)
);

INSERT INTO category(name) VALUES
	('bebida energetica')
);
```

## Permisos de usuario a tabla

```sql
GRANT SELECT ON `database`.* TO 'nombre_usuario'@'%';

SHOW GRANTS FOR 'nombre_usuario';
```


## Opcional, establecer restricciones para el usuario.

```sql
set global max_user_connections = 30;
ALTER USER 'nombre_usuario'@'%' WITH MAX_CONNECTIONS_PER_HOUR 20;
```
