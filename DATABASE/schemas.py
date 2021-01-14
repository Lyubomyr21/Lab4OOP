from flask_bcrypt import generate_password_hash
from marshmallow import validate, Schema, fields


class CustomerData(Schema):
    id = fields.Integer()
    customername = fields.String()
    firstname = fields.String()
    lastname = fields.String()
    email =  fields.String(validate=validate.Email())
    phone = fields.String()


class CustomerToCreate(Schema):
    customername = fields.String()
    firstname = fields.String()
    lastname = fields.String()
    email =  fields.String(validate=validate.Email())
    password = fields.String()
    phone = fields.String()

class CustomerToUpdate(Schema):
    customername = fields.String()
    firstname = fields.String()
    lastname = fields.String()
    email =  fields.String(validate=validate.Email())
    password = fields.String()
    phone = fields.String()

class StatusResponse(Schema):
    code = fields.Integer()
    type = fields.String(default="OK")
    message = fields.String(default="OK")


class GoodsData(Schema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Integer()
    status = fields.Integer()


class GoodsToCreate(Schema):
    name = fields.String()
    price = fields.Integer()
    status = fields.Integer()

class GoodsToUpdate(Schema):
    name = fields.String()
    price = fields.Integer()
    status = fields.Integer()

class ListGoodsRequest(Schema):
    name = fields.String()
    price = fields.Integer()
    status = fields.Integer()

class BuyGoodsData(Schema):
    c_id = fields.Integer()
    g_id = fields.Integer()
    quantity = fields.Integer()

class GoodsToBuy(Schema):
    status = fields.Integer()

class Customer_Log_Info(Schema):
    email =  fields.Email()
    password = fields.String()