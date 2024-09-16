#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2021, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def get_xacro_file_content(
    xacro_file=PathJoinSubstitution([FindPackageShare('xarm_description'), 'urdf', 'xarm_device.urdf.xacro']), 
    arguments={}):
    command = [
        PathJoinSubstitution([FindExecutable(name='xacro')]),
        ' ',
        xacro_file,
        ' '
    ]
    if arguments and isinstance(arguments, dict):
        for key, val in arguments.items():
            command.extend([
                '{}:='.format(key),
                val,
                ' '
            ])
    return Command(command)


# print xacro command. Useful for debugging!
def get_xacro_command(
    xacro_file, 
    arguments, context):
    command = [
        PathJoinSubstitution([FindExecutable(name='xacro')]).perform(context),
        ' ',
        xacro_file.perform(context),
        ' '
    ]
    if arguments and isinstance(arguments, dict):
        for key, val in arguments.items():
            if type(val) is str:
                command.extend([
                    '{}:='.format(key),
                    val,
                    ' '
                ])
            else:
                command.extend([
                    '{}:='.format(key),
                    val.perform(context),
                    ' '
                ])
    return "".join(command)