#!/usr/bin/env python
# -*- mode: python; coding: utf-8; fill-column: 80; -*-
"""Switches alacritty color themes.
"""

import argparse
import io
import os
import sys
import yaml

try:
    from yaml import CLoader as YLoader, CDumper as YDumper
except ImportError:
    from yaml import Loader as YLoader, Dumper as YDumper


def load_color_theme(theme, theme_path):
    """Load color theme from file."""
    theme_name = theme + ".yml"
    theme_file = os.path.sep.join((theme_path, theme_name))

    try:
        with io.open(theme_file, 'r', encoding='utf-8') as f:
            theme_data = yaml.load(f, Loader=YLoader)
    except FileNotFoundError:
        raise ValueError(f"Unable to find `{theme_file}`!")

    if 'colors' not in theme_data:
        raise ValueError('Unable to find color definitions in theme file!')
    return theme_data['colors']


def load_config(conf_file):
    """Load `alacritty` configuration file."""
    try:
        with io.open(conf_file, 'r', encoding='utf-8') as f:
            conf_data = yaml.load(f, Loader=YLoader)
    except FileNotFoundError:
        raise ValueError(f"Unable to find `{conf_file}`!")

    if not conf_data:
        raise ValueError(f"No configuration data in `{conf_file}`!")

    if 'colors' not in conf_data:
        sys.stderr.write("Warn: No colors set in configuration!\n")
        conf_data['colors'] = None

    return conf_data


def switch_theme(conf, theme):
    """Switch color theme in configuration."""
    conf['colors'] = theme


def write_config(conf, conf_file):
    """Persist configuration to file."""
    with io.open(conf_file, 'w', encoding='utf-8') as f:
        f.write(yaml.dump(conf, Dumper=YDumper))


def expand_path(p):
    """Convert paths to absolute values."""
    return os.path.expanduser(p)


def main (args):
    args.theme_path = os.path.expanduser(args.theme_path)
    args.conf_file = os.path.expanduser(args.conf_file)

    try:
        theme = load_color_theme(args.theme, args.theme_path)
        conf = load_config(args.conf_file)
        switch_theme(conf, theme)
        write_config(conf, args.conf_file)
    except Exception as e:
        sys.stderr.write(f'Error: {e}\n')
        sys.exit(1)


def __parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Switch `alacritty` color theme")
    parser.add_argument('theme', metavar='theme',
                        type=str,
                        help='<theme name>')
    parser.add_argument('--theme-path', dest='theme_path',
                        metavar='theme-path',
                        type=str,
                        default='~/.config/alacritty/themes',
                        help=('Path to where themes are stored'))
    parser.add_argument('--conf-file', dest='conf_file',
                        metavar='conf-file',
                        type=str,
                        default='~/.config/alacritty/alacritty.yml',
                        help=('Path to `alacritty` configuration file'))
    return parser.parse_args()


if __name__ == '__main__':
    main(__parse_args())
