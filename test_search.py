from selene import browser, be, have


def test_search_successful():
    browser.open('https://ya.ru')
    browser.element('[id="text"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_unsuccessful():
    browser.open('https://ya.ru')
    browser.element('[id="text"]').should(be.blank).type('fhgghghjghjghgj').press_enter()
    browser.element('html').should(have.text('Ничего не нашли'))
