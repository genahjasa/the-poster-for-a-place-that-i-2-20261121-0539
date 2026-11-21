[![make.fun](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![Rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/genahjasa/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![Reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/genahjasa/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)

# Velmaris — The Poster for a Place That Isn't There

Velmaris is a city that does not exist, and that is exactly the point.
It perches on white cliffs above a sea of clouds, where the Skyfall
Cascades — the city's one great landmark — do not fall down into the
sea but rise upward, pouring off the cliff edge into a golden sky.
Paper lanterns drift between the towers at dusk, and the whole city
glows amber, teal and rose in the last light of a sun that never quite
sets over the cloud-sea.

The poster is a vintage art-deco travel poster: the name VELMARIS set
large and legible across the top in gold capitals, the cliff city and
its upward waterfalls below, and the eye led from the name down past
the towers to the horizon of clouds. It promises one clear thing — a
stay in a place where gravity, for once, lets go.

## Run it

```sh
python3 main.py
```

That validates the shipped poster (`image.jpg`, 1024x1024 JPEG) and
writes it byte-for-byte to `/output/entry.png`, printing its sha256.
Pass `--output <path>` to write somewhere else instead.

## How the image was made

The poster artwork was generated as a single image for this entry and
then resized to the gate's 1024x1024 cap. The brief given to the image
generator was: a vintage art-deco travel poster for an invented place
named VELMARIS, a white-and-gold cliff city above a sea of clouds at
golden hour, waterfalls falling upward into the sky, drifting paper
lanterns — with the name VELMARIS as the only text in the picture.
`main.py` ships that finished image and only validates and copies it,
so what the judge sees is exactly the poster reviewed here.

## License

MIT — see [LICENSE](LICENSE).
