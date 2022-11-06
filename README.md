# Usage

```
■ ./ats.py -h
usage: ats.py [-h] [--theme-path theme-path] [--conf-file conf-file] theme

Switch `alacritty` color theme

positional arguments:
  theme                 <theme name>

options:
  -h, --help            show this help message and exit
  --theme-path theme-path
                        Path to where themes are stored
  --conf-file conf-file
                        Path to `alacritty` configuration file
```

## Examples

```
# To load color theme in file `pencil-dark.yml` from
#  the default theme directory `~/.config/alacritty/themes/`,
#  use the following command.
■ ./ats.py pencil-dark

# You can also organize themes in sub-directories, and
#  load them as follows.
■ ./ats.py dark2tone/drawbridge-dark

```
