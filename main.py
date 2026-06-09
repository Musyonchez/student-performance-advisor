from knowledge_base import run_inference, FACTS


def get_int(prompt, lo=0, hi=100):
    while True:
        try:
            val = int(input(prompt))
            if lo <= val <= hi:
                return val
            print(f"  Please enter a value between {lo} and {hi}.")
        except ValueError:
            print("  Invalid input. Enter a whole number.")


def get_float(prompt, lo=0):
    while True:
        try:
            val = float(input(prompt))
            if val >= lo:
                return val
            print(f"  Please enter a value of {lo} or more.")
        except ValueError:
            print("  Invalid input. Enter a number.")


def get_bool(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("  Enter y or n.")


def main():
    print("=" * 55)
    print("   STUDENT PERFORMANCE ADVISOR – Knowledge-Based System")
    print("=" * 55)

    student = {
        "grade":               get_int("\nCurrent grade (0-100): "),
        "attendance":          get_int("Attendance percentage (0-100): "),
        "assignments_submitted": get_int("Assignments submitted % (0-100): "),
        "study_hours":         get_float("Average study hours per day: "),
        "has_prior_failures":  get_bool("Any prior module failures? (y/n): "),
    }

    wm, fired_rules = run_inference(student)

    print("\n" + "=" * 55)
    print("  REASONING TRACE")
    print("=" * 55)
    for rule in fired_rules:
        print(f"\n  [{rule['id']}] {rule['name']}")
        print(f"       IF   {rule['if']}")
        print(f"       THEN {rule['then']}")
        print(f"       WHY  {rule['explanation']}")

    print("\n" + "=" * 55)
    print("  CONCLUSION")
    print("=" * 55)
    print(f"\n  >>> {wm['conclusion']} <<<")

    if wm["recommendations"]:
        print("\n  Recommendations:")
        for i, rec in enumerate(wm["recommendations"], 1):
            print(f"    {i}. {rec}")
    else:
        print("\n  No additional recommendations — keep up the good work!")

    print("\n" + "=" * 55)


if __name__ == "__main__":
    main()
