import pyglet

window = pyglet.window.Window()
keystatehandler = pyglet.window.key.KeyStateHandler()
window.push_handlers(keystatehandler)

x_center = window.width // 2
y_center = window.height // 2
ship_color = (192, 128, 164)


x1, y1 = x_center, y_center + 5
x2, y2 = (x1 - 10, y1 - 30)
x3, y3 = (x1 + 10, y1 - 30)


spatial_ship = pyglet.shapes.Polygon(
    (x1, y1),
    (x2, y2),
    (x3, y3),
    color=ship_color,
)

spatial_ship.anchor_y = -15
spatial_ship.position = (x_center, y_center)


def move_ship(dt):
    # print(dt)
    pos_old = spatial_ship.position
    pos_new = pos_old[0], pos_old[1] + 10 * dt
    spatial_ship.position = pos_new
    # print(spatial_ship.position)
    # print(spatial_ship.anchor_position)

fps_display = pyglet.window.FPSDisplay(window=window)

@window.event
def on_draw():
    window.clear()
    fps_display.draw()

    if keystatehandler[pyglet.window.key.LEFT]:
        spatial_ship.rotation -= 1
    if keystatehandler[pyglet.window.key.RIGHT]:
        spatial_ship.rotation += 1

    spatial_ship.draw()


pyglet.clock.schedule_interval(move_ship, 1 / 60.0)

pyglet.app.run()
