CREATE TABLE Customer (
    id SERIAL NOT NULL,
    customername VARCHAR NOT NULL,
    firstName VARCHAR NOT NULL,
    lastName VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    phone VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE Goods (
    id SERIAL NOT NULL,
    name VARCHAR,
    price INT,
    status INT,
    PRIMARY KEY (id)
);

CREATE TABLE Buy (
    id SERIAL NOT NULL,
    id SERIAL NOT NULL,
    quantity INT
    PRIMARY KEY (id)
    PRIMARY KEY (id)
);