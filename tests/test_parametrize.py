"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""


import pytest
from selene.support.shared import browser as browser_web
from selene import have


@pytest.fixture(params=[(1500, 1080), (600, 1000)])
def browser(request):
    browser_web.config.window_width = request.param[0]
    browser_web.config.window_height = request.param[1]


@pytest.mark.parametrize('browser', [(1500, 1000)], indirect=True)
def test_github_desktop(browser):
    browser_web.open('https://github.com')
    browser_web.element('.HeaderMenu-link--sign-in').click()
    browser_web.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('browser', [(600, 1000)], indirect=True)
def test_github_mobile(browser):
    browser_web.open('https://github.com')
    browser_web.all('.Button-label').first.click()
    browser_web.element('.HeaderMenu-link--sign-in').click()
    browser_web.element('.auth-form-header').should(have.text('Sign in to GitHub'))