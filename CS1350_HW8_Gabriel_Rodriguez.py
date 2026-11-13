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
        try:
            return a / b
        except ZeroDivisionError:
            return None

    # Test your function
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")

    # TODO 2: Fix list index error
    def safe_get_item(lst, index):
        """Get item at index or return 'Not found'"""
        # Add appropriate exception handling
        try:
            return lst[index]
        except IndexError:
            return "Not found"

    # Test your function
    my_list = [1, 2, 3]
    print(f"Item at index 1: {safe_get_item(my_list, 1)}")
    print(f"Item at index 10: {safe_get_item(my_list, 10)}")

    # TODO 3: Handle multiple exceptions
    def convert_to_number(value):
        """Convert string to int or float, return None if impossible"""
        # Try int first, then float, handle ValueError
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError):
                return None

    # Test conversions
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = convert_to_number(val)
        print(f"Converting '{val}': {result}")


# Run the practice
practice_1_basic_exceptions()


def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "=" * 50)
    print("EXERCISE 5: Custom Exceptions")
    print("=" * 50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""

        def __init__(self, message="A game error occurred"):
            super().__init__(message)

    class InvalidMoveError(GameError):
        """Invalid game move."""

        # TODO: Add __init__ with position and reason
        def __init__(self, reason, column, row):
            self.reason = reason
            self.column = column
            self.row = row
            super().__init__(f"{reason}: {column}, {row} (Invalid move)")

    class GameOverError(GameError):
        """Game has ended."""

        # TODO: Add __init__ with winner
        def __init__(self, winner):
            self.winner = winner
            message = (
                "It's a draw!" if winner is None else f"Player {winner} already won!"
            )
            super().__init__(message)

    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[" " for _ in range(3)] for _ in range(3)]
            self.current_player = "X"
            self.game_over = False

        def make_move(self, row, col):
            # TODO: Raise GameOverError if game_over is True
            if self.game_over:
                raise GameOverError(None)
            # TODO: Raise InvalidMoveError if position is out of bounds
            if not (0 <= row < 3 and 0 <= col < 3):
                raise InvalidMoveError("Out of bounds", col, row)
            # TODO: Raise InvalidMoveError if position is taken
            if self.board[row][col] != " ":
                raise InvalidMoveError("Position taken", col, row)
            self.board[row][col] = self.current_player

    # Test the game
    game = TicTacToe()

    test_moves = [
        (0, 0),  # Valid
        (0, 0),  # Already taken
        (5, 5),  # Out of bounds
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")


# Run the practice
practice_2_custom_exceptions()


def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    print("\n" + "=" * 50)
    print("EXERCISE 6: Complete Error Handler")
    print("=" * 50)

    # TODO: Build a file processing system with proper error handling

    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            # TODO: Implement with try-except-else-finally
            f = None
            try:
                f = open(filename)
                f.read()
            # TODO: Handle FileNotFoundError
            except FileNotFoundError:
                self.failed_files.append(filename)
            # TODO: Handle PermissionError
            except PermissionError:
                self.failed_files.append(filename)
            # TODO: Handle general exceptions
            except Exception:
                self.failed_files.append(filename)
            else:
                self.processed_files.append(filename)
            # TODO: Ensure file is closed
            finally:
                if f:
                    f.close()

        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            import os

            # TODO: Process each file
            # TODO: Continue on errors
            # TODO: Track successes and failures
            for name in os.listdir(directory):
                self.process_file(os.path.join(directory, name))

        def get_report(self):
            """
            Get processing report.
            """
            # TODO: Return summary of processing
            return {"processed": self.processed_files, "failed": self.failed_files}

    # Test the processor
    processor = FileProcessor()

    test_files = ["valid.txt", "missing.txt", "/root/restricted.txt"]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")


# Run the practice
practice_3_complete_system()
