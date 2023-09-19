import logging
import warnings
from datetime import datetime, timedelta

from lesscode.utils.encryption_algorithm import AES
from tornado.options import options


def format_company_id_en(value, route_key):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    key = options.aes_key
    if route_key in ["core.patent", "core.patent_lite"]:
        for data in value.get("tags", {}).get("proposer_type", []):
            if data.get("code"):
                data["code"] = AES.encrypt(key, data["code"])
    elif route_key in ["core.research_institution"]:
        for data in value.get("tags", {}).get("support_unit", []):
            if data.get("id"):
                data["id"] = AES.encrypt(key, data["id"])
    elif route_key in ["core.investment"]:
        for data in value.get("tags", {}).get("invest_company", []):
            if data.get("company_id"):
                data["company_id"] = AES.encrypt(key, data["company_id"])


def format_es_param_result(r, param_list, is_need_decrypt_oralce, is_need_es_score, route_key):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    result_dict = {}
    format_company_id_en(r["_source"], route_key)
    if param_list and r["_source"]:
        for key in param_list:
            value = r["_source"]
            key_list = key.split(".")
            for key in key_list:
                if isinstance(value, list):
                    if value:
                        result = []
                        for v in value:
                            if isinstance(v.get(key, None), list):
                                result = result + v[key]
                            else:
                                result.append(v.get(key, None))
                        value = result
                elif isinstance(value, dict):
                    if value:
                        value = value.get(key, None)
                else:
                    pass
            if result_dict.get(key) is None:
                if value is not None:
                    result_dict[key] = value
    else:
        result_dict = r["_source"]
    if is_need_decrypt_oralce:
        r["_id"] = AES.encrypt(options.aes_key, r["_id"])
    result_dict["_id"] = r["_id"]
    if is_need_es_score:
        result_dict["_score"] = r["_score"]
    return result_dict


def es_condition_by_match_phrase(bool_list, column, param, slop=0):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if param:
        if isinstance(param, list):
            bool_list.append({
                "match_phrase": {
                    column: {
                        "query": param[0],
                        "slop": slop
                    }
                }
            })
        if isinstance(param, str):
            bool_list.append({
                "match_phrase": {
                    column: {
                        "query": param,
                        "slop": slop
                    }
                }
            })


def es_condition_by_match(bool_list, column, param):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if param:
        if isinstance(param, list):
            bool_list.append({
                "match": {
                    column: {
                        "query": param[0],
                    }
                }
            })
        if isinstance(param, str):
            bool_list.append({
                "match": {
                    column: {
                        "query": param,
                    }
                }
            })


def es_condition_by_not_null(boo_must_list, column, param):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if param:
        boo_must_list.append({
            "exists": {
                "field": column
            }
        })


def es_condition_by_range(bool_must_list, column, date_list, is_contain_end_date=False, is_contain_start_date=True):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if date_list:
        range_dict = {}
        if date_list[0]:
            if is_contain_start_date:
                range_dict["gte"] = date_list[0]
            else:
                range_dict["gt"] = date_list[0]
        if len(date_list) == 2 and date_list[1]:
            end = date_list[1]
            if is_contain_end_date:
                range_dict["lte"] = end
            else:
                range_dict["lt"] = end

        if range_dict:
            bool_must_list.append({
                "range": {
                    column: range_dict
                }})


def es_condition_by_terms(bool_must_list, column, param_list, is_need_decrypt_oralce=False):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if param_list:
        param_list = [i for i in param_list if i not in [None, "", "all"]]
        if is_need_decrypt_oralce:
            for index, id in enumerate(param_list):
                try:
                    id = AES.decrypt(options.aes_key, id)
                    param_list[index] = int(id)
                except:
                    pass
        if param_list:
            bool_must_list.append({
                "terms": {
                    column: param_list
                }})


def es_condition_by_wildcard(bool_list, column, param):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if param:
        bool_list.append({"wildcard": {column: f"*{param}*"}})


def es_condition_by_exist(bool_must_list, param, is_exists="是"):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if param:
        if is_exists == "是" or is_exists == "true" or is_exists == True:
            bool_must_list.append({
                "exists": {
                    "field": param
                }})
        else:
            bool_must_list.append({
                "bool": {
                    "must_not": [
                        {
                            "exists": {
                                "field": param
                            }
                        }
                    ]
                }
            })


def es_condition_by_exist_or_not(bool_must_list, param_dict):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if param_dict:
        for key in param_dict:
            if param_dict[key] in ["是", "true", True]:
                bool_must_list.append({
                    "exists": {
                        "field": key
                    }})
            else:
                bool_must_list.append({
                    "bool": {
                        "must_not": [
                            {
                                "exists": {
                                    "field": key
                                }
                            }
                        ]
                    }
                })


def es_condition_by_not_in(bool_must_list: list = None, column="", param_list=None):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if param_list:
        bool_must_list.append({
            "bool": {
                "must_not": {
                    "terms": {
                        column: param_list
                    }}
            }
        })


def es_condition_by_geo_shape(bool_must_list: list = None, column="", polygon=None, geo_type="MultiPolygon",
                              relation="intersects"):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if polygon:
        bool_must_list.append({
            "geo_shape": {
                column: {
                    "shape": {
                        "type": geo_type,
                        "coordinates": polygon
                    },
                    "relation": relation
                }
            }
        })


def format_bool_must_and_should(bool_must_list, bool_should_more_list):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if bool_should_more_list:
        for bool_should in bool_should_more_list:
            bool_must_list.append({
                "bool": {
                    "should": bool_should
                }
            })


def format_bool_must_and_must_not(bool_must_list, bool_must_not_more_list):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if bool_must_not_more_list:
        for bool_must_not in bool_must_not_more_list:
            bool_must_list.append({
                "bool": {
                    "must_not": bool_must_not
                }
            })


def parse_es_sort_list(column=None, order=None):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if column and order:
        if order == "asc":
            sort_list = [
                {
                    column: {
                        "order": order,
                        "missing": "_last"
                    }
                }
            ]
        else:
            sort_list = [
                {
                    column: {
                        "order": order,
                        "missing": "_last"
                    }
                }
            ]
    else:
        sort_list = []

    return sort_list


def es_condition_by_geo_distance(bool_must_list: list = None, column="", geo_distance=None):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    if geo_distance:
        bool_must_list.append({
            "geo_distance": {
                "distance": "{}{}".format(geo_distance.get("radius", 0), geo_distance.get("unit", "km")),
                column: {
                    "lat": geo_distance.get("lat", 0),
                    "lon": geo_distance.get("lon", 0),
                }
            }
        })


def es_mapping2dict(mapping):
    warnings.warn("此方法已弃用，不推荐使用，切换到lesscode-utils包里", DeprecationWarning)
    mapping_dict = dict()

    if isinstance(mapping, dict):
        if "properties" in mapping:
            for k, v in mapping.get("properties").items():
                if isinstance(v, dict):
                    if "properties" not in v:
                        if "fields" not in v and "type" in v:
                            field_type = v.get("type")
                            mapping_dict[k] = field_type
                        elif "fields" in v and "type" in v:
                            field_type = v.get("type")
                            mapping_dict[k] = field_type
                            if isinstance(v.get("fields"), dict):
                                for fk, fv in v.get("fields").items():
                                    if "type" in fv:
                                        mapping_dict[f"{k}.{fk}"] = fv.get("type")

                    else:
                        mapping_dict[k] = es_mapping2dict(v)

    return mapping_dict
