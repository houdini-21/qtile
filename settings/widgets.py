from libqtile import widget
from .theme import colors
from libqtile.widget.battery import Battery, BatteryState
from libqtile.widget.volume import Volume
from os import path
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)


home = path.expanduser('~')      # Allow using 'home +' to expand ~


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator(linewidth=0, padding=5):
    return widget.Sep(**base(), linewidth=linewidth, padding=padding)


def icon(fg='text', bg='dark', fontsize=16, text="?", padding=3):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=padding
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",  # Icon: nf-oct-triangle_left
        fontsize=36,
        padding=-5
    )


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='FiraCode Nerd Font Regular',
            fontsize=16,
            margin_y=4,
            margin_x=0,
            padding_y=5,
            padding_x=6,
            borderwidth=4,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=13,
                          padding=5, max_chars=21),
        separator(),
    ]


class MyBattery(Battery):
    def build_string(self, status):
        if status.state == BatteryState.DISCHARGING:
            if status.percent >= 1:
                char = ''
            elif status.percent > 0.90:
                char = ''
            elif status.percent > 0.80:
                char = ''
            elif status.percent > 0.70:
                char = ''
            elif status.percent > 0.60:
                char = ''
            elif status.percent > 0.50:
                char = ''
            elif status.percent > 0.40:
                char = ''
            elif status.percent > 0.30:
                char = ''
            elif status.percent > 0.20:
                char = ''
            else:
                char = ''
        elif status.percent >= 1 or status.state == BatteryState.FULL:
            char = ''
        elif status.state == BatteryState.CHARGING:
            if status.percent > 0.90:
                char = ''
            elif status.percent > 0.80:
                char = ''
            elif status.percent > 0.70:
                char = ''
            elif status.percent > 0.60:
                char = ''
            elif status.percent > 0.50:
                char = ''
            elif status.percent > 0.40:
                char = ''
            elif status.percent > 0.30:
                char = ''
            elif status.percent > 0.20:
                char = ''
            else:
                char = ''
        else:  # status.state == BatteryState.EMPTY or \
            # (status.state == BatteryState.UNKNOWN and status.percent == 0):
            char = ''
        return self.format.format(char=char, percent=status.percent)

    def restore(self):
        self.format = '{char}{percent:2.0%}'
        self.timer_setup()


battery = MyBattery(
    format='{char}',
    background=colors['dark'],
    foreground=colors['color3'],
    fontsize=14,
    padding=5,
)


class MyVolume(Volume):
    def _update_drawer(self):
        if self.volume <= 0:
            self.volume = 'M'
            self.text = str(self.volume)
        elif self.volume < 30:
            self.text = str(self.volume) + '%'
        elif self.volume < 80:
            self.text = str(self.volume) + '%'
        else:  # self.volume >=80:
            self.text = str(self.volume) + '%'

    def restore(self):
        self.timer_setup()


volume = MyVolume(
    foreground=colors['color2'],
    background=colors["dark"],
    fontsize=12,
    padding=5
)

primary_widgets = [
    *workspaces(),

    widget.TextBox(width=350, **base(bg='dark')),
    widget.Clock(**base(bg='dark'), format='%b %d %Y %H:%M'),
    widget.TextBox(width=350, **base(bg='dark')),

    widget.CurrentLayoutIcon(
        custom_icon_paths=[(home + "/.config/qtile/icons")],
        scale=0.65,
        background=colors['dark'],
    ),
    # widget.CurrentLayout(**base(bg='dark')),
    separator(0, 9),
    # Icon: nf-fa-microchip
    #icon(fg="color4", bg="dark", fontsize=17, text='', padding=9),
    #widget.CPU(**base(fg="color4", bg='dark'), format='{freq_current}GHz'),
    #separator(0, 11),
    icon(fg="focus", bg="dark", fontsize=17, text='﬙', padding=2),
    widget.Memory(**base(fg="focus", bg='dark'), format='{MemUsed: .0f}MB'),
    
    #widget.Systray(background=colors['dark']),
    separator(0, 9),

    #
    icon(fg="color2", bg="dark", fontsize=15, text='', padding=5),
    volume,
    separator(0, 9),
    battery,
    separator(0, 9),
    # Icon: nf-fa-power_off
    widget.QuickExit(**base(fg='color1', bg="dark"),
                     default_text="⏻", countdown_format="{}", padding=9),
    separator(0, 11),

]

secondary_widgets = [
    *workspaces(),

    widget.TextBox(width=600, **base(bg='dark')),
    widget.Clock(**base(bg='dark'), format='%b %d %Y %H:%M'),
    widget.TextBox(width=600, **base(bg='dark')),

    widget.CurrentLayoutIcon(
        custom_icon_paths=[(home + "/.config/qtile/icons")],
        scale=0.65,
        background=colors['dark'],
    ),
    # widget.CurrentLayout(**base(bg='dark')),
    separator(0, 9),
    # Icon: nf-fa-microchip
    #icon(fg="color4", bg="dark", fontsize=17, text='', padding=9),
    #widget.CPU(**base(fg="color4", bg='dark'), format='{freq_current}GHz'),
    #separator(0, 11),
    icon(fg="focus", bg="dark", fontsize=17, text='﬙', padding=2),
    widget.Memory(**base(fg="focus", bg='dark'), format='{MemUsed: .0f}MB'),
    
    #widget.Systray(background=colors['dark']),
    separator(0, 9),

    #
    icon(fg="color2", bg="dark", fontsize=15, text='', padding=5),
    volume,
    separator(0, 9),
    battery,
    separator(0, 9),
    # Icon: nf-fa-power_off
    widget.QuickExit(**base(fg='color1', bg="dark"),
                     default_text="⏻", countdown_format="{}", padding=9),
    separator(0, 11),
]

widget_defaults = {
    'font': 'FiraCode Nerd Font SemiBold',
    'fontsize': 13,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
