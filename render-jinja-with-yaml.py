#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Copyright:
#   2018 PM <github.com/perfide>
# License:
#   BSD-3
#   http://directory.fsf.org/wiki/License:BSD_3Clause

"""
Use a yaml-config to render Jinja2 templates
"""

# included
import argparse
import os
import sys

# 3rd-party
import jinja2
import yaml


def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Use a yaml-config to render Jinja2 templates')
    parser.add_argument(
        'yaml',
        help='Path to the yaml-config')
    parser.add_argument(
        'templates',
        help='Dir containing j2-files')
    return parser.parse_args(args)
# end def parse_args


def main(yaml_path, templates_dir):
    with open(yaml_path, 'rt') as f:
        config = yaml.safe_load(f.read())
    fs_loader = jinja2.FileSystemLoader(templates_dir, encoding='utf-8')
    env = jinja2.Environment(loader=fs_loader)
    for name in env.list_templates():
        if not name.endswith('.j2'):
            continue
        tmpl = env.get_template(name)
        cfn = tmpl.render(**config)
        # strip the trailing '.j2' extension
        output_file = name.rsplit('.', 1)[0]
        output_path = os.path.join(templates_dir, output_file)
        with open(output_path, 'w') as fh:
            fh.write(cfn)
            # the jinja renderer seems to strip the end-of-file new-line
            fh.write('\n')
    return
# end def main


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    rc = main(args.yaml, args.templates)
    sys.exit(rc)

# [EOF]
