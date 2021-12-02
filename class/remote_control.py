class RemoteControl:

    def __init__(self, television, room):
        self.television = television
        self.room = room

    def next_channel(self):
        print("Next Channel")

    def previous_channel(self):
        print("Previous Channel")

    def choice_channel(self, channel):
        print("It was changed for other channel: {}".format(channel))


room_remote_control = RemoteControl("Samsung", "Room")
print(room_remote_control.television)
print(room_remote_control.room)
room_remote_control.next_channel()
room_remote_control.previous_channel()
room_remote_control.choice_channel("SBT")


kitchen = RemoteControl("LG", "Kitchen")
print(kitchen.television)
print(kitchen.room)
kitchen.next_channel()
kitchen.previous_channel()
kitchen.choice_channel("Record")
