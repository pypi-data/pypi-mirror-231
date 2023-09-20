import os
import csv
import json
import argparse

import requests
from rich import print
from rich.tree import Tree
from glyphoji import glyph
from rich.markdown import Markdown

from .__init__ import __author__, __version__, __about_me__

PROGRAM_DIRECTORY = os.path.join(os.path.expanduser("~"), "likee-downloader")


def notice():
    return f"""
likee-downloader v{__version__} Copyright (C) 2022-2023 {__author__}

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
"""


def check_updates():
    """
    Checks the program's updates by comparing the current program version tag and the remote version tag from GitHub.
    """
    print(f"{glyph.information} Checking for updates... Please wait.")
    response = requests.get(
        "https://api.github.com/repos/rly0nheart/likee-downloader/releases/latest"
    ).json()
    remote_version = response.get("tag_name")

    # Ignore if the remote version matches the program's local version tag (assumes the program is up to date)
    if remote_version == __version__:
        print(f"{glyph.check_mark_button} Running an Up-to-date release")
    else:
        print(
            f"{glyph.information} {PROGRAM_DIRECTORY} version {remote_version} is available. "
            f"Run 'pip install --upgrade likee-downloader' to get the updates.\n"
        )
        release_notes = Markdown(response.get("body"))
        print(release_notes)
        print("\n")


def video_data_tree(video_data: dict, video_index: int):
    """
    Visualises a video's data in a treeview structure.

    :param video_data: A JSON object containing a video's data.
    :param video_index: Index of the post being visualised to a treeview.
    """
    tree = Tree(
        f"\nPost #{video_index} [bold]{video_data.get('title')}[/]",
        guide_style="bold bright_blue",
    )
    # Iterate over each key value pair in a video data object
    for video_key, video_value in video_data.items():
        # Skip the sound, hashtagInfos and cloudMusic objects, because they will have their own branches
        if video_key == "sound":
            continue
        if video_key == "cloudMusic":
            continue
        if video_key == "hashtagInfos":
            continue
        tree.add(f"{video_key}: {video_value}")

    # Add a sound branch to the main tree if the sound object is available in the video data
    if video_data.get("sound"):
        sound_branch = tree.add(f"{glyph.speaker_high_volume} [bold]Sound[/]")
        for sound_key, sound_value in video_data.get("sound").items():
            sound_branch.add(f"{sound_key}: {sound_value}")

    # Add a Cloud Music branch to the main tree if the cloudMusic object is available in the video data
    if video_data.get("cloudMusic"):
        cloud_music_branch = tree.add(f"{glyph.cloud} [bold]Cloud Music[/]")
        for cloud_music_key, cloud_music_value in video_data.get("cloudMusic").items():
            cloud_music_branch.add(f"{cloud_music_key}: {cloud_music_value}")

    # Add an Hashtag Info branch to the main tree if the hashtagInfos object is available in the video data
    if video_data.get("hashtagInfos"):
        hashtag_info_branch = tree.add(f"{glyph.keycap_number_sign} Hashtag Info")
        for hashtag in json.loads(video_data.get("hashtagInfos")):
            for hashtag_key, hashtag_value in hashtag.items():
                hashtag_info_branch.add(f"{hashtag_key}: {hashtag_value}")

    print(tree)


def path_finder(username: str):
    """
    Create a set of directories for a given user's data.

    The function creates a main directory for the user inside the 'likee-downloader' directory.
    Inside this main directory, it creates subdirectories for different types of data:
    'videos', 'screenshots', and 'json'.

    :param username: The username of the target user.
     It is used to create a personalized directory structure where data related to the user will be stored.

    Examples:
    >>> path_finder('username123')
    # This will create the following directory structure:
    # likee-downloader/username123/
    # likee-downloader/username123/videos/
    # likee-downloader/username123/screenshots/
    # likee-downloader/username123/json/
    """
    directory_list = [
        os.path.join(PROGRAM_DIRECTORY, username),
        os.path.join(PROGRAM_DIRECTORY, username, "videos"),
        os.path.join(PROGRAM_DIRECTORY, username, "screenshots"),
        os.path.join(PROGRAM_DIRECTORY, username, "csv"),
        os.path.join(PROGRAM_DIRECTORY, username, "json"),
    ]
    for directory in directory_list:
        os.makedirs(directory, exist_ok=True)


def dump_data(video_data: dict, dump_to: argparse, username: str):
    """
    Dump video data to a specified format (JSON or CSV).

    :param video_data: A JSON object containing data of a video to dump.
    :param dump_to: An argparse namespace object that contains values: 'csv' and 'json'.
    :param username: The username of the target.
    """
    video_id = video_data.get("postId")

    # Define the path to save the JSON file
    json_file_path = os.path.join(
        PROGRAM_DIRECTORY, username, "json", f"{video_id}.json"
    )

    # Define the path to save the CSV file
    csv_file_path = os.path.join(PROGRAM_DIRECTORY, username, "csv", f"{video_id}.csv")

    if dump_to == "json":
        # Open the JSON file in write mode and dump the video data into it
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(video_data, json_file, indent=4, ensure_ascii=False)

        print(
            f"{glyph.page_facing_up} Data dumped: [link file://{json_file_path}]{json_file_path}"
        )
    else:  # Assume value is "csv"
        # Open the CSV file in write mode
        with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)

            # Write the keys of the video data dictionary as the header row of the CSV file
            writer.writerow(video_data.keys())

            # Write the values of the video data dictionary as the second row of the CSV file
            writer.writerow(video_data.values())

        print(
            f"{glyph.page_facing_up} Data dumped: [link file://{csv_file_path}]{csv_file_path}"
        )


def create_parser():
    parser = argparse.ArgumentParser(
        description=f"likee-downloader — by {__author__} | {__about_me__}",
        epilog="A program for downloading videos from Likee, given a username",
    )
    parser.add_argument("username", help="username")
    parser.add_argument(
        "-s",
        "--screenshot",
        help="capture a screenshot of the target's profile",
        action="store_true",
    )
    parser.add_argument(
        "-l",
        "--limit",
        help="number of videos to get (default: %(default)s)",
        default=10,
        type=int,
    )
    parser.add_argument(
        "-d",
        "--dump",
        help="dump video data to a specified file type",
        choices=["csv", "json"],
    )
    parser.add_argument(
        "-dl",
        "--download",
        help="Download all returned videos",
        action="store_true",
        dest="download",
    )
    return parser
