use llista_compra_m06; 

drop table if exists usuaris;

create table if not exists usuaris(
    id bigint unsigned AUTO_INCREMENT PRIMARY KEY,
    usuari VARCHAR(20) NOT NULL UNIQUE,
    password_hash VARCHAR(256) NOT NULL
);
