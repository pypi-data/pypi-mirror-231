# resumer
pandoc based generator with advanced filter support

## About
tired of recreating resumes for different jobs?
this python library integrates pandoc to generate resumes based on the same set data files.

## Installation
```sh
pip install resumer
```

## Usage
### command line

```sh
resumer <config.toml> <tag1> /<tag2> ^<tag3> <x.tag4>
```
### python implementation

```py
from resumer import engines, ResumerData

data = ResumerData.fromConfig("examples/config.toml", useKey="data")

data.extra["color_highlights"] = "awesome-emerald"

engine = engines.ResumerTexEngine.fromConfig("examples/config.toml", useKey="engine")

gendata = data.format(None)

engine.generate("output/output.pdf", gendata)

engine.openLastGenerated()
```

## Tags Specifications
| Tag Format | Usage               | Scope                                             |
| ---------- | ------------------- | ------------------------------------------------- |
| tag      | standard tag        | all                                               |
| ^tag     | drill exclusive tag | will only parse on drill strings                  |
| /tag     | negation tag        | exclusions                                        |
| name.tag | structured tag      | will only filter objects as `ResumerEntry` (dict) |

* what is a drill tag?

suppose theres a string as follows
```py
string = "hello {w:world}{e:!}"
```
| input   | output       |
| ------- | ------------ |
| [w, e]  | hello world! |
| [w, /e] | hello world  |

# Acknowledgements
- [pandoc](https://pandoc.org/)
- [awesome-cv](https://github.com/posquit0/Awesome-CV)