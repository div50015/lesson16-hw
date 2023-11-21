"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


import pytest
from selene.support.shared import browser
from selene import have


@pytest.fixture(scope='function')
def desktop():
    browser.config.window_width = 1500
    browser.config.window_height = 1000


@pytest.fixture(scope='function')
def mobile():
    browser.config.window_width = 600
    browser.config.window_height = 1000


def test_github_desktop(desktop):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(mobile):
    browser.open('https://github.com')
    browser.all('.Button-label').first.click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
