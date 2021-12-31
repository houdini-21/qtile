from libqtile import widget
from .theme import colors
from libqtile.widget.battery import Battery, BatteryState
from libqtile.widget.volume import Volume
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
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
            font='FiraCode Nerd Font Medium',
            fontsize=20,
            margin_y=5,
            margin_x=0,
            padding_y=8,
            padding_x=6,
            borderwidth=1,
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
            char = ''
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
    fontsize=14,
    padding=5,
)


class MyVolume(Volume):
    def _update_drawer(self):
        if self.volume <= 0:
            self.volume = 'M'
            self.text = '婢 ' + str(self.volume)
        elif self.volume < 30:
            self.text = ' ' + str(self.volume) + '%'
        elif self.volume < 80:
            self.text = ' ' + str(self.volume) + '%'
        else:  # self.volume >=80:
            self.text = ' ' + str(self.volume) + '%'

    def restore(self):
        self.timer_setup()


volume = MyVolume(
    background=colors["dark"],
    fontsize=13,
    padding=5,
)

primary_widgets = [
    *workspaces(),

    separator(),


    powerline('color2', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color4', 'color2'),

    icon(bg="color4", text=' '),  # Icon: nf-fa-download

    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
        padding=5,
    ),


    powerline('color1', 'color4'),

    icon(bg="color1", fontsize=17, text=' '),  # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color1'),
    volume,
    widget.Systray(background=colors['dark'], padding=5),
    battery,
    widget.QuickExit(background=colors['dark'], default_text="⏻",
                     padding=7, countdown_format="{}"),  # Icon: nf-fa-power_off
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'FiraCode Nerd Font Medium',
    'fontsize': 13,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
