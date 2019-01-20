<!-- attrib title: map() - PICO-8 Wiki -->
<!-- attrib description: Draws a portion of the map to the graphics buffer. -->
<!-- attrib template: default -->
## `map(celx, cely, sx, sy, celw, celh, [layer])` ##
Draws a portion of the map to the graphics buffer.

### Arguments ###
 - `celx` - The column location of the map cell in the upper left corner of the region to draw, where 0 is the leftmost column.
 - `cely` - The row location of the map cell in the upper left corner of the region to draw, where 0 is the topmost row.
 - `sx` - The x coordinate of the screen to place the upper left corner.
 - `sy` - The y coordinate of the screen to place the upper left corner.
 - `celw` - The number of map cells wide in the region to draw.
 - `celh` - The number of map cells tall in the region to draw.
 - `layer` - If specified, only draw sprites that have flags set for every bit in this value (a bitfield). The default is 0 (draw all sprites).

Note: `mapdraw()` is the original name for this function, and may still be found in older carts. Its use is deprecated.

### Usage ###

The map is a grid of sprites from the sprite sheet, where each cell in the grid is assigned a sprite number. You can edit the map using the Pico-8 map editor. You call the `map()` function to draw a region of the map (a subsection of the grid cells) onto the screen.

You can use the map to draw large pictures by reusing sprite tiles in multiple cells. This is more memory efficient than drawing large images in pixels with the sprite editor, and easier to use than storing tables of sprite numbers in code.

Any map cell set to sprite number 0 is not drawn, effectively making that cell transparent. You can use this along with using the transparent color for pixels in sprites to make regions of transparency in the image. A common technique is to layer multiple maps on top of one another, then animate the positions of these layers to produce effects such as parallax scrolling.

Another use for maps is to design interactive levels or areas of a game world. When doing this, it is often necessary to determine which sprite is at a given location on the map, such as to determine whether a location next to the player is an obstruction. See [[`mget()`]].
