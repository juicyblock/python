import pytest
from television import Television

class Test_Television:
    def setup_method(self):
        self.tv1 = Television()
        self.tv2 = Television()
        
    def teardown_method(self):
        del self.tv1
        del self.tv2
        
    def test_init(self): #Test defaults
        assert self.tv1.status == False
        assert self.tv1.muted == False
        assert self.tv1.volume == Television.MIN_VOLUME
        assert self.tv1.channel == Television.MIN_CHANNEL
        
    def test_power(self):
        self.tv1.power()
        assert self.tv1.status == True #Powers on tv1
        assert self.tv2.status == False #Doesn't affect other TVs
        self.tv1.power()
        assert self.tv1.status == False #Toggles again

    def test_mute(self):
        self.tv1.mute()
        assert self.tv1.muted == False #Doesn't work without TV on
        self.tv1.power()
        self.tv2.power()
        self.tv1.volume = 1
        self.tv1.mute()
        assert self.tv1.muted == True #TV mutes
        assert self.tv1.get_volume() == 0 #Volume is 0 during mute
        assert self.tv2.muted == False #Doesn't affect other tvs
        self.tv1.mute()
        assert self.tv1.muted == False #Toggle again
        assert self.tv1.get_volume() == 1 #Volume returns to normal

    def test_channel_up(self):
        self.tv1.channel_up()
        assert self.tv1.channel == Television.MIN_CHANNEL #Channel doesn't change when off
        self.tv1.power()
        self.tv2.power()
        self.tv1.channel_up()
        assert self.tv1.channel == Television.MIN_CHANNEL + 1 #Channel increments by one when on
        assert self.tv2.channel == Television.MIN_CHANNEL #Other TV doesn't change
        self.tv1.channel = Television.MAX_CHANNEL
        self.tv1.channel_up()
        assert self.tv1.channel == Television.MIN_CHANNEL #Channel loops to MIN

    def test_channel_down(self):
        self.tv1.channel_down()
        assert self.tv1.channel == Television.MIN_CHANNEL #Channel doesn't change when off
        self.tv1.power()
        self.tv2.power()
        self.tv1.channel_down()
        assert self.tv1.channel == Television.MAX_CHANNEL #Channel loops up to MAX
        assert self.tv2.channel == Television.MIN_CHANNEL #Other TV doesn't change
        self.tv1.channel = Television.MAX_CHANNEL
        self.tv1.channel_down()
        assert self.tv1.channel == Television.MAX_CHANNEL - 1 #Channel decrements by 1

    def test_volume_up(self):
        self.tv1.volume_up()
        assert self.tv1.volume == Television.MIN_VOLUME #Volume doesn't change when off
        self.tv1.power()
        self.tv2.power()
        self.tv1.volume_up()
        assert self.tv1.volume == Television.MIN_VOLUME + 1 #Volume increments by one
        assert self.tv2.volume == Television.MIN_VOLUME #Other TV doesn't change
        self.tv1.volume = Television.MAX_VOLUME
        self.tv1.volume_up()
        assert self.tv1.volume == Television.MAX_VOLUME #Volume doesn't loop

    def test_volume_down(self):
        self.tv1.volume_down()
        assert self.tv1.volume == Television.MIN_VOLUME #Volume doesn't change when off
        self.tv1.power()
        self.tv2.power()
        self.tv1.volume_down()
        assert self.tv1.volume == Television.MIN_VOLUME #Volume doesn't loop
        self.tv2.volume = Television.MAX_VOLUME
        self.tv1.volume = Television.MAX_VOLUME
        self.tv1.volume_down()
        assert self.tv1.volume == Television.MAX_VOLUME - 1 #Volume decrements by one
        assert self.tv2.volume == Television.MAX_VOLUME  #Other TV doesn't change

if __name__ == '__main__':
    pytest.main()