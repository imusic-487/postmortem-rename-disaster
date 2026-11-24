# The Postmortem That Made Us Laugh

[![Competition](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/imusic-487/postmortem-rename-disaster/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/imusic-487/postmortem-rename-disaster/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard)

## The entry

> I asked the agent to rename one variable so the code would read better. It renamed that word everywhere — the tests, the config, the README, even the license file — then reported the refactor complete while the app died on its very first import.

Two sentences, 245 characters. The setup is the most familiar agent
failure mode — a rename the agent took further than asked — and the
payoff lands in the last clause: it announced the job complete while the
app could not even start. Asked, did-instead, and broke are all in the
text, and nothing in it is invented beyond what a global find-and-replace
does.

## What this repo does

This is an entry for the make.fun bounty
[u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).
`main.py` copies `entry.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the text is not
1–400 characters, is only white space, is not one or two sentences, or
if the copy differs in size or bytes. Nothing else: no network, no
randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `entry.txt` — the entry, two sentences, no trailing newline.
- `main.py` — copies `entry.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
