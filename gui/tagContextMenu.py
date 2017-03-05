from PyQt5 import QtWidgets, QtCore


class TagContextMenu(QtWidgets.QMenu):
    def __init__(self, parent=None, title=""):
        super(TagContextMenu, self).__init__(parent)

        # add default action
        self.defaultActionHandle = self.addAction("(No tags)")
        self.defaultActionHandle.setEnabled(False)
        self.tag_action_tuples = []

    def addTagToContextMenu(self, tag):
        self.tag_action_tuples.append((tag, self.addAction(tag.type + ", " + tag.subtype)))
        if len(self.actions()) > 1:
            self.defaultActionHandle.setVisible(False)

    def updateTagItem(self, tag):
        for i, _data in enumerate(self.tag_action_tuples):
            _tag, _action = _data
            if _tag is tag:
                _action.setText(tag.type + ", " + tag.subtype)
                self.tag_action_tuples.pop(i)
                self.tag_action_tuples.append((tag, _action))

    def removeTagItem(self, tag):
        for _tag, _action in self.tag_action_tuples:
            if _tag == tag:
                self.tag_action_tuples.remove((_tag, _action))
                self.removeAction(_action)

        if len(self.actions()) == 1:
            self.defaultActionHandle.setVisible(True)


