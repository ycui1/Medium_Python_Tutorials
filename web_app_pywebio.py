from pywebio import input as pin
from pywebio import output as pout

# pout.put_code("""pin.input("What's your favorite fruit?")""")
# pin.input("What's your favorite fruit?")
#
# pout.put_code("""pin.slider("How old are you?", min_value=0, max_value=120)""")
# pin.slider("How old are you?", min_value=0, max_value=120)
#
# pout.put_code("""pin.checkbox("What toppings for pizza?", options=["pepperoni", "sausage", "chicken"])""")
# pin.checkbox("What toppings for pizza?", options=["pepperoni", "sausage", "chicken"])
#
# pout.put_code("""pin.select("Who's GOAT in NBA?", options=["Bryant", "Jordan", "James"])""")
# pin.select("Who's GOAT in NBA?", options=["Bryant", "Jordan", "James"])
#
# pout.put_code("""pin.radio("Are you ready to try pyWebIO?", options=["Yes", "No"])""")
# pin.radio("Are you ready to try pyWebIO?", options=["Yes", "No"])

pout.put_text("This is an awesome library.")

pout.put_table([
    ("Col 1 Title", "Col 2 Title"),
    ("Row 1, Col 1", "Row 1, Col 2"),
    ("Row 2, Col 1", "Row 2, Col2")
])

pout.put_markdown("# This is the Title")
pout.put_markdown("## This is the Subtitle")
pout.put_markdown("_Bold Text_")
pout.put_markdown("__Italic Text__")
pout.put_markdown("*__Bold & Italic__*")
pout.put_markdown("[google.com](google.com)")

pout.put_image(open("airplane.jpg", "rb").read())
pout.toast("Please Pay Attention!", duration=10)

def show_text():
    pout.toast("Button is clicked!", duration=10)

pout.put_button("I'm Ready!", onclick=show_text)
pout.toast("test")
