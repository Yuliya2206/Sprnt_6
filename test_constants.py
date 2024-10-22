from locators.order_page_locators import OrderPageLocators


class OrderTestData:
    CASE_1 = {
        "name": "Юлия",
        "surname": "Дементьева",
        "address": "Улица Ленина, дом 1й",
        "phone_number": "79009009090",
        "scooter_color": OrderPageLocators.BLACK_PEARL_CHECKBOX,
        "comment": "Как можно скорее"
    }

    CASE_2 = {
        "name": "Мария",
        "surname": "Иванова",
        "address": "улица Ленина, дом 21",
        "phone_number": "89999999999",
        "scooter_color": OrderPageLocators.GRAY_HOPELESSNESS,
        "comment": "Как можно скорее"
    }
