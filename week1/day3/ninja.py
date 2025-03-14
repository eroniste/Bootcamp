class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
    
    def call(self, other_phone):
        call_message = f"Call from {self.phone_number} to {other_phone.phone_number}"
        self.call_history.append(call_message)
        print(call_message)
    
    def show_call_history(self):
        print("Call History:")
        for call in self.call_history:
            print(call)
    
    def send_message(self, other_phone, content):
        message = {
            'to': other_phone.phone_number,
            'from': self.phone_number,
            'content': content
        }
        self.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: {content}")
    
    def show_outgoing_messages(self):
        print("Outgoing Messages:")
        for message in self.messages:
            if message['from'] == self.phone_number:
                print(f"To: {message['to']}, Content: {message['content']}")
    
    def show_incoming_messages(self):
        print("Incoming Messages:")
        for message in self.messages:
            if message['to'] == self.phone_number:
                print(f"From: {message['from']}, Content: {message['content']}")
    
    def show_messages_from(self, other_phone):
        print(f"Messages from {other_phone.phone_number}:")
        for message in self.messages:
            if message['from'] == other_phone.phone_number:
                print(f"To: {message['to']}, Content: {message['content']}")

# Example usage
if __name__ == "__main__":
    phone1 = Phone("123-456-7890")
    phone2 = Phone("987-654-3210")
    
    phone1.call(phone2)
    phone1.send_message(phone2, "Hello!")
    phone2.send_message(phone1, "Hi, how are you?")
    
    phone1.show_call_history()
    phone1.show_outgoing_messages()
    phone2.show_incoming_messages()
    phone1.show_messages_from(phone2)
