<<<<<<< HEAD
# BUG BUSTERS

# Test Plan: CleanCity Waste Pickup Scheduler

## 1. System Under Test (SUT)

A web-based waste pickup management platform with:

- User roles: Regular User & Admin
- Core modules: Login, Register, Pickup Request Form, Feedback, Dashboard, Admin Panel, Awareness Page
- Technologies: HTML, CSS, JavaScript, LocalStorage (for mock data persistence)

## 2. Tools & Technologies Used

| Category                 | Tools                                          |
| ------------------------ | ---------------------------------------------- |
| **Test Management**      | JIRA                                           |
| **Automated Testing**    | Selenium, Mocha, Jest, PyTest, JUnit           |
| **Static Code Analysis** | SonarQube                                      |
| **Methodology**          | Agile (Scrum/Kanban practices)                 |
| **CI/CD**                | (To be integrated later, e.g., GitHub Actions) |
| **Test Execution**       | Manual Testing & Automated Testing (UI + Unit) |

## 3. Test Strategy

### Testing Types

- **Static Testing**: Code reviews, linting, SonarQube scanning
- **Dynamic Testing**:
  - Unit Testing (Jest, Mocha, PyTest)
  - Functional Testing (Manual)
  - Integration Testing
  - Regression Testing
  - End-to-End UI Testing (Selenium)

### Testing Levels

- **Unit Tests** – JS logic, validation, form handlers
- **Integration Tests** – Navigation, role-based UI behavior
- **System Tests** – Whole user flow: Register → Login → Request Pickup → View Dashboard → Submit Feedback
- **Acceptance Tests** – Based on user stories and acceptance criteria

## 4. Test Plan Objectives

- Ensure all form validations are working
- Ensure user role access behaves as expected (user/admin)
- Confirm storage and retrieval of data (localStorage)
- Validate UI responsiveness and correctness

## 5. Test Suites Overview

| Test Suite                | Purpose                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------- |
| **Authentication Suite**  | Test login, logout, registration logic and error handling                               |
| **Form Validation Suite** | Validate all required form fields and validation messages                               |
| **Dashboard Suite**       | Ensure data is correctly rendered and filtered                                          |
| **Admin Suite**           | Ensure admin functionalities (status update, statistics) work as expected               |
| **Feedback Suite**        | Validate feedback form submission and UI flow                                           |
| **Navigation Suite**      | Confirm menu links and page visibility by role                                          |
| **Security Suite**        | Check for lack of encryption, direct access bypass, weak passwords (manual+static scan) |

## 6. Sample Test Cases (Manual & Automated)

### Login Tests

| TC ID  | Test Case                    | Type               | Expected Result       |
| ------ | ---------------------------- | ------------------ | --------------------- |
| TC-001 | Login with valid credentials | Manual + Automated | Redirect to Dashboard |
| TC-002 | Login with wrong password    | Manual             | Error message shown   |
| TC-003 | Login as admin               | Manual + Automated | Admin tab is visible  |

### Registration Tests

| TC ID  | Test Case                    | Type            | Expected Result        |
| ------ | ---------------------------- | --------------- | ---------------------- |
| TC-010 | Register with valid data     | Manual          | Success message        |
| TC-011 | Register with existing email | Manual          | “Email exists” error   |
| TC-012 | Password too short           | Static + Manual | Validation error shown |

### Pickup Form Tests

| TC ID  | Test Case                   | Type              | Expected Result          |
| ------ | --------------------------- | ----------------- | ------------------------ |
| TC-020 | Submit valid request        | Manual + Selenium | Confirmation alert       |
| TC-021 | Missing full name           | Manual            | Error message shown      |
| TC-022 | Select hazardous waste type | Manual            | Field accepted and saved |

### Dashboard & Filtering

| TC ID  | Test Case                    | Type                | Expected Result                                    |
| ------ | ---------------------------- | ------------------- | -------------------------------------------------- |
| TC-030 | Filter by ‘Pending’          | Manual + Automated  | Only pending shown                                 |
| TC-031 | Filter by city (Eldoret bug) | Manual + Bug Report | Eldoret wrongly shows Nairobi data (Bug confirmed) |

### Admin Panel

| TC ID  | Test Case                               | Type   | Expected Result                 |
| ------ | --------------------------------------- | ------ | ------------------------------- |
| TC-040 | Update status to Completed              | Manual | Data updates and reflects in UI |
| TC-041 | Unauthorized user tries to access Admin | Manual | Redirected to login page        |

## 7. Static Code Analysis Plan

Tool: **SonarQube**

- Check for:
  - Plaintext password storage (high severity)
  - Validation bypass risks
  - Broken access controls
  - Duplicate code or unused functions

## 8. Test Management

- **JIRA Integration**
  - User stories linked to test cases
  - Sprint-based test execution reports
- **Defect Tracking**:
  - All bugs logged with severity, steps to reproduce, screenshots

## 9. Schedule (Agile Context)

| Sprint   | Activity                                  |
| -------- | ----------------------------------------- |
| Sprint 1 | Test Planning, Tool Setup, Static Testing |
| Sprint 2 | Manual Test Case Design, Unit Test Stubs  |
| Sprint 3 | Execute Tests, Bug Fixes, Regression      |
| Sprint 4 | Retesting, Final Report, Demo             |

## 10. Entry & Exit Criteria

### Entry Criteria:

- Code is committed & reviewed
- Development is completed for a module
- Dev environment is stable

### Exit Criteria:

- 95% test cases passed
- All critical bugs resolved
- Code scanned and accepted by SonarQube

## 11. Reporting

- Daily standup bug updates
- Weekly Test Summary Reports
- Final Test Plan Document submitted
=======
# BUG BUSTERS

# Test Plan: CleanCity Waste Pickup Scheduler

## 1. System Under Test (SUT)

A web-based waste pickup management platform with:

- **User roles**: Regular User & Admin
- **Core modules**: Login, Register, Pickup Request Form, Feedback, Dashboard, Admin Panel, Awareness Page
- **Technologies**: HTML, CSS, JavaScript, LocalStorage (for mock data persistence)

## 2. Tools & Technologies Used

| Category                 | Tools                                          |
| ------------------------ | ---------------------------------------------- |
| **Test Management**      | JIRA                                           |
| **Automated Testing**    | Selenium, Mocha, Jest, PyTest, JUnit           |
| **Static Code Analysis** | SonarQube                                      |
| **Methodology**          | Agile (Scrum/Kanban practices)                 |
| **CI/CD**                | (To be integrated later, e.g., GitHub Actions) |
| **Test Execution**       | Manual Testing & Automated Testing (UI + Unit) |

## 3. Test Strategy

### Testing Types

- **Static Testing**: Code reviews, linting, SonarQube scanning
- **Dynamic Testing**:
  - Unit Testing (Jest, Mocha, PyTest)
  - Functional Testing (Manual)
  - Integration Testing
  - Regression Testing
  - End-to-End UI Testing (Selenium)

### Testing Levels

- **Unit Tests** – JS logic, validation, form handlers
- **Integration Tests** – Navigation, role-based UI behavior
- **System Tests** – Whole user flow: Register → Login → Request Pickup → View Dashboard → Submit Feedback
- **Acceptance Tests** – Based on user stories and acceptance criteria

## 4. Test Plan Objectives

- **Form Validations** - Ensure all form validations are working
- **User Role Access** - Ensure user role access behaves as expected (user/admin)
- **Data Storage and Retrieval** - Confirm storage and retrieval of data (localStorage)
- **UI Responsiveness and Correctness** - Validate UI responsiveness and correctness

## 5. Test Suites Overview

| Test Suite                | Purpose                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------- |
| **Authentication Suite**  | Test login, logout, registration logic and error handling                               |
| **Form Validation Suite** | Validate all required form fields and validation messages                               |
| **Dashboard Suite**       | Ensure data is correctly rendered and filtered                                          |
| **Admin Suite**           | Ensure admin functionalities (status update, statistics) work as expected               |
| **Feedback Suite**        | Validate feedback form submission and UI flow                                           |
| **Navigation Suite**      | Confirm menu links and page visibility by role                                          |
| **Security Suite**        | Check for lack of encryption, direct access bypass, weak passwords (manual+static scan) |

## 6. Sample Test Cases (Manual & Automated)

### Login Tests

| TC ID  | Test Case                    | Type               | Expected Result       |
| ------ | ---------------------------- | ------------------ | --------------------- |
| TC-001 | Login with valid credentials | Manual + Automated | Redirect to Dashboard |
| TC-002 | Login with wrong password    | Manual             | Error message shown   |
| TC-003 | Login as admin               | Manual + Automated | Admin tab is visible  |

### Registration Tests

| TC ID  | Test Case                    | Type            | Expected Result        |
| ------ | ---------------------------- | --------------- | ---------------------- |
| TC-010 | Register with valid data     | Manual          | Success message        |
| TC-011 | Register with existing email | Manual          | “Email exists” error   |
| TC-012 | Password too short           | Static + Manual | Validation error shown |

### Pickup Form Tests

| TC ID  | Test Case                   | Type              | Expected Result          |
| ------ | --------------------------- | ----------------- | ------------------------ |
| TC-020 | Submit valid request        | Manual + Selenium | Confirmation alert       |
| TC-021 | Missing full name           | Manual            | Error message shown      |
| TC-022 | Select hazardous waste type | Manual            | Field accepted and saved |

### Dashboard & Filtering

| TC ID  | Test Case                    | Type                | Expected Result                                    |
| ------ | ---------------------------- | ------------------- | -------------------------------------------------- |
| TC-030 | Filter by ‘Pending’          | Manual + Automated  | Only pending shown                                 |
| TC-031 | Filter by city (Eldoret bug) | Manual + Bug Report | Eldoret wrongly shows Nairobi data (Bug confirmed) |

### Admin Panel

| TC ID  | Test Case                               | Type   | Expected Result                 |
| ------ | --------------------------------------- | ------ | ------------------------------- |
| TC-040 | Update status to Completed              | Manual | Data updates and reflects in UI |
| TC-041 | Unauthorized user tries to access Admin | Manual | Redirected to login page        |

## 7. Static Code Analysis Plan

Tool: **SonarQube**

- Check for:
  - Plaintext password storage (high severity)
  - Validation bypass risks
  - Broken access controls
  - Duplicate code or unused functions

## 8. Test Management

- **JIRA Integration**
  - User stories linked to test cases
  - Sprint-based test execution reports
- **Defect Tracking**:
  - All bugs logged with severity, steps to reproduce, screenshots

## 9. Schedule (Agile Context)

| Sprint   | Activity                                  |
| -------- | ----------------------------------------- |
| Sprint 1 | Test Planning, Tool Setup, Static Testing |
| Sprint 2 | Manual Test Case Design, Unit Test Stubs  |
| Sprint 3 | Execute Tests, Bug Fixes, Regression      |
| Sprint 4 | Retesting, Final Report, Demo             |

## 10. Entry & Exit Criteria

### Entry Criteria:

- Code is committed & reviewed
- Development is completed for a module
- Dev environment is stable

### Exit Criteria:

- 95% test cases passed
- All critical bugs resolved
- Code scanned and accepted by SonarQube

## 11. Reporting

- Daily standup bug updates
- Weekly Test Summary Reports
- Final Test Plan Document submitted
>>>>>>> f712e875776abbd2272200b29419716254070b29
