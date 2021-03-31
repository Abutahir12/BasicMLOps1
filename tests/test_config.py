import pytest

class NotInRange(Exception):
    def __init__(self,message="The value is not in range"):
        self.message=message
        super().__init__(self.message)

def test():
    a=15
    # with pytest.raises(NotInRange):
    if a not in range(10,20):
        raise NotInRange
    else:
        assert True