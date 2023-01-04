from passerby_file import *
import pytest

####################################################################
#### CREATE ####

json_datas=[
        {"appid":"DATABASE2","action":"cre","price":"100","model":"T2","qty":""},
        {"appid":"DATABASE2","action":"cre","price":"","model":"T2","qty":"100"},
        {"appid":"DATABASE2","action":"cre","price":"100","model":"","qty":"20"},
        {"appid":"DATABASE2","action":None,"price":"100","model":"","qty":"20"},
        {"appid":"DATABASE2","action":"crre","price":"100","model":"T2","qty":"100"},
        {"appid":"DATABASE2","action":"","price":"100","model":"T2","qty":"100"},
        {"appid":"DATABASE2","action":"cre","price":"100","model":"T2","qty":"100"},
        {"appid":"DATABASE1","action":"cre","price":"100","model":"T2","qty":"100"},
        {"appid":"SM3","action":"cre","price":"100","model":"T2","qty":"100"},
        {"appid":"","action":"cre","price":"100","model":"T2","qty":"100"},
        {"appid":"DATABASE1","action":"cre","uid":"3","price":"100","model":"T2","qty":"100"}
        ]

@pytest.mark.parametrize("appid,action,model,qty,price",create_func(json_datas))
def test_create(appid,action,model,qty,price):
    assert appid == 'DATABASE1' or appid == 'DATABASE2'
    assert action == 'cre'
    assert model != "",'model not mentioned'

####################################################################
#### DELETE ####

json_datas=[
        {"appid":"DATABASE2","action":"del","uid":"8","model":"200","qty":"100","price":"100"},
        {"appid":"DATABASE2","action":"del","uid":"8","model":"200","qty":"100","price":""},
        {"appid":"DATABASE2","action":"del","uid":"8","model":"200","qty":"","price":"100"},
        {"appid":"DATABASE2","action":"del","uid":"8","model":"","qty":"100","price":"100"},
        {"appid":"DATABASE2","action":"del","uid":"8","model":"200","qty":"","price":""},
        {"appid":"DATABASE2","action":"del","uid":"8","model":"","qty":"100","price":""},
        {"appid":"DATABASE2","action":"del","uid":"8","model":"","qty":"","price":"100"},
        {"appid":"DATABASE2","action":"del","uid":"8","model":"","qty":"","price":""},
        {"appid":"DATABASE2","action":"del","uid":"","model":"","qty":"","price":""},
        {"appid":"DATABASE2","action":"delp","uid":"8","model":"200","qty":"100","price":"100"},
        {"appid":"DATABASE2","action":"","uid":"8","model":"200","qty":"100","price":"100"},
        {"appid":"SM3","action":"del","uid":"8","model":"200","qty":"100","price":"100"},
        {"appid":"","action":"del","uid":"8","model":"200","qty":"100","price":"100"}
        ]

@pytest.mark.parametrize("appid,action,uid,model,qty,price",del_upd_ret_func(json_datas))
def test_delete(appid,action,uid,model,qty,price):
    if ((uid=="") and (model=="") and (qty=="") and (price=="")):
        statfail = "No Value found"
        assert 0==1,statfail
    else:
        assert appid == 'DATABASE1' or appid == 'DATABASE2'
        assert action == 'del'

####################################################################
#### UPDATE ####

json_datas=[
        {"appid":"DATABASE2","action":"upd","uid":"8","model":"200","qty":"100","price":"100"},
        {"appid":"DATABASE2","action":"upd","uid":"8","model":"200","qty":"100","price":""},
        {"appid":"DATABASE2","action":"upd","uid":"8","model":"200","qty":"","price":"100"},
        {"appid":"DATABASE2","action":"upd","uid":"8","model":"","qty":"100","price":"100"},
        {"appid":"DATABASE2","action":"upd","uid":"8","model":"","qty":"","price":""},
        {"appid":"DATABASE2","action":"upd","uid":"8","model":"200","qty":"","price":""},
        {"appid":"DATABASE2","action":"upd","uid":"8","model":"","qty":"","price":"100"},
        {"appid":"DATABASE2","action":"upd","uid":"8","model":"","qty":"100","price":""},
        {"appid":"DATABASE2","action":"upd","uid":"","model":"200","qty":"100","price":"100"},
        {"appid":"DATABASE2","action":"","uid":"8","model":"200","qty":"100","price":"100"},
        {"appid":"","action":"upd","uid":"8","model":"200","qty":"100","price":"100"}
        ]

@pytest.mark.parametrize("appid,action,uid,model,qty,price",del_upd_ret_func(json_datas))
def test_update(appid,action,uid,model,qty,price):
    assert appid == 'DATABASE1' or appid == 'DATABASE2' , 'DB not mentioned or wrongly given'
    assert action == 'upd','wrong action given or not given any upd'
    assert uid != "",'UID not mentioned'
    assert model != "",'model not mentioned'

####################################################################
#### READ ####
json_datas=[
        {"appid":"DATABASE2","action":"ret","uid":"8","model":"200","qty":"100","price":"100"},
        {"appid":"DATABASE2","action":"ret","uid":"","model":"","qty":"","price":""},
        {"appid":"DATABASE2","action":"ret","uid":"8","model":"200","qty":"100","price":""},
        {"appid":"DATABASE2","action":"ret","uid":"8","model":"200","qty":"","price":"100"},
        {"appid":"DATABASE2","action":"ret","uid":"8","model":"","qty":"100","price":"100"},
        {"appid":"DATABASE2","action":"ret","uid":"","model":"200","qty":"100","price":"100"},
        {"appid":"DATABASE2","action":"ret","uid":"8","model":"200","qty":"","price":""},
        {"appid":"DATABASE2","action":"ret","uid":"8","model":"","qty":"100","price":""},
        {"appid":"DATABASE2","action":"ret","uid":"8","model":"","qty":"","price":"100"},
        {"appid":"DATABASE2","action":"ret","uid":"8","model":"","qty":"","price":""},
        {"appid":"DATABASE2","action":"","uid":"8","model":"200","qty":"100","price":"100"},
        {"appid":"","action":"ret","uid":"8","model":"200","qty":"100","price":"100"}
        ]

@pytest.mark.parametrize("appid,action,uid,model,qty,price",del_upd_ret_func(json_datas))
def test_read(appid,action,uid,model,qty,price):
    if uid=="" and model=="" and qty=="" and price=="":
        statret = "No data'S provided..."
        assert 0==1,statret
    else:
        assert appid == 'DATABASE1' or appid == 'DATABASE2' , 'DB not mentioned or wrongly given'
        assert action == 'ret','wrong action given or not given any ret'

####################################################################
