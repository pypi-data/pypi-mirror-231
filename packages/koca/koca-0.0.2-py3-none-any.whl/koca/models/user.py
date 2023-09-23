#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: ewkoll ideath@operatorworld.com
Date: 2023-09-17 23:48:16
LastEditors: ewkoll
LastEditTime: 2023-09-18 16:13:38
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorworld.com, All Rights Reserved.
'''
from koca.models.model_base import BaseTable
from werkzeug.security import generate_password_hash, check_password_hash
from koca.server import db
from koca.utils import db2json
from . import generate_uuid
from datetime import datetime


class User(BaseTable):
    '''
    用户表
    '''
    __tablename__ = 'user'

    role_id = db.Column(db.String(40), db.ForeignKey('role.role_id'))
    username = db.Column(db.String(32), index=True, unique=True, nullable=False, comment='用户账户')
    password = db.Column(db.String(128), nullable=False, comment='用户密码')
    email = db.Column(db.String(32), index=True, unique=True, nullable=False, comment='用户邮箱')
    phone = db.Column(db.String(32), comment='用户手机')
    avatar = db.Column(db.LargeBinary, comment='用户头像')

    @property
    def security_password(self):
        '''
        获取密码信息。
        '''
        return self.password

    @security_password.setter
    def security_password(self, password):
        '''
        存储哈希后的密码。
        '''
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        '''
        验证密码是否正确。
        '''
        return check_password_hash(self.password, password)

    def as_dict(self):
        '''
        转换成常规字典。
        '''
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        '''
        输出表字段。
        '''
        return db2json(self)


class Role(db.Model):
    '''
    角色表
    '''
    __tablename__ = 'role'
    users = db.relationship("User", backref="Role")

    role_id = db.Column(db.String(40), primary_key=True, default=generate_uuid, comment='角色编号')
    role_name = db.Column(db.String(32), index=True, unique=True, nullable=False, comment='角色名称')
    create_time = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment='更新时间')

    def as_dict(self):
        '''
        转换成常规字典。
        '''
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        '''
        输出表字段。
        '''
        return db2json(self)
