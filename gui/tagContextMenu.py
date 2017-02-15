from PyQt5 import QtWidgets


class TagContextMenu(QtWidgets.QMenu):
    def __init__(self, parent=None, title=""):
        super(TagContextMenu, self).__init__(parent)

        self.menuItemList = []

    def addTagToContextMenu(self, _name):
        listEntry = (_name, self.addAction(_name))
        self.menuItemList.append(listEntry)

    def updateTagItem(self, _old_name, _new_name):
        for i, entry in enumerate(self.menuItemList):
            if entry[0] == _old_name:
                entry[1].setText(_new_name)
                self.menuItemList[i] = (_new_name, entry[1])

    def removeTagItem(self, _name):
        for i, entry in enumerate(self.menuItemList):
            if entry[0] == _name:
                self.removeAction(entry[1])
                del self.menuItemList[i]
                return

    def getMenuItemList(self):
        return self.menuItemList


class Tag():
    def __init__(self, _name, _type, _icon):
        self.name = _name
        self.type = _type
        self.icon = _icon