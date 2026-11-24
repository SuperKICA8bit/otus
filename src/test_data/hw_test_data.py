import json
import csv

with open('users.json', 'r') as file:
    users = json.load(file)

with open('books.csv', 'r') as file:
    reader = csv.DictReader(file)
    all_books = list(reader)

total_books = len(all_books)
total_users = len(users)

books_per_user = total_books // total_users
remainder = total_books % total_users

result_users = []

for i in range(len(users)):
    user = users[i]
    books_to_give = books_per_user

    if i < remainder:
        books_to_give += 1

    user_books = []
    books_for_this_user = all_books[:books_to_give]

    for book in books_for_this_user:
        clean_book = {
            "title": book["Title"],
            "author": book["Author"],
            "pages": int(book["Pages"]),
            "genre": book["Genre"]
        }

        user_books.append(clean_book)

    new_user = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": int(user["age"]),
        "books": user_books
    }

    result_users.append(new_user)
    all_books = all_books[books_to_give:]

with open('result.json', 'w') as file:
    json.dump(result_users, file, indent=4)