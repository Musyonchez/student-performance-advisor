# Test Cases - Student Performance Advisor

---

## Test Case 1 - High Achiever

**Input**

| Field | Value |
|---|---|
| Grade | 90 |
| Attendance | 95% |
| Assignments submitted | 100% |
| Study hours/day | 5 |
| Prior failures | No |

**Expected conclusion:** PASS - Performing Well  
**Expected recommendation:** Consider enrolling in advanced or Honours modules.

**Rules fired:** R01, R04, R07, R10, R13, R22  
**Result:** ✅ Pass

---

## Test Case 2 - Failing Student

**Input**

| Field | Value |
|---|---|
| Grade | 35 |
| Attendance | 45% |
| Assignments submitted | 55% |
| Study hours/day | 1 |
| Prior failures | Yes |

**Expected conclusion:** FAIL - Requires Intervention  
**Expected recommendations:** Increase study hours, improve attendance, complete assignments, seek counselling.

**Rules fired:** R03, R06, R09, R12, R14, R18, R19, R20, R21  
**Result:** ✅ Pass

---

## Test Case 3 - Borderline Student

**Input**

| Field | Value |
|---|---|
| Grade | 62 |
| Attendance | 72% |
| Assignments submitted | 80% |
| Study hours/day | 3 |
| Prior failures | No |

**Expected conclusion:** AT RISK - Needs Improvement  
**Expected recommendation:** None (moderate study, average everything).

**Rules fired:** R02, R05, R08, R11, R16  
**Result:** ✅ Pass

---

## Test Case 4 - Good Grades, Poor Attendance

**Input**

| Field | Value |
|---|---|
| Grade | 78 |
| Attendance | 50% |
| Assignments submitted | 92% |
| Study hours/day | 4 |
| Prior failures | No |

**Expected conclusion:** AT RISK - Needs Improvement  
**Expected recommendation:** Improve class attendance to at least 80%.

**Rules fired:** R01, R06, R07, R10, R15, R19  
**Result:** ✅ Pass

---

## Test Case 5 - Poor Grade but Good Attendance

**Input**

| Field | Value |
|---|---|
| Grade | 42 |
| Attendance | 85% |
| Assignments submitted | 75% |
| Study hours/day | 1.5 |
| Prior failures | No |

**Expected conclusion:** AT RISK - Needs Improvement  
**Expected recommendations:** Increase daily study hours to at least 4 hours per day.

**Rules fired:** R03, R04, R08, R12, R17, R18  
**Result:** ✅ Pass

---

## Summary

| # | Grade | Attendance | Assignments | Study hrs | Conclusion |
|---|---|---|---|---|---|
| 1 | 90 | 95% | 100% | 5 | PASS |
| 2 | 35 | 45% | 55% | 1 | FAIL |
| 3 | 62 | 72% | 80% | 3 | AT RISK |
| 4 | 78 | 50% | 92% | 4 | AT RISK |
| 5 | 42 | 85% | 75% | 1.5 | AT RISK |
