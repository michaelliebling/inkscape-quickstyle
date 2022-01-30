# inkscape-quickstyle
Quickly and consistently adjust line styles of simple inkscape drawings

## Usage

1. Select an Inkscape object or a group of objects (Bézier drawing, rectangle, ellipse, etc.)
2. Open the `Quick Style...` extension panel (if it is not already open)
3. Enter a `Style Code` in the panel's text field (following Gilles Castel's style conventions)
4. Press `Apply` to apply the style to the selected object(s) 

## Introduction

I was in awe after reading Gille Castel's blog post on  
[how \[he\] draw\[s\] figures for \[his\] mathematical lecture notes using Inkscape](https://castel.dev/post/lecture-notes-2/) at lightning speed. As part of his arsenal of tools, he set up an [Inkscape shorcut manager](https://github.com/gillescastel/inkscape-shortcut-manager) through which he manages to adjust styling (line styles, arrows heads, shadings, and more...) just by pressing a few key "chords." This just seems incredibly powerful and infinitely faster than going through Inkscape's intricate styling panels. Since I work on  MacOS and would rather stay away from X11 altogether (with recent releases of Inkscape that no longer need XQuartz, that now seems to become possible). Sadly, the shortcut manager, seems to rely on `Xlib` for keyboard event interception, which puts all the goodness out of reach.

I therefore opted to modify bits and pieces of his manager into a standalone Inkscape Extension (with Python as the only extra requirement).

## Installation 

* Copy the files `default-styles-keys2_small.png`, `quickstyle.inx`, and `quickstyle.py` to
```
 ~/Library/Application\ Support/org.inkscape.Inkscape/config/inkscape/extensions/
```
* Restart inkscape.
