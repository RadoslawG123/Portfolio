from bs4 import BeautifulSoup
import requests
import sys

user_choice = ""
category_choice = ""

## Ask user what he wants to see
def user_choices():
    global user_choice
    global category_choice
    global book_choice

    while user_choice != "book" and user_choice != "books":
        print("""Do you want to search books or check out a specific book? (Input "book" or "books")""")
        user_choice = input("> ")
        user_choice = user_choice.lower().strip()
        if user_choice != "book" and user_choice != "books":
            print("\nWrong input! Try again.\n")

    if user_choice == "book":
        print("\nWhat book are you looking for? (Input title)")
        book_choice = input("> ")
        book_choice = book_choice.lower().strip()
        print(f"""\nSearching book "{book_choice.capitalize()}"...\n""")
    elif user_choice == "books":
        print("""\nWhat category do you want? (For all categories input "all")""")
        category_choice = input("> ")
        category_choice = category_choice.replace(" ", "-").lower().strip()
        print(f"\nChecking for {category_choice} books...\n")

user_choices()

## Checking different errors 
try:
    requests.get("https://books.toscrape.com")
except:
    print("Error! It's possible the website is having some connection issues right now. Please try again later.\n")
    sys.exit()

## Checking what number is in category link (examples: /.../travel_2/index.html has number 2, /.../music_14/index.html has number 14)
i = 51
while i > 50:
    i = 1
    if(category_choice == "all" or user_choice == "book"):
        category_choice = "books"
        category_html_text = requests.get(f"https://books.toscrape.com/catalogue/category/{category_choice}_{i}/index.html").text
        category_soup = BeautifulSoup(category_html_text, 'lxml')

    ## This also checks that category name existed
    else:
        category_html_req = requests.get(f"https://books.toscrape.com/catalogue/category/books/{category_choice}_{i}/index.html")
        category_html_req = str(category_html_req)
        while category_html_req == "<Response [404]>" and i <= 50:
            i += 1
            category_html_req = requests.get(f"https://books.toscrape.com/catalogue/category/books/{category_choice}_{i}/index.html")
            category_html_req = str(category_html_req)
        if i > 50:
            print("This category does not exist")
            wrong_choice_checker = "books"
            user_choices()

## Checking that category have one page or more
if category_choice != "books":
    books_or_nothing = "books"
    pages_checking_html_req = requests.get(f"https://books.toscrape.com/catalogue/category/books/{category_choice}_{i}/page-2.html")
    pages_checking_html_req = str(pages_checking_html_req)
else:
    books_or_nothing = ""
    pages_checking_html_req = requests.get(f"https://books.toscrape.com/catalogue/category/{category_choice}_{i}/page-2.html")
    pages_checking_html_req = str(pages_checking_html_req)

## One page
if pages_checking_html_req == "<Response [404]>":
    html_text = requests.get(f"https://books.toscrape.com/catalogue/category/books/{category_choice}_{i}/index.html").text
    soup = BeautifulSoup(html_text, 'lxml')

    books = soup.find_all("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for book in books:
        title = book.h3.a["title"]
        div_product_price = book.find("div", class_ = "product_price")
        price = div_product_price.find("p", class_ = "price_color").text
        availability = div_product_price.find("p", class_ = "instock availability").text.strip()
        link = "https://books.toscrape.com/catalogue/" + book.h3.a["href"][6:]
        rating = book.p["class"][1]
        if rating == "One":
            rating = "★"
        elif rating == "Two":
            rating = "★ ★"
        elif rating == "Three":
            rating = "★ ★ ★"
        elif rating == "Four":
            rating = "★ ★ ★ ★"
        elif rating == "Five":
            rating = "★ ★ ★ ★ ★"
    
        print("")
        print("Title:", title)
        print("Price:", price)
        print("Rating:", rating)
        print("Avaibility:", availability)
        print("Link:", link)
        print("")
## More pages
else:
    if user_choice == "book":  
        page_existed = True
        page_number = 0
        found_book = False

        while page_existed == True:

            page_existed = False
            page_number += 1
            html_text = requests.get(f"https://books.toscrape.com/catalogue/category/{books_or_nothing}/{category_choice}_{i}/page-{page_number}.html").text
            soup = BeautifulSoup(html_text, 'lxml')

            books = soup.find_all("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")

            for book in books:
                page_existed = True
                title = book.h3.a["title"]
                title = title.lower().strip()
                rating = book.p["class"][1]
                if rating == "One":
                    rating = "★"
                elif rating == "Two":
                    rating = "★ ★"
                elif rating == "Three":
                    rating = "★ ★ ★"
                elif rating == "Four":
                    rating = "★ ★ ★ ★"
                elif rating == "Five":
                    rating = "★ ★ ★ ★ ★"

                if book_choice == title:
                    found_book = True
                    link = "https://books.toscrape.com/catalogue/" + book.h3.a["href"][6:]
                    html_text = requests.get(link).text
                    soup = BeautifulSoup(html_text, 'lxml')

                    product_main_info = soup.find("div", class_="col-sm-6 product_main")
                    title = product_main_info.h1.text
                    price = product_main_info.find("p", class_="price_color").text
                    availability = product_main_info.find("p", class_="instock availability").text.strip()
                    description = soup.find("div", id="product_description").h2
                    description = description.find_next("p").text
                    upc = soup.find("table", class_="table table-striped").tr.td.text

                    print("")
                    print("Title:", title)
                    print("Price:", price)
                    print("Rating:", rating)
                    print("Avaibility:", availability)
                    print("UPC:", upc)
                    print("Link:", link)
                    print("\nProduct Description:\n", description)
                    print("")

                    break

            if found_book == True:
                break
            ## If user typed invalid name for book
            elif page_existed == False:
                print("Invalid book name.")
                user_choices()
                page_existed = True
                page_number = 0  
    else:
        page_existed = True
        page_number = 0

        while page_existed == True:

            page_existed = False
            page_number += 1
            html_text = requests.get(f"https://books.toscrape.com/catalogue/category/{books_or_nothing}/{category_choice}_{i}/page-{page_number}.html").text
            soup = BeautifulSoup(html_text, 'lxml')

            books = soup.find_all("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")

            for book in books:
                page_existed = True
                title = book.h3.a["title"]
                div_product_price = book.find("div", class_ = "product_price")
                price = div_product_price.find("p", class_ = "price_color").text
                availability = div_product_price.find("p", class_ = "instock availability").text.strip()
                link = "https://books.toscrape.com/catalogue/" + book.h3.a["href"][6:]
                rating = book.p["class"][1]
                if rating == "One":
                    rating = "★"
                elif rating == "Two":
                    rating = "★ ★"
                elif rating == "Three":
                    rating = "★ ★ ★"
                elif rating == "Four":
                    rating = "★ ★ ★ ★"
                elif rating == "Five":
                    rating = "★ ★ ★ ★ ★"

                print("")
                print(f"Page nr. {page_number}")
                print("Title:", title)
                print("Price:", price)
                print("Rating:", rating)
                print("Avaibility:", availability)
                print("Link:", link)
                print("")