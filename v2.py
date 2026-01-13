#!/usr/bin/env python3
import argparse
import subprocess
import uuid

PUSH_INTERVAL = 10000

def push_if_needed(count, args):
    if args.push:
        if args.dry_run:
            print(f"[DRY RUN] git push (after {count} commits)")
        else:
            subprocess.run(["git", "push"], check=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int, help="Number of commits")
    parser.add_argument("-p", "--push", action="store_true", help="Push commits")
    parser.add_argument("--dry-run", action="store_true", help="Show commands only")
    args = parser.parse_args()

    if args.count <= 0:
        raise SystemExit("Count must be positive")

    for i in range(1, args.count + 1):
        msg = str(uuid.uuid4())

        if args.dry_run:
            print(f"[DRY RUN] git commit --allow-empty -m {msg}")
        else:
            subprocess.run(["git", "commit", "--allow-empty", "-m", msg], check=True)

        if i % PUSH_INTERVAL == 0:
            push_if_needed(i, args)

    if args.count % PUSH_INTERVAL != 0:
        push_if_needed(args.count, args)

if __name__ == "__main__":
    main()
