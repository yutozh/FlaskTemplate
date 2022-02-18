from common.db.sqlalchemy import db
from datetime import datetime
import abc


class BaseModel(db.Model):
    __abstract__ = True

    is_delete = db.Column(db.Boolean, comment='是否软删除', default=False)
    create_time = db.Column(db.DateTime, comment='创建时间')
    update_time = db.Column(db.DateTime, comment='更新时间')
    top = db.Column(db.Integer, default=1, comment='优先级（越大越靠前）')

    @classmethod
    def page_query(cls, **kwargs):
        """
        分页搜素
        """
        qs = cls.query.filter_by(**kwargs).all()
        count = cls.query.filter_by(**kwargs).count()

    @abc.abstractmethod
    def rollback(self):
        """
        回退
        """
        db.session.rollback()

    @abc.abstractmethod
    def save(self):
        """
        保存
        """
        db.session.add(self)
        db.session.commit()

    @abc.abstractmethod
    def delete(self):
        """
        删除
        """

    @abc.abstractmethod
    def bulk_create(self):
        """
        批量创建
        """

    @abc.abstractmethod
    def bluk_update(self):
        """
        批量更新
        """

    @abc.abstractmethod
    def bluk_delete(self):
        """
        批量删除
        """
