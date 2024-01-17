from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import (DeclareLaunchArgument, OpaqueFunction)
from launch.substitutions import LaunchConfiguration


def launch_setup(context, *args, **kwargs):

    # Initialize Arguments
    marker_size = LaunchConfiguration("marker_size")
    aruco_dictionary_id = LaunchConfiguration("aruco_dictionary_id")
    image_topic = LaunchConfiguration("image_topic")
    camera_info_topic = LaunchConfiguration("camera_info_topic")
    tracking_base_frame = LaunchConfiguration("tracking_base_frame")
    marker_id_list = LaunchConfiguration("marker_id_list")

    aruco_node = Node(
        package='ros2_aruco',
        executable='aruco_node',
        parameters=[{
            'marker_size': float(context.perform_substitution(marker_size)),
            'aruco_dictionary_id': str(context.perform_substitution(aruco_dictionary_id)),
            'image_topic': str(context.perform_substitution(image_topic)),
            'camera_info_topic': str(context.perform_substitution(camera_info_topic)),
            'tracking_base_frame': str(context.perform_substitution(tracking_base_frame)),
            'marker_id_list': marker_id_list,
        }])

    nodes_to_start = [aruco_node]
    return nodes_to_start


def generate_launch_description():

    declared_arguments = []

    declared_arguments.append(
        DeclareLaunchArgument(
            "marker_size",
            description="aruco marker size.",
            default_value='0.0705',
        ))
    declared_arguments.append(
        DeclareLaunchArgument(
            "aruco_dictionary_id",
            description="aruco dictionary id.",
            default_value='DICT_5X5_250',
            choices=[
                "DICT_4X4_100", "DICT_4X4_1000", "DICT_4X4_250", "DICT_4X4_50", "DICT_5X5_100",
                "DICT_5X5_1000", "DICT_5X5_250", "DICT_5X5_50", "DICT_6X6_100", "DICT_6X6_1000",
                "DICT_6X6_250", "DICT_6X6_50", "DICT_7X7_100", "DICT_7X7_250", "DICT_7X7_50",
                "DICT_ARUCO_ORIGINAL"
            ],
        ))
    declared_arguments.append(
        DeclareLaunchArgument(
            "image_topic",
            description="image topic name.",
            default_value='/camera/color/image_rect_raw',
        ))
    declared_arguments.append(
        DeclareLaunchArgument(
            "camera_info_topic",
            description="camera info topic name.",
            default_value='/camera/color/camera_info',
        ))
    declared_arguments.append(
        DeclareLaunchArgument(
            "tracking_base_frame",
            description=".",
            default_value='camera_color_optical_frame',
        ))
    declared_arguments.append(
        DeclareLaunchArgument(
            "marker_id_list",
            description="list of marker IDs to be detected.",
            default_value='[0, 1, 2, 3]',
        ))

    return LaunchDescription(declared_arguments + [OpaqueFunction(function=launch_setup)])
