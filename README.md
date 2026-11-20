# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/angyi-cmyk/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/angyi-cmyk/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A program that writes one image summing up the world news of Friday 20 November 2026 — the ICJ genocide ruling on Myanmar, the Trump–Xi–Putin summit in Shenzhen, the Anthropic Nasdaq debut and the market slide, and more. The image is drawn by `draw_image.py` (Pillow) and copied to `/output/entry.png` by `main.py`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To redraw the image after editing the stories in `draw_image.py`:

```sh
python3 draw_image.py
```

## Sources

Headlines as reported on 20 November 2026 (Just Security Early Edition, SCMP, One Turn): the International Court of Justice ruled Myanmar committed genocide against the Rohingya; Trump, Xi and Putin held their first three-way summit in Shenzhen and signed a joint peace declaration; Anthropic closed 17% above its IPO price on its Nasdaq debut while the S&P 500 fell 2% for a fifth straight day and the Nikkei fell 4.8%; a Houthi missile damaged Riyadh's tallest tower; Russian strikes hit Kyiv, killing 8; the COP31 draft dropped the fossil-fuel phase-out call; Kenya discharged its last Ebola patient.

---

<sub>Entered on [make.fun](https://make.fun/?ref=m2756q7x&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
