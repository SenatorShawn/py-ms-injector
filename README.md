# NGS Bypass Injector

This (extremely small) program will wait for `BlackCipher64.aes` to be in the process list
and, when it is, inejct an NGS bypass to the appropriate address. I hope to add more in the
future.

## Installation

```bash
> pip install .
```

(Alternatively, if you plan on developing...)

```bash
> pip install -e .
```

## Running

Ensure you're running in a virtual environment with this package installed. Then,

```bash
> bypass-ngs
Looking for `BlackCipher64.aes`...
Attached to `BlackCipher64.aes`!
Writing bypass to BlackCipher64.aes+2842fc2 (2c42fc2)
Bypass successfully written.
```
