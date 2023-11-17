import pytest
from television import *


class Test:

    def setup_method(self):
        self.t1 = Television()
        self.t2 = Television()

    def teardown_methos(self):
        del self.t1
        del self.t2

    def test_init(self):
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"
        assert self.t2.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        pass

    def test_mute(self):
        pass

    def test_channel_up(self):
        pass

    def test_channel_down(self):
        pass

    def test_volume_up(self):
        pass

    def test_volume_down(self):
        pass
