"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser as browser_web
from selene import have


@pytest.fixture(params=[(1500, 1000, 'desktop'), (600, 1000, 'mobile')])
def browser(request):
    browser_web.config.window_width = request.param[0]
    browser_web.config.window_height = request.param[1]
    return request.param[2]


def test_github_desktop(browser):
    if browser == 'mobile':
        pytest.skip('mobile size')
    browser_web.open('https://github.com')
    browser_web.element('.HeaderMenu-link--sign-in').click()
    browser_web.element('.auth-form-header').should(have.text('Sign in to GitHub'))
    pass


def test_github_mobile(browser):
    if browser == 'desktop':
        pytest.skip('desktop size')
    browser_web.open('https://github.com')
    browser_web.all('.Button-label').first.click()
    browser_web.element('.HeaderMenu-link--sign-in').click()
    browser_web.element('.auth-form-header').should(have.text('Sign in to GitHub'))

