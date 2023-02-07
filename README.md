<h1 align="center"> 🖼️ Pexels scraper </h1>

<div align="center">
    <img src="https://img.shields.io/github/v/release/toshy/pexels-scraper?label=Release&sort=semver" alt="Current bundle version" />
    <a href="https://hub.docker.com/r/t0shy/pexels-scraper"><img src="https://img.shields.io/badge/Docker%20Hub-t0shy%2Fpexels--scraper-blue" alt="Docker Hub" /></a>
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/pexels-scraper/pylint.yml?branch=main&label=Pylint" alt="Code style">
    <img src="https://img.shields.io/badge/Code%20Style-PEP8-orange.svg" alt="Code style" />
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/pexels-scraper/security.yml?branch=main&label=Security%20check" alt="Security check" />
    <br /><br />
A python command-line tool for scraping images from <a href="https://www.pexels.com/">Pexels.com</a> by topic search.
</div>

## Info

[Pexels.com](https://www.pexels.com/) is a platform which provides royalty-free photos and videos.

## 🧰 Requirements

* A Pexels API key (can be requested after sign-up)
* [Docker](https://docs.docker.com/get-docker/)

> Note: By default, the API is rate-limited to 200 requests per hour and 20,000 requests per month.
> Read the [Pexels Guidelines](https://www.pexels.com/api/documentation/#guidelines) for more info.

## 🐋 Usage

1. Pull the image.

```shell
docker pull t0shy/pexels-scraper:latest
```

2. Run it.

Supply a JSON payload to search for a specific category. For available query parameters, see
the [API documentation](https://www.pexels.com/api/documentation/#photos-search).

```shell
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/pexels/results:/output \
  t0shy/pexels-scraper:latest \
  -k "37c01053e18949935e52c0e9ddabc706166de7ca42c8357f0f4bf93e" \
  -p '{"query":"Nature"}'
```

> Note: make sure to mount to the `/output` directory on the container.

3. Check the results.

```text
|-- ./pexels/results
  |-- 7203981.jpeg
  |-- ...
  |-- 7758348.jpeg
```

> Note: a filename consists of `id` and `original` file extension.

## 🙋 Help

```shell
docker run -it --rm t0shy/pexels-scraper:latest -h
```

```text
 _____              _         _____
|  __ \            | |       / ____|
| |__) |____  _____| |___   | (___   ___ _ __ __ _ _ __   ___ _ __
|  ___/ _ \ \/ / _ \ / __|   \___ \ / __| '__/ _` | '_ \ / _ \ '__|
| |  |  __/>  <  __/ \__ \   ____) | (__| | | (_| | |_) |  __/ |
|_|   \___/_/\_\___|_|___/  |_____/ \___|_|  \__,_| .__/ \___|_|
                                                  | |
                                                  |_|

usage: main.py [-h] -k API_KEY -p PAYLOAD [-d] [-v]

A python command-line tool for scraping images from Pexels.com by topic search.

options:
  -h, --help            show this help message and exit
  -k API_KEY, --key API_KEY
                        API key.
  -p PAYLOAD, --payload PAYLOAD
                        Payload in JSON format.
  -d, --debug           Debug loglevel; Fallback to WARNING.
  -v, --verbose         Info loglevel.

Repository: https://github.com/ToshY/pexels-scraper
```

## 🛠️ Contribute

### Prerequisites

* [Pre-commit](https://pre-commit.com/#installation)
* [Docker Compose v2](https://docs.docker.com/compose/install/)
* [Task (optional)](https://taskfile.dev/installation/)

### Pre-commit

Set up `pre-commit`.

```shell
pre-commit install
```

### Checks

```shell
task contribute
```

> Note: you can use `task black:fix` to resolve codestyle issues.

## ❕ License

This repository comes with a [MIT license](./LICENSE).
