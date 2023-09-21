"""
Focus behavior for a widget.
"""
from collections import deque
from weakref import ReferenceType, WeakSet, ref

from ...io import Key, MouseEventType


class Focusable:
    """
    Focus behavior for a widget.

    Focusable widgets can be given "focus" by pressing tab or shift + tab
    or by clicking on them. When a widget is focused, all focusable ancestors
    also gain focus.

    Attributes
    ----------
    is_focused : bool
        True if widget has focus.
    any_focused : bool
        True if any widget has focus.

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
    """

    __focus_widgets: deque[ReferenceType] = deque()
    __focused = WeakSet()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_add(self):
        super().on_add()
        Focusable.__focus_widgets.append(ref(self))
        self.focus()

    def on_remove(self):
        self.blur()
        Focusable.__focus_widgets.remove(ref(self))
        super().on_remove()

    @property
    def is_focused(self) -> bool:
        """
        True if widget has focus.
        """
        return self in Focusable.__focused

    @property
    def any_focused(self) -> bool:
        """
        True if any widget has focus.
        """
        return bool(Focusable.__focused)

    def focus(self):
        """
        Focus widget.
        """
        if not self.is_enabled:
            return

        ancestors = WeakSet(
            ancestor
            for ancestor in self.walk(reverse=True)
            if isinstance(ancestor, Focusable)
        )
        ancestors.add(self)

        focused = Focusable.__focused
        Focusable.__focused = ancestors

        for blurred in focused - ancestors:
            blurred.on_blur()

        for needs_focus in ancestors - focused:
            needs_focus.on_focus()

        focus_widgets = Focusable.__focus_widgets
        while (widget := focus_widgets[0]()) is not self:
            if widget is None:
                focus_widgets.popleft()
            else:
                focus_widgets.rotate(-1)

    def blur(self):
        """
        Un-focus widget.
        """
        if self.is_focused:
            for ancestor in self.walk(reverse=True):
                if isinstance(ancestor, Focusable):
                    ancestor.focus()
                    return

            Focusable.__focused.remove(self)
            self.on_blur()

    def focus_next(self):
        """
        Focus next focusable widget.
        """
        focus_widgets = Focusable.__focus_widgets

        if self.any_focused:
            focus_widgets.rotate(-1)

        for _ in range(len(focus_widgets)):
            widget = focus_widgets[0]()
            if widget is None:
                focus_widgets.popleft()
            elif not widget.is_visible or not widget.is_enabled:
                focus_widgets.rotate(-1)
            else:
                widget.focus()
                return

    def focus_previous(self):
        """
        Focus previous focusable widget.
        """
        focus_widgets = Focusable.__focus_widgets

        if self.any_focused:
            focus_widgets.rotate(1)

        for _ in range(len(focus_widgets)):
            widget = focus_widgets[0]()
            if widget is None:
                focus_widgets.popleft()
            elif not widget.is_visible or not widget.is_enabled:
                focus_widgets.rotate(1)
            else:
                widget.focus()
                return

    def on_key(self, key_event):
        if super().on_key(key_event):
            return True

        if key_event.key is Key.Tab:
            if key_event.mods.shift:
                self.focus_previous()
            else:
                self.focus_next()
            return True

        return False

    def dispatch_mouse(self, mouse_event):
        handled = super().dispatch_mouse(mouse_event)
        if handled and not self.is_focused and self.is_visible:
            self.focus()
        return handled

    def on_mouse(self, mouse_event):
        if mouse_event.event_type is MouseEventType.MOUSE_DOWN and self.is_visible:
            collides = self.collides_point(mouse_event.position)
            if not self.is_focused and collides:
                self.focus()
            elif self.is_focused and not collides:
                self.blur()

        return super().on_mouse(mouse_event)

    def on_focus(self):
        """
        Called when widget gains focus.
        """

    def on_blur(self):
        """
        Called when widget loses focus.
        """
