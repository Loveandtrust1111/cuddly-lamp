# cuddly-lamp

A simple, elegant project template for quick repository setup and transfer.

## Overview

This repository provides a clean starting point for new projects with proper documentation and structure.

## Features

- Clean repository structure
- Well-documented codebase
- Easy to fork and customize
- Ready for collaboration

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Loveandtrust1111/cuddly-lamp.git
   cd cuddly-lamp
   ```

2. Install dependencies:
   ```bash
   pip install pytest
   ```

3. Run tests:
   ```bash
   python3 -m pytest -v
   ```

## Code Examples

This repository demonstrates refactoring of duplicated code patterns:

### calculator.py
- **Before**: Repeated input validation in each arithmetic function (91 lines)
- **After**: Extracted validation into reusable helper functions (69 lines)
- **Improvement**: 24% reduction in code, better maintainability

### data_processor.py
- **Before**: Repeated data validation and field checking (56 lines)
- **After**: Generic validation function with configurable fields (41 lines)
- **Improvement**: 27% reduction in code, more flexible design

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue in this repository.
