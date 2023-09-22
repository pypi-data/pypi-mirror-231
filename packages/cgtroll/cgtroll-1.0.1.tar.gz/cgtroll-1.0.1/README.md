[![Build](https://github.com/FrequentlyMissedDeadlines/cgtroll/actions/workflows/package.yml/badge.svg)](https://github.com/FrequentlyMissedDeadlines/cgtroll/actions/workflows/package.yml)
[![Publish](https://github.com/FrequentlyMissedDeadlines/cgtroll/actions/workflows/publish.yml/badge.svg)](https://github.com/FrequentlyMissedDeadlines/cgtroll/actions/workflows/publish.yml)
[![Version](https://img.shields.io/pypi/v/cgtroll)](https://pypi.org/project/cgtroll)
[![Version](https://img.shields.io/pypi/pyversions/cgtroll)](https://pypi.org/project/cgtroll)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cgtroll)
# codingame-troll
A tool to disguise your code in an other language. Funny to troll the language ranking.

| Language | Support |
|---|---|
| Bash | ✅ |
| C | ❌ |
| C++ | ❌ |
| C# | ❌ |
| Clojure | ❌ |
| D | ❌ |
| Dart | ❌ |
| F# | ❌ |
| Go | ❌ |
| Groovy | ❌ |
| Haskell | ❌ |
| Java | ❌ |
| Javascript | ❌ |
| Kotlin | ❌ |
| Lua | ❌ |
| Objective-C | ❌ |
| OCaml | ❌ |
| Pascal | ❌ |
| Perl | ❌ |
| PHP | ❌ |
| Python3 | ✅ |
| Ruby | ❌ |
| Rust | ❌ |
| Scala | ❌ |
| Swift | ❌ |
| TypeScript | ❌ |
| VB.NET | ❌ |

## Installation
```
pip install cgtroll
```
or to update to the latest version:
```
pip install cgtroll -U
```

## Usage

```
python -m cgtroll language file
```

or for a most advanced usage use `-h` option to get the description of all parameters:

```
python -m cgtroll -h
usage: cgtroll [-h] {bash} file

Convert your python code to any language supported by codingame to troll the language ranking.

positional arguments:
  {bash}      The language you want to make your code look like.
  file        The file containing your python code.

options:
  -h, --help  show this help message and exit
```

## Known limitations
Your python code must:
- NOT contain double quotes (`"`), replace them with single quotes (`'`)
- NOT contain comments (`#`), remove them