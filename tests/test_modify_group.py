import words as words

from model.group import Group
from random import randrange
import random


def test_modify_group(app,db,check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="dsererererer", header="ererer", footer="footer"))
    def clean(group):
        return Group(id = group.id, name = group.name.strip())
    old_groups = db.get_group_list()
    group_index = random.choice(range(len(old_groups)))
    id = old_groups[group_index].id
    group_to_modify = Group(name='Изменённое имя', id=id)
    app.group.modify_group_by_id(id, group_to_modify)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[group_index] = group_to_modify
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(clean,new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


"""def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="dsererererer", header="ererer", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="Изменнный хэдер"))
    app.group.modify_first_group(Group(name="Изменнное имя"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)"""