from unittest import TestCase
from selenium import webdriver
from AOS_Homepage import Home_page
from AOS_Tool_Bar import Tool_Bar
from AOS_Category_Page import Category_Page
from AOS_Product_Page import Product_Page
from AOS_Product_details import Product
from AOS_Cart_Page import Cart_Page
from AOS_Order_Payment_Page import Order_Payment_Page
from AOS_Sign_In_Window import Sign_In_Window
from AOS_Create_Account_page import Create_Account_Page
from AOS_Thank_You_Page import Thank_You_Page
from AOS_My_Orders_Page import My_Orders_Page
from AOS_My_Account_page import My_Account_Page
from random import choice, randint
from time import sleep
import datetime


class Test_AOS_Shop(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.get("http://www.advantageonlineshopping.com/#/")

        self.driver.maximize_window()

        # Define timeout - In case an element is not found in the program
        self.driver.implicitly_wait(10)

        self.home_page = Home_page(self.driver)
        self.tool_bar = Tool_Bar(self.driver)
        self.category_page = Category_Page(self.driver)
        self.product_page = Product_Page(self.driver)
        self.cart_page = Cart_Page(self.driver)
        self.order_payment_page = Order_Payment_Page(self.driver)
        self.create_account_page = Create_Account_Page(self.driver)
        self.signin_window = Sign_In_Window(self.driver)
        self.thank_you_page = Thank_You_Page(self.driver)
        self.my_orders_page = My_Orders_Page(self.driver)
        self.my_account_page = My_Account_Page(self.driver)

    def tearDown(self):
        sleep(3)
        self.tool_bar.logo_click()
        self.driver.quit()

    def test_1_total_items_of_on_cart_preview_1(self):
        """Choose 2 products, in different quantities,
        Check that the total amount of products appears correctly
        and accurately in the shopping cart preview on the upper right side of the screen."""

        for i in range(2):
            # Choose a random category from homepage
            choice(self.home_page.categories()).click()

            # Choose a random product from a category page, ensuring it's not the sold-out product with id="13"
            while True:
                choose_item = choice(self.category_page.items())
                if choose_item.get_attribute("id") != "13":
                    choose_item.click()
                    break

            # Choose a random color
            rand_color = randint(0, len(self.product_page.colors()) - 1)
            self.product_page.colors()[rand_color].click()
            # print(f"color index: {rand_color}, color name: {self.product_page.get_color_title(rand_color)}")

            # Update quantity
            rand_quantity = randint(1, 10)
            self.product_page.type_quantity(str(rand_quantity))

            # Click 'Add To Cart' button
            self.product_page.add_to_cart_click()

            sleep(2)

            self.tool_bar.logo_click()

        sum_product_quantity = 0

        for i in range(len(self.tool_bar.table_rows_products_in_cart_preview())):
            self.tool_bar.cart_preview()
            quantity = self.tool_bar.quantity_cart_preview(i)
            sum_product_quantity += int(quantity)

        total_items = int(self.tool_bar.total_items_in_cart_preview().text[1:-7])

        self.assertEqual(sum_product_quantity, total_items)

    def test_1_total_items_of_on_cart_preview_2(self):
        """Choose 2 products, in different quantities,
        Check that the total amount of products appears correctly
        and accurately in the shopping cart preview on the upper right side of the screen."""

        sum_product_quantity = 0

        for i in range(2):
            # Choose a random category from homepage
            choice(self.home_page.categories()).click()

            # Choose a random product from a category page, ensuring it's not the sold-out product with id="13"
            while True:
                choose_item = choice(self.category_page.items())
                if choose_item.get_attribute("id") != "13":
                    choose_item.click()
                    break

            # Choose a random color
            rand_color = randint(0, len(self.product_page.colors()) - 1)
            self.product_page.colors()[rand_color].click()

            # Update quantity
            rand_quantity = randint(1, 10)
            self.product_page.type_quantity(str(rand_quantity))

            # Get quantity value
            quantity_value = int(self.product_page.get_quantity_value())
            sum_product_quantity += quantity_value

            # Click 'Add To Cart' button
            self.product_page.add_to_cart_click()

            # Go back to Homepage
            self.tool_bar.logo_click()

        total_items = int(self.tool_bar.total_items_in_cart_preview().text[1:-7])
        print(f"total_items: {total_items}, sum_product_quantity: {sum_product_quantity}")

        self.assertEqual(sum_product_quantity, total_items)

    def test_2_product_details_in_cart_preview(self):
        """Choose 3 products, in different quantities,
         check that the products appear correctly: including name, color,
        quantity and price in the shopping cart preview on the upper right side of the screen."""

        # dict_items = {}
        list_products = []
        for i in range(3):
            # Choose a random category from homepage
            choice(self.home_page.categories()).click()
            sleep(2)
            # Choose a random product from a category page, ensuring it's not the sold-out product with id="13"
            while True:
                rand_item = randint(0, len(self.category_page.items()) - 1)
                choose_item = self.category_page.items()[rand_item]
                if choose_item.get_attribute("id") != "13":
                    item_id = self.category_page.get_item_id_value(rand_item)
                    choose_item.click()
                    break

            # Product description
            product_description = self.product_page.product_description().text

            # Choose a random color
            rand_color = randint(0, len(self.product_page.colors()) - 1)
            self.product_page.colors()[rand_color].click()

            # Get Color name by 'title' attribute value
            color_name = self.product_page.get_color_title(rand_color)

            # If we got the same item again, skip it

            # option_1 using dictionary

            # if item_id not in dict_items:
            #     dict_items[item_id] = [color_name]
            # elif color_name not in dict_items[item_id]:
            #     dict_items[item_id].append(color_name)
            # else:
            #     self.tool_bar.logo_click()  # Return to the homepage if the same item and color is already in the cart
            #     continue

            # option_2 using Product object

            product = Product(item_id, color_name)
            if product not in list_products:
                list_products.append(product)
            else:
                print(product)
                self.tool_bar.logo_click()
                continue

            # Update quantity before adding to cart
            rand_quantity = randint(1, 10)
            self.product_page.type_quantity(str(rand_quantity))

            # Click 'Add To Cart' button
            self.product_page.add_to_cart_click()

            # Get quantity value
            quantity_value = int(self.product_page.get_quantity_value())

            # Product Price
            product_price = float(self.product_page.price().text[1:].replace(",", ""))

            # Product Price * Quantity
            total_product_price = float(quantity_value * product_price)
            total_product_price = round(total_product_price, 2)

            # Refresh the cart preview and ensure the elements are present
            self.tool_bar.cart_preview()
            self.tool_bar.wait_for_cart_preview()

            # Product details on cart preview
            product_description_cart_preview = self.tool_bar.product_description_cart_preview(0)
            if product_description_cart_preview[-3:] == "...":
                product_description_cart_preview = product_description_cart_preview[:27]
                product_description = product_description[:27]

            color_name_cart_preview = self.tool_bar.color_cart_preview(0)
            quantity_value_cart_preview = int(self.tool_bar.quantity_cart_preview(0))
            product_price_cart_preview = float(self.tool_bar.price_cart_preview(0))

            print(f"Product page details {i + 1}:\nDescription: {product_description}\nColor: {color_name}"
                  f"\nQuantity:{quantity_value}\ntotal product price: {total_product_price}$")
            print(f"Product details on cart preview {i + 1}:\nDescription: {product_description_cart_preview}"
                  f"\nColor: {color_name_cart_preview}\nQuantity:{quantity_value_cart_preview}"
                  f"\n{product_price_cart_preview}$\n")

            self.assertEqual(product_description, product_description_cart_preview)
            self.assertEqual(color_name, color_name_cart_preview)
            self.assertEqual(quantity_value, quantity_value_cart_preview)
            self.assertEqual(total_product_price, product_price_cart_preview)

            self.tool_bar.logo_click()

        # print(dict_items)
        print(list_products)

    def test_3_remove_product_from_cart_preview(self):
        """ Choose at least two products and remove one product
         by using the shopping cart preview on the top right,
         check that the product has indeed removed from the cart preview."""

        for i in range(3):
            # Choose a random category from homepage
            choice(self.home_page.categories()).click()

            # Choose a random product from a category page, ensuring it's not the sold-out product with id="13"
            while True:
                choose_item = choice(self.category_page.items())
                if choose_item.get_attribute("id") != "13":
                    choose_item.click()
                    break

            # Choose a random color
            rand_color = randint(0, len(self.product_page.colors()) - 1)
            self.product_page.colors()[rand_color].click()

            # Update quantity
            rand_quantity = randint(1, 10)
            self.product_page.type_quantity(str(rand_quantity))

            # Click 'Add To Cart' button
            self.product_page.add_to_cart_click()

            self.tool_bar.logo_click()

        products_in_cart = self.tool_bar.table_rows_products_in_cart_preview()
        # Choose a random item to remove
        rand_item_index = randint(0, len(products_in_cart) - 1)

        chosen_item_description = self.tool_bar.product_description_cart_preview(rand_item_index)
        chosen_item_color = self.tool_bar.color_cart_preview(rand_item_index)
        full_description_chosen = chosen_item_description + " " + chosen_item_color
        print("chosen item:", full_description_chosen)

        if len(products_in_cart) > 0:
            # self.tool_bar.cart_preview()
            sleep(2)
            self.tool_bar.remove_product_cart_preview(rand_item_index).click()
        else:
            print("No products in cart")

        # Check that the chosen item has been removed
        remaining_items = self.tool_bar.table_rows_products_in_cart_preview()
        for i in range(len(remaining_items)):
            description = self.tool_bar.product_description_cart_preview(i)
            color = self.tool_bar.color_cart_preview(i)
            full_description_remaining = description + " " + color
            print(f"Remaining item {i + 1}: {description}, {color}")
            self.assertNotEqual(full_description_remaining, full_description_chosen)

    def test_4_shopping_cart_text_navigation_bar(self):
        """Choose any product and go to the shopping cart page
        by clicking the shopping cart button on the upper right side,
        make sure you switch to the shopping cart page
        by checking the appearance of the Shopping Cart text on the top left."""

        # Choose a random category from homepage
        choice(self.home_page.categories()).click()

        # Choose a random product from a category page, ensuring it's not the sold-out product with id="13"
        while True:
            choose_item = choice(self.category_page.items())
            if choose_item.get_attribute("id") != "13":
                choose_item.click()
                break

        # Choose a random color
        rand_color = randint(0, len(self.product_page.colors()) - 1)
        self.product_page.colors()[rand_color].click()

        # Update quantity
        rand_quantity = randint(1, 10)
        self.product_page.type_quantity(str(rand_quantity))

        # Click 'Add To Cart' button
        self.product_page.add_to_cart_click()

        self.tool_bar.cart_click()

        self.cart_page.wait_for_shopping_cart_page()
        shopping_cart_text_bar = self.tool_bar.navigation_bar()[1].text
        self.assertEqual("SHOPPING CART", shopping_cart_text_bar,
                         f"Expected: SHOPPING CART, but got: {shopping_cart_text_bar}")

    def test_5_total_order_price(self):
        """Choose 3 products in different quantities and go to the shopping cart page,
        check that the total amount of the order
        matches the prices of the products and the quantities ordered,
        according to the summary of the prices that appeared when selecting the products."""

        sum_total_price = 0

        for i in range(3):
            # Choose a random category from homepage
            choice(self.home_page.categories()).click()

            # Choose a random product from a category page, ensuring it's not the sold-out product with id="13"
            while True:
                choose_item = choice(self.category_page.items())
                if choose_item.get_attribute("id") != "13":
                    choose_item.click()
                    break

            # Choose a random color
            rand_color = randint(0, len(self.product_page.colors()) - 1)
            self.product_page.colors()[rand_color].click()

            # Update quantity
            rand_quantity = randint(1, 10)
            self.product_page.type_quantity(str(rand_quantity))

            # Get quantity and price
            product_quantity = int(self.product_page.get_quantity_value())
            product_price = float(self.product_page.price().text[1:].replace(",", ""))

            # Calculate total price per product
            total_price_per_product = float(product_quantity * product_price)
            total_price_per_product = round(total_price_per_product, 2)
            sum_total_price += total_price_per_product

            # Click 'Add To Cart' button
            self.product_page.add_to_cart_click()

            self.tool_bar.logo_click()

        self.tool_bar.cart_click()

        total_price_cart = float(self.cart_page.total_price_cart().text[1:].replace(",", ""))
        # print(total_price_cart)
        # print(sum_total_price)

        for i in range(len(self.cart_page.table_rows_products_in_cart())):
            product_name = self.cart_page.product_name(i)
            product_color = self.cart_page.get_color_by_title(i)
            product_quantity = self.cart_page.product_quantity(i)
            product_price = self.cart_page.product_price(i)[1:]
            print(f"product {i + 1}:\nPRODUCT NAME: {product_name}\nCOLOR: {product_color}"
                  f"\nQUANTITY: {product_quantity}\nPRICE: {product_price}$\n")

        self.assertEqual(sum_total_price, total_price_cart)

    def test_6_edit_quantity_on_shopping_cart(self):
        """Choose at least two products, go to the shopping cart page
         and make two changes to the quantities of the two products.
         Check that the changes are reflected on the shopping cart page."""

        for i in range(3):
            # Choose a random category from homepage
            choice(self.home_page.categories()).click()

            # Choose a random product from a category page, ensuring it's not the sold-out product with id="13"
            while True:
                choose_item = choice(self.category_page.items())
                if choose_item.get_attribute("id") != "13":
                    choose_item.click()
                    break

            # Choose a random color
            rand_color = randint(0, len(self.product_page.colors()) - 1)
            self.product_page.colors()[rand_color].click()

            # Update quantity
            rand_quantity = randint(1, 10)
            self.product_page.type_quantity(str(rand_quantity))

            # Click 'Add To Cart' button
            self.product_page.add_to_cart_click()

            self.tool_bar.logo_click()

        self.tool_bar.cart_click()

        old_quantity_list = []
        expected_new_quantity_list = []
        actual_new_quantity_list = []

        for product_index in range(len(self.cart_page.table_rows_products_in_cart())):
            # Get product quantity as text
            old_quantity = self.cart_page.product_quantity(product_index)
            old_quantity_list.append(old_quantity)

            # Click the edit button
            while True:
                try:
                    self.cart_page.edit_button(product_index).click()
                    break
                except:
                    pass

            # Update the existing quantity
            new_rand_quantity = randint(1, 10)
            while str(new_rand_quantity) == old_quantity:
                new_rand_quantity = randint(1, 10)
            expected_new_quantity_list.append(str(new_rand_quantity))

            # Type new quantity
            self.product_page.type_quantity(str(new_rand_quantity))

            # Click 'Add To Cart' button
            self.product_page.add_to_cart_click()

            # Get the updated quantity
            new_quantity = self.cart_page.product_quantity(product_index)

            print(f"Per Iteration:\nproduct {self.cart_page.product_name(product_index)}:"
                  f"\nOld quantity: {old_quantity}"
                  f"\nExpected quantity: {new_rand_quantity}"
                  f"\nActual New quantity: {new_quantity}\n")

        print("Final Updated quantities:")
        for product_index in range(len(self.cart_page.table_rows_products_in_cart())):
            actual_quantity = self.cart_page.product_quantity(product_index)
            actual_new_quantity_list.append(actual_quantity)
            print(f"\nproduct {self.cart_page.product_name(product_index)}:"
                  f"\nOld quantity: {old_quantity_list[product_index]}"
                  f"\nExpected New quantity: {expected_new_quantity_list[product_index]}"
                  f"\nActual New quantity: {actual_quantity}")
        # print(old_quantity_list,expected_new_quantity_list,actual_new_quantity_list)

        for product_index in range(len(self.cart_page.table_rows_products_in_cart())):
            self.assertNotEqual(expected_new_quantity_list[product_index], old_quantity_list[product_index])
            self.assertEqual(expected_new_quantity_list[product_index], actual_new_quantity_list[product_index])

    def test_7_go_back_from_tablet_product(self):
        """Select a tablet type product, go back and check that you have returned
         to the Tablet products page and again go back
          and check that you have returned to the main screen."""

        # Choose 'Tablets' category from homepage
        self.home_page.category_click(1)

        # Choose a random product from a category page, ensuring it's not the sold-out product with id="13"
        while True:
            choose_item = choice(self.category_page.items())
            if choose_item.get_attribute("id") != "13":
                choose_item.click()
                break

        # return to 'Tablets' page
        self.driver.back()
        expected_url = 'https://www.advantageonlineshopping.com/#/category/Tablets/3'
        current_url = self.driver.current_url

        self.assertEqual(current_url, expected_url)

        # return to Homepage
        self.driver.back()

        expected_url = 'https://www.advantageonlineshopping.com/#/'
        current_url = self.driver.current_url

        self.assertEqual(current_url, expected_url)

    def test_8_place_an_order_new_account(self):
        """Select any products to buy, perform checkout, fill in new User information,
        pay using SafePay, check that the payment was made successfully,
         check that the shopping cart is empty and that the order is in the User's orders list."""

        for i in range(1):
            # Choose a random category from homepage
            choice(self.home_page.categories()).click()

            # Choose a random product from a category page, ensuring it's not the sold-out product with id="13"
            while True:
                choose_item = choice(self.category_page.items())
                if choose_item.get_attribute("id") != "13":
                    choose_item.click()
                    break

            # Choose a random color
            rand_color = randint(0, len(self.product_page.colors()) - 1)
            self.product_page.colors()[rand_color].click()

            # Update quantity
            rand_quantity = randint(1, 10)
            self.product_page.type_quantity(str(rand_quantity))

            # Click 'Add To Cart' button
            self.product_page.add_to_cart_click()

            # Return to Homepage
            self.tool_bar.logo_click()

        # Click the checkout in the cart preview
        self.tool_bar.checkout().click()

        # Click the registration button in order payment page
        self.order_payment_page.registration().click()

        # Fill in mandatory fields
        self.create_account_page.type_name("Aviva012")
        self.create_account_page.type_email("aviva@gmail.com")
        self.create_account_page.type_password("Aa12345")
        self.create_account_page.type_confirm_password("Aa12345")
        self.create_account_page.choose_country("Israel")
        self.create_account_page.condition_of_use().click()

        # Click on the 'Register' button
        self.create_account_page.register_btn().click()

        # Click the 'NEXT' button on the order payment page
        self.order_payment_page.next().click()

        # Fill the SafePay details
        self.order_payment_page.type_safepay_username("Aviva")
        self.order_payment_page.type_safepay_password("Aa12345")

        # Click the Pay Now button
        self.order_payment_page.pay_now_safepay().click()

        # Details from the 'Thank You' Page
        self.thank_you_page.wait_for_order_number()
        order_number_thank_you = self.thank_you_page.get_order_number_text()
        thank_you_text = self.thank_you_page.get_confirmation_text()

        # Check that the payment was made successfully
        self.assertEqual("Thank you for buying with Advantage", thank_you_text)

        # Check that the shopping cart is empty
        self.tool_bar.cart_click()
        # empty shopping cart
        empty_cart = self.cart_page.empty_cart().text
        self.assertEqual("Your shopping cart is empty", empty_cart)

        # Click the account icon
        sleep(2)
        self.tool_bar.account_icon().click()

        # Click on "My Orders"
        while True:
            try:
                self.tool_bar.my_orders_button().click()
                break
            except:
                pass

        # Order number from the 'My Orders' Page
        order_number_my_orders = self.my_orders_page.order_number()[0].text

        # Check that the order is in the User's orders list
        self.assertEqual(order_number_thank_you, order_number_my_orders)

        # Enter "My Account" page
        self.tool_bar.account_icon().click()
        self.tool_bar.my_account_button().click()

        # Delete the Account
        self.my_account_page.delete().click()
        self.my_account_page.confirm_deletion().click()

    def test_9_place_an_order_existing_account(self):
        """Select any products to buy, perform checkout, sign in to the account,
        pay using credit card, check that the payment was made successfully,
         check that the shopping cart is empty and that the order is in the User's orders list."""

        for i in range(1):
            # Choose a random category from homepage
            choice(self.home_page.categories()).click()

            # Choose a random product from a category page, ensuring it's not the sold-out product with id="13"
            while True:
                choose_item = choice(self.category_page.items())
                if choose_item.get_attribute("id") != "13":
                    choose_item.click()
                    break
            # Choose a random color
            rand_color = randint(0, len(self.product_page.colors()) - 1)
            self.product_page.colors()[rand_color].click()

            # Update quantity
            rand_quantity = randint(1, 10)
            self.product_page.type_quantity(str(rand_quantity))

            # Click 'Add To Cart' button
            self.product_page.add_to_cart_click()

            # Return to Homepage
            self.tool_bar.logo_click()

        # Click the checkout in the cart page
        self.tool_bar.cart_click()
        self.cart_page.checkout_button().click()

        # Sign in as a customer
        self.order_payment_page.type_username("Aviva31415")
        self.order_payment_page.type_password("Aa12345")
        self.order_payment_page.login().click()

        # Click the 'NEXT' button on the order payment page
        self.order_payment_page.next().click()

        # Click the Credit Card button
        self.order_payment_page.creditcard().click()

        # Fill the Credit Card details
        today = datetime.date.today()
        self.order_payment_page.type_card_number("123456789101")
        self.order_payment_page.type_cvv_number("123")
        random_year = randint(today.year, 2033)
        self.order_payment_page.choose_expiration_year(str(random_year))
        random_month = randint(1, 12)
        while random_month < today.month and random_year == today.year:
            random_month = randint(1, 12)
        if len(str(random_month)) == 1:
            random_month = "0" + str(random_month)
        else:
            random_month = str(random_month)

        self.order_payment_page.choose_expiration_month(random_month)
        self.order_payment_page.type_card_holder("Aviva")

        # Uncheck "Save Changes" button"
        self.order_payment_page.save_card_payment_changes().click()

        # Click the "Pay Now" button
        while True:
            try:
                self.order_payment_page.pay_now_card().click()
                break
            except:
                pass

        # Details from the 'Thank You' Page
        self.thank_you_page.wait_for_order_number()
        order_number_thank_you = self.thank_you_page.get_order_number_text()
        thank_you_text = self.thank_you_page.get_confirmation_text()

        # Check that the payment was made successfully
        self.assertEqual("Thank you for buying with Advantage", thank_you_text)

        # Check that the shopping cart is empty
        self.tool_bar.cart_click()
        sleep(3)
        # empty shopping cart
        empty_cart = self.cart_page.empty_cart().text
        self.assertEqual("Your shopping cart is empty", empty_cart)

        # Go to 'My Orders' page
        self.tool_bar.account_icon().click()

        # Click on "My Orders"
        while True:
            try:
                self.tool_bar.my_orders_button().click()
                break
            except:
                pass

        # Order number from the 'My Orders' Page
        order_number_my_orders = self.my_orders_page.order_number()[0].text

        # Check that the order is in the User's orders list
        self.assertEqual(order_number_thank_you, order_number_my_orders)

    def test_10_login_logout(self):
        """Check Login, Logout processes:
        Log in to the system using an existing user. Verify that the connection was successful.
        Log out and verify that the logout was successful."""

        # Log in as an existing user
        self.tool_bar.account_icon().click()

        # Enter correct Username and Password
        self.signin_window.type_username("Aviva012")
        self.signin_window.type_password("Aa12345")
        sleep(2)
        self.signin_window.sign_in().click()

        # Verify logging in
        self.tool_bar.wait_to_menu_user()
        customer_name = self.tool_bar.menu_user().text
        self.assertEqual("Aviva012", customer_name)

        # Sign Out
        sleep(2)
        self.tool_bar.account_icon().click()
        self.tool_bar.sign_out().click()

        # Verify Signing Out
        self.tool_bar.wait_for_user_to_disappear()
        updated_customer_name = self.tool_bar.menu_user().text
        self.assertEqual("", updated_customer_name)
