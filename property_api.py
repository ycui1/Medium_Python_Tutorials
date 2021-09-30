class ClientV0:
    def __init__(self, first_name, last_name, middle_initial='-'):
        print("Instantiate Client Class V0")
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial
        self.initials = first_name[0] + middle_initial + last_name[0]


# With V0
client = ClientV0("Jack", "Davis", "E")
print("Client V0 Initials:", client.initials)


class ClientV1:
    def __init__(self, first_name, last_name, middle_initial='-'):
        print("Instantiate Client Class V1")
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial

    def initials(self):
        return self.first_name[0] + self.middle_initial + self.last_name[0]


# With V1
client = ClientV1("Jack", "Davis", "E")
print("Client V1 Initials:", client.initials)
print("Updated API Call - Client V1 Initials:", client.initials())


class ClientV2:
    def __init__(self, first_name, last_name, middle_initial='-'):
        print("Instantiate Client Class V2")
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial

    @property
    def initials(self):
        print("Alert! Someone is accessing the initials.")
        return self.first_name[0] + self.middle_initial + self.last_name[0]


# With V2
client = ClientV2("Jack", "Davis", "E")
print("Client V2 Initials:", client.initials)


# With V0
client0 = ClientV0("Jack", "Davis", "E")
print("Before Changing Initials:", client0.initials)
client0.initials = "ABC"
print("After Changing Initials:", client0.initials)

# With V2
client2 = ClientV2("Jack", "Davis", "E")
print("Before Changing Initials:", client2.initials)
client2.initials = "ABC"
print("After Changing Initials:", client2.initials)