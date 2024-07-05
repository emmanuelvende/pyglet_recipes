import pyglet

window = pyglet.window.Window()
keystatehandler = pyglet.window.key.KeyStateHandler()
window.push_handlers(keystatehandler)

x_center = window.width // 2
y_center = window.height // 2
ship_color = (192, 128, 164)


x, y = x_center, y_center
x2, y2 = (
    x_center - 10,
    y_center - 30,
)
x3, y3 = (
    x_center + 10,
    y_center - 30,
)


class SpatialShip(pyglet.shapes.Triangle):

    def __init__(self, x, y, x2, y2, x3, y3, *args, **kwargs):
        super().__init__(x, y, x2, y2, x3, y3, *args, **kwargs)
        self.anchor_y = -15

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        self._rotation = rotation
        self._vertex_list.rotation[:] = (rotation,) * self._num_verts


spatial_ship = SpatialShip(
    x,
    y,
    x2,
    y2,
    x3,
    y3,
    color=ship_color,
)


@window.event
def on_draw():
    window.clear()

    if keystatehandler[pyglet.window.key.LEFT]:
        spatial_ship.rotation -= 1
    if keystatehandler[pyglet.window.key.RIGHT]:
        spatial_ship.rotation += 1

    spatial_ship.draw()


pyglet.app.run()
