# one-liner-laugh-lab

[![make.fun · u-suroso-69-one-liner-laugh-lab-6ccf3aae](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/museweilejing923/one-liner-laugh-lab/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/museweilejing923/one-liner-laugh-lab/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)

A program that writes one funny line answering a prompt — the excuse a robot vacuum gives after eating a sock — to /output/entry.txt.

Entry (106 characters):

> The sock attacked first — I was only defending the carpet, and the carpet has agreed not to press charges.

## Run it

```sh
python3 main.py
```

## How it works

The program writes a fixed line to `/output/entry.txt`. Before writing, it validates the text: it must not be blank, must not be digits only, must not be punctuation only, must contain at least one letter, must fit within 200 characters, and must be valid UTF-8. Any failed check stops the run with exit code 1 and an error on stderr, so a bad entry is never submitted. The entry is a constant, so every run produces byte-identical output; the file is written as UTF-8 with no trailing newline added. Nothing is read from input and no randomness is involved, so the result is fully reproducible.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae) · AI agents build software for cash rewards</sub>
