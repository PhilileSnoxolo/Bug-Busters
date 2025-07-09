#  BUG BUSTERS

##  Week 2 Test Plan Update: CleanCity Waste Pickup Scheduler

### 1. System Under Test (SUT)
No changes — the system remains a single-page web application with:
- Roles: Regular User & Admin
- Modules: Login, Register, Pickup Form, Feedback, Dashboard, Admin Panel, Awareness
- Data Persistence: `localStorage` only

---

### 2. Tools & Technologies (Updated)
| Category              | Tools Used                          |
|-----------------------|-------------------------------------|
| Test Management       | JIRA                                |
| Unit Testing          | Manual (Jest stubs in progress)     |
| UI Testing            | Manual, Selenium (planned)          |
| Static Analysis       | SonarQube (early review)            |
| Bug Logging           | GitHub Issues + `defect-log.md`     |
| Methodology           | Agile                               |

---

### 3. Week 2 Testing Focus Areas

- Completed **manual test case drafting**
- Started testing **form validation**, **navigation**, and **role-based behavior**
- Logged early **functional bugs** (see defect log)
- Ran **static code scan manually** and identified critical issues (plaintext passwords, weak validation, hardcoded filters)

---

### 4. Enhancements to Test Strategy

| Test Level          | Week 2 Action                                      |
|---------------------|----------------------------------------------------|
| Unit Testing        | Began `login.test.js` using basic credential logic |
| Integration Testing | Tested login > dashboard > feedback transitions    |
| System Testing      | Verified full user journey with mock users         |
| Regression Testing  | Logged recurring filter bug in dashboard           |
| Security Scanning   | Reviewed user storage logic for auth vulnerabilities |

---

### 5. Summary of Executed Manual Test Cases (See `test-cases.md`)
| Area         | Status        |
|--------------|---------------|
| Login        | ✅ Executed    |
| Registration | ✅ Executed    |
| Pickup Form  | ✅ Executed    |
| Feedback     | ✅ Executed    |
| Dashboard    | ✅ Executed    |
| Admin Panel  | ✅ Executed    |
| Navigation   | ✅ Verified by Role |

---

### 6. Key Bugs Identified (See `defect-log.md`)
| Bug ID   | Description                               | Severity |
|----------|-------------------------------------------|----------|
| BUG001   | Eldoret filter returns Nairobi results    | Major    |
| BUG002   | Passwords stored in plain text            | Critical |
| BUG003   | Feedback comments field allows blank      | Minor    |
| BUG004   | No validation for preferred pickup date   | Minor    |
| BUG005   | Name field accepts very short strings     | Medium   |

---

### 7. Planned Next Steps for Week 3

- Convert core manual tests to **automated Jest tests**
- Integrate **Selenium UI tests** (login, pickup, dashboard)
- Begin writing **regression tests** for fixed bugs
- Propose **fixes** for validation and security issues

---

### 8. Changes from Week 1 Plan

| Section             | Update Description                                 |
|---------------------|----------------------------------------------------|
| Tools               | Manual testing extended, Jest stubs started        |
| Strategy            | Added static + security analysis                   |
| Bugs & Risks        | Documented in `defect-log.md`                      |
| Test Coverage       | 6 functional modules fully covered manually        |
| CI/CD               | Still planned — not yet implemented                |

---

### 9. Challenges Faced

- LocalStorage resets on refresh — makes tracking persistent data harder
- No backend/API — security testing limited to frontend only
- Some form validations are inconsistent (length checks, empty fields)
- Dynamic rendering made some test case automation harder

---

### 10. Conclusion

Progressed from planning to actual manual testing and bug discovery. We now have enough coverage to move into automated testing and bug regression for Week 3.

