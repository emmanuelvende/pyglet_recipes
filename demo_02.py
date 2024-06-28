import pyglet

window = pyglet.window.Window()

x_center = window.width // 2
y_center = window.height // 2
ship_color = (192, 128, 164)


spatial_ship = pyglet.shapes.Triangle(
    x_center,
    y_center,
    x_center - 15,
    y_center - 60,
    x_center + 15,
    y_center - 60,
    color=ship_color,
)


@window.event
def on_draw():
    window.clear()
    spatial_ship.draw()


pyglet.app.run()
