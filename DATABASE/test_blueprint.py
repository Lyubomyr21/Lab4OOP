#from app import app
from app import app

a_test = app.test_client()

############################################################

def test_create_customer():
    data = a_test.post("/api/store/customer", json = {
    "customername" : "Bttt21",
    "firstname" : "Bob",
    "lastname" : "Marley",
    "email" : "888@gmail.com",
    "password" : "rtr55",
    "phone" : "+38050665"
    })
    assert "200" in str(data)

def test_create_goods():
    data = a_test.post("/api/store/goods", json = {
    "name" : "Vovrik",
    "price" : "80",
    "status" : "9"
    })
    assert "200" in str(data)

##############################################################

def test_update_customer():
    data = a_test.put("/api/store/customer/4", json = {
    "customername" : "Bttt21",
    "firstname" : "Bob",
    "lastname" : "Marley",
    "email" : "888FFFF_ffTar@gmail.com",
    "password" : "rtr55",
    "phone" : "+38050665"
    })
    assert "200" in str(data)

def test_update_goods():
    data = a_test.put("/api/store/goods/22", json = {
    "name" : "MMovrik",
    "price" : "220",
    "status" : "100"
    })
    assert "200" in str(data)

#############################################################

def test_delete_goods():
    data = a_test.delete("/api/store/goods/34", json = {})
    assert "200" in str(data)

def test_delete_customer():
    data = a_test.delete("/api/store/customer/53", json = {})
    assert "200" in str(data)

#############################################################

def test_get_goods_by_id():
    data = a_test.get("/api/store/goods/22", json = {})
    assert "200" in str(data)

def test_list_goods():
    data = a_test.get("/api/store/goods", json = {})
    assert "200" in str(data)

#############################################################

def test_create_buy():
    data = a_test.post("/api/store/buy", json = {
    "c_id" : "45",
    "g_id" : "22",
    "quantity" : "4"
})

#############################################################
