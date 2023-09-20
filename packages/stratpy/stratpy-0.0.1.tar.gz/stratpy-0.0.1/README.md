<p align="center">
    <picture>
    <source media="(prefers-color-scheme: dark)" srcset="res/stratpy-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="res/stratpy-light.png">
    <img alt="starpy logo" src="res/stratpy-light.png">
    </picture>
</p>

## Stratpy - A python module for Game Theory written in rust

### Motivation:
- Create an easy to use python package for game theory catering to alternate disciplines like polisci.
- Backend created in rust offering a modern fast and memory-safe language, while python allows for an easy api for 
the scientific community.

### Features:

- Normal form and Extensive form games (including incomplete information)
- Solve games using user-ordered preferences (unknown but orderable variables)
- Easily export games to latex and other formats

### Installation

 Will upload as pip package in future

```bash
$ pip install stratpy
```

### Usage

```python
>>> import stratpy as sp
>>> 
>>> game1 = sp.Game()

```