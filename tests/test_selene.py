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
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "mjwat")
@allure.feature("Чистый Selene (без шагов)")
@allure.story("Написать тест на проверку названия Issue, используя чистый Selene")
@allure.link(github_url, name="Testing")
def test_github_selene(set_browser_name, set_window_size):
    browser.open(github_url)
    s(".header-search-input").click().send_keys(user_and_repository).submit()
    s(by.link_text(user_and_repository)).click()
    s("#issues-tab").click()
    s(by.partial_text(issue_name)).should(be.visible)
