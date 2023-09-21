def auto_list(request, table_name):
    return {
        "code": 200,
        "data": [table_name, "list"],
        "msg": "Success"
    }


def auto_get(request, table_name, param_id):
    print(param_id)
    return {
        "code": 200,
        "data": [table_name, "list", param_id],
        "msg": "Success"
    }


def auto_post(request, table_name):
    return {
        "code": 200,
        "data": [table_name, "list"],
        "msg": "Success"
    }


def auto_put(request, table_name, param_id):
    print(param_id)
    return {
        "code": 200,
        "data": [table_name, "list", param_id],
        "msg": "Success"
    }


def auto_delete(request, table_name, param_id):
    print(param_id)
    return {
        "code": 200,
        "data": [table_name, "list", param_id],
        "msg": "Success"
    }


def auto_drop(request, table_name, param_id):
    print(param_id)
    return {
        "code": 200,
        "data": [table_name, "list", param_id],
        "msg": "Success"
    }


auto_config = {
    "list": auto_list,
    "get": auto_get,
    "post": auto_post,
    "put": auto_put,
    "delete": auto_delete,
    "drop": auto_drop
}
