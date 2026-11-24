class Television:
    #Constant class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the status of the TV
        """
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self) -> None:
        """
        Toggles the muted status of the TV, unless powered off
        """
        if self.status:
            if self.muted:
                self.muted = False
            else:
                self.muted = True

    def channel_up(self) -> None:
        """
        increases the channel by 1 unless powered off
        """
        if self.status:
            if self.channel < Television.MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        decreases the channel by 1 unless powered off
        """
        if self.status:
            if self.channel > Television.MIN_CHANNEL:
                self.channel -= 1
            else:
                self.channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        increases the volume by 1 unless powered off
        """
        if self.status:
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1
            if self.muted:
                self.mute()

    def volume_down(self) -> None:
        """
        decreases the volume by 1 unless powered off
        """
        if self.status:
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1
            if self.muted:
                self.mute()

    def get_volume(self) -> integer:
        """
        :return: Volume of the TV, unless muted, which returns 0 instead
        """
        if self.muted:
            return 0
        return self.volume

    def __str__(self) -> string:
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.get_volume()}'