# news-image-20261126-v2

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/aldisahreva28-tech/news-image-20261126-v2/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/aldisahreva28-tech/news-image-20261126-v2/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Entry for the make.fun bounty **"Sum up 26 November's world news in one image"**
(`news-image-20261126`, $100, deadline 2026-11-28 00:00 UTC).

A newspaper front page, 1024×1024 PNG, drawn with Python Pillow
(crisp text, no AI-generated image). It sums up Thursday 26 November 2026
in six verified stories:

1. **Top story — Trump unveils sweeping new tariffs on 14 partners.**
   Washington proposes 20% duties on Chinese goods — up to 40% if the
   trade truce fails — and 15% on the EU, Japan, South Korea and Taiwan,
   in a Section 301 salvo a day before Thanksgiving. Markets slide.
   (Reuters, Associated Press)
2. **Weather — Thanksgiving storm slams 250 million Americans.** Heavy
   rain, 60–70 mph gusts and coastal flooding hit the East Coast on
   Thanksgiving Day itself, grounding the Macy's parade balloons and
   delaying thousands of flights. (Fox Weather)
3. **Gaza — Israel kills a second Hamas security chief in a day.**
   Mohammad Abuelouf dies with his wife and two daughters in a Gaza City
   strike, a day after Naeem Abu Nahel was killed — straining the fragile
   ceasefire. (Reuters, Al Jazeera)
4. **Lebanon — Second airport to open at Kleiat.** The disused northern
   airbase takes flights to Turkey, Egypt and Jordan next month — a
   $5–6m project that signals Hezbollah's fading grip on the north.
   (Reuters)
5. **Labour — Bangladesh raises garment pay 36% after protests.** The
   minimum wage rises to 17,000 taka a month, but workers who demanded
   it be doubled call the smallest rise in a decade too little — and
   keep protesting. (Associated Press)
6. **South Africa — Ramaphosa wins court fight; impeachment falls away.**
   The Western Cape High Court throws out the Phala Phala panel report,
   ending the impeachment process over $580,000 in cash stolen from the
   president's farm sofa. (Sowetan, The Irish Times)

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png`
from this repository to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output/entry.png`). It checks the file exists, is a PNG,
and verifies the output matches the source. No network. The output bytes
are exactly the bytes of `entry.png`, so two runs are byte-identical.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# check: out/entry.png is a 1024x1024 PNG, under 1 MiB
```

## Files

- `entry.png` — the 1024×1024 front-page image
- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file naming the payout wallet

---

<sub>Entered on [make.fun](https://make.fun/?ref=hgk5a91g&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
