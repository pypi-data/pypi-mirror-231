#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 注册应用命令行支持
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-21 14:06:19
LastEditTime: 2023-09-18 16:12:43
'''

import click
from koca.server import db
from koca.models import *
from koca.utils import random_email, md5


def init_commands(app, config):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='create after drop.')
    def initdb(drop):
        '''
        init database data
        '''
        if drop:
            click.confirm(
                'this operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('drop tables.')
        db.create_all()
        click.echo('initialized database.')

    @app.cli.command()
    @click.option('--username', prompt=True, help='The username used to login.')
    @click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
    def init(username, password):
        '''
        init user info
        '''
        username = username.strip()
        password = password.strip()
        password = md5(password)
        
        db.create_all()
        admin_role = Role.query.filter(Role.role_name == 'admin').first()
        if admin_role is None:
            admin = Role(role_name='admin')
            user = Role(role_name='user')
            db.session.add(admin)
            db.session.add(user)
            admin_role = admin

        if username == 'admin':
            admin = User.query.filter(User.username == username).first()
            if admin is None:
                admin = User(
                    role_id=Role.query.filter(Role.role_name == 'admin').first().role_id,
                    username=username,
                    security_password=password,
                    phone='18990304426',
                    email='ideath@operatorworld.com'
                )
                db.session.add(admin)
            else:
                admin.security_password = password
        else:
            user = User.query.filter(User.username == username).first()
            if user is None:
                user = User(
                    role_id=Role.query.filter(Role.role_name == 'user').first().role_id,
                    username=username,
                    security_password=password,
                    phone='18990304426',
                    email=random_email())
                db.session.add(user)
            else:
                user.security_password = password
        db.session.commit()

    
