import math
import pyglet

window = pyglet.window.Window()
keystatehandler = pyglet.window.key.KeyStateHandler()
window.push_handlers(keystatehandler)

x_center = window.width // 2
y_center = window.height // 2


class LabelledDot(pyglet.shapes.Circle):

    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._label = pyglet.text.Label(
            text=f"{text} ({self.x}, {self.y})",
            x=self.x + 15,
            y=self.y + 15,
            color=self.color,
            batch=self._batch,
        )


batch = pyglet.graphics.Batch()

x_a, y_a = x_center - 200, y_center - 200
x_b, y_b = x_center + 200, y_center - 200
x_c, y_c = x_center - 200, y_center + 200
x_d, y_d = x_center + 200, y_center + 200

RED = 255, 0, 0, 255
GREEN = 0, 255, 0, 255
BLUE = 0, 0, 255, 255
YELLOW = 255, 255, 0, 255

dot_a = LabelledDot("A", x_a, y_a, radius=2, color=RED, batch=batch)
dot_b = LabelledDot("B", x_b, y_b, radius=2, color=GREEN, batch=batch)
dot_c = LabelledDot("C", x_c, y_c, radius=2, color=BLUE, batch=batch)
dot_d = LabelledDot("D", x_d, y_d, radius=2, color=YELLOW, batch=batch)

SHIP_COLOR = (192, 128, 164)
MAX_SPEED = 500  #  pixels per second

x1, y1 = x_center + 15, y_center
x2, y2 = x_center - 15, y_center - 10
x3, y3 = x_center - 15, y_center + 10


spatial_ship = pyglet.shapes.Polygon(
    (x1, y1), (x2, y2), (x3, y3), color=SHIP_COLOR, batch=batch
)

print(spatial_ship.anchor_position)

spatial_ship.anchor_x = -15
spatial_ship.position = (x_center, y_center)
spatial_ship.speed = 0

position_label = pyglet.text.Label(x=25, y=65, batch=batch)
rotation_label = pyglet.text.Label(x=25, y=50, batch=batch)
speed_label = pyglet.text.Label(x=25, y=35, batch=batch)


def deg2rad(d):
    return (-d) * math.pi / 180


def move_ship(dt):
    # print(dt)
    pos_old = spatial_ship.position
    v_speed = pyglet.math.Vec2(spatial_ship.speed, 0).rotate(
        deg2rad(spatial_ship.rotation)
    )
    pos_new = pos_old[0] + v_speed.x * dt, pos_old[1] + v_speed.y * dt
    spatial_ship.position = pos_new


fps_display = pyglet.window.FPSDisplay(window=window)


@window.event
def on_draw():
    window.clear()
    batch.draw()
    fps_display.draw()


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
    x, y = spatial_ship.position
    position_label.text = f"position = ({x:0.1f}px, {y:0.1f}px) "
    rotation_label.text = f"rotation = {spatial_ship.rotation:0.1f}°"
    speed_label.text = f"speed = {spatial_ship.speed}"


for func in (move_ship, manage_keypress, refresh_telemetry):
    pyglet.clock.schedule_interval(func, 1 / 60.0)


pyglet.app.run()
