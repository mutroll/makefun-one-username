#!/usr/bin/env python3
"""Entry for make.fun bounty "One Word, One Username, One Reward".

Writes the entrant's own make.fun username — one word, nothing else —
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Python 3.13, standard library only. Deterministic: no network, no
randomness, no clock, no environment input beyond the output directory.
The output is the fixed 11-character handle "abdulrh1173", exactly.
"""

import os
import sys

# The entrant's own make.fun handle, sent as a single word.
# This is the whole entry: the brief fixes it, so it is a constant,
# not something computed or chosen at run time.
HANDLE = "abdulrh1173"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    # Write with a restrictive umask first, then open the file
    # world-readable: make.fun collects outputs as another user, so
    # the file must be mode 0644; its folder is set to 0755 only on a
    # best-effort basis below, since the sandbox may own it already.
    old_umask = os.umask(0o022)
    try:
        path = os.path.join(output_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(HANDLE)
    finally:
        os.umask(old_umask)

    os.chmod(path, 0o644)
    # Best effort only: in the grader sandbox the output directory is
    # pre-created and owned by another user, so chmod'ing it raises
    # PermissionError there. The directory's mode is the sandbox's own
    # business — never let this fail the run.
    try:
        os.chmod(output_dir, 0o755)
    except (PermissionError, OSError):
        pass

    # Read the file back and refuse to exit cleanly unless it holds
    # exactly the handle — no extra bytes, no trailing newline, no
    # encoding surprise. A wrong file must fail here, not at grading.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != HANDLE.encode("utf-8"):
        print(
            "entry.txt mismatch: expected %r, wrote %r" % (HANDLE, written),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
