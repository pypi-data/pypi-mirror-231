from logging import root
import click
import yaml
import tomllib
import tomli_w
import git
import os


def get_git_repo(ctx):
    path = ctx.obj["ROOT"]
    try:
        git_repo = git.Repo(path, search_parent_directories=True)
        return git_repo
    except Exception:
        raise click.UsageError(
            f'The current working directory "{path}" is not a git repo'
        )


def get_git_root(ctx):
    repo = get_git_repo(ctx)
    return repo.working_dir


def read_config(ctx):
    filename = "config.yaml"
    base_path = get_git_root(ctx)

    path = os.path.join(base_path, filename)

    if not os.path.isfile(path):
        raise click.UsageError(
            f"urnc expects a config file called {filename} "
            f"in the git root folder '{base_path}' "
            "make sure you a in a course directory",
        )
    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f)
            return config
    except Exception as e:
        raise click.FileError(path, str(e))


def write_config(ctx, data):
    filename = "config.yaml"
    base_path = get_git_root(ctx)

    path = os.path.join(base_path, filename)
    try:
        with open(path, "w") as f:
            yaml.dump(data, f)
    except Exception as e:
        raise click.FileError(path, str(e))


def read_pyproject(ctx):
    filename = "pyproject.toml"
    base_path = get_git_root(ctx)

    path = os.path.join(base_path, filename)

    try:
        with open(path, "rb") as f:
            config = tomllib.load(f)
            return config
    except Exception as e:
        raise click.FileError(path, str(e))


def write_pyproject(ctx, data):
    filename = "pyproject.toml"
    base_path = get_git_root(ctx)

    path = os.path.join(base_path, filename)
    try:
        with open(path, "wb") as f:
            tomli_w.dump(data, f)
    except Exception as e:
        raise click.FileError(path, str(e))
