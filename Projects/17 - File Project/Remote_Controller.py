import time


class Remote_Controller():

    def __init__(self, Tv_Status="Off", Tv_Volume=0, Channel_List=["BBC1"], Channel="BBC1"):
        print("Creating a remote controller")

        self.Tv_Status = Tv_Status
        self.Tv_Volume = Tv_Volume
        self.Channel_List = Channel_List
        self.Channel = Channel

    def Tv_On(self):

        if self.Tv_Status == "On":
            print("TV is already on")
        else:
            print("Tv is turning on")
            self.Tv_Status = "On"

    def Tv_Off(self):

        if self.Tv_Status == "Off":
            print("TV is already off")
        else:
            print("Tv is turning off")
        self.Tv_Status = "Off"

    def Volume_Adjustment(self):

        while True:
            Answer = input("Volume Down : '<' \nVolume Up : '>' \nExit : 'exit'")

            if Answer == "<":
                if self.Tv_Volume != 0 :
                    self.Tv_Volume -=1
                    print("Volume: ",self.Tv_Volume)

            elif Answer == ">":
                    if self.Tv_Volume != 50:
                        self.Tv_Volume +=1
                        print("Volume: ",self.Tv_Volume)

                    else:
                        print("The sound level has updated.")
                    break

    def Add_Channel (self, Channel_Name):

        print("Adding channel ...")
        time.sleep(1)

        self.Channel_List.append(Channel_Name)
        print("Channel added")



    def __len__(self):
        return len(self.Channel_List)

    def __str__(self):
        return "Tv_Status: {}\nTv_Volume: {} \nChannel List: {} \nWatching Channel: {}\n".format(self.Tv_Status,self.Tv_Volume,self.Channel_List,self.Channel)


Remote_Controller_1 = Remote_Controller()


print("""

Remote Controller

1.Turn on TV
2.Turn off TV
3.Volume Adjustment
4.Add Channel
5.Number of Channels
6.TV info

For exit press Q

""")

while True:

    Operation = input("Choose the operation you want: ")

    if Operation == "Q" or Operation == "q":
        print("Program is closing")
        break

    elif Operation == "1":

        Remote_Controller_1.Tv_On()

    elif Operation == "2":
        Remote_Controller_1.Tv_Off()

    elif Operation == "3":
        Remote_Controller_1.Volume_Adjustment()

    elif Operation == "4":
        Channel_Names = input("input channel names separated by comas")
        Channel_List = Channel_Names.split(",")
        for adding in Channel_List:
            Remote_Controller_1.Add_Channel(adding)

    elif Operation == "5":
        print("Number of Channel: ",len(Remote_Controller_1))


    elif Operation == "6":
        print(Remote_Controller_1)

    else:
        print("Invalid Operation")




