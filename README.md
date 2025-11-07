# cuddly-lamp

A simple, elegant project template for quick repository setup and transfer.

## Overview

This repository provides a clean starting point for new projects with proper documentation and structure.

## Features

- Clean repository structure
- Well-documented codebase
- Easy to fork and customize
- Ready for collaboration
- Performance optimization examples and best practices

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

## Performance Optimization

This repository includes comprehensive examples and guidance for writing efficient code:

- **[PERFORMANCE.md](PERFORMANCE.md)** - Complete guide to performance optimization
- **[examples/](examples/)** - Side-by-side comparisons of inefficient vs efficient code
  - Python examples with real-world performance patterns
  - JavaScript examples for web development
- **[benchmark.py](benchmark.py)** - Run benchmarks to see the performance differences

### Quick Example

Run the benchmark to see performance improvements in action:

```bash
python3 benchmark.py
```

This demonstrates speedups ranging from 2x to 250x by using proper data structures and algorithms!

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue in this repository.
