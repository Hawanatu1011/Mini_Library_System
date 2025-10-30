from operations import *

add_book("201", "Virtual Reality", "Amandus", "Non-Fiction", 2)
add_member("M02", "Mr.Hawa", "Hawa@example.com")

# Test adding and borrowing
assert borrow_book("M02", "201") == "Mr.Hawa borrowed 'Virtual Reality'."
assert return_book("M02", "201") == "Mr.Hawa returned 'Virtual Reality'."
assert delete_book("201") == "Book deleted."

print("✅ All tests passed successfully!")