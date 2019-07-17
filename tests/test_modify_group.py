from model.group import Group
from random import randrange
import random

def test_modify_group_name(app,db,check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="dsererererer", header="ererer", footer="footer"))
    def clean(group):
        return Group(id = group.id, name = group.name.strip())
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id,Group(name="Изменнное 2") )
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    #old_groups(тут как-то обратиться  кэл-ту списка не зная его индекса и заменить содержимое на новое содердимое группы)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

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