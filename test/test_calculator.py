from app.calculator import add,substract

# from aap -> folder 
# calculator -> file 
# add, sub (functioin)

def test_add():
   assert add(2,3) == 5


def test_sub():
   assert substract(5,3) == 2
