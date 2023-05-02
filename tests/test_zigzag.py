from algorithms.zigzag import ZigZag
import pytest

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]


class TestZigZag:

    def setup_method(self):
        self.z = ZigZag(a, b)

    def test_next(self):
        assert self.z.next() == 1
        assert self.z.next() == 2
        assert self.z.next() == 3
        assert self.z.next() == 4
        assert self.z.next() == 5
        assert self.z.next() == 6
        assert self.z.next() == 7
        assert self.z.next() == 8
        assert self.z.next() == 9
        assert self.z.next() == 10

    
    def test_has_next(self):
        assert self.z.has_next() is True
        for _ in range(10):
            self.z.next()
        assert self.z.has_next() is False


if __name__ == "__main__":
    pytest.main()
