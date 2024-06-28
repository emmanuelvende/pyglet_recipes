import pyglet

window = pyglet.window.Window()
keystatehandler = pyglet.window.key.KeyStateHandler()
window.push_handlers(keystatehandler)

x_center = window.width // 2
y_center = window.height // 2
ship_color = (192, 128, 164)


spatial_ship = pyglet.shapes.Rectangle(
    x_center,
    y_center,
    width=30,
    height=90,
    color=ship_color,
)


@window.event
def on_draw():
    window.clear()

    if keystatehandler[pyglet.window.key.LEFT]:
        spatial_ship.rotation -= 1
    if keystatehandler[pyglet.window.key.RIGHT]:
        spatial_ship.rotation += 1
    # if key_is_down:
    #     if key == pyglet.window.key.LEFT:
    #         spatial_ship.rotation -= 1
    #     if key == pyglet.window.key.RIGHT:
    #         spatial_ship.rotation += 1

    spatial_ship.draw()


# @window.event
# def on_key_press(symbol, modifiers):
#     key = symbol


# @window.event
# def on_key_release(symbol, modifiers):
#     key_is_down = False


pyglet.app.run()
