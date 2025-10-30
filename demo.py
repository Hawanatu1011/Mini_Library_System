from operations import *

print(add_book("101", "Inovation", "Jestina Lavalie", "Education", 3))
print(add_book("102", "AI World", "Mbalu Kabia", "Sci-Fi", 2))
print(add_member("M02", "Hawa", "Hawa@example.com"))

print(search_book("python"))

print(borrow_book("M02", "102"))
print(return_book("M02", "102"))
print(delete_book("102"))
