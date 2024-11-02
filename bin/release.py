#!/usr/bin/env -S uv run
import sys
import subprocess


def run_command(command: list[str], error_message: str) -> None:
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"{error_message}: {e.stderr}")
        sys.exit(1)


def ensure_git_is_clean() -> None:
    result = subprocess.run(
        ["git", "status", "--porcelain"], capture_output=True, text=True
    )
    if result.stdout.strip():
        print(
            "Error: Git working directory is not clean. Commit or stash changes first."
        )
        sys.exit(1)


def update_version(new_version: str) -> None:
    cmd = f"sed -i 's/^version = .*/version = \"{new_version}\"/' pyproject.toml"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("Version updated")
    except subprocess.CalledProcessError as e:
        print(f"Error updating version: {e}")
        sys.exit(1)


def release():
    if len(sys.argv) != 2:
        print("Usage: $0 <new_version>")
        sys.exit(1)

    new_version = sys.argv[1]
    print(f"🚀 Will release version: {new_version}")

    ensure_git_is_clean()
    update_version(new_version)
    run_command(
        ["uv", "lock", "--upgrade-package", "mediathequeroubaix"],
        "Error locking package",
    )
    run_command(["git", "add", "pyproject.toml", "uv.lock"], "Error adding changes")
    run_command(
        ["git", "commit", "--no-verify", "-m", f"chore: bump version to {new_version}"],
        "Error committing version change",
    )
    run_command(
        ["git", "tag", "-a", new_version, "-m", f"Release {new_version}"],
        "Error creating git tag",
    )
    run_command(["git", "push", "--tags"], "Error pushing")
    run_command(["uv", "build"], "Error building package")
    run_command(["uv", "publish"], "Error publishing package")
    print(f"✅ Released version: {new_version}")


if __name__ == "__main__":
    release()
