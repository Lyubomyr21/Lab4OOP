CREATE TABLE Customer (
    customer_id SERIAL NOT NULL,
    customername VARCHAR NOT NULL,
    firstName VARCHAR NOT NULL,
    lastName VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    phone VARCHAR,
    PRIMARY KEY (customer_id)
);

CREATE TABLE Goods (
    goods_id SERIAL NOT NULL,
    name VARCHAR,
    price INT,
    status INT,
    PRIMARY KEY (goods_id)
);