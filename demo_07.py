import pyglet

window = pyglet.window.Window()
keystatehandler = pyglet.window.key.KeyStateHandler()
window.push_handlers(keystatehandler)

x_center = window.width // 2
y_center = window.height // 2
ship_color = (192, 128, 164)
MAX_SPEED = 20  #  pixels per second

x1, y1 = x_center, y_center + 5
x2, y2 = (x1 - 10, y1 - 30)
x3, y3 = (x1 + 10, y1 - 30)

b = pyglet.graphics.Batch()

spatial_ship = pyglet.shapes.Polygon(
    (x1, y1), (x2, y2), (x3, y3), color=ship_color, batch=b
)

spatial_ship.anchor_y = -15
spatial_ship.position = (x_center, y_center)
spatial_ship.speed = 0

position_label = pyglet.text.Label(x=25, y=50, batch=b)
rotation_label = pyglet.text.Label(x=25, y=70, batch=b)


def move_ship(dt):
    # print(dt)
    pos_old = spatial_ship.position
    v_speed = pyglet.math.Vec2(spatial_ship.speed, 0).rotate(spatial_ship.rotation)
    pos_new = pos_old[0] + v_speed.x * dt, pos_old[1] + v_speed.y * dt
    spatial_ship.position = pos_new


fps_display = pyglet.window.FPSDisplay(window=window)


@window.event
def on_draw():
    window.clear()
    b.draw()
    fps_display.draw()
    # display_telemetry()


def manage_keypress(dt):
    if keystatehandler[pyglet.window.key.LEFT]:
        spatial_ship.rotation -= 1
    if keystatehandler[pyglet.window.key.RIGHT]:
        spatial_ship.rotation += 1
    if keystatehandler[pyglet.window.key.A]:
        spatial_ship.speed += 1
        if spatial_ship.speed > MAX_SPEED:
            spatial_ship.speed = MAX_SPEED
    if keystatehandler[pyglet.window.key.Q]:
        spatial_ship.speed -= 1
        if spatial_ship.speed < 0:
            spatial_ship.speed = 0


def refresh_telemetry(dt):
    position_label.text = f"{spatial_ship.position=}"
    rotation_label.text = f"{spatial_ship.rotation=}°"


for func in (move_ship, manage_keypress, refresh_telemetry):
    pyglet.clock.schedule_interval(func, 1 / 60.0)

# pyglet.clock.schedule_interval(move_ship, 1 / 60.0)
# pyglet.clock.schedule_interval(manage_keypress, 1 / 60.0)

pyglet.app.run()
