
class Testmystuff:
    def test_type(self):
        assert type(1,3) == int    #fail

    def test_string(self):
        str = "my string"
        assert str.capitalize() == "My string" # pass
