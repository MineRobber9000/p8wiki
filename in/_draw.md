<!-- attrib title: _draw() - PICO-8 Wiki -->
<!-- attrib description: Called every frame, intended for drawing to the screen -->
<!-- attrib template: default -->
## `_draw()` ##

The `_draw()` function is the second part of the game loop.

If a cartridge's source code includes both an [[`_update()`]] function and a `_draw()` function, then Pico-8 will attempt to call these functions once for each animation frame, at a rate of 30 frames per second (60 if [[`_update60()`]] is used.)

You define this function in your game's source code. It takes no arguments.

The intended purpose of `_draw()` is to draw the state of the game onto the screen, such as with calls to `map()` and `spr()`. A typical `_draw()` function starts with a call to `cls()` to clear the screen then draws all of the game elements, but this is not required.

If `_update()` and `_draw()` together take longer than 1/30th of a second (or 1/60th with `_update60()`) to complete, Pico-8 may decide not to call `_draw()` for a given frame. See the entry on the game loop.
