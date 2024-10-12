from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from AOS_Homepage import Home_page
from AOS_Tool_Bar import Tool_Bar
from AOS_Category_Page import Category_Page
from AOS_Product_Page import Product_Page
from AOS_Cart_Page import Cart_Page
from AOS_Order_Payment_Page import Order_Payment_Page
from AOS_Sign_In_Window import Sign_In_Window
from AOS_Create_Account_page import Create_Account_Page
from AOS_Product_details import Product

from random import randint, choice
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://www.advantageonlineshopping.com/#/")

driver.maximize_window()

# Define timeout - In case an element is not found in the program
driver.implicitly_wait(10)

home_page = Home_page(driver)
tool_bar = Tool_Bar(driver)
category_page = Category_Page(driver)
product_page = Product_Page(driver)
cart_page = Cart_Page(driver)
order_payment = Order_Payment_Page(driver)
account_page = Create_Account_Page(driver)
signin_window = Sign_In_Window(driver)


# # Click on Speakers category by ID
# # home_page.category_click("speakersImg")
#
# # Click on a Random category
# choice(home_page.categories()).click()
#
# # Check the logo returns to Homepage
# tool_bar.logo_click()
#
# # Click on the search icon - index 3
# tool_bar.header_element_click(3)
#
# # If item is sold out choose again
# home_page.categories()[4].click()
# # Choose a random product from a category page
# while True:
#     choose_item = choice(category_page.items())
#     if choose_item.get_attribute("id") != "13":
#         choose_item.click()
#         break
# print(product_page.product_description().text)
#
# sleep(3)

# ---------------------------------------------------------
# tool_bar.account_icon().click()
# while True:
#     try:
#         signin_window.create_new_account_button().click()
#         break
#     except:
#         pass
# account_page.type_name("Aviva")
# sleep(3)

# ---------------------------------------------------------
# tool_bar.logo_click()
#
list_products = []
for i in range(3):
    home_page.categories()[0].click()
    # Get the item ID and color
    item_id = category_page.get_item_id_value(3)
    category_page.items()[3].click()
    # Choose a random color
    random_color = randint(0, len(product_page.colors()) - 1)
    product_page.colors()[random_color].click()

    color_name = product_page.get_color_title(random_color)

    product = Product(item_id, color_name)
    if product not in list_products:
        list_products.append(product)
    else:
        print(product)
        tool_bar.logo_click()
        continue

    # Update quantity before adding to cart
    rand_quantity = randint(1, 10)
    product_page.type_quantity(str(rand_quantity))

    # Click 'Add To Cart' button
    product_page.add_to_cart_click()

    print(product_page.product_description().text, color_name)

    tool_bar.logo_click()

print(list_products)
sleep(3)

# ---------------------------------------------------------

# tool_bar.logo_click()
# sleep(2)
#
# dict_items = {}
# for i in range(3):
#     # Click on the first category
#     home_page.categories()[0].click()
#
#     # Get the item ID and color
#     item_id = category_page.get_item_id_value(3)
#     category_page.items()[3].click()
#     # Choose a random color
#     random_color = randint(0, len(product_page.colors()) - 1)
#     color_name = product_page.get_color_title(random_color)
#
#     # If we got the same item again, skip it
#     if item_id not in dict_items:
#         dict_items[item_id] = [color_name]
#     elif color_name not in dict_items[item_id]:
#         dict_items[item_id].append(color_name)
#     else:
#         tool_bar.logo_click()  # Return to the homepage if the same item and color is already in the cart
#         continue
#
#     # Update quantity before adding to cart
#     rand_quantity = randint(1, 10)
#     product_page.type_quantity(str(rand_quantity))
#
#     # Click 'Add To Cart' button
#     product_page.add_to_cart_click()
#
#     print(product_page.product_description().text, color_name)
#
#     tool_bar.logo_click()
#
# print(dict_items)
#
# sleep(3)

# ---------------------------------------------------------

# Update quantity of 2 random products from random categories

# for i in range(2):
#     # Choose a random category from homepage
#     choice(home_page.categories()).click()
#     sleep(2)
#     # Choose a random product from a category page
#     choice(category_page.items()).click()
#     sleep(2)
#
#     # Choose a random color
#     rand_color = randint(0, len(product_page.colors()) - 1)
#     product_page.colors()[rand_color].click()
#     print(f"color index: {rand_color}, color name: {product_page.get_color_title(rand_color)}")
#     # product_page.color("black").click()
#
#     # Update quantity
#     rand_quantity = randint(1, 5)
#     product_page.type_quantity(str(rand_quantity))
#
#     # Click 'Add To Cart' button
#     product_page.add_to_cart_click()
#
#     sleep(2)
#
#     driver.back()
#     driver.back()
#
# sum_product_quantity = 0
#
# for i in range(len(tool_bar.table_rows_products_in_cart_preview())):
#     tool_bar.cart_preview()
#     quantity = tool_bar.quantity_cart_preview(i)
#     sum_product_quantity += int(quantity)
#
# total_items = int(tool_bar.total_items_in_cart_preview().text[1])
#
# print(f"sum_product_quantity:{sum_product_quantity}, total_items {total_items}")
#
# if sum_product_quantity == total_items:
#     print(f"test passed. Total is correct")
# else:
#     print(f"test failed for. "
#           f"Expected total: {sum_product_quantity}"
#           f"Actual total: ${total_items}")
#
# tool_bar.cart_click()
# print(len(cart_page.row_columns_in_cart(0)))

# GPT
# # Wait until the colors are visible
# WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.colors > [class=''] > span")))
#
# # Choose a random color
# colors = product_page.colors()
# if colors:
#     rand_color = randint(0, len(colors) - 1)
#     colors[rand_color].click()

# try:
#     # Check the logo returns to Homepage
#     tool_bar.tool_bar_element_click(0)
# except Exception as e:
#     print(f"An error occurred: {e}")
#
