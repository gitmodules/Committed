#!/usr/bin/env python3
import argparse
import subprocess
import uuid

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int, help="Number of commits")
    parser.add_argument("-p", "--push", action="store_true", help="Push after commits")
    parser.add_argument("--dry-run", action="store_true", help="Show commands only")
    args = parser.parse_args()

    if args.count <= 0:
        raise SystemExit("Count must be positive")

    for _ in range(args.count):
        msg = str(uuid.uuid4())

        if args.dry_run:
            print(f"[DRY RUN] git commit --allow-empty -m {msg}")
        else:
            subprocess.run(
                ["git", "commit", "--allow-empty", "-m", msg],
                check=True
            )

    if args.push:
        if args.dry_run:
            print("[DRY RUN] git push")
        else:
            subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    main()
