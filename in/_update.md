<!-- attrib title: _update() - PICO-8 Wiki -->
<!-- attrib description: Called every frame, intended for game logic -->
<!-- attrib template: default -->
## `_update()` ##

The first part of a game loop is normally an update. In PICO-8, this is done with either an `_update()` function, for 30fps games, or `_update60()` for 60fps games.

If a cartridge's source code includes both an `_update()` function and a [[`_draw()`]] function, then Pico-8 will attempt to call these functions once for each animation frame, at a rate of 30 frames per second for `_update()` or 60 frames per second with with `_update60()`.

You define this function in your game's source code. It takes no arguments.

The intended purpose of `_update()` is to test for user inputs (button presses), perform all of the calculations to advance the state of the game, and update the game's data structures with the results. For example, you might compare the state of variables to see if the player's avatar is near an item during `_update()`. Typically, this function does not update the display, though it may initiate sound effects (`sfx()`) and music (`music()`).

See the entry on the game loop.
