#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: ewkoll ideath@operatorworld.com
Date: 2023-09-17 23:50:12
LastEditors: ewkoll
LastEditTime: 2023-09-17 23:52:20
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorworld.com, All Rights Reserved.
"""
from koca.server import db
from . import generate_uuid
from koca.utils import db2json
from datetime import datetime


class BaseTable(db.Model):
    __tablename__ = "abstract_table"
    __abstract__ = True
    __table_args__ = (db.PrimaryKeyConstraint("data_id"),)

    data_id = db.Column(
        db.String(40), primary_key=True, default=generate_uuid, comment="主键编号"
    )
    create_time = db.Column(db.DateTime, default=datetime.utcnow, comment="创建时间")
    update_time = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间"
    )

    def as_dict(self):
        """
        转换成常规字典。
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        """
        输出表字段。
        """
        return db2json(self)
