"""
A textbox widget for single-line editable text.
"""
from collections.abc import Callable

import numpy as np
from numpy.typing import NDArray
from wcwidth import wcswidth

from ..io import Key, KeyEvent, Mods, MouseButton, MouseEvent, PasteEvent
from .behaviors.focusable import Focusable
from .behaviors.grabbable import Grabbable
from .behaviors.themable import Themable
from .text_widget import TextWidget, style_char
from .widget import Char, Rect, Widget, intersection

WORD_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_")


class Textbox(Themable, Focusable, Grabbable, Widget):
    """
    A textbox widget for single-line editable text.

    Supports pasting, mouse selection, and cursor navigation.

    Parameters
    ----------
    enter_callback : Callable[[Textbox], None] | None, default: None
        If provided, called when textbox has focus and `enter` is pressed.
        The widget will be passed as first argument to the callback.
    placeholder : str, default: ""
        Placeholder text for textbox.
    hide_input : bool, default: False
        If true, input is hidden with :attr:`hide_char`.
    hide_char : str, default: "*"
        Character to hide input when :attr:`hide_input` is true.
    max_chars : int | None, default: None
        Maximum allowed number of characters in textbox.
    is_grabbable : bool, default: True
        If false, grabbable behavior is disabled.
    disable_ptf : bool, default: False
        If true, widget will not be pulled to front when grabbed.
    mouse_button : MouseButton, default: MouseButton.LEFT
        Mouse button used for grabbing.
    size : Size, default: Size(10, 10)
        Size of widget.
    pos : Point, default: Point(0, 0)
        Position of upper-left corner in parent.
    size_hint : SizeHint, default: SizeHint(None, None)
        Proportion of parent's height and width. Non-None values will have
        precedent over :attr:`size`.
    min_height : int | None, default: None
        Minimum height set due to size_hint. Ignored if corresponding size
        hint is None.
    max_height : int | None, default: None
        Maximum height set due to size_hint. Ignored if corresponding size
        hint is None.
    min_width : int | None, default: None
        Minimum width set due to size_hint. Ignored if corresponding size
        hint is None.
    max_width : int | None, default: None
        Maximum width set due to size_hint. Ignored if corresponding size
        hint is None.
    pos_hint : PosHint, default: PosHint(None, None)
        Position as a proportion of parent's height and width. Non-None values
        will have precedent over :attr:`pos`.
    anchor : Anchor, default: "center"
        The point of the widget attached to :attr:`pos_hint`.
    is_transparent : bool, default: False
        If true, background_char and background_color_pair won't be painted.
    is_visible : bool, default: True
        If false, widget won't be painted, but still dispatched.
    is_enabled : bool, default: True
        If false, widget won't be painted or dispatched.
    background_char : str | None, default: None
        The background character of the widget if not `None` and if the widget
        is not transparent.
    background_color_pair : ColorPair | None, default: None
        The background color pair of the widget if not `None` and if the
        widget is not transparent.

    Attributes
    ----------
    text : str
        The textbox's text.
    placeholder : str
        Placeholder text for textbox.
    hide_input : bool
        If true, input is hidden with :attr:`hide_char`.
    hide_char : str
        Character to hide input when :attr:`hide_input` is true.
    max_chars : int | None
        Maximum allowed number of characters in textbox.
    is_focused : bool
        Return true if widget has focus.
    any_focused : bool
        Return true if any widget has focus.
    is_grabbable : bool
        If false, grabbable behavior is disabled.
    disable_ptf : bool
        If true, widget will not be pulled to front when grabbed.
    mouse_button : MouseButton
        Mouse button used for grabbing.
    is_grabbed : bool
        True if widget is grabbed.
    mouse_dyx : Point
        Last change in mouse position.
    mouse_dy : int
        Last vertical change in mouse position.
    mouse_dx : int
        Last horizontal change in mouse position.
    size : Size
        Size of widget.
    height : int
        Height of widget.
    rows : int
        Alias for :attr:`height`.
    width : int
        Width of widget.
    columns : int
        Alias for :attr:`width`.
    pos : Point
        Position relative to parent.
    top : int
        Y-coordinate of position.
    y : int
        Y-coordinate of position.
    left : int
        X-coordinate of position.
    x : int
        X-coordinate of position.
    bottom : int
        :attr:`top` + :attr:`height`.
    right : int
        :attr:`left` + :attr:`width`.
    absolute_pos : Point
        Absolute position on screen.
    center : Point
        Center of widget in local coordinates.
    size_hint : SizeHint
        Size as a proportion of parent's size.
    height_hint : float | None
        Height as a proportion of parent's height.
    width_hint : float | None
        Width as a proportion of parent's width.
    min_height : int
        Minimum height allowed when using :attr:`size_hint`.
    max_height : int
        Maximum height allowed when using :attr:`size_hint`.
    min_width : int
        Minimum width allowed when using :attr:`size_hint`.
    max_width : int
        Maximum width allowed when using :attr:`size_hint`.
    pos_hint : PosHint
        Position as a proportion of parent's size.
    y_hint : float | None
        Vertical position as a proportion of parent's size.
    x_hint : float | None
        Horizontal position as a proportion of parent's size.
    anchor : Anchor
        Determines which point is attached to :attr:`pos_hint`.
    background_char : str | None
        Background character.
    background_color_pair : ColorPair | None
        Background color pair.
    parent : Widget | None
        Parent widget.
    children : list[Widget]
        Children widgets.
    is_transparent : bool
        True if widget is transparent.
    is_visible : bool
        True if widget is visible.
    is_enabled : bool
        True if widget is enabled.
    root : Widget | None
        If widget is in widget tree, return the root widget.
    app : App
        The running app.

    Methods
    -------
    focus:
        Focus widget.
    blur:
        Un-focus widget.
    focus_next:
        Focus next focusable widget.
    focus_previous:
        Focus previous focusable widget.
    on_focus:
        Called when widget is focused.
    on_blur:
        Called when widget loses focus.
    update_theme:
        Paint the widget with current theme.
    grab:
        Grab the widget.
    ungrab:
        Ungrab the widget.
    grab_update:
        Update widget with incoming mouse events while grabbed.
    on_size:
        Called when widget is resized.
    apply_hints:
        Apply size and pos hints.
    to_local:
        Convert point in absolute coordinates to local coordinates.
    collides_point:
        True if point is within widget's bounding box.
    collides_widget:
        True if other is within widget's bounding box.
    add_widget:
        Add a child widget.
    add_widgets:
        Add multiple child widgets.
    remove_widget:
        Remove a child widget.
    pull_to_front:
        Move to end of widget stack so widget is drawn last.
    walk_from_root:
        Yield all descendents of root widget.
    walk:
        Yield all descendents (or ancestors if `reverse` is True).
    subscribe:
        Subscribe to a widget property.
    unsubscribe:
        Unsubscribe to a widget property.
    on_key:
        Handle key press event.
    on_mouse:
        Handle mouse event.
    on_paste:
        Handle paste event.
    tween:
        Sequentially update a widget property over time.
    on_add:
        Called after a widget is added to widget tree.
    on_remove:
        Called before widget is removed from widget tree.
    prolicide:
        Recursively remove all children.
    destroy:
        Destroy this widget and all descendents.
    """

    def __init__(
        self,
        *,
        enter_callback: Callable[["Textbox"], None] | None = None,
        placeholder: str = "",
        hide_input: bool = False,
        hide_char: str = "*",
        max_chars: int | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self._prev_cursor_x = 0
        self._selection_start = self._selection_end = None
        self._line_length = 0

        self._placeholder_widget = TextWidget()
        self._placeholder_widget.set_text(placeholder)
        self._cursor = TextWidget(size=(1, 1), is_enabled=False)
        self._box = TextWidget(size=self._placeholder_widget.size)
        self._box.add_widgets(self._placeholder_widget, self._cursor)

        self.add_widgets(self._box)

        self.enter_callback = enter_callback
        self.placeholder = placeholder
        self.hide_input = hide_input
        self.hide_char = hide_char
        self.max_chars = max_chars

    @property
    def placeholder(self) -> str:
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder: str):
        self._placeholder = placeholder
        self._placeholder_widget.set_text(placeholder)
        self._placeholder_widget.colors[:] = self.color_theme.textbox_placeholder
        if self._line_length == 0 and placeholder:
            self._placeholder_widget.is_enabled = True
            self._cursor.canvas[0, 0] = self._placeholder_widget.canvas[0, 0]
        else:
            self._placeholder_widget.is_enabled = False

    @property
    def text(self) -> str:
        return "".join(self._box.canvas["char"][0, : self._line_length])

    @text.setter
    def text(self, text: str):
        text = text.replace("\n", " ")
        self._line_length = wcswidth(text)

        box = self._box
        box.canvas[:] = style_char(" ")
        box.width = max(self._line_length + 1, self.width)
        box.add_str(text)
        if self._line_length == 0 and self._placeholder:
            self._placeholder_widget.is_enabled = True
        self.cursor = self._line_length

    @property
    def cursor(self) -> int:
        return self._cursor.x

    @cursor.setter
    def cursor(self, cursor: int):
        """
        After setting cursor position, move textbox so that cursor is visible.
        """
        self._prev_cursor_x = self._cursor.x
        self._cursor.x = cursor
        if self._line_length == 0 and self._placeholder:
            self._placeholder_widget.is_enabled = True
            self._cursor.canvas[0, 0] = self._placeholder_widget.canvas[0, 0]
        else:
            self._placeholder_widget.is_enabled = False
            self._cursor.canvas[0, 0] = self._box.canvas[0, cursor]

        max_x = self.width - 1
        if (rel_x := cursor + self._box.x) > max_x:
            self._box.x += max_x - rel_x
        elif rel_x < 0:
            self._box.x -= rel_x

        self._update_selection()

    @property
    def has_selection(self) -> bool:
        return self._selection_start is not None and self._selection_end is not None

    def update_theme(self):
        primary = self.color_theme.textbox_primary

        self.background_color_pair = primary
        self._placeholder_widget.colors[:] = self.color_theme.textbox_placeholder
        self._box.colors[:] = primary
        self._box.default_color_pair = primary
        self._cursor.colors[:] = primary.reversed()

        self._highlight_selection()

    def on_size(self):
        self._input_hider.size = self.size

        if self.width > self._box.width:
            self._box.width = self.width
        elif self.width < self._box.width:
            self._box.width = max(self.width, self._line_length + 1)
        self._highlight_selection()

    def on_focus(self):
        self._cursor.is_enabled = True

    def on_blur(self):
        self._cursor.is_enabled = False

    def render(
        self,
        canvas_view: NDArray[Char],
        colors_view: NDArray[np.uint8],
        source: tuple[slice, slice],
    ):
        """
        Paint region given by source into canvas_view and colors_view.
        """
        super().render(canvas_view, colors_view, source)

        if self.hide_input and not self._placeholder_widget.is_enabled:
            vert, hori = source
            srctop = vert.start
            srcbot = vert.stop
            srcleft = hori.start
            srcright = hori.stop

            intersect = intersection(
                Rect(0, 1, 0, min(self._line_length + self._box.left, self.width)),
                Rect(srctop, srcbot, srcleft, srcright),
            )
            if intersect is not None:
                src, _ = intersect
                canvas_view[src] = style_char(self.hide_char)

    def select(self):
        if not self.has_selection:
            self._selection_start = self._selection_end = self.cursor

    def unselect(self):
        self._selection_start = self._selection_end = None

    def delete_selection(self):
        if not self.has_selection:
            return

        box = self._box

        start = self._selection_start
        end = self._selection_end

        len_end = self._line_length - end
        new_len = self._line_length = start + len_end

        box.canvas[0, start:new_len] = box.canvas[0, end : end + len_end]
        box.canvas[0, new_len:] = style_char(box.default_char)

        self.unselect()
        self.cursor = start

    def _highlight_selection(self):
        colors = self._box.colors
        colors[:] = self._box.default_color_pair

        if self._selection_start != self._selection_end:
            start = self._selection_start
            end = self._selection_end

            colors[0, start:end] = self.color_theme.textbox_selection_highlight

    def _update_selection(self):
        if self.has_selection:
            if self._prev_cursor_x == self._selection_start:
                self._selection_start = self.cursor
            elif self._prev_cursor_x == self._selection_end:
                self._selection_end = self.cursor

            if self._selection_start > self._selection_end:
                self._selection_start, self._selection_end = (
                    self._selection_end,
                    self._selection_start,
                )

        self._highlight_selection()

    def move_cursor_left(self, n: int = 1):
        text_before_cursor = "".join(self._box.canvas["char"][0, : self.cursor])
        nchars_before_cursor = len(text_before_cursor)
        if n <= nchars_before_cursor:
            self.cursor = wcswidth(text_before_cursor[:-n])
        else:
            self.cursor = 0

    def move_cursor_right(self, n: int = 1):
        text_after_cursor = "".join(
            self._box.canvas["char"][0, self.cursor : self._line_length]
        )
        nchars_after_cursor = len(text_after_cursor)
        if n <= nchars_after_cursor:
            self.cursor += wcswidth(text_after_cursor[:n])
        else:
            self.cursor = self._line_length

    def move_word_left(self):
        last_x = self.cursor
        first_char_found = False
        while True:
            self.move_cursor_left()
            if self.cursor == last_x:
                break

            last_x = self.cursor

            current_char = self._box.canvas[0, self.cursor]["char"]
            if not first_char_found:
                if not current_char.isspace():
                    first_char_found = True
                    is_word_char = current_char in WORD_CHARS
            elif current_char.isspace() or is_word_char != (current_char in WORD_CHARS):
                self.move_cursor_right()
                break

    def move_word_right(self):
        last_x = self.cursor
        first_char_found = False
        while True:
            self.move_cursor_right()
            if self.cursor == last_x:
                break

            last_x = self.cursor

            current_char = self._box.canvas[0, self.cursor]["char"]
            if not first_char_found:
                if not current_char.isspace():
                    first_char_found = True
                    is_word_char = current_char in WORD_CHARS
            elif current_char.isspace() or is_word_char != (current_char in WORD_CHARS):
                break

    def _enter(self):
        if self.enter_callback is not None:
            self.enter_callback(self)

    def _backspace(self):
        if not self.has_selection:
            self.select()
            self.move_cursor_left()
        self.delete_selection()

    def _delete(self):
        if not self.has_selection:
            self.select()
            self.move_cursor_right()
        self.delete_selection()

    def _left(self):
        if self.has_selection:
            select_start = self._selection_start
            self.unselect()
            self.cursor = select_start
        else:
            self.move_cursor_left()

    def _right(self):
        if self.has_selection:
            select_end = self._selection_end
            self.unselect()
            self.cursor = select_end
        else:
            self.move_cursor_right()

    def _ctrl_left(self):
        self.unselect()
        self.move_word_left()

    def _ctrl_right(self):
        self.unselect()
        self.move_word_right()

    def _home(self):
        self.unselect()
        self.cursor = 0

    def _end(self):
        self.unselect()
        self.cursor = self._line_length

    def _shift_left(self):
        self.select()
        self.move_cursor_left()

    def _shift_right(self):
        self.select()
        self.move_cursor_right()

    def _shift_ctrl_left(self):
        self.select()
        self.move_word_left()

    def _shift_ctrl_right(self):
        self.select()
        self.move_word_right()

    def _shift_home(self):
        self.select()
        self.cursor = 0

    def _shift_end(self):
        self.select()
        self.cursor = self._line_length

    def _escape(self):
        if self.has_selection:
            self.unselect()
            self._highlight_selection()
        else:
            self.blur()

    def _ascii(self, key):
        self.delete_selection()

        if self._line_length == self.max_chars:
            return

        x = self.cursor
        box = self._box

        self._line_length += 1
        if self._line_length >= box.width:
            box.width = self._line_length + 1

        box.canvas[0, x + 1 :] = box.canvas[0, x:-1]
        box.canvas[0, x] = style_char(key)

        self.cursor = x + 1

    __HANDLERS = {
        (Key.Enter, Mods.NO_MODS): _enter,
        (Key.Backspace, Mods.NO_MODS): _backspace,
        (Key.Delete, Mods.NO_MODS): _delete,
        (Key.Left, Mods.NO_MODS): _left,
        (Key.Right, Mods.NO_MODS): _right,
        (Key.Left, Mods(False, True, False)): _ctrl_left,
        (Key.Right, Mods(False, True, False)): _ctrl_right,
        (Key.Home, Mods.NO_MODS): _home,
        (Key.End, Mods.NO_MODS): _end,
        (Key.Left, Mods(False, False, True)): _shift_left,
        (Key.Right, Mods(False, False, True)): _shift_right,
        (Key.Left, Mods(False, True, True)): _shift_ctrl_left,
        (Key.Right, Mods(False, True, True)): _shift_ctrl_right,
        (Key.Home, Mods(False, False, True)): _shift_home,
        (Key.End, Mods(False, False, True)): _shift_end,
        (Key.Escape, Mods.NO_MODS): _escape,
    }

    def on_key(self, key_event: KeyEvent) -> bool | None:
        if not self.is_focused:
            return

        if key_event.mods == Mods.NO_MODS and len(key_event.key) == 1:
            self._ascii(key_event.key)
        elif handler := self.__HANDLERS.get(key_event):
            handler(self)
        else:
            return super().on_key(key_event)

        return True

    def on_paste(self, paste_event: PasteEvent) -> bool | None:
        if not self.is_focused:
            return

        self.delete_selection()

        x = self.cursor
        box = self._box
        paste = paste_event.paste.replace("\n", " ")
        width_paste = wcswidth(paste)

        input_text = (
            "".join(box.canvas["char"][0, :x])
            + paste
            + "".join(box.canvas["char"][0, x : self._line_length])
        )[: self.max_chars]

        len_input = wcswidth(input_text)

        if len_input >= box.width:
            box.width = len_input + 1

        box.add_str(input_text)
        box.canvas[0, len_input:] = style_char(box.default_char)

        self._line_length = len_input
        self.cursor = min(len_input, x + width_paste)

        return True

    def grab(self, mouse_event):
        if mouse_event.button is MouseButton.LEFT and self._box.collides_point(
            mouse_event.position
        ):
            super().grab(mouse_event)

            _, x = self._box.to_local(mouse_event.position)

            if not mouse_event.mods.shift:
                self.unselect()

            self.cursor = min(x, self._line_length)
            self.select()  # Need at least an empty selection for `grab_update`.

    def grab_update(self, mouse_event: MouseEvent):
        if self._box.collides_point(mouse_event.position):
            _, x = self._box.to_local(mouse_event.position)
            self.cursor = min(x, self._line_length)
        else:
            _, x = self.to_local(mouse_event.position)

            if x < 0:
                self.move_cursor_left()
            elif x >= self.width:
                self.move_cursor_right()

    def ungrab(self, mouse_event):
        super().ungrab(mouse_event)
        if self._selection_start == self._selection_end:
            self.unselect()
