import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

github_url = 'https://github.com'
user_and_repository = 'mjwat/qa_guru_python_4_9_vera_S'
issue_name = 'first issue'


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "mjwat")
@allure.feature("Шаги с декоратором @allure.step")
@allure.story("Написать тест на проверку названия Issue, используя шаги с декоратором")
@allure.link(github_url, name="Testing")
def test_decorator_steps(set_browser_name, set_window_size):
    open_main_page()
    search_for_repository(user_and_repository)
    go_to_repository(user_and_repository)
    open_issue_tab()
    should_see_issue_with_number(issue_name)


@allure.step("Open home page")
def open_main_page():
    browser.open(github_url)


@allure.step("Find user and repository {repo}")
def search_for_repository(repo):
    s(".header-search-input").click().send_keys(repo).submit()


@allure.step("Open repository page {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Open Issues tab")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Check Issue name {name}")
def should_see_issue_with_number(name):
    s(by.partial_text(name)).click()
