# CleanCity Waste Pickup Scheduler – Initial Defect Log (Week 2)

##bug busters!!!

| Bug ID   | Description                                                 | Module             | Severity  | Status  | Notes                                                  |
|----------|-------------------------------------------------------------|--------------------|-----------|---------|--------------------------------------------------------|
| BUG-001  | Eldoret filter returns Nairobi data instead of Eldoret      | Dashboard Filter   | Major     | Open    | Located in `filterRequestsByLocation()` — hardcoded    |
| BUG-002  | Passwords stored in plain text in localStorage              | Auth (Login/Register) | Critical  | Open    | No encryption or hashing applied to password fields    |
| BUG-003  | No validation for "preferred date" in pickup form          | Pickup Form        | Minor     | Open    | Submits with empty or default "Not specified" value    |
| BUG-004  | Feedback form allows empty comments                        | Feedback Form      | Minor     | Open    | Should require user comment to aid feedback tracking   |
| BUG-005  | Name field accepts very short (1-letter) names              | Pickup/Register    | Medium    | Open    | Needs minimum length enforcement                       |
| BUG-006  | Session is not fully cleared on logout                     | Auth               | Medium    | Fixed   | `currentUser` was not removed in some logout flows     |
| BUG-007  | Admin page editable without auth check (direct access)     | Admin Panel        | Critical  | Open    | No role-based redirect enforcement in route handling   |
| BUG-008  | Missing error messages on empty login fields               | Login Form         | Medium    | Open    | Form fails silently unless credentials are invalid     |
| BUG-009  | UI responsiveness issue on narrow screens (table overlap)  | Dashboard (UI)     | Minor     | Open    | Table rows overflow horizontally on < 480px width      |
| BUG-010  | Form resets even on validation error                       | Pickup Form        | Minor     | Open    | Input fields clear even when error is shown            |

---

## Legend:

- **Severity**:
  - 🔴 Critical – Security/data loss or unauthorized access
  - 🟠 Major – Core feature malfunction
  - 🟡 Medium – Impacts usability but not core flow
  - 🟢 Minor – Cosmetic or optional validations

- **Status**:
  - ✅ Fixed – Bug corrected and retested
  - 🔄 Open – Known issue, pending fix
  - ⚠ Deferred – Low priority, scheduled for future phase


#steps to reproduce section using the format Gerald loves..

## CleanCity Waste Pickup Scheduler – Initial Defect Log (Week 2)



###  BUG-001: Eldoret filter returns Nairobi data
- **Module**: Dashboard Filter
- **Severity**: Major
- **Status**: Open
- **Steps to Reproduce**:
  1. Log in as any user.
  2. Navigate to the dashboard.
  3. Select "Eldoret" from the location filter.
  4. Observe that results returned are from "Nairobi".
- **Expected Result**: Only requests from Eldoret should appear.
- **Actual Result**: Requests from Nairobi are shown instead.

---

###  BUG-002: Passwords stored in plain text in localStorage
- **Module**: Login/Register (Auth)
- **Severity**: Critical
- **Status**: Open
- **Steps to Reproduce**:
  1. Register or log in as a new user.
  2. Open browser DevTools → Application → LocalStorage.
  3. Observe the password saved in plain text.
- **Expected Result**: Passwords should be hashed and stored securely (or not stored at all).
- **Actual Result**: Plain text passwords visible in localStorage.

---

###  BUG-003: Preferred date field does not validate
- **Module**: Pickup Form
- **Severity**: Minor
- **Status**: Open
- **Steps to Reproduce**:
  1. Navigate to the Pickup Request form.
  2. Leave the "Preferred Date" empty.
  3. Submit the form.
- **Expected Result**: Validation message requiring a date.
- **Actual Result**: Request is submitted with "Not specified".

---

###  BUG-004: Feedback form allows empty comments
- **Module**: Feedback
- **Severity**: Minor
- **Status**: Open
- **Steps to Reproduce**:
  1. Navigate to the Feedback form.
  2. Enter a valid Request ID and select a reason.
  3. Leave the comments section empty.
  4. Submit the form.
- **Expected Result**: Comments should be required.
- **Actual Result**: Form is accepted without any comments.

---

###  BUG-005: Name field accepts 1-letter names
- **Module**: Register / Pickup
- **Severity**: Medium
- **Status**: Open
- **Steps to Reproduce**:
  1. Go to the registration or pickup form.
  2. Enter a 1-letter name (e.g., "A").
  3. Submit the form.
- **Expected Result**: Error message for short name.
- **Actual Result**: Form allows short names without error.

---

###  BUG-006: Session not fully cleared on logout
- **Module**: Auth
- **Severity**: Medium
- **Status**: Fixed
- **Steps to Reproduce**:
  1. Login as any user.
  2. Click "Logout".
  3. Refresh the page.
- **Expected Result**: No session data should remain.
- **Actual Result**: Some users still detected as logged in.

---

###  BUG-007: Admin page accessible without auth check
- **Module**: Admin Panel
- **Severity**: Critical
- **Status**: Open
- **Steps to Reproduce**:
  1. Login as a regular user.
  2. Manually enter the URL or click the admin tab.
- **Expected Result**: Redirect to login or access denied.
- **Actual Result**: Page loads with editable request options.

---

###  BUG-008: Empty login fields give no feedback
- **Module**: Login Form
- **Severity**: Medium
- **Status**: Open
- **Steps to Reproduce**:
  1. Go to the login page.
  2. Leave email and password empty.
  3. Submit the form.
- **Expected Result**: Display "Fields required" message.
- **Actual Result**: Form tries to submit with no response.

---

### BUG-009: Dashboard table overflows on small screens
- **Module**: Dashboard (UI)
- **Severity**: Minor
- **Status**: Open
- **Steps to Reproduce**:
  1. Open dashboard on mobile screen (< 480px).
  2. View request table.
- **Expected Result**: Responsive table formatting.
- **Actual Result**: Table overflows horizontally.

---

###  BUG-010: Form resets on validation error
- **Module**: Pickup Form
- **Severity**: Minor
- **Status**: Open
- **Steps to Reproduce**:
  1. Open Pickup form.
  2. Fill all fields except location.
  3. Submit.
- **Expected Result**: Fields remain filled to fix inputs.
- **Actual Result**: All inputs are cleared on error.


