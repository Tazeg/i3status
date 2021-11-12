# i3 status bar

This is a sample code to help you to build your personal i3 bar.

![i3status](i3status.jpg)

It comes with :

- public IP address
- local IP address
- crypto-currencies
- VPN on/off (sample with ProtonVPN)
- disk usage
- memory usage
- CPU usage
- date and time
- weather
- volume information
- battery information
- log out

Please read [Create your own i3/sway status bar with some bash and python](https://en.jeffprod.com/blog/2020/create-your-own-i3-sway-status-bar/).

## Install

In your `~/.config/i3/config` file, add the path to the script `mybar.sh` :

```bash
bar {
  status_command exec /home/you/.config/i3status/mybar.sh
}
```

Replace `/home/you` in this project with your home path.

Copy the files from this `i3status` repository directory to `~/.config/i3status`.

⚠️ Please, read and modify each script !

- it is given as an example. You may not have ProtonVPN. You need to set you city for the weather informations...
- Replace `/home/you/` with your home path in the `mybar.sh` file.
- if you get errors, try to run each bash and python script separately.

Restart i3 : `MOD4+SHIFT+R`.

You may also need to install, i.e. for Arch Linux :

```bash
yay -S pamixer # for volume information
yay -S pacman-contrib # for checkupdates, to count available packages
yay -S ttf-font-awesome # for icons
yay -S alsa-utils # for alsamixer (sound volume)
pip3 install psutil --user # for cpu, memory, disk usage
```

## Documentation

- <https://i3wm.org/docs/i3bar-protocol.html>
- <https://i3wm.org/i3status/manpage.html>
- <https://github.com/i3/i3status/tree/master/contrib>
- <https://fontawesome.com/cheatsheet?from=io>
