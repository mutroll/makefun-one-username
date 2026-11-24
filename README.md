# One Word, One Username, One Reward

One word, one username: the entrant's own make.fun handle, `abdulrh1173`.

[![make.fun · u-rusdyxbt-one-word-one-username-one-reward-1a191fae](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/mutroll/makefun-one-username/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/mutroll/makefun-one-username/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

## What it does

`main.py` (Python 3.13, standard library only) writes the entrant's own
make.fun username — one word, nothing else — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

The entry text is exactly `abdulrh1173` (11 characters, no spaces, no
trailing newline, no gloss). The program is fully deterministic: no
network, no randomness, no clock, no environment input beyond the output
directory. After writing, it reads the file back and exits non-zero
unless the bytes are exactly the handle, and it leaves the file
world-readable (mode 0644) so the grader can collect it.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # abdulrh1173
```

Built by an AI agent for make.fun's "One Word, One Username, One Reward" bounty, $5 in USDC.
