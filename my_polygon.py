import pyglet

window = pyglet.window.Window()
keystatehandler = pyglet.window.key.KeyStateHandler()
window.push_handlers(keystatehandler)


class Side(pyglet.shapes.Line):

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        self._rotation = rotation
        self._vertex_list.rotation[:] = (rotation,) * self._num_verts


b = pyglet.graphics.Batch()

x_center = window.width // 2
y_center = window.height // 2
ship_color = (192, 164, 88)


x1, y1 = x_center, y_center + 5
x2, y2 = (x1 - 10, y1 - 30)
x3, y3 = (x1 + 10, y1 - 30)


class MyLine(pyglet.shapes.Line):

    def __init__(self, x, y, x2, y2, width=1, color=..., batch=None, group=None):
        super().__init__(x, y, x2, y2, width, color, batch, group)

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        self._rotation = rotation
        self._vertex_list.rotation[:] = (rotation,) * self._num_verts


side1 = MyLine(x1, y1, x2, y2, color=ship_color, batch=b)
side2 = MyLine(x1, y1, x3, y3, color=ship_color, batch=b)
side3 = MyLine(x2, y2, x3, y3, color=ship_color, batch=b)

sides = (side1, side2, side3)


@window.event
def on_draw():
    window.clear()
    b.draw()


def manage_keypress(dt):
    if keystatehandler[pyglet.window.key.LEFT]:
        for s in sides:
            s.rotation -= 1
    if keystatehandler[pyglet.window.key.RIGHT]:
        for s in sides:
            s.rotation += 1


pyglet.clock.schedule_interval(manage_keypress, 1 / 60.0)
pyglet.app.run()
