import allure
from selene import browser, have, command
from tests import resource

def test_fill_form():
    with allure.step("Open registrations form"):
        browser.open('https://demoqa.com/automation-practice-form')

    with allure.step("Fill form"):
        browser.element('#firstName').type('Ivan')
        browser.element('#lastName').type('Neverov')
        browser.element('#userEmail').type('neverovsky@mail.ru')
        browser.element('[for="gender-radio-1"]').click()
        browser.element('#userNumber').type('8927654341')
        browser.element('.react-datepicker-wrapper').perform(command.js.scroll_into_view)
        browser.element('.react-datepicker-wrapper').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('option[value="2"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('option[value="1998"]').click()
        browser.element('.react-datepicker__day--002').click()
        browser.element('#subjectsInput').type('Physics').press_enter()
        browser.element('#subjectsInput').perform(command.js.scroll_into_view)
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').set_value(resource.path('1.jpg'))
        browser.element('#currentAddress').type('Saint-Petersburg')
        browser.element('#react-select-3-input').type('NCR').press_enter()
        browser.element('#react-select-4-input').type('Delhi').press_enter()
        browser.element('#submit').click()

    with allure.step("Check form results"):
        browser.element('.modal-content').should(have.text('Ivan Neverov'))
        browser.element('.modal-content').should(have.text('neverovsky@mail.ru'))
        browser.element('.modal-content').should(have.text('Male'))
        browser.element('.modal-content').should(have.text('8927654341'))
        browser.element('.modal-content').should(have.text('02 March,1998'))
        browser.element('.modal-content').should(have.text('Physics'))
        browser.element('.modal-content').should(have.text('Sports'))
        browser.element('.modal-content').should(have.text('1.jpg'))
        browser.element('.modal-content').should(have.text('Saint-Petersburg'))
        browser.element('.modal-content').should(have.text('NCR Delhi'))
