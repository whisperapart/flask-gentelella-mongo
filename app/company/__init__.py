#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
@File:      __init__.py.py
@Author:    Jim.Dai.Cn
@Date:      2020/9/22 上午11:26
@Desc:         
"""

from flask import Blueprint

blueprint = Blueprint(
    'abc_blueprint',
    __name__,
    url_prefix='/company',
    template_folder='templates',
    static_folder='static'
)