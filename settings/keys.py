# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "space", lazy.layout.next()),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),
    ([mod], "n", lazy.layout.normalize()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    ([mod, "shift"], "Return", lazy.layout.toggle_split()),
    ([mod], "Return", lazy.spawn('alacritty')),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod], "w", lazy.window.kill()),

    ([mod, "control"], "r", lazy.reload_config()),
    #([mod, "control"], "q", lazy.shutdown()),
    #([mod], "r", lazy.spawncmd()),

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # File Manager
    ([mod], "f", lazy.spawn("nautilus")),

    # Spotify
    ([mod], "s", lazy.spawn("spotify")),

    # Chrome
    ([mod], "g", lazy.spawn("google-chrome-stable")),

    # Screenshot
    ([mod], "Print", lazy.spawn(
        "scrot '/home/houdini/Pictures/ArchLinux-%Y-%m-%d-%s_screenshot.png'")),
    ([mod, "shift"], "Print", lazy.spawn(
        "scrot -s '/home/houdini/Pictures/ArchLinux-%Y-%m-%d-%s_screenshot.png'")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    (["control"], "1", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    (["control"], "2", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),

    (["control"], "3", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    # brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # music control
    (
        [], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause")
    ),
    (
        [], "XF86AudioNext",
        lazy.spawn("playerctl next")
    ),
    (
        [], "XF86AudioPrev",
        lazy.spawn("playerctl previous")
    ),

    ([mod, "shift"], "8", lazy.spawn("playerctl play-pause")),

    ([mod, "shift"], "9", lazy.spawn("playerctl previous")),

    ([mod, "shift"], "0", lazy.spawn("playerctl next")),


]]
