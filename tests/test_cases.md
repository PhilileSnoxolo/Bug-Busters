#  bug busters

Below are the test cases we were able to come up with as a group, making sure that we all participate and contribute into making the system as air-tight as possible.

The test cases were put in chronological order of operation for everyone to have a clear understanding on how to attack and collaborate more efficiantly.



##  Login Functionality

| TC ID | Test Case Description                        | Input                       | Expected Result                         |
|-------|----------------------------------------------|-----------------------------|------------------------------------------|
| TC001 | Login with valid user credentials            | user@cleancity.com / pass   | Login success, redirect to dashboard     |
| TC002 | Login with incorrect email                   | wrong@cleancity.com / pass  | "Invalid email or password" shown       |
| TC003 | Login with incorrect password                | user@cleancity.com / wrong  | "Invalid email or password" shown       |
| TC004 | Login with empty fields                      | "" / ""                     | "Invalid email or password" shown       |
| TC005 | Login stores session in localStorage         | Valid login                 | `localStorage.currentUser` is set       |
| TC006 | Login user has correct role stored           | Admin login                 | Role is `admin` in localStorage          |
| TC007 | Login redirects to dashboard after 1s delay  | Valid login                 | Page = dashboard after timeout           |

---

##  Registration Functionality

| TC ID | Test Case Description                          | Input                                | Expected Result                        |
|-------|------------------------------------------------|--------------------------------------|-----------------------------------------|
| TC008 | Register with valid inputs                     | Name, Email, Password, ConfirmPass   | Success alert, form resets              |
| TC009 | Register with existing email                   | Existing Email                       | "User with this email already exists"  |
| TC010 | Register with missing name                     | "" name                              | "Name is required"                     |
| TC011 | Register with invalid email (no @)             | "invalidemail.com"                   | "Please enter a valid email address"   |
| TC012 | Register with empty email                      | "" email                             | "Email is required"                    |
| TC013 | Register with short password (e.g. 'ab')       | < 3 characters                       | "Password must be at least 3 characters"|
| TC014 | Register with password mismatch                | Password ≠ ConfirmPassword           | "Passwords do not match"              |
| TC015 | Registers saved in localStorage                | Valid user                           | Appears in `dataService.getAllUsers()`|

---

##  Pickup Request Form

| TC ID | Test Case Description                           | Input Fields             | Expected Result                            |
|-------|--------------------------------------------------|--------------------------|---------------------------------------------|
| TC016 | Submit valid pickup request                      | All fields filled        | Success message, form resets                |
| TC017 | Submit with empty name                           | "" fullName              | "Full name is required"                     |
| TC018 | Submit with short name (1 letter)                | "A"                      | "Name must be at least 2 characters"        |
| TC019 | Submit with no location selected                 | "" location              | "Please select a location"                  |
| TC020 | Submit with no waste type selected               | "" wasteType             | "Please select a waste type"                |
| TC021 | Submit with all fields missing                   | All empty                | Shows all validation errors                 |
| TC022 | Validate preferredDate missing (bug)             | "" preferredDate         | ⚠ No error shown (should be required)       |
| TC023 | Request saved to localStorage                    | Valid request            | Appears in `getAllPickupRequests()`        |

---

##  Feedback Form

| TC ID | Test Case Description                          | Input Fields                 | Expected Result                        |
|-------|-------------------------------------------------|------------------------------|-----------------------------------------|
| TC024 | Submit valid feedback                           | Valid requestId, reason      | Feedback saved, form resets             |
| TC025 | Missing request ID                              | "" requestId                 | "Request ID is required"                |
| TC026 | Missing reason selection                        | "" reason                    | "Please select a reason"                |
| TC027 | Missing comments (no validation - flaw)         | "" comments                  | Accepted ( Should reject - bug)       |
| TC028 | Feedback saved in storage                       | Valid feedback               | Appears in `getAllFeedback()`          |

---

##  Dashboard & Filtering

| TC ID | Test Case Description                          | Input Filter Values         | Expected Result                          |
|-------|-------------------------------------------------|-----------------------------|-------------------------------------------|
| TC029 | Filter by status = "Pending"                    | status = Pending            | Shows only Pending requests              |
| TC030 | Filter by location = "Eldoret"                  | location = Eldoret          |  BUG: Shows Nairobi requests instead    |
| TC031 | Filter by both = "Scheduled" + "Nairobi"        | Both filters                | Returns accurate match set               |
| TC032 | Reset filters to "All"                          | status = all, location = all| Shows all pickup requests                |
| TC033 | No matching results                             | status = Completed + invalid location | Shows 0 results                  |

---

##  Admin Panel

| TC ID | Test Case Description                          | Action Taken                        | Expected Result                         |
|-------|------------------------------------------------|--------------------------------------|------------------------------------------|
| TC034 | Admin can select a request                     | Click "Edit" on row                  | Select populated in dropdown            |
| TC035 | Status dropdown updates                         | Choose new status from list          | Status input updated                    |
| TC036 | Click Update with valid selections             | Select request + status, click update| Request status updated in storage       |
| TC037 | Update without selecting request               | No request selected                  | Button disabled or error shown          |
| TC038 | Non-admin user tries to access admin panel     | Login as regular user                | Redirected to login page                |

---

##  Navigation & Auth State

| TC ID | Test Case Description                          | Scenario                           | Expected Result                         |
|-------|------------------------------------------------|------------------------------------|------------------------------------------|
| TC039 | Logged-in user sees dashboard and feedback     | Logged in                          | Links visible in navbar                 |
| TC040 | Admin sees Admin panel                         | Login as admin                     | Admin link visible                      |
| TC041 | Logged-out user sees login/register only       | Logged out                         | Only auth links visible                 |
| TC042 | Manual page reload retains auth session        | Refresh after login                | Session restored from localStorage      |
| TC043 | Logout clears session                          | Click logout                       | Redirected to home, session null        |



#Here is the checklist of the test case execution, still to be updated.

##  Test Case Execution Checklist

| Area              | Test Category         | Status       | Notes                          |
|-------------------|-----------------------|--------------|---------------------------------|
| Login             | Functional            | ✅ Tested     | Manual test complete           |
| Registration      | Functional/Validation | ✅ Tested     | Password/Email checks validated|
| Pickup Request    | Form Validation       | ✅ Tested     | Preferred date needs rule fix  |
| Feedback Form     | Form Validation       | ✅ Tested     | Comment validation missing (⚠) |
| Dashboard         | Filtering             | ✅ Tested     | Eldoret bug identified         |
| Admin Panel       | Admin-only features   | ✅ Tested     | Status update tested           |
| Navigation        | Role-based UI         | ✅ Tested     | Working per role               |
| LocalStorage      | Data Persistence      | ✅ Verified   | All modules save data          |
| Security (Basic)  | Static Review         | ⚠ Partially  | Plaintext passwords found      |
| Automation (Jest) | Unit Auth/Forms       | 🕐 In Progress | Login logic stub created       |

Legend:  
✅ = Completed  
⚠ = Issue found  
🕐 = In Progress



---

##  Challenges Faced & Lessons Learned

### 1.  Lack of Early Direction
Our team often found ourselves unsure of the exact deliverables or expectations at the start of each phase. It took additional time to understand the task requirements clearly, which delayed progress and test preparation.

### 2.  Last-Minute Collaborations
We tended to start collaborating only close to deadlines. While we managed to pull things together, the lack of early coordination affected the quality and efficiency of our contributions. Testing responsibilities sometimes overlapped or were missed.

### 3.  Communication Gaps
There was minimal communication during the week regarding task status, updates, or planning for the next steps. This led to confusion about who was working on what, and whether the current phase had started or not.

### 4.  Technical Issues Encountered
- **Missing form validation**: We had to manually identify and implement missing validation logic in the Pickup and Feedback forms (e.g., name length, preferred date, empty feedback comments).
- **LocalStorage resets**: During testing, localStorage would reset on page refresh, leading to data loss and forced re-entry of test data.
- **Hardcoded filter bug**: A filter function intended for “Eldoret” requests was returning “Nairobi” data due to a copy-paste logic flaw we had to trace and document.
- **Session persistence inconsistencies**: Authentication state wasn't retained properly on refresh until we debugged the `getCurrentUser()` logic and browser behavior.

### 5.  Security Oversights
We discovered during review that passwords were stored in plain text and that there was no authorization check on sensitive admin functions. These issues were noted and are planned for future hardening.

---

###  What We Learned
- Starting earlier and discussing weekly milestones improves collaboration.
- Regular check-ins (even async messages) could prevent overlaps or confusion.
- Early manual testing helped catch issues that could be missed by code reviews alone.
- Building test cases *while coding* makes the process more efficient and accurate.
