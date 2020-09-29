#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
@File:      routes.py.py
@Author:    Jim.Dai.Cn
@Date:      2020/9/22 上午11:26
@Desc:         
"""

from app.company import blueprint
from flask import render_template, jsonify, current_app, request


@blueprint.route('/company', methods=['GET'])
def get_company_list():
    clist = [
        {"ID":1017,"USER_ID":117,"STATE":50,"THIS_ROLE":"","SYS_ID":4501,"USER_NAME_ABCDEF":"江苏乐福德新材料技术有限公司","USER_TYPE_ABCDEF":11,"AREA_ID_C_ABCDEF":450102,"AREA_ID_B_ABCDEF":4501,"AREA_ID_A_ABCDEF":45,"AREA_ID_ABCDEF":450102005,"PAPER_TYPE_ABCDEF":"","PAPER_NO_ABCDEF":"91320206MA1MWACH6R","PAPER_VALIDITY_ABCDEF":"","BANK_OPEN_ABCDEF":"","BANK_ACCOUNT_ABCDEF":"","OPEN_NAME_ABCDEF":"","OPEN_NO_ABCDEF":"","CONTACTS_ABCDEF":"吴迦迦","FIXED_TEL_ABCDEF":"","MOVE_TEL_ABCDEF":13814244466,"MAIL_ABCDEF":"","FAX_ABCDEF":"","ADDR_ABCDEF":"","REGIST_TIME_ABCE":"","REGIST_CAPITAL_AC":"","WORKERS_NO_AC":"","DEVELOP_NO_A":"","IP_NO_AC":"","IP_SYS_NO_AC":"","MAIN_PRODUCT_A":"","MAIN_MARKET_A":"","IS_ISO_A":"","COMPANY_TYPE_A":"","INDUSTRY_A":"","NATURE_A":"","PROJ_A":"","IS_GAUGE":"","IS_CONTINUE_HIGH":"","LEGAL_PERSON_C":"","PROVINCES_RECORD_C":"","IS_HQ_C":"","HQ_USER_NAME_C":"","HQ_ADDR_C":"","HQ_ZIP_CODE_C":"","HQ_REGIST_ADDR_C":"","HQ_LEGAL_PERSON_C":"","HQ_NO_C":"","HQ_REGIST_TIME_C":"","HQ_EMPLOYMENT_C":"","HQ_PRACTISING_AGENT_C":"","HQ_CONTACTS_C":"","HQ_TEL_C":"","AGENT_NO_C":"","LAW_NO_C":"","NATIONAL_START_C":"","PROVINCE_START_C":"","REGISTRATION_C":"","REGISTRATION_VALIDITY_C":"","CREATE_TIME":"36:43.7","REMARK":"","SPARE1":"","SPARE2":"","SPARE3":"","IS_DELETE":0,"ISO_CREATE_TIME":"","BUSSINESS_TIME_START":"","BUSSINESS_TIME_END":"","REGISTER_PLACE":"","CHECK_DAY":"","REGISTER_STATUS":"","TECHNOLOGY_FIELD":"","INVESTMENT_MONEY":"","DEV_MASTER_NUM":"","DEV_DOCTOR_NUM":"","INDEPENTDENT_LEGAL_PERSON":"","NATIONAL_ECONOMY_INDUSTRY":"","COMPANY_ATTRIBUTE":"","COMPANY_SCALE":"","COMPANY_PROFILE":"","COMPANY_CREDIT_RATING":"","IS_ON_LISTED":"","COMPANY_LISTING_SECTOR":"","LEGAL_PERSON_TEL":"","FINANCE_CONTACT":"","FINANCE_TEL":"","FINANCE_MOBEL":"","FINANCE_EMAIL":"","COMPANY_TYPE":"","IS_TECHNOLOGY":1,"REG_ADDRESS":""},
        {"ID":1018,"USER_ID":118,"STATE":50,"THIS_ROLE":"","SYS_ID":4501,"USER_NAME_ABCDEF":"无锡市易动智能装备有限公司","USER_TYPE_ABCDEF":11,"AREA_ID_C_ABCDEF":450102,"AREA_ID_B_ABCDEF":4501,"AREA_ID_A_ABCDEF":45,"AREA_ID_ABCDEF":450102005,"PAPER_TYPE_ABCDEF":"","PAPER_NO_ABCDEF":"91320206MA1W9HMH22","PAPER_VALIDITY_ABCDEF":"","BANK_OPEN_ABCDEF":"","BANK_ACCOUNT_ABCDEF":"","OPEN_NAME_ABCDEF":"","OPEN_NO_ABCDEF":"","CONTACTS_ABCDEF":"邱林峰","FIXED_TEL_ABCDEF":"","MOVE_TEL_ABCDEF":13306199950,"MAIL_ABCDEF":"","FAX_ABCDEF":"","ADDR_ABCDEF":"无锡市惠山区长安街道畅惠路10","REGIST_TIME_ABCE":"","REGIST_CAPITAL_AC":"","WORKERS_NO_AC":"","DEVELOP_NO_A":"","IP_NO_AC":"","IP_SYS_NO_AC":"","MAIN_PRODUCT_A":"","MAIN_MARKET_A":"","IS_ISO_A":"","COMPANY_TYPE_A":"","INDUSTRY_A":"","NATURE_A":"","PROJ_A":"","IS_GAUGE":"","IS_CONTINUE_HIGH":"","LEGAL_PERSON_C":"","PROVINCES_RECORD_C":"","IS_HQ_C":"","HQ_USER_NAME_C":"","HQ_ADDR_C":"","HQ_ZIP_CODE_C":"","HQ_REGIST_ADDR_C":"","HQ_LEGAL_PERSON_C":"","HQ_NO_C":"","HQ_REGIST_TIME_C":"","HQ_EMPLOYMENT_C":"","HQ_PRACTISING_AGENT_C":"","HQ_CONTACTS_C":"","HQ_TEL_C":"","AGENT_NO_C":"","LAW_NO_C":"","NATIONAL_START_C":"","PROVINCE_START_C":"","REGISTRATION_C":"","REGISTRATION_VALIDITY_C":"","CREATE_TIME":"36:43.7","REMARK":"","SPARE1":"","SPARE2":"","SPARE3":"","IS_DELETE":0,"ISO_CREATE_TIME":"","BUSSINESS_TIME_START":"","BUSSINESS_TIME_END":"","REGISTER_PLACE":"","CHECK_DAY":"","REGISTER_STATUS":"","TECHNOLOGY_FIELD":"","INVESTMENT_MONEY":"","DEV_MASTER_NUM":"","DEV_DOCTOR_NUM":"","INDEPENTDENT_LEGAL_PERSON":"","NATIONAL_ECONOMY_INDUSTRY":"","COMPANY_ATTRIBUTE":"","COMPANY_SCALE":"","COMPANY_PROFILE":"","COMPANY_CREDIT_RATING":"","IS_ON_LISTED":"","COMPANY_LISTING_SECTOR":"","LEGAL_PERSON_TEL":"","FINANCE_CONTACT":"","FINANCE_TEL":"","FINANCE_MOBEL":"","FINANCE_EMAIL":"","COMPANY_TYPE":"","IS_TECHNOLOGY":1,"REG_ADDRESS":""},
        {"ID":1020,"USER_ID":120,"STATE":50,"THIS_ROLE":"","SYS_ID":4501,"USER_NAME_ABCDEF":"无锡达美新材料有限公司","USER_TYPE_ABCDEF":11,"AREA_ID_C_ABCDEF":450102,"AREA_ID_B_ABCDEF":4501,"AREA_ID_A_ABCDEF":45,"AREA_ID_ABCDEF":450102006,"PAPER_TYPE_ABCDEF":"","PAPER_NO_ABCDEF":"91320206MA1M97J91B","PAPER_VALIDITY_ABCDEF":"","BANK_OPEN_ABCDEF":"","BANK_ACCOUNT_ABCDEF":"","OPEN_NAME_ABCDEF":"","OPEN_NO_ABCDEF":"","CONTACTS_ABCDEF":"郑巍","FIXED_TEL_ABCDEF":"","MOVE_TEL_ABCDEF":13951582299,"MAIL_ABCDEF":"","FAX_ABCDEF":"","ADDR_ABCDEF":"","REGIST_TIME_ABCE":"","REGIST_CAPITAL_AC":"","WORKERS_NO_AC":"","DEVELOP_NO_A":"","IP_NO_AC":"","IP_SYS_NO_AC":"","MAIN_PRODUCT_A":"","MAIN_MARKET_A":"","IS_ISO_A":"","COMPANY_TYPE_A":"","INDUSTRY_A":"","NATURE_A":"","PROJ_A":"","IS_GAUGE":1,"IS_CONTINUE_HIGH":"","LEGAL_PERSON_C":"","PROVINCES_RECORD_C":"","IS_HQ_C":"","HQ_USER_NAME_C":"","HQ_ADDR_C":"","HQ_ZIP_CODE_C":"","HQ_REGIST_ADDR_C":"","HQ_LEGAL_PERSON_C":"","HQ_NO_C":"","HQ_REGIST_TIME_C":"","HQ_EMPLOYMENT_C":"","HQ_PRACTISING_AGENT_C":"","HQ_CONTACTS_C":"","HQ_TEL_C":"","AGENT_NO_C":"","LAW_NO_C":"","NATIONAL_START_C":"","PROVINCE_START_C":"","REGISTRATION_C":"","REGISTRATION_VALIDITY_C":"","CREATE_TIME":"36:43.7","REMARK":"","SPARE1":"","SPARE2":"","SPARE3":"","IS_DELETE":0,"ISO_CREATE_TIME":"","BUSSINESS_TIME_START":"","BUSSINESS_TIME_END":"","REGISTER_PLACE":"","CHECK_DAY":"","REGISTER_STATUS":"","TECHNOLOGY_FIELD":"","INVESTMENT_MONEY":"","DEV_MASTER_NUM":"","DEV_DOCTOR_NUM":"","INDEPENTDENT_LEGAL_PERSON":"","NATIONAL_ECONOMY_INDUSTRY":"","COMPANY_ATTRIBUTE":"","COMPANY_SCALE":"","COMPANY_PROFILE":"","COMPANY_CREDIT_RATING":"","IS_ON_LISTED":"","COMPANY_LISTING_SECTOR":"","LEGAL_PERSON_TEL":"","FINANCE_CONTACT":"","FINANCE_TEL":"","FINANCE_MOBEL":"","FINANCE_EMAIL":"","COMPANY_TYPE":"","IS_TECHNOLOGY":1,"REG_ADDRESS":""},
        {"ID":1021,"USER_ID":121,"STATE":50,"THIS_ROLE":"","SYS_ID":4501,"USER_NAME_ABCDEF":"江苏韦兰德特种装备科技有限公司","USER_TYPE_ABCDEF":11,"AREA_ID_C_ABCDEF":450102,"AREA_ID_B_ABCDEF":4501,"AREA_ID_A_ABCDEF":45,"AREA_ID_ABCDEF":450102006,"PAPER_TYPE_ABCDEF":"","PAPER_NO_ABCDEF":913204000000000000,"PAPER_VALIDITY_ABCDEF":"","BANK_OPEN_ABCDEF":"","BANK_ACCOUNT_ABCDEF":"","OPEN_NAME_ABCDEF":"","OPEN_NO_ABCDEF":"","CONTACTS_ABCDEF":"沈伟栋","FIXED_TEL_ABCDEF":"","MOVE_TEL_ABCDEF":18020301820,"MAIL_ABCDEF":"","FAX_ABCDEF":"","ADDR_ABCDEF":"无锡市惠山工业转型集聚区北惠路123号","REGIST_TIME_ABCE":"00:00.0","REGIST_CAPITAL_AC":7000,"WORKERS_NO_AC":65,"DEVELOP_NO_A":10,"IP_NO_AC":"","IP_SYS_NO_AC":"","MAIN_PRODUCT_A":"","MAIN_MARKET_A":"","IS_ISO_A":"","COMPANY_TYPE_A":104,"INDUSTRY_A":41,"NATURE_A":"","PROJ_A":999,"IS_GAUGE":1,"IS_CONTINUE_HIGH":"","LEGAL_PERSON_C":"","PROVINCES_RECORD_C":"","IS_HQ_C":"","HQ_USER_NAME_C":"","HQ_ADDR_C":"","HQ_ZIP_CODE_C":"","HQ_REGIST_ADDR_C":"","HQ_LEGAL_PERSON_C":"沈其明","HQ_NO_C":"","HQ_REGIST_TIME_C":"","HQ_EMPLOYMENT_C":"","HQ_PRACTISING_AGENT_C":"","HQ_CONTACTS_C":"","HQ_TEL_C":"","AGENT_NO_C":"","LAW_NO_C":"","NATIONAL_START_C":"","PROVINCE_START_C":"","REGISTRATION_C":"","REGISTRATION_VALIDITY_C":"","CREATE_TIME":"19:46.8","REMARK":"","SPARE1":"","SPARE2":"","SPARE3":"","IS_DELETE":0,"ISO_CREATE_TIME":"","BUSSINESS_TIME_START":"","BUSSINESS_TIME_END":"","REGISTER_PLACE":"","CHECK_DAY":"","REGISTER_STATUS":1,"TECHNOLOGY_FIELD":807,"INVESTMENT_MONEY":0,"DEV_MASTER_NUM":0,"DEV_DOCTOR_NUM":0,"INDEPENTDENT_LEGAL_PERSON":1,"NATIONAL_ECONOMY_INDUSTRY":873,"COMPANY_ATTRIBUTE":"其他","COMPANY_SCALE":"中型","COMPANY_PROFILE":"","COMPANY_CREDIT_RATING":"","IS_ON_LISTED":0,"COMPANY_LISTING_SECTOR":"","LEGAL_PERSON_TEL":18020301818,"FINANCE_CONTACT":"","FINANCE_TEL":"","FINANCE_MOBEL":"","FINANCE_EMAIL":"","COMPANY_TYPE":"","IS_TECHNOLOGY":1,"REG_ADDRESS":""},
        {"ID":1071,"USER_ID":171,"STATE":50,"THIS_ROLE":"","SYS_ID":4501,"USER_NAME_ABCDEF":"无锡正则精准医学检验有限公司","USER_TYPE_ABCDEF":11,"AREA_ID_C_ABCDEF":450102,"AREA_ID_B_ABCDEF":4501,"AREA_ID_A_ABCDEF":45,"AREA_ID_ABCDEF":450102004,"PAPER_TYPE_ABCDEF":"","PAPER_NO_ABCDEF":"91320206MA1MCH2R4R","PAPER_VALIDITY_ABCDEF":"","BANK_OPEN_ABCDEF":"","BANK_ACCOUNT_ABCDEF":"","OPEN_NAME_ABCDEF":"","OPEN_NO_ABCDEF":"","CONTACTS_ABCDEF":"杨丽华","FIXED_TEL_ABCDEF":"0510-85993951","MOVE_TEL_ABCDEF":13915279492,"MAIL_ABCDEF":"14445505@qq.com","FAX_ABCDEF":"","ADDR_ABCDEF":"无锡惠山经济开发区惠山大道1699号八号楼五层","REGIST_TIME_ABCE":"00:00.0","REGIST_CAPITAL_AC":2000,"WORKERS_NO_AC":42,"DEVELOP_NO_A":16,"IP_NO_AC":"","IP_SYS_NO_AC":"","MAIN_PRODUCT_A":"医学检验；生物技术的研发、技术咨询、技术服务、技术转让；医疗器械的租赁。（依法须经批准的项目，经相关部门批准后方可开展经营活动）。","MAIN_MARKET_A":"","IS_ISO_A":"","COMPANY_TYPE_A":104,"INDUSTRY_A":21,"NATURE_A":"","PROJ_A":999,"IS_GAUGE":0,"IS_CONTINUE_HIGH":"","LEGAL_PERSON_C":"","PROVINCES_RECORD_C":"","IS_HQ_C":"","HQ_USER_NAME_C":"","HQ_ADDR_C":"","HQ_ZIP_CODE_C":"","HQ_REGIST_ADDR_C":"","HQ_LEGAL_PERSON_C":"盛青松","HQ_NO_C":"","HQ_REGIST_TIME_C":"","HQ_EMPLOYMENT_C":"","HQ_PRACTISING_AGENT_C":"","HQ_CONTACTS_C":"","HQ_TEL_C":"","AGENT_NO_C":"","LAW_NO_C":"","NATIONAL_START_C":"","PROVINCE_START_C":"","REGISTRATION_C":"","REGISTRATION_VALIDITY_C":"","CREATE_TIME":"08:05.6","REMARK":"","SPARE1":"","SPARE2":"","SPARE3":"","IS_DELETE":0,"ISO_CREATE_TIME":"","BUSSINESS_TIME_START":"","BUSSINESS_TIME_END":"","REGISTER_PLACE":"","CHECK_DAY":"","REGISTER_STATUS":1,"TECHNOLOGY_FIELD":201,"INVESTMENT_MONEY":"","DEV_MASTER_NUM":10,"DEV_DOCTOR_NUM":2,"INDEPENTDENT_LEGAL_PERSON":1,"NATIONAL_ECONOMY_INDUSTRY":44,"COMPANY_ATTRIBUTE":"其他","COMPANY_SCALE":"小型","COMPANY_PROFILE":"","COMPANY_CREDIT_RATING":"","IS_ON_LISTED":0,"COMPANY_LISTING_SECTOR":"","LEGAL_PERSON_TEL":13706159105,"FINANCE_CONTACT":"蒋静","FINANCE_TEL":"","FINANCE_MOBEL":"0510-85993951","FINANCE_EMAIL":"","COMPANY_TYPE":"","IS_TECHNOLOGY":1,"REG_ADDRESS":""},
        {"ID":1072,"USER_ID":172,"STATE":50,"THIS_ROLE":"","SYS_ID":4501,"USER_NAME_ABCDEF":"无锡申联专用汽车有限公司","USER_TYPE_ABCDEF":11,"AREA_ID_C_ABCDEF":450102,"AREA_ID_B_ABCDEF":4501,"AREA_ID_A_ABCDEF":45,"AREA_ID_ABCDEF":450102009,"PAPER_TYPE_ABCDEF":"","PAPER_NO_ABCDEF":"91320206132603380D","PAPER_VALIDITY_ABCDEF":"","BANK_OPEN_ABCDEF":"","BANK_ACCOUNT_ABCDEF":"","OPEN_NAME_ABCDEF":"","OPEN_NO_ABCDEF":"","CONTACTS_ABCDEF":"陆芸","FIXED_TEL_ABCDEF":66681359,"MOVE_TEL_ABCDEF":13812188070,"MAIL_ABCDEF":"luyun01@saicmotor.com","FAX_ABCDEF":"","ADDR_ABCDEF":"无锡市惠山区惠际路86号","REGIST_TIME_ABCE":"00:00.0","REGIST_CAPITAL_AC":6640,"WORKERS_NO_AC":142,"DEVELOP_NO_A":24,"IP_NO_AC":"","IP_SYS_NO_AC":"","MAIN_PRODUCT_A":"汽车零部件及配件的研发、制造，机械零部件加工，汽车及汽车零部件、配件、医疗器械的销售，汽车制造的技术咨询、技术服务，空调修理，自营和代理各类商品及技术的进出口业务（国家限定企业经营或禁止进出口的商品和技术除外）。（依法须经批准的项目，经相关部门批准后方可开展经营活动）","MAIN_MARKET_A":"","IS_ISO_A":"","COMPANY_TYPE_A":104,"INDUSTRY_A":"请选择...","NATURE_A":"","PROJ_A":999,"IS_GAUGE":1,"IS_CONTINUE_HIGH":"","LEGAL_PERSON_C":"蓝青松","PROVINCES_RECORD_C":"","IS_HQ_C":"","HQ_USER_NAME_C":"","HQ_ADDR_C":"","HQ_ZIP_CODE_C":"","HQ_REGIST_ADDR_C":"","HQ_LEGAL_PERSON_C":"蓝青松","HQ_NO_C":"","HQ_REGIST_TIME_C":"","HQ_EMPLOYMENT_C":"","HQ_PRACTISING_AGENT_C":"","HQ_CONTACTS_C":"","HQ_TEL_C":"","AGENT_NO_C":"","LAW_NO_C":"","NATIONAL_START_C":"","PROVINCE_START_C":"","REGISTRATION_C":"","REGISTRATION_VALIDITY_C":"","CREATE_TIME":"38:06.4","REMARK":"","SPARE1":"","SPARE2":"","SPARE3":"","IS_DELETE":0,"ISO_CREATE_TIME":"","BUSSINESS_TIME_START":"","BUSSINESS_TIME_END":"","REGISTER_PLACE":"","CHECK_DAY":"","REGISTER_STATUS":1,"TECHNOLOGY_FIELD":"请选择...","INVESTMENT_MONEY":"","DEV_MASTER_NUM":5,"DEV_DOCTOR_NUM":"","INDEPENTDENT_LEGAL_PERSON":1,"NATIONAL_ECONOMY_INDUSTRY":36,"COMPANY_ATTRIBUTE":"","COMPANY_SCALE":"小型","COMPANY_PROFILE":"","COMPANY_CREDIT_RATING":"","IS_ON_LISTED":0,"COMPANY_LISTING_SECTOR":"","LEGAL_PERSON_TEL":18661097799,"FINANCE_CONTACT":"邱文华","FINANCE_TEL":66680152,"FINANCE_MOBEL":13921299955,"FINANCE_EMAIL":"qiuwenhua@saicmotor.com","COMPANY_TYPE":2,"IS_TECHNOLOGY":2,"REG_ADDRESS":"无锡市惠山区惠际路86号"},
        {"ID":1077,"USER_ID":177,"STATE":50,"THIS_ROLE":"","SYS_ID":4501,"USER_NAME_ABCDEF":"无锡新纺欧迪诺电梯有限公司","USER_TYPE_ABCDEF":11,"AREA_ID_C_ABCDEF":450102,"AREA_ID_B_ABCDEF":4501,"AREA_ID_A_ABCDEF":45,"AREA_ID_ABCDEF":450102009,"PAPER_TYPE_ABCDEF":"","PAPER_NO_ABCDEF":913202000000000000,"PAPER_VALIDITY_ABCDEF":"","BANK_OPEN_ABCDEF":"","BANK_ACCOUNT_ABCDEF":"","OPEN_NAME_ABCDEF":"","OPEN_NO_ABCDEF":"","CONTACTS_ABCDEF":"王丹华","FIXED_TEL_ABCDEF":"","MOVE_TEL_ABCDEF":13861811885,"MAIL_ABCDEF":"","FAX_ABCDEF":"","ADDR_ABCDEF":"无锡惠山开发区堰新路580号","REGIST_TIME_ABCE":"00:00.0","REGIST_CAPITAL_AC":12800,"WORKERS_NO_AC":109,"DEVELOP_NO_A":30,"IP_NO_AC":"","IP_SYS_NO_AC":"","MAIN_PRODUCT_A":"电梯","MAIN_MARKET_A":"","IS_ISO_A":"","COMPANY_TYPE_A":"","INDUSTRY_A":"","NATURE_A":"","PROJ_A":"","IS_GAUGE":"","IS_CONTINUE_HIGH":"","LEGAL_PERSON_C":"","PROVINCES_RECORD_C":"","IS_HQ_C":"","HQ_USER_NAME_C":"","HQ_ADDR_C":"","HQ_ZIP_CODE_C":"","HQ_REGIST_ADDR_C":"","HQ_LEGAL_PERSON_C":"","HQ_NO_C":"","HQ_REGIST_TIME_C":"","HQ_EMPLOYMENT_C":"","HQ_PRACTISING_AGENT_C":"","HQ_CONTACTS_C":"","HQ_TEL_C":"","AGENT_NO_C":"","LAW_NO_C":"","NATIONAL_START_C":"","PROVINCE_START_C":"","REGISTRATION_C":"","REGISTRATION_VALIDITY_C":"","CREATE_TIME":"","REMARK":"","SPARE1":"","SPARE2":"","SPARE3":"","IS_DELETE":"","ISO_CREATE_TIME":"","BUSSINESS_TIME_START":"","BUSSINESS_TIME_END":"","REGISTER_PLACE":"","CHECK_DAY":"","REGISTER_STATUS":"","TECHNOLOGY_FIELD":"","INVESTMENT_MONEY":"","DEV_MASTER_NUM":"","DEV_DOCTOR_NUM":"","INDEPENTDENT_LEGAL_PERSON":"","NATIONAL_ECONOMY_INDUSTRY":"","COMPANY_ATTRIBUTE":"","COMPANY_SCALE":"","COMPANY_PROFILE":"","COMPANY_CREDIT_RATING":"","IS_ON_LISTED":"","COMPANY_LISTING_SECTOR":"","LEGAL_PERSON_TEL":"","FINANCE_CONTACT":"","FINANCE_TEL":"","FINANCE_MOBEL":"","FINANCE_EMAIL":"","COMPANY_TYPE":"","IS_TECHNOLOGY":"","REG_ADDRESS":""}
    ]
    return jsonify(clist)


@blueprint.route('/company', methods=['POST'])
def add_company():
    company = {}
    if request.method == 'POST':
        company["USER_NAME_ABCDEF"] = request.form.get("first-name")
        company["middle_name"] = request.form.get("middle-name")
        company["last_name"] = request.form.get("last-name")
        company["gender"] = request.form.get("gender")
        company["birthday"] = request.form.get("birthday")

    current_app.mongoc.db.user_info.insert_one(company)
    return jsonify("success")


@blueprint.route('/companyDB', methods=['GET'])
def get_company_list_from_db():
    conn = current_app.mongoc.db.user_info.find({},{'_id':0})
    cList = []
    for i in conn:
        cList.append(i)
    return jsonify(cList)


@blueprint.route('/course', methods=['GET'])
def get_course_from_db():
    # conn = current_app.mongoc.db.user_info.find({"type": "course"}, {'_id': 0})
    conn = current_app.mongoc.db.user_info.find({"type":"course","chapters.author":"唐国安"},{'_id':0})
    cList = []
    for i in conn:
        cList.append(i)
    return jsonify(cList)


@blueprint.route('/<template>')
def route_template(template):
    return render_template(template + '.html')

