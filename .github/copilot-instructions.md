# Copilot Instructions for cuddly-lamp

## Project Overview

This is a Python project demonstrating best practices in code organization, refactoring, and performance optimization. It provides a clean starting point for new projects with proper documentation, structure, and examples of refactored code that eliminates duplication.

## Code Architecture

### Core Structure

- **src/base_manager.py**: Base class providing common CRUD operations for all entity managers
  - Contains `_generate_id()`, `_create_record()`, `_update_record()`, and `_get_record()` methods
  - All manager classes should extend this base class
  
- **src/utils.py**: Shared utility functions used across the project
  - `get_timestamp()`: Generate ISO format timestamps
  - `validate_min_length()`: Generic length validation
  - `validate_email()`: Email format validation with regex
  - `validate_positive_number()`: Numeric validation for positive numbers

- **src/user_manager.py**: User entity management extending BaseManager
- **src/product_manager.py**: Product entity management extending BaseManager

## Code Style and Conventions

1. **Follow DRY Principle**: Don't Repeat Yourself
   - Extract duplicated code into reusable components
   - Use the base class for common functionality
   - Utilize shared utility functions

2. **Class Design**:
   - New entity managers should extend `BaseManager`
   - Use protected methods (prefixed with `_`) for internal base class methods
   - Public methods should handle entity-specific business logic

3. **Validation**:
   - Use utility functions from `src/utils.py` for common validations
   - Validate input before creating or updating records
   - Raise `ValueError` with clear messages for validation failures

4. **Documentation**:
   - All functions must have docstrings describing purpose, parameters, and return values
   - Use Google-style docstrings
   - Document exceptions that can be raised

5. **Error Handling**:
   - Use descriptive error messages
   - Pass `entity_name` parameter to base class methods for customized error messages
   - Consistently use `ValueError` for validation and not-found errors

## Testing Requirements

- All tests are located in the `tests/` directory
- Use Python's built-in `unittest` framework
- Run tests with: `python -m unittest discover -s tests -v`
- All tests must pass before committing changes
- Test coverage expectations:
  - Every new manager class needs corresponding test file
  - Test all CRUD operations
  - Test validation logic thoroughly
  - Test both success and failure cases
  
## Development Workflow

1. **Making Changes**:
   - Keep commits focused and atomic
   - Write clear, descriptive commit messages
   - Test thoroughly before committing

2. **Adding New Entity Managers**:
   ```python
   from src.base_manager import BaseManager
   from src.utils import validate_min_length
   
   class NewManager(BaseManager):
       """Manager for handling new entities."""
       
       def create_entity(self, name):
           """Create a new entity."""
           validate_min_length(name, 3, "Name")
           record = self._create_record({'name': name})
           return record
   ```

3. **Running Tests**:
   - Always run full test suite: `python -m unittest discover -s tests -v`
   - Expected: 35 tests passing (as of last update)

4. **Performance Considerations**:
   - See PERFORMANCE.md for optimization guidelines
   - Use appropriate data structures for the task
   - Run benchmarks when making performance-related changes: `python3 benchmark.py`

## Key Files

- **README.md**: Project overview and getting started guide
- **CONTRIBUTING.md**: Contribution guidelines
- **REFACTORING.md**: Documentation of refactoring decisions and benefits
- **PERFORMANCE.md**: Performance optimization examples and best practices
- **benchmark.py**: Performance benchmarking script

## Important Notes

- This project emphasizes clean code and proper refactoring patterns
- When adding features, ensure they follow the established architecture
- Maintain test coverage - add tests for new functionality
- Update documentation when making structural changes
- The project uses simple in-memory storage (`_storage` dict) - don't assume a real database
