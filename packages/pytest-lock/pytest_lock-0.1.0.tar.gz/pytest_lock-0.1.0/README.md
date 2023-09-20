# pytest-lock
## Overview
**'pytest-lock'** is a pytest plugin that allows you to "lock" the results of unit tests, storing them in a local cache. This is particularly useful for tests that are resource-intensive or don't need to be run every time. When the tests are run subsequently, 
**'pytest-lock'** will compare the current results with the locked results and issue a warning if there are any discrepancies.

## Installation
To install pytest-lock, you can use pip:

```bash
pip install pytest-lock
```
Or, you can clone the repository and install it manually:

```bash
git clone https://github.com/yourusername/pytest-lock.git
cd pytest-lock
pip install -e .
```
## Usage
### Locking Tests

To lock a test, use the lock fixture and mark the test with @pytest.mark.lock. Here's an example:

```python
import pytest

def custom_sum(arg):
    if len(arg) == 0:
        raise ValueError("Cannot sum an empty list")
    return sum(arg)

@pytest.mark.lock
def test_lock_sum(lock):
    lock(custom_sum, ([]))
    lock(custom_sum, ([1, 2, 3]))
```

Run pytest with the --lock option to generate the lock files:

```bash
pytest --lock
```

This will generate JSON files in a .pytest-lock directory, storing the results of the locked tests.

### Running Tests
Simply run pytest as you normally would:

```bash
pytest
```

If a test result differs from its locked value, a warning will be issued.

### Configuration
The locked test results are stored in a .pytest-lock directory at the root of your project. You can delete this directory to reset all locks.

## Contributing
Contributions are welcome! Please read the contributing guidelines to get started.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
