import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

github_url = 'https://github.com'
user_and_repository = 'mjwat/qa_guru_python_4_9_vera_S'
issue_name = 'first issue'


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "mjwat")
@allure.feature("Лямбда шаги через with allure.step")
@allure.story("Написать тест на проверку названия Issue, используя Лямбда шаги")
@allure.link(github_url, name="Testing")
def test_github_steps(set_browser_name, set_window_size):
    with allure.step("Open home page"):
        browser.open(github_url)

    with allure.step("Find user and repository"):
        s(".header-search-input").click().send_keys(user_and_repository).submit()

    with allure.step("Open repository page"):
        s(by.link_text(user_and_repository)).click()

    with allure.step("Open Issues tab"):
        s("#issues-tab").click()

    with allure.step("Check Issue name"):
        s(by.partial_text(issue_name)).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
