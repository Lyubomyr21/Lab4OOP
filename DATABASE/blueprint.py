from flask import Blueprint, jsonify, request

import func
from Models import Session, Customer, Goods, Buy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

from werkzeug.security import check_password_hash

from schemas import (
    CustomerData,
    CustomerToCreate,
    CustomerToUpdate,
    StatusResponse,
    GoodsData,
    GoodsToCreate,
    GoodsToUpdate,
    ListGoodsRequest,
    GoodsToBuy,
    BuyGoodsData,
    Customer_Log_Info
)


api_blueprint = Blueprint('api', __name__)

##############################################################

@api_blueprint.route("/customer", methods=["POST"])
def create_customer():
    customer_data = CustomerToCreate().load(request.json)
    customer = func.create_entry(Customer, **customer_data)
    return jsonify(CustomerData().dump(customer))

@api_blueprint.route("/goods", methods=["POST"])
def create_goods():
    goods_data = GoodsToCreate().load(request.json)
    goods = func.create_entry(Goods, **goods_data)
    return jsonify(GoodsData().dump(goods))

##############################################################

@api_blueprint.route("/customer/<id>", methods = ["PUT"])
def update_customer(id):
    session = Session()
    customer_data = CustomerToUpdate().load(request.json)
    original_customer_data = session.query(Customer).filter_by(id = id).one()
    for key , value in customer_data.items():
        setattr(original_customer_data,key,value)
    session.commit()
    return jsonify(CustomerData().dump(original_customer_data)),200

@api_blueprint.route("/goods/<id>", methods = ["PUT"])
def update_goods(id):
    session = Session()
    goods_data = GoodsToUpdate().load(request.json)
    original_goods_data = session.query(Goods).filter_by(id = id).one()
    for key , value in goods_data.items():
        setattr(original_goods_data,key,value)
    session.commit()
    return jsonify(GoodsData().dump(original_goods_data)),200

##############################################################

@api_blueprint.route("/customer/<id>", methods=["DELETE"])
def delete_customer(id):
    func.delete_entry(Customer, id)
    return jsonify(StatusResponse().dump({"code": 200}))


@api_blueprint.route("/goods/<id>", methods=["DELETE"])
def delete_goods(id):
    func.delete_entry(Goods, id)
    return jsonify(StatusResponse().dump({"code": 200}))

##############################################################

@api_blueprint.route("/goods/<id>", methods=["GET"])
def get_goods_by_id(id):
    goods = func.get_entry_by_id(Goods, id)
    return jsonify(GoodsData().dump(goods))

@api_blueprint.route("/goods", methods=["GET"])
def list_goods():
    args = ListGoodsRequest().load(request.args)
    goods = func.list_goods(
        args.get("name"), args.get("price"), args.get("status")
    )
    return jsonify(GoodsData(many=True).dump(goods))

##############################################################

@api_blueprint.route("/buy", methods=["POST"])
def create_buy():
    buy_data = BuyGoodsData().load(request.json)
    session = Session()
    goods = session.query(Goods).filter_by(id=int(buy_data.get("g_id"))).first()
    if (goods.status - int(buy_data.get("quantity"))) >= 0:
        buy = func.create_entry(Buy, **buy_data)
        goods.update({Goods.status: goods.status - int(buy_data.get("quantity"))})
    else:
        return jsonify({"Error": "request not available"}), 400
    session.commit()
    return jsonify(BuyGoodsData().dump(buy))

##############################################################

