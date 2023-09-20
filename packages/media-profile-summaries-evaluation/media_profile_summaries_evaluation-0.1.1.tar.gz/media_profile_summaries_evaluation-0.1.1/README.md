# Media Profile Summaries Evaluation

![pytest](https://github.com/ripjar/media-profile-summaries-evaluation/actions/workflows/pytest.yml/badge.svg?event=push&branch=master)
![style](https://github.com/ripjar/media-profile-summaries-evaluation/actions/workflows/style.yml/badge.svg?event=push&branch=master)

Automated evaluation of media profile summaries. Datasets are expected to include the predicted summary, the input evidence (prompt), and the expected summary.

## Setup

```bash
poetry install --with dev
```

## Usage

```bash
poetry run python scripts/evaluate.py
```

* You must have access to an instance of bowler hat.
* See `bowlerhat` section in config and `bowlerhat.Client` for more information
* `evaluate.py` is configured with hydra (`python evaluate.py --help` for config options)
* Datasets are loaded from file or hugging face hub via `datasets.load_dataset`