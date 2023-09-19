import argparse
import logging
import os
import subprocess
import tomllib
from datetime import datetime

import frontmatter
import randomname

logging.basicConfig(level=logging.ERROR)


def load_config_file():
    file_path = os.path.expanduser("~/.config/zeka.toml")
    if os.path.isfile(file_path):
        try:
            with open(file_path, "rb") as f:
                config = tomllib.load(f)
            return config
        except Exception as e:
            logging.error(f"Error loading config file: {e}")
            return None

    else:
        return None


def get_files_in_directory(directory):
    """
    Returns all markdown files in the specified directory
    """
    return [
        i
        for i in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, i)) and i.endswith(".md")
    ]


def parse_args():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    new_parser = subparser.add_parser("new", help="create new note")
    new_parser.add_argument("-t", "--title")
    new_parser.add_argument("-a", "--tags", default="[]")
    new_parser.add_argument("-l", "--lang", default="en-US")
    new_parser.add_argument("-o", "--open")

    sync_parser = subparser.add_parser("sync", help="sync notes")
    sync_parser.set_defaults(sync=sync)

    # TODO: Create clean parser to delete empty files or with only front matter
    # clean_parser = subparser.add_parser("clean", help="clean up!")

    args = parser.parse_args()

    return args


def create_front_matter(args):
    metadata = {}
    time = datetime.now().isoformat()
    metadata["time"] = time

    if args.title:
        metadata["title"] = args.title
    else:
        metadata["title"] = randomname.get_name()

    if args.lang:
        metadata["lang"] = args.lang
    else:
        metadata["lang"] = "en-US"

    if args.tags:
        metadata["tags"] = args.tags
    else:
        metadata["tags"] = "[]"

    front_matter = ""

    for key, value in metadata.items():
        front_matter += f"{key}: {value}\n"

    front_matter = f"---\n{front_matter}---\n"

    return metadata["title"], front_matter


def create_zeka(filename: str, front_matter, path):
    path += filename
    with open(f"{path}.md", "w") as f:
        f.write(front_matter)


def get_save_path():
    config = load_config_file()

    if config is None:
        save_path = "./"
    else:
        save_path = config["settings"]["save_path"]
        save_path = os.path.expanduser(save_path)

    return save_path


def open_zeka(filename: str, args):
    if "editor" in args:
        editor = args.editor

    elif "EDITOR" in os.environ:
        editor = os.environ.get("EDITOR")

        if editor is not None:
            subprocess.run([editor, f"{filename}.md"])

    else:
        raise Exception("No default editor found and none was specified")


def sync():
    save_path = get_save_path()
    files = get_files_in_directory(save_path)
    files = [f"{save_path}{i}" for i in files]

    sync_required = False

    for i in files:
        with open(i, "r") as f:
            file = frontmatter.load(f)
            if "title" in file:
                if f"{file['title']}" != f"{i.split('/')[-1].split('.')[0]}":
                    sync_required = True
                    foo = i.split("/")
                    foo.pop()
                    new_path = f"{'/'.join(foo)}/{file['title']}.md"
                    os.rename(i, new_path)
                    print(f"Changed {i} to {new_path}")

    if sync_required is False:
        print("Nothing to sync.")


def main():
    args = parse_args()

    if "sync" in args:
        args.sync()
        return

    filename, front_matter = create_front_matter(args)

    save_path = get_save_path()

    create_zeka(filename=filename, front_matter=front_matter, path=save_path)

    file = save_path + filename

    open_zeka(file, args)
