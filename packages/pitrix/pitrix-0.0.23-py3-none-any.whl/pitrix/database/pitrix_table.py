#!/usr/bin/python3
# -*- coding: utf-8 -*-

import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, REAL, Text, create_engine, Integer

from pitrix.constants.constants import DataBase


Base = declarative_base()


class Api(Base):
    """
    流量表
    """

    __tablename__ = DataBase.API_TABLE

    id = Column(Integer, autoincrement=True, primary_key=True)
    start_time = Column(Text())
    host = Column(Text())
    url = Column(Text())
    method = Column(Text())
    headers = Column(Text())
    body = Column(Text())
    response = Column(Text())
    duration = Column(REAL())
    status_code = Column(Integer())

    def __repr__(self) -> str:
        return f"<api(id={self.id}," \
               f"start_time={self.start_time}," \
               f"host={self.host}," \
               f"url={self.url}," \
               f"method={self.method}," \
               f"headers={self.headers}," \
               f"body={self.body}," \
               f"response={self.response}," \
               f"duration={self.duration}," \
               f"status_code={self.status_code})>"


class Config(Base):
    """
    配置表
    """

    __tablename__ = DataBase.CONFIG_TABLE

    key = Column(Text(), primary_key=True)
    value = Column(Text())

    def __repr__(self) -> str:
        return f"<config(key={self.key}," \
               f"value={self.value})>"


class Cache(Base):
    """
    缓存表
    """

    __tablename__ = DataBase.CACHE_TABLE

    var_name = Column(Text(), primary_key=True)
    response = Column(Text())
    worker = Column(Text())
    api_info = Column(Text())

    def __repr__(self) -> str:
        return f"<cache(var_name={self.var_name}," \
               f"response={self.response}," \
               f"worker={self.worker}," \
               f"api_info={self.api_info})>"


class Schema(Base):
    """
    Schema表
    """

    __tablename__ = DataBase.SCHEMA_TABLE

    api_name = Column(Text(), primary_key=True)
    schema = Column(Text())

    def __repr__(self) -> str:
        return f"<cache(api_name={self.var_name}," \
               f"schema={self.response})>"


class SqliteSqlalchemy:
    """
    eg:
    session = SqliteSqlalchemy('./database/pitrix.db').session
    schema = Schema(api_name='TYW',schema='TEST')
    session.add(schema)
    session.commit()
    """

    def __init__(self, pitrix_db_path):
        engine = create_engine(f"sqlite:///{pitrix_db_path}", echo=True)
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()


def create_tables(pitrix_db_path):
    """
    创建数据表
    @return:
    """
    try:
        engine = create_engine(f"sqlite:///{pitrix_db_path}")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)
        click.echo(f"创建数据库:{pitrix_db_path} 完成")
    except Exception as e:
        click.echo(f"创建数据库:{pitrix_db_path} 失败，str{e}")