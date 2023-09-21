"""
A grid layout widget.
"""
from itertools import accumulate, product
from typing import Literal

from .widget import Size, Widget

__all__ = "GridLayout", "Orientation"

Orientation = Literal[
    "lr-tb",
    "lr-bt",
    "rl-tb",
    "rl-bt",
    "tb-lr",
    "tb-rl",
    "bt-lr",
    "bt-rl",
]
"""
Orientation of the grid.

Describes how the grid fills as children are added. As an example, the orientation
"lr-tb" means left-to-right, then top-to-bottom.
"""


class _RepositionProperty:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)
        instance._reposition_children()


class GridLayout(Widget):
    """
    A widget that automatically positions children into a grid.

    Notes
    -----
    Re-ordering children (such as through :meth:`pull_to_front`) and calling
    :meth:`_reposition_children` will change the positions of the children in the grid.

    The read-only attribute :attr:`minimum_grid_size` is the minimum size the grid must
    be to show all children. This can be used to set the size of the grid layout, e.g.,
    ``my_grid.size = my_grid.minimum_grid_size``.

    Parameters
    ----------
    grid_rows : int, default: 1
        Number of rows.
    grid_columns : int, default: 1
        Number of columns.
    orientation : Orientation, default: "lr-tb"
        The orientation of the grid. Describes how the grid fills as children are added.
        The default is left-to-right then top-to-bottom.
    padding_left : int, default: 0
        Padding on left side of grid.
    padding_right : int, default: 0
        Padding on right side of grid.
    padding_top : int, default: 0
        Padding at the top of grid.
    padding_bottom : int, default: 0
        Padding at the bottom of grid.
    horizontal_spacing : int, default: 0
        Horizontal spacing between children.
    vertical_spacing : int, default: 0
        Vertical spacing between children.
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
    minimum_grid_size : Size
        Minimum grid size needed to show all children.
    grid_rows : int
        Number of rows.
    grid_columns : int
        Number of columns.
    orientation : Orientation
        The orientation of the grid.
    padding_left : int
        Padding on left side of grid.
    padding_right : int
        Padding on right side of grid.
    padding_top : int
        Padding at the top of grid.
    padding_bottom : int
        Padding at the bottom of grid.
    horizontal_spacing : int
        Horizontal spacing between children.
    vertical_spacing : int
        Vertical spacing between children.
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
    index_at:
        Return index of widget in :attr:`children` at position `row, col` in the grid.
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

    Raises
    ------
    ValueError
        If grid is full and :meth:`add_widget` is called.
    """

    grid_rows: int = _RepositionProperty()

    grid_columns: int = _RepositionProperty()

    padding_left: int = _RepositionProperty()

    padding_right: int = _RepositionProperty()

    padding_top: int = _RepositionProperty()

    padding_bottom: int = _RepositionProperty()

    horizontal_spacing: int = _RepositionProperty()

    vertical_spacing: int = _RepositionProperty()

    def __init__(
        self,
        grid_rows: int = 1,
        grid_columns: int = 1,
        *,
        orientation: Orientation = "lr-tb",
        padding_left: int = 0,
        padding_right: int = 0,
        padding_top: int = 0,
        padding_bottom: int = 0,
        horizontal_spacing: int = 0,
        vertical_spacing: int = 0,
        **kwargs,
    ):
        self._grid_rows = grid_rows
        self._grid_columns = grid_columns
        self._orientation = orientation
        self._padding_left = padding_left
        self._padding_right = padding_right
        self._padding_top = padding_top
        self._padding_bottom = padding_bottom
        self._horizontal_spacing = horizontal_spacing
        self._vertical_spacing = vertical_spacing
        self._minimum_grid_size = Size(0, 0)

        super().__init__(**kwargs)

    @property
    def orientation(self) -> Orientation:
        return self._orientation

    @orientation.setter
    def orientation(self, orientation: Orientation):
        if self._orientation not in Orientation.__args__:
            raise TypeError(f"{orientation} is not a valid orientation.")
        self._orientation = orientation
        self._reposition_children()

    def on_size(self):
        self._reposition_children()

    def index_at(self, row: int, col: int) -> int:
        """
        Return the index of the widget in :attr:`children` at a given row and column in
        the grid.
        """
        rows = self.grid_rows
        cols = self.grid_columns

        match self.orientation:
            case "lr-tb":
                return col + row * cols
            case "lr-bt":
                return col + (rows - row - 1) * cols
            case "rl-tb":
                return (cols - col - 1) + row * cols
            case "rl-bt":
                return (cols - col - 1) + (rows - row - 1) * cols
            case "tb-lr":
                return row + col * rows
            case "tb-rl":
                return row + (cols - col - 1) * rows
            case "bt-lr":
                return (rows - row - 1) + col * rows
            case "bt-rl":
                return (rows - row - 1) + (cols - col - 1) * rows

    def _row_height(self, i: int) -> int:
        """
        Height of row `i`.
        """
        return max(
            (
                self.children[index].height
                for col in range(self.grid_columns)
                if (index := self.index_at(i, col)) < len(self.children)
            ),
            default=0,
        )

    def _col_width(self, i: int) -> int:
        """
        Width of column `i`.
        """
        return max(
            (
                self.children[index].width
                for row in range(self.grid_rows)
                if (index := self.index_at(row, i)) < len(self.children)
            ),
            default=0,
        )

    @property
    def minimum_grid_size(self) -> Size:
        """
        Return the minimum grid size to show all children.
        """
        nrows, ncols = self.grid_rows, self.grid_columns
        if nrows == 0 or ncols == 0:
            return Size(0, 0)

        bottom = (
            self.padding_top
            + sum(self._row_height(i) for i in range(nrows))
            + self.vertical_spacing * (nrows - 1)
            + self.padding_bottom
        )
        right = (
            self.padding_left
            + sum(self._col_width(i) for i in range(ncols))
            + self.horizontal_spacing * (ncols - 1)
            + self.padding_right
        )

        return Size(bottom, right)

    def _reposition_children(self):
        if self.grid_rows == 0 or self.grid_columns == 0:
            return

        row_tops = tuple(
            accumulate(
                self.padding_top
                if i == 0
                else self._row_height(i - 1) + self.vertical_spacing
                for i in range(self.grid_rows)
            )
        )
        col_lefts = tuple(
            accumulate(
                self.padding_left
                if i == 0
                else self._col_width(i - 1) + self.horizontal_spacing
                for i in range(self.grid_columns)
            )
        )

        for row, col in product(range(self.grid_rows), range(self.grid_columns)):
            if (i := self.index_at(row, col)) < len(self.children):
                self.children[i].pos = row_tops[row], col_lefts[col]

    def add_widget(self, widget):
        if len(self.children) >= self.grid_rows * self.grid_columns:
            raise ValueError("too many children, grid is full")

        super().add_widget(widget)

        self._reposition_children()

    def remove_widget(self, widget):
        super().remove_widget(widget)
        self._reposition_children()
