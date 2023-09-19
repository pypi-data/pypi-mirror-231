# -*- coding: utf-8 -*-
import functools
import logging

from dataclasses import dataclass, field
from typing import List

from PIL import Image

from vindauga.types.display import Display
from vindauga.types.draw_buffer import DrawBuffer
from vindauga.types.rect import Rect
from vindauga.types.screen import Screen
from vindauga.utilities.colours.colours import colourFindRGB, colour_256to16, getColorMap
from vindauga.widgets.desktop import Desktop

logger = logging.getLogger(__name__)


@dataclass
class BitMap:
    pattern: int
    charOrd: int
    char: str


BLOCK = BitMap(0x0000ffff, 0x2584, '▄')  # lower 1/2


@dataclass
class Color:
    r: int = 0
    g: int = 0
    b: int = 0

    def __floordiv__(self, other):
        r = self.r // other
        g = self.g // other
        b = self.b // other
        return Color(r, g, b)

    def __ifloordiv__(self, other):
        self.r //= other
        self.g //= other
        self.b //= other
        return self

    def __add__(self, other):
        r = self.r + other[0]
        g = self.g + other[1]
        b = self.b + other[2]
        return Color(r, g, b)

    def __iadd__(self, other):
        self.r += other[0]
        self.g += other[1]
        self.b += other[2]
        return self

    def __iter__(self):
        yield from (self.r, self.g, self.b)


@dataclass
class CharData:
    fgColor: Color = field(default_factory=Color)
    bgColor: Color = field(default_factory=Color)
    char: str = '▄'


@dataclass
class Size:
    width: int
    height: int

    def scaled(self, scale):
        return Size(int(self.width * scale), int(self.height * scale))

    def fittedWithin(self, container):
        scale = min(container.width / self.width, container.height / self.height)
        return self.scaled(scale)


@functools.lru_cache(1)
def init_16_col_palette() -> List[Color]:
    from .colours.xterm_colors import palette
    p = []
    for bg in range(8):
        c = palette[bg]
        r = c['rgb']['r']
        g = c['rgb']['g']
        b = c['rgb']['b']
        color = Color(r, g, b)
        for fg in range(16):
            c = palette[fg]
            r = c['rgb']['r']
            g = c['rgb']['g']
            b = c['rgb']['b']
            p.append((color + (r, g, b)) // 2)
    return p


def c_dist(c1, c2):
    return (c1.r - c2.r) ** 2 + (c1.g - c2.g) ** 2 + (c1.b - c2.b) ** 2


@functools.lru_cache(127)
def nearest_color(r, g, b) -> int:
    min_dist = 0x30000
    origin = Color(r, g, b)
    closest = None
    for i, c in enumerate(init_16_col_palette()):
        if (dist := c_dist(c, origin)) < min_dist:
            if dist == 0:
                return i
            closest = i
            min_dist = dist
    return closest


def openFile(filename):
    im = Image.open(filename)
    im.draft("RGB", im.size)
    return im


def getBitmapCharData(bitmap: BitMap, input_image, x0: int, y0: int):
    result = CharData()
    result.char = bitmap.char

    fgCount = 0
    bgCount = 0
    mask = 0x80000000

    for y in range(y0, y0 + 8):
        for x in range(x0, x0 + 4):
            if bitmap.pattern & mask:
                avg = result.fgColor
                fgCount += 1
            else:
                avg = result.bgColor
                bgCount += 1

            avg += input_image[x, y]
            mask >>= 1

    if bgCount:
        result.bgColor //= bgCount

    if fgCount:
        result.fgColor //= fgCount
    return result


def emitImage256(image):
    w, h = image.size
    pixels = image.load()
    lines = []
    for y in range(0, h - 8, 8):
        buffer = DrawBuffer(True)
        for i, x in enumerate(range(0, w - 4, 4)):
            charData = getBitmapCharData(BLOCK, pixels, x, y)
            bg = colourFindRGB(charData.bgColor.r, charData.bgColor.g, charData.bgColor.b)
            fg = colourFindRGB(charData.fgColor.r, charData.fgColor.g, charData.fgColor.b)
            pair = (fg * 256 + bg)
            buffer.putChar(i, charData.char)
            buffer.putAttribute(i, pair)
        lines.append(buffer)
    return lines


def emitImage16(image):
    w, h = image.size
    colorMap = getColorMap()
    pixels = image.load()
    lines = []
    for y in range(0, h - 8, 8):
        buffer = DrawBuffer(True)
        buffer.moveChar(0, Desktop.DEFAULT_BACKGROUND, 0, 256)
        for i, x in enumerate(range(0, w - 4, 4)):
            charData = getBitmapCharData(BLOCK, pixels, x, y)
            c = (Color(*charData.fgColor) + list(charData.bgColor)) // 2
            pair = nearest_color(*list(c))

            # bg = colour_256to16(colourFindRGB(charData.bgColor.r, charData.bgColor.g, charData.bgColor.b))
            # fg = colour_256to16(colourFindRGB(charData.fgColor.r, charData.fgColor.g, charData.fgColor.b))
            # pair = ((15 - fg) << 4) | (bg & 0x7)
            buffer.moveChar(i, charData.char, pair, 1)
            buffer.putChar(i, charData.char)
            buffer.putAttribute(i, pair << 8)
        lines.append(buffer)
    return lines


def wallpaper(filename, bounds: Rect):
    maxWidth = bounds.width * 4
    maxHeight = bounds.height * 8

    img = openFile(filename).convert('RGB')
    iw, ih = img.size
    size = Size(iw, ih)
    if iw > maxWidth or ih > maxHeight:
        size = size.fittedWithin(Size(maxWidth, maxHeight))
        img = img.resize((size.width, size.height))
    if Screen.screen.screenMode != Display.smCO256:
        return size.width // 4, size.height // 8, emitImage16(img)
    return size.width // 4, size.height // 8, emitImage256(img)
