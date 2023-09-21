"""
A slider widget.
"""
from collections.abc import Callable

from ..clamp import clamp
from ..colors import Color, ColorPair
from ..io import MouseEvent, MouseEventType
from .behaviors.grabbable import Grabbable
from .text_widget import TextWidget
from .widget import subscribable


class Slider(Grabbable, TextWidget):
    """
    A slider widget.

    Parameters
    ----------
    min : float
        Minimum value of slider.
    max : float
        Maximum value of slider.
    start_value: float | None, default: None
        Start value of slider. If `None`, start value is :attr:`min`.
    callback : Callable | None, default: None
        Single argument callable called with new value of slider when slider is updated.
    handle_color_pair : ColorPair | None, default: None
        Color pair of slider handle. If None, handle color pair is
        :attr:`default_color_pair`.
    handle_char : str, default: "█"
        Character used for slider handle.
    fill_color: Color | None, default: None
        Color of "filled" portion of slider.
    fill_char: str, default: "▬"
        Character used for slider.
    slider_enabled : bool, default: True
        Whether slider value can be changed.
    default_char : str, default: " "
        Default background character. This should be a single unicode half-width
        grapheme.
    default_color_pair : ColorPair, default: WHITE_ON_BLACK
        Default color of widget.
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
        If true, background color and whitespace in text widget won't be painted.
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
    min : float
        Minimum value of slider.
    max : float
        Maximum value of slider.
    value : float
        Current value of slider.
    callback : Callable
        Single argument callable called with new value of slider when slider is updated.
    handle_color_pair : ColorPair
        Color pair of slider handle.
    handle_char : str
        Character used for slider handle.
    fill_color : Color
        Color of "filled" portion of slider.
    fill_char : str
        Character used for slider.
    slider_enabled : bool
        True if slider value can be changed.
    proportion : float
        Current proportion of slider.
    canvas : NDArray[Char]
        The array of characters for the widget.
    colors : NDArray[np.uint8]
        The array of color pairs for each character in `canvas`.
    default_char : str
        Default background character.
    default_color_pair : ColorPair
        Default color pair of widget.
    default_fg_color : Color
        The default foreground color.
    default_bg_color : Color
        The default background color.
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
    add_border:
        Add a border to the widget.
    normalize_canvas:
        Ensure column width of text in the canvas is equal to widget width.
    add_str:
        Add a single line of text to the canvas.
    set_text:
        Resize widget to fit text, erase canvas, then fill canvas with text.
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
        Yield all descendents (or ancestors if `reverse` is true).
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
        min: float,
        max: float,
        start_value: float | None = None,
        callback: Callable | None = None,
        handle_color_pair: ColorPair | None = None,
        handle_char: str = "█",
        fill_color: Color | None = None,
        fill_char: str = "▬",
        slider_enabled: bool = True,
        **kwargs,
    ):
        super().__init__(**kwargs)

        if min >= max:
            raise ValueError(f"{min=} >= {max=}")
        self._min = min
        self._max = max

        self._handle = TextWidget(size=(1, 1), pos_hint=(0.5, None))
        self.add_widget(self._handle)
        self.handle_color_pair = handle_color_pair or self.default_color_pair
        self.handle_char = handle_char

        self.fill_color = fill_color or self.default_fg_color
        self.fill_char = fill_char

        self.callback = callback

        self.slider_enabled = True
        self.value = self.min if start_value is None else start_value
        self.slider_enabled = slider_enabled

    @property
    def min(self) -> float:
        return self._min

    @min.setter
    def min(self, value: float):
        if value >= self.max:
            raise ValueError("Min can't be greater than or equal to max.")

        self._min = value
        self.proportion = self.proportion

    @property
    def max(self) -> float:
        return self._max

    @max.setter
    def max(self, value: float):
        if value <= self.min:
            raise ValueError("Max can't be less than or equal to min.")

        self._max = value
        self.proportion = self.proportion

    @property
    def handle_color_pair(self) -> ColorPair:
        return self._handle_color_pair

    @handle_color_pair.setter
    def handle_color_pair(self, color_pair: ColorPair):
        self._handle_color_pair = color_pair
        self._handle.colors[:] = color_pair

    @property
    def handle_char(self) -> str:
        return self._handle_char

    @handle_char.setter
    def handle_char(self, char: str):
        self._handle_char = char
        self._handle.canvas["char"][:] = char

    @property
    def fill_color(self) -> Color:
        return self._fill_color

    @fill_color.setter
    def fill_color(self, color: Color):
        self._fill_color = color
        self.colors[self.height // 2, :, :3] = color

    @property
    def fill_char(self) -> str:
        return self._fill_char

    @fill_char.setter
    def fill_char(self, char: str):
        self._fill_char = char
        self.canvas["char"][self.height // 2] = char

    def on_size(self):
        super().on_size()
        self.canvas["char"][:] = self.default_char
        self.canvas["char"][self.height // 2] = self.fill_char
        self.colors[:] = self.default_color_pair
        self.proportion = self.proportion

    @property
    def proportion(self) -> float:
        return self._proportion

    @proportion.setter
    @subscribable
    def proportion(self, value: float):
        if not self.slider_enabled:
            return

        self._proportion = clamp(value, 0, 1)
        self._value = (self.max - self.min) * self._proportion + self.min

        self._handle.x = x = round(self._proportion * self.fill_width)
        y = self.height // 2
        self.colors[y, :x, :3] = self.fill_color
        self.colors[y, x:, :3] = self.default_fg_color

        if self.callback is not None:
            self.callback(self._value)

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    @subscribable
    def value(self, value: float):
        value = clamp(value, self.min, self.max)
        self.proportion = (value - self.min) / (self.max - self.min)

    @property
    def fill_width(self):
        """
        Width of the slider minus the width of the handle.
        """
        return self.width - self._handle.width

    def grab(self, mouse_event: MouseEvent):
        if (
            mouse_event.event_type == MouseEventType.MOUSE_DOWN
            and self.collides_point(mouse_event.position)
            and self.to_local(mouse_event.position).y == self.height // 2
        ):
            super().grab(mouse_event)
            self.grab_update(mouse_event)

    def grab_update(self, mouse_event: MouseEvent):
        x = clamp(self.to_local(mouse_event.position).x, 0, self.width - 1)
        self._handle.x = x
        self.proportion = 0 if self.fill_width == 0 else x / self.fill_width
