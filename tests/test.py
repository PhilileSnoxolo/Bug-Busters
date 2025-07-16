import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time
import json


class TestBugSuite:
    """Test suite for reported bugs in the application"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup method to initialize driver and common variables"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://clean-city-bug-busters.netlify.app"  
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()
    
    def login_user(self, email="test@example.com", password="testpass123"):
        """Helper method to login a user"""
        self.driver.get(f"{self.base_url}/login")
        email_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "password")
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        # Wait for login to complete
        self.wait.until(EC.url_changes(f"{self.base_url}/login"))
    
    def test_bug_001_eldoret_filter_returns_nairobi_data(self):
        """
        BUG-001: Eldoret filter returns Nairobi data
        Test that location filter works correctly
        """
        # Step 1: Log in as any user
        self.login_user()
        
        # Step 2: Navigate to the dashboard
        self.driver.get(f"{self.base_url}/dashboard")
        
        # Step 3: Select "Eldoret" from the location filter
        location_filter = Select(self.driver.find_element(By.ID, "location-filter"))
        location_filter.select_by_visible_text("Eldoret")
        
        # Wait for filter to apply
        time.sleep(2)
        
        # Step 4: Observe that results returned are from "Nairobi"
        results = self.driver.find_elements(By.CLASS_NAME, "request-location")
        
        # Expected: Only requests from Eldoret should appear
        # Actual: Requests from Nairobi are shown instead
        for result in results:
            location_text = result.text.lower()
            assert "eldoret" in location_text, f"Expected Eldoret data, but found: {location_text}"
            assert "nairobi" not in location_text, f"Found Nairobi data when filtering for Eldoret: {location_text}"
    
    def test_bug_002_passwords_stored_in_plain_text(self):
        """
        BUG-002: Passwords stored in plain text in localStorage
        Test that passwords are not stored in plain text
        """
        # Step 1: Register or log in as a new user
        self.driver.get(f"{self.base_url}/register")
        
        # Fill registration form
        name_field = self.driver.find_element(By.ID, "name")
        email_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "password")
        
        test_password = "TestPassword123"
        name_field.send_keys("Test User")
        email_field.send_keys("testuser@example.com")
        password_field.send_keys(test_password)
        
        register_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        register_button.click()
        
        # Wait for registration to complete
        time.sleep(2)
        
        # Step 2 & 3: Check localStorage for plain text password
        local_storage = self.driver.execute_script("return window.localStorage;")
        
        # Convert localStorage to string for searching
        storage_str = json.dumps(local_storage).lower()
        
        # Expected: Passwords should be hashed and stored securely (or not stored at all)
        # Actual: Plain text passwords visible in localStorage
        assert test_password.lower() not in storage_str, "Plain text password found in localStorage"
        
        # Additional check: look for any key that might contain password
        for key, value in local_storage.items():
            if "password" in key.lower():
                assert test_password not in str(value), f"Plain text password found in localStorage key: {key}"
    
    def test_bug_003_preferred_date_field_validation(self):
        """
        BUG-003: Preferred date field does not validate
        Test that preferred date field requires validation
        """
        # Step 1: Navigate to the Pickup Request form
        self.login_user()
        self.driver.get(f"{self.base_url}/pickup-request")
        
        # Fill other required fields but leave preferred date empty
        name_field = self.driver.find_element(By.ID, "name")
        location_field = self.driver.find_element(By.ID, "location")
        
        name_field.send_keys("Test User")
        location_field.send_keys("Test Location")
        
        # Step 2: Leave the "Preferred Date" empty
        preferred_date_field = self.driver.find_element(By.ID, "preferred-date")
        preferred_date_field.clear()
        
        # Step 3: Submit the form
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        
        # Expected: Validation message requiring a date
        # Check for validation message
        try:
            error_message = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
            )
            assert "date" in error_message.text.lower(), "Expected date validation message"
        except TimeoutException:
            # If no error message, check if form was submitted (this would be the bug)
            current_url = self.driver.current_url
            assert "pickup-request" in current_url, "Form was submitted without date validation"
    
    def test_bug_004_feedback_form_allows_empty_comments(self):
        """
        BUG-004: Feedback form allows empty comments
        Test that feedback form requires comments
        """
        # Step 1: Navigate to the Feedback form
        self.login_user()
        self.driver.get(f"{self.base_url}/feedback")
        
        # Step 2: Enter a valid Request ID and select a reason
        request_id_field = self.driver.find_element(By.ID, "request-id")
        reason_select = Select(self.driver.find_element(By.ID, "reason"))
        
        request_id_field.send_keys("REQ123")
        reason_select.select_by_visible_text("Late Pickup")
        
        # Step 3: Leave the comments section empty
        comments_field = self.driver.find_element(By.ID, "comments")
        comments_field.clear()
        
        # Step 4: Submit the form
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        
        # Expected: Comments should be required
        # Check for validation message or form rejection
        try:
            error_message = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
            )
            assert "comment" in error_message.text.lower(), "Expected comments validation message"
        except TimeoutException:
            # Check if form was submitted (this would be the bug)
            success_message = self.driver.find_elements(By.CLASS_NAME, "success-message")
            assert len(success_message) == 0, "Form was submitted without comments validation"
    
    def test_bug_005_name_field_accepts_single_letter(self):
        """
        BUG-005: Name field accepts 1-letter names
        Test that name field validates minimum length
        """
        # Step 1: Go to the registration form
        self.driver.get(f"{self.base_url}/register")
        
        # Step 2: Enter a 1-letter name
        name_field = self.driver.find_element(By.ID, "name")
        email_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "password")
        
        name_field.send_keys("A")
        email_field.send_keys("test@example.com")
        password_field.send_keys("TestPassword123")
        
        # Step 3: Submit the form
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        
        # Expected: Error message for short name
        # Check for validation message
        try:
            error_message = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
            )
            assert "name" in error_message.text.lower(), "Expected name validation message"
        except TimeoutException:
            # Check if we're still on the registration page (form rejected)
            current_url = self.driver.current_url
            assert "register" in current_url, "Form was submitted with single-letter name"
    
    def test_bug_006_session_not_cleared_on_logout(self):
        """
        BUG-006: Session not fully cleared on logout
        Test that session data is completely cleared on logout
        """
        # Step 1: Login as any user
        self.login_user()
        
        # Verify user is logged in
        self.wait.until(EC.presence_of_element_located((By.ID, "user-menu")))
        
        # Step 2: Click "Logout"
        logout_button = self.driver.find_element(By.ID, "logout-button")
        logout_button.click()
        
        # Wait for logout to complete
        self.wait.until(EC.url_contains("login"))
        
        # Step 3: Refresh the page
        self.driver.refresh()
        
        # Expected: No session data should remain
        # Check localStorage and sessionStorage
        local_storage = self.driver.execute_script("return window.localStorage;")
        session_storage = self.driver.execute_script("return window.sessionStorage;")
        
        # Check that no authentication tokens remain
        auth_keys = ["token", "user", "session", "auth"]
        for key in auth_keys:
            for storage_key in local_storage.keys():
                assert key not in storage_key.lower(), f"Authentication data found in localStorage: {storage_key}"
            for storage_key in session_storage.keys():
                assert key not in storage_key.lower(), f"Authentication data found in sessionStorage: {storage_key}"
        
        # Verify user is redirected to login page
        current_url = self.driver.current_url
        assert "login" in current_url, "User not redirected to login after logout"
    
    def test_bug_007_admin_page_accessible_without_auth(self):
        """
        BUG-007: Admin page accessible without auth check
        Test that admin page requires proper authentication
        """
        # Step 1: Login as a regular user (not admin)
        self.login_user("regular@example.com", "password")
        
        # Step 2: Manually enter the admin URL
        self.driver.get(f"{self.base_url}/admin")
        
        # Expected: Redirect to login or access denied
        # Wait for page to load
        time.sleep(2)
        
        current_url = self.driver.current_url
        page_content = self.driver.page_source.lower()
        
        # Check if we're redirected away from admin page
        assert "/admin" not in current_url or "access denied" in page_content or "unauthorized" in page_content, \
            "Regular user has access to admin page"
        
        # Alternative: Check for admin-specific elements that shouldn't be accessible
        admin_elements = self.driver.find_elements(By.CLASS_NAME, "admin-controls")
        assert len(admin_elements) == 0, "Admin controls visible to regular user"
    
    def test_bug_008_empty_login_fields_no_feedback(self):
        """
        BUG-008: Empty login fields give no feedback
        Test that empty login fields show proper validation
        """
        # Step 1: Go to the login page
        self.driver.get(f"{self.base_url}/login")
        
        # Step 2: Leave email and password empty
        email_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "password")
        
        email_field.clear()
        password_field.clear()
        
        # Step 3: Submit the form
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        
        # Expected: Display "Fields required" message
        try:
            error_message = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
            )
            error_text = error_message.text.lower()
            assert "required" in error_text or "empty" in error_text, "Expected field validation message"
        except TimeoutException:
            # Check if we're still on login page (form rejected)
            current_url = self.driver.current_url
            assert "login" in current_url, "Form processed without validation feedback"
    
    def test_bug_009_dashboard_table_overflow_mobile(self):
        """
        BUG-009: Dashboard table overflows on small screens
        Test responsive design on mobile screens
        """
        # Step 1: Set mobile screen size (< 480px)
        self.driver.set_window_size(400, 800)
        
        # Login and navigate to dashboard
        self.login_user()
        self.driver.get(f"{self.base_url}/dashboard")
        
        # Step 2: View request table
        table = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "request-table")))
        
        # Expected: Responsive table formatting
        # Check if table width exceeds viewport
        table_width = table.size['width']
        viewport_width = self.driver.get_window_size()['width']
        
        assert table_width <= viewport_width, f"Table width ({table_width}px) exceeds viewport width ({viewport_width}px)"
        
        # Check for horizontal scrollbar
        has_horizontal_scroll = self.driver.execute_script(
            "return document.documentElement.scrollWidth > document.documentElement.clientWidth;"
        )
        assert not has_horizontal_scroll, "Page has horizontal scrollbar on mobile"
    
    def test_bug_010_form_resets_on_validation_error(self):
        """
        BUG-010: Form resets on validation error
        Test that form fields retain values after validation error
        """
        # Step 1: Open Pickup form
        self.login_user()
        self.driver.get(f"{self.base_url}/pickup-request")
        
        # Step 2: Fill all fields except location
        name_field = self.driver.find_element(By.ID, "name")
        phone_field = self.driver.find_element(By.ID, "phone")
        address_field = self.driver.find_element(By.ID, "address")
        
        test_name = "Test User"
        test_phone = "1234567890"
        test_address = "123 Test Street"
        
        name_field.send_keys(test_name)
        phone_field.send_keys(test_phone)
        address_field.send_keys(test_address)
        
        # Leave location field empty
        location_field = self.driver.find_element(By.ID, "location")
        location_field.clear()
        
        # Step 3: Submit form
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        
        # Wait for validation error
        time.sleep(2)
        
        # Expected: Fields remain filled to fix inputs
        # Check that previously filled fields still have their values
        assert name_field.get_attribute("value") == test_name, "Name field was cleared on validation error"
        assert phone_field.get_attribute("value") == test_phone, "Phone field was cleared on validation error"
        assert address_field.get_attribute("value") == test_address, "Address field was cleared on validation error"


# Additional utility tests and fixtures
class TestSetup:
    """Setup and utility methods for testing"""
    
    @pytest.fixture
    def create_test_user(self):
        """Fixture to create a test user for testing"""
        # This would typically involve database setup
        # For now, assume user exists or create via API
        pass
    
    @pytest.fixture
    def clean_storage(self):
        """Fixture to clean browser storage before tests"""
        driver = webdriver.Chrome()
        driver.get("about:blank")
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
        driver.quit()


# Configuration for running tests
if __name__ == "__main__":
    pytest.main([
        __file__,
        "-v",  # Verbose output
        "--tb=short",  # Short traceback format
        "--html=test_report.html",  # HTML report (requires pytest-html)
        "--self-contained-html"  # Embed CSS/JS in HTML report
    ])