# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="dsererererer", header="ererer", footer="footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))