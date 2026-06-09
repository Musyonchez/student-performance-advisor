FACTS = {
    "grade_pass_threshold":       75,
    "grade_average_lower":        50,
    "attendance_good_threshold":  80,
    "attendance_average_lower":   60,
    "assignment_good_threshold":  90,
    "assignment_average_lower":   70,
    "study_hours_sufficient":      4,
    "study_hours_moderate":        2,
    "excellence_grade":           85,
    "maximum_grade":             100,
    "maximum_attendance":        100,
    "minimum_pass_assignments":   70,
    "risk_factor_count_high":      2,
    "academic_year_semesters":     2,
    "weekly_contact_hours":       20,
}

POSSIBLE_CONCLUSIONS = [
    "PASS - Performing Well",
    "AT RISK - Needs Improvement",
    "FAIL - Requires Intervention",
]


RULES = [
    # Phase 1 – classify inputs
    {"id": "R01", "name": "Good Academic Performance",
     "if": "grade >= 75", "then": "academic_performance = good",
     "explanation": "A grade of 75 or above meets the pass threshold."},
    {"id": "R02", "name": "Average Academic Performance",
     "if": "50 <= grade < 75", "then": "academic_performance = average",
     "explanation": "A grade between 50 and 74 is borderline."},
    {"id": "R03", "name": "Poor Academic Performance",
     "if": "grade < 50", "then": "academic_performance = poor",
     "explanation": "A grade below 50 indicates failing performance."},

    {"id": "R04", "name": "Good Attendance",
     "if": "attendance >= 80%", "then": "attendance_status = good",
     "explanation": "Attendance of 80% or more supports learning outcomes."},
    {"id": "R05", "name": "Average Attendance",
     "if": "60% <= attendance < 80%", "then": "attendance_status = average",
     "explanation": "Attendance between 60% and 79% means some content is missed."},
    {"id": "R06", "name": "Poor Attendance",
     "if": "attendance < 60%", "then": "attendance_status = poor",
     "explanation": "Attendance below 60% means significant instructional time is lost."},

    {"id": "R07", "name": "Good Assignment Completion",
     "if": "assignments_submitted >= 90%", "then": "assignment_status = good",
     "explanation": "Submitting 90%+ of assignments shows consistent effort."},
    {"id": "R08", "name": "Average Assignment Completion",
     "if": "70% <= assignments_submitted < 90%", "then": "assignment_status = average",
     "explanation": "Submitting 70-89% of assignments is acceptable but improvable."},
    {"id": "R09", "name": "Poor Assignment Completion",
     "if": "assignments_submitted < 70%", "then": "assignment_status = poor",
     "explanation": "Fewer than 70% submitted means lost marks on the final grade."},

    {"id": "R10", "name": "Sufficient Study Hours",
     "if": "study_hours >= 4", "then": "study_status = sufficient",
     "explanation": "Studying 4+ hours per day provides adequate preparation."},
    {"id": "R11", "name": "Moderate Study Hours",
     "if": "2 <= study_hours < 4", "then": "study_status = moderate",
     "explanation": "Studying 2-3 hours per day is moderate; more is advisable."},
    {"id": "R12", "name": "Insufficient Study Hours",
     "if": "study_hours < 2", "then": "study_status = insufficient",
     "explanation": "Fewer than 2 hours per day is not enough to keep up with coursework."},

    # Phase 2 – determine conclusion
    {"id": "R13", "name": "Student is Passing",
     "if": "academic_performance = good AND attendance_status in [good, average]",
     "then": "conclusion = PASS",
     "explanation": "Good grade with adequate attendance means the student is on track."},
    {"id": "R14", "name": "Student Requires Intervention",
     "if": "academic_performance = poor AND attendance_status = poor",
     "then": "conclusion = FAIL",
     "explanation": "Poor grade AND poor attendance signal a critical situation."},
    {"id": "R15", "name": "Good Grade but Attendance Risk",
     "if": "academic_performance = good AND attendance_status = poor",
     "then": "conclusion = AT RISK",
     "explanation": "Good grades undermined by poor attendance puts future performance at risk."},
    {"id": "R16", "name": "Average Grade is Borderline",
     "if": "academic_performance = average",
     "then": "conclusion = AT RISK",
     "explanation": "An average grade is borderline; improvement is needed to secure a pass."},
    {"id": "R17", "name": "Poor Grade Despite Attendance",
     "if": "academic_performance = poor AND attendance_status in [good, average]",
     "then": "conclusion = AT RISK",
     "explanation": "Poor grade despite attending suggests an understanding problem that can still be fixed."},

    # Phase 3 – recommendations
    {"id": "R18", "name": "Increase Study Time",
     "if": "study_status = insufficient",
     "then": "recommend: Increase daily study hours to at least 4 hours.",
     "explanation": "Insufficient study time is a strong predictor of academic failure."},
    {"id": "R19", "name": "Improve Attendance",
     "if": "attendance_status = poor",
     "then": "recommend: Improve class attendance to at least 80%.",
     "explanation": "Missing classes creates knowledge gaps and missed assessments."},
    {"id": "R20", "name": "Complete Outstanding Assignments",
     "if": "assignment_status = poor",
     "then": "recommend: Complete and submit all outstanding assignments immediately.",
     "explanation": "Each unsubmitted assignment directly reduces the final grade."},
    {"id": "R21", "name": "Seek Counselling",
     "if": "has_prior_failures = True AND conclusion != PASS",
     "then": "recommend: Seek academic counselling given prior failure history.",
     "explanation": "Repeated failures alongside current struggles indicate systemic issues."},
    {"id": "R22", "name": "Consider Advanced Modules",
     "if": "conclusion = PASS AND grade >= 85",
     "then": "recommend: Consider enrolling in advanced or Honours modules.",
     "explanation": "A grade of 85+ with adequate attendance qualifies for advanced coursework."},
]


def run_inference(student_data):
    wm = dict(student_data)
    wm["recommendations"] = []
    fired = []

    f = FACTS

    # Phase 1: classify
    g = wm["grade"]
    if g >= f["grade_pass_threshold"]:
        wm["academic_performance"] = "good"
        fired.append(RULES[0])
    elif g >= f["grade_average_lower"]:
        wm["academic_performance"] = "average"
        fired.append(RULES[1])
    else:
        wm["academic_performance"] = "poor"
        fired.append(RULES[2])

    a = wm["attendance"]
    if a >= f["attendance_good_threshold"]:
        wm["attendance_status"] = "good"
        fired.append(RULES[3])
    elif a >= f["attendance_average_lower"]:
        wm["attendance_status"] = "average"
        fired.append(RULES[4])
    else:
        wm["attendance_status"] = "poor"
        fired.append(RULES[5])

    asn = wm["assignments_submitted"]
    if asn >= f["assignment_good_threshold"]:
        wm["assignment_status"] = "good"
        fired.append(RULES[6])
    elif asn >= f["assignment_average_lower"]:
        wm["assignment_status"] = "average"
        fired.append(RULES[7])
    else:
        wm["assignment_status"] = "poor"
        fired.append(RULES[8])

    sh = wm["study_hours"]
    if sh >= f["study_hours_sufficient"]:
        wm["study_status"] = "sufficient"
        fired.append(RULES[9])
    elif sh >= f["study_hours_moderate"]:
        wm["study_status"] = "moderate"
        fired.append(RULES[10])
    else:
        wm["study_status"] = "insufficient"
        fired.append(RULES[11])

    # Phase 2: conclude
    perf, att = wm["academic_performance"], wm["attendance_status"]
    if perf == "good" and att in ("good", "average"):
        wm["conclusion"] = POSSIBLE_CONCLUSIONS[0]
        fired.append(RULES[12])
    elif perf == "poor" and att == "poor":
        wm["conclusion"] = POSSIBLE_CONCLUSIONS[2]
        fired.append(RULES[13])
    elif perf == "good" and att == "poor":
        wm["conclusion"] = POSSIBLE_CONCLUSIONS[1]
        fired.append(RULES[14])
    elif perf == "average":
        wm["conclusion"] = POSSIBLE_CONCLUSIONS[1]
        fired.append(RULES[15])
    else:
        wm["conclusion"] = POSSIBLE_CONCLUSIONS[1]
        fired.append(RULES[16])

    # Phase 3: recommend
    if wm["study_status"] == "insufficient":
        wm["recommendations"].append("Increase daily study hours to at least 4 hours.")
        fired.append(RULES[17])
    if wm["attendance_status"] == "poor":
        wm["recommendations"].append("Improve class attendance to at least 80%.")
        fired.append(RULES[18])
    if wm["assignment_status"] == "poor":
        wm["recommendations"].append("Complete and submit all outstanding assignments immediately.")
        fired.append(RULES[19])
    if wm.get("has_prior_failures") and wm["conclusion"] != POSSIBLE_CONCLUSIONS[0]:
        wm["recommendations"].append("Seek academic counselling given prior failure history.")
        fired.append(RULES[20])
    if wm["conclusion"] == POSSIBLE_CONCLUSIONS[0] and wm["grade"] >= f["excellence_grade"]:
        wm["recommendations"].append("Consider enrolling in advanced or Honours modules.")
        fired.append(RULES[21])

    return wm, fired
