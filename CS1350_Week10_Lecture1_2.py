def practice_1_basic_exceptions():
    """
    Practice identifying and handling common exceptions
    """
    print("\n" + "=" * 50)
    print("EXERCISE 1: Handle the Exceptions")
    print("=" * 50)

    # TODO 1: Fix division by zero
    def safe_divide(a, b):
        """Return a/b or None if division by zero"""
        # Add try-except block here
        pass  # Replace with your code

    # Test your function
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")

    # TODO 2: Fix list index error
    def safe_get_item(lst, index):
        """Get item at index or return 'Not found'"""
        # try:
        pass

    # Test your function
    my_list = [1, 2, 3]
    print(f"Item at index 1: {safe_get_item(my_list, 1)}")
    print(f"Item at index 10: {safe_get_item(my_list, 10)}")

    # TODO 3: Handle multiple exceptions
    def convert_to_number(value):
        """Convert string to int or float, return None if impossible"""
        try:
            return int(value)
        except ValueError:
            print(f"{value} can't be converted")
        except Exception as e:
            print(f"{e.args}")

    # Test conversions
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = convert_to_number(val)
        print(f"Converting '{val}': {result}")


# Run the practice
practice_1_basic_exceptions()


def practice_2_exception_hierarchy():
    """
    Practice with exception hierarchy
    """
    print("\n" + "=" * 50)
    print("EXERCISE 2: Exception Hierarchy")
    print("=" * 50)

    # TODO 1: Catch multiple related exceptions efficiently
    def access_data(data_structure, key):
        """
        Access data[key] whether data is list or dict.
        Return None if key doesn't exist.
        """
        try:
            return data_structure[key]
        except LookupError:  # TODO: Replace with appropriate parent exception
            return None

    # Test with different data structures
    test_list = [10, 20, 30]
    test_dict = {"a": 1, "b": 2}

    print(f"List[1]: {access_data(test_list, 1)}")
    print(f"List[10]: {access_data(test_list, 10)}")
    print(f"Dict['a']: {access_data(test_dict, 'a')}")
    print(f"Dict['z']: {access_data(test_dict, 'z')}")

    # TODO 2: Order exception handlers correctly
    def parse_value(value):
        """
        Try to parse value as int, then float, then return as string.
        """
        # TODO: Fix the order of exception handlers
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError):
                return str(value)  # Add specific exceptions in correct order

    # Test parsing
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = parse_value(val)
        print(f"Parsing '{val}': {result} (type: {type(result).__name__})")


# Run the practice
practice_2_exception_hierarchy()


def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "=" * 50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("=" * 50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            # TODO: Open file
            file = open(filename)
            return file.read()
        except FileNotFoundError:
            # TODO: Handle missing file
            return None
        except PermissionError:
            # TODO: Handle permission issues
            return None
        else:
            # TODO: Process file content (only if opened successfully)
            print("Processing file...")
        finally:
            # TODO: Ensure file is closed
            print("Closing file")

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            # TODO: Implement with possible RuntimeError
            pass

        def release(self):
            """Release resource - must always happen."""
            # TODO: Implement cleanup
            pass

        def use(self):
            """Use resource - only if acquired."""
            # TODO: Implement usage
            pass

    # Test resource management
    rm = ResourceManager("Database")
    # TODO: Use try-except-else-finally to manage resource


# Run the practice
practice_3_complete_pattern()
