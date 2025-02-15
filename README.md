# Pandas vs Polars

[![Build Icon]][Build Status]&emsp;[![License Icon]][LICENSE]

[Build Icon]: https://img.shields.io/github/actions/workflow/status/1Git2Clone/polars-vs-pandas/rust_build.yml?branch=main
[Build Status]: https://github.com/1git2clone/polars-vs-pandas/actions?query=branch%3Amain
[License Icon]: https://img.shields.io/badge/license-MIT-blue.svg
[LICENSE]: LICENSE

CSV heading parsing comparison for a 1 million line randomly generated CSV file.

## Table of contents

- [Pandas vs Polars](#pandas-vs-polars)
  - [Making the CSV file](#making-the-csv-file)
  - [Benchmarking Pandas and Polars](#benchmarking-pandas-and-polars)
  - [Results](#results)
    - [Specs](#specs)

## Making the CSV file

Run [`src/main.rs`](./src/main.rs) for CSV file generation.

## Benchmarking Pandas and Polars

```sh
cd pl_vs_pd
uv venv
source .venv/bin/activate # `.venv\Scripts\Activate` on Windows
uv pip install -r pyproject.toml
uv run python main.py
```

## Results

On [my machine](#specs) Polars is consistently 39~40 times faster than Pandas.

### Specs

- Ryzen 5 3600X
- Arch Linux `6.13.2-zen1-1-zen`
- Transcend NVMe SSD (`TS512GMTE220S`)
