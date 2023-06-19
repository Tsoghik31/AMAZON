import time
from tests.baseTest.baseTest import BaseTest
from sources.accountPages.yourAccountPage import YourAccountPage
from sources.accountPages.manageYourProfilesPage import ManageYourAccountPage
from sources.accountPages.editYourNameWindow import EditYourNameWindow
from sources.logInPage import LoginPage
from sources.navigationBar.actionsAndListsView import ActionsAndListsView
from sources.navigationBar.navigationBar import NavigationBar


class EditProfileUsernameTest(BaseTest):
    def test_edit_username_with_generated_name(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.logInPage = LoginPage(self.driver)
        self.logInPage.fill_username_field("acompap@yahoo.com")
        self.logInPage.click_on_continue_button()
        self.logInPage.fill_password_field("Selenium!")
        time.sleep(3)
        self.logInPage.click_on_signIn_button()
        time.sleep(5)

        self.navigationBarPage = NavigationBar(self.driver)
        self.navigationBarPage.mouse_move_action_and_list_menu()

        self.actionsAndListsView = ActionsAndListsView(self.driver)
        self.actionsAndListsView.click_on_account_button()

        self.yourAccountPage = YourAccountPage(self.driver)
        self.yourAccountPage.click_on_yourProfiles_button()
        #
        # self.manageYourAccountPage = ManageYourAccountPage(self.driver)
        # self.manageYourAccountPage.click_on_profileName()
        # self.manageYourAccountPage.click_on_edit_username_button()
        #
        # self.editYourNameWindow = EditYourNameWindow(self.driver)
        # self.editYourNameWindow.input_generated_name()
        # self.editYourNameWindow.click_on_save_changes_button()
        #






