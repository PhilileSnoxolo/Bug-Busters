# CleanCity: Waste Pickup Scheduler - Test Plan

## Project Overview
CleanCity is a web-based application designed to help users manage waste pickup services efficiently. Users can:

- Create an account and log in

- Access a personalized dashboard

- Schedule and monitor waste pickup requests

- Provide feedback on services received

Additionally, administrators have the ability to oversee all requests and update their statuses as needed.

### Application: CleanCity Waste Pickup Scheduler

### Type: Web Application (HTML, CSS, JavaScript)

### Purpose: Allow users to schedule waste pickup services, track requests, and provide feedback

## Key Features to Test

Authentication Flow Testing

Form Validation Testing

Dashboard Functionality

Admin Panel Testing

Core Functionality Testing

Data Validation Testing

User Experience Testing

## Testing Strategy

We will use **Jest** to perform the following types of testing:

### Unit Testing
- Validate individual functions
- Check form validation logic (e.g., required fields, email formats)

### UI Interaction (Simulated DOM Testing)
- Simulate button clicks, form submissions
- Check visible feedback messages
- Show/hide elements based on login role

## Components to Test

| Component              | Test Scenarios |
|------------------------|----------------|
| **Login Form**         | Email/password validation, error messages |
| **Register Form**      | Password confirmation, empty fields |
| **Pickup Request Form**| Dropdowns, radio buttons, required fields |
| **Dashboard Filters**  | Filter by status/location |
| **Feedback Form**      | Valid/invalid request ID, reason selection |
| **Admin Panel**        | Admin-only visibility, status updates |

---

## 🛠 Tools & Environment
- Test Runner: **Jest**

- Setup command: `npm install jest` 

- Tests will be located in `/tests/` folder