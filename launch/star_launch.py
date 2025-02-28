from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim'
        ),
        Node(
            package='mur_iry_kisbeadando',
            executable='draw_star',
            name='draw_star',
            output='screen'
        ),
    ])
