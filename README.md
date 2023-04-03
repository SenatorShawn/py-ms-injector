# NGS Bypass Injector

This (extremely small) program will wait for `BlackCipher64.aes` to be in the process list
and, when it is, inejct an NGS bypass to the appropriate address. I hope to add more in the
future.

## Installation

```bash
> pip install .
```

## Running

Ensure you're running in a virtual environment with this package installed. Then,

```bash
> bypass-ngs
Looking for `BlackCipher64.aes`...
Attached to `BlackCipher64.aes`!
Writing bypass to BlackCipher64.aes+2842fc2 (2c42fc2)...
Bypass successfully written.
```

## Contributing

To perform a developer install, simply create a virtual environment (`python==3.10` preferred)
and then run


```bash
> pip install -e .[dev]
```

or however you prefer to manage your editable installations.

### Versioning

This project follows the [Semantic Versioning](https://semver.org/) standard. To keep things simple:

- If the change does not change the API, it is a PATCH change
    - `0.1.0 -> 0.1.1`
- If the change to the API is backwards compatible, then it is a MINOR change
    - `0.1.1 -> 0.2.0`
- If the change to the API is not backwards compatible, then it is a MAJOR change
    - `0.1.1 -> 1.0.0`
