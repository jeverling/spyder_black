# -*- coding: utf-8 -*-
""":author: Joseph Martinot-Lagarde, Jesaja Everling."""

# Standard library imports
from __future__ import absolute_import, division, print_function, unicode_literals

from qtpy.QtGui import QTextCursor
from spyder.config.base import get_translation
from spyder.config.gui import fixed_shortcut
from spyder.plugins import SpyderPluginMixin
from spyder.utils import icon_manager as ima
from spyder.utils.qthelpers import create_action

# Third party imports
ERR_MSG = ""
try:
    import black
except ImportError:
    ERR_MSG = "Please install black."


try:
    from spyder.py3compat import to_text_string
except ImportError:
    # Python 2
    to_text_string = unicode  # noqa


_ = get_translation("black", dirname="spyder_black")


class Black(SpyderPluginMixin):  # pylint: disable=R0904
    """Python source code automatic formatting based on black.

    QObject is needed to register the action.
    """

    CONF_SECTION = "spyder.autopep8"

    # --- SpyderPlugin API ----------------------------------------------------
    def get_plugin_title(self):
        """Return widget title."""
        return _("black")

    def get_plugin_icon(self):
        """Return widget icon."""
        return ima.icon(self.CONF_SECTION)

    def register_plugin(self):
        """Register plugin in Spyder's main window."""
        black_act = create_action(
            self.main,
            _("Run black code autoformatting"),
            icon=self.get_plugin_icon(),
            triggered=self.run_black,
        )
        fixed_shortcut("Shift+F8", self.main, self.run_black)
        self.main.source_menu_actions += [None, black_act]
        self.main.editor.pythonfile_dependent_actions += [black_act]

    def apply_plugin_settings(self, options):
        """Needs to be redefined."""
        pass

    def closing_plugin(self, cancelable=False):
        """Perform actions before parent main window is closed."""
        return True

    # --- Public API ---------------------------------------------------------
    def run_black(self):
        """Format code with black."""
        if ERR_MSG:
            self.main.statusBar().showMessage(_("Unable to run: {0}".format(ERR_MSG)))
            return

        # Retrieve text of current opened file
        editorstack = self.main.editor.get_current_editorstack()
        index = editorstack.get_stack_index()
        finfo = editorstack.data[index]
        editor = finfo.editor
        cursor = editor.textCursor()
        cursor.beginEditBlock()  # Start cancel block
        position_start = 0
        cursor.select(QTextCursor.Document)  # Select all

        # replace(): See qt doc for QTextCursor.selectedText()
        text_before = to_text_string(cursor.selectedText().replace("\u2029", "\n"))

        # Run black
        text_after = black.format_str(text_before, line_length=88)

        # Apply new text if needed
        if text_before != text_after:
            cursor.insertText(text_after)  # Change text

        cursor.endEditBlock()  # End cancel block

        # Select changed text
        position_end = cursor.position()
        cursor.setPosition(position_start, QTextCursor.MoveAnchor)
        cursor.setPosition(position_end, QTextCursor.KeepAnchor)
        editor.setTextCursor(cursor)

        self.main.statusBar().showMessage(_("black finished !"))
