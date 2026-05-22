from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        self.validate_value(value)
        super().__init__(value)

    def validate_value(self, value):
         if not re.fullmatch(r"^\d{10}$", value):
            raise ValueError(f"Invalid phone number: {value}")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_value: str):
        if not any(phone.value == phone_value for phone in self.phones):  
            self.phones.append(Phone(phone_value))

    def remove_phone(self, phone_value: str):
        phone = self.find_phone(phone_value)
        if phone is not None:
            self.phones.remove(phone)
            print(f"Phone {phone_value} was deleted")
        else:
            print(f"Phone {phone_value} not found to delete")
                
    def edit_phone(self, phone_value: str, new_phone_value: str):
        phone = self.find_phone(phone_value)
        if phone is not None:
            phone.value = new_phone_value
            print(f"Phone {phone_value} was updated")
        else:
            print(f"Phone {phone_value} not found to edit")

    def find_phone(self, phone_value):
        for phone in self.phones:
            if phone.value == phone_value:
                return phone
            
        return None
            

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
    
    def add_record(self, new_record: Record):
        if new_record not in self.data:
            self.data[new_record.name.value] = new_record

    def find(self, name: str):
        if name in self.data:
            return self.data[name]
        
        return None
    
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        