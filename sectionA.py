"""Student grade management system."""

MIN_GRADE = 0.0
MAX_GRADE = 100.0
HONOR_THRESHOLD = 90.0
PASS_THRESHOLD = 60.0
LETTER_THRESHOLDS = ((90.0, "A"), (80.0, "B"), (70.0, "C"), (60.0, "D"))


class Student:
    """A student with an ID, a name and a list of grades."""

    def __init__(self, student_id, name):
        """Create a student, the ID and the name must not be empty."""
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")
        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []

    def add_grade(self, grade):
        """Add a numeric grade between 0 and 100."""
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            raise ValueError(f"Grade must be numeric: {grade!r}")
        if not MIN_GRADE <= grade <= MAX_GRADE:
            raise ValueError(f"Grade must be between 0 and 100: {grade}")
        self.grades.append(float(grade))

    def remove_grade_at(self, index):
        """Remove the grade at the given index."""
        if not isinstance(index, int) or not 0 <= index < len(self.grades):
            raise ValueError(f"Invalid grade index: {index!r}")
        del self.grades[index]

    def remove_grade_by_value(self, value):
        """Remove the first grade equal to the given value."""
        if value not in self.grades:
            raise ValueError(f"Grade not found: {value!r}")
        self.grades.remove(value)

    def calculate_average(self):
        """Return the average of all grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Return the letter grade for the average."""
        average = self.calculate_average()
        for threshold, letter in LETTER_THRESHOLDS:
            if average >= threshold:
                return letter
        return "F"

    def is_passed(self):
        """Return True if the average is 60 or higher."""
        return self.calculate_average() >= PASS_THRESHOLD

    def is_honor_roll(self):
        """Return True if the average is 90 or higher."""
        return self.calculate_average() >= HONOR_THRESHOLD

    def generate_report(self):
        """Return the summary report of the student."""
        status = "Passed" if self.is_passed() else "Failed"
        honor = "Yes" if self.is_honor_roll() else "No"
        return (
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Number of Grades: {len(self.grades)}\n"
            f"Average: {self.calculate_average():.2f}\n"
            f"Letter Grade: {self.get_letter_grade()}\n"
            f"Status: {status}\n"
            f"Honor Roll: {honor}"
        )


def main():
    """Run a demo of the student grade system."""
    try:
        Student("", "Ana")
    except ValueError as error:
        print(f"Error: {error}")

    student = Student("x", "Ana Perez")
    for grade in (100, 95.5, "Fifty", 120, -5, 72.5):
        try:
            student.add_grade(grade)
        except ValueError as error:
            print(f"Error: {error}")

    for action, argument in (
        (student.remove_grade_at, 5),
        (student.remove_grade_by_value, 72.5),
    ):
        try:
            action(argument)
        except ValueError as error:
            print(f"Error: {error}")

    print(student.generate_report())


if __name__ == "__main__":
    main()