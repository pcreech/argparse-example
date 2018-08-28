```
./argparse-example.py --help
usage: argparse-example.py [-h] {changelog,setup} ...

positional arguments:
  {changelog,setup}  Which action to execute
    changelog        The 'changelog' command writes a RPM changelog entry for
                     the current version and release.
    setup            The 'setup' command installs packages required for a
                     successful workflow.

optional arguments:
  -h, --help         show this help message and exit
```

```
./argparse-example.py changelog --help
usage: argparse-example.py changelog [-h] [--changelog CHANGELOG]
                                     package [package ...]

positional arguments:
  package               The package to add a changelog entry for

optional arguments:
  -h, --help            show this help message and exit
  --changelog CHANGELOG
                        The text for the changelog entry
```

```
./argparse-example.py setup --help
usage: argparse-example.py setup [-h]

optional arguments:
  -h, --help  show this help message and exit
```
