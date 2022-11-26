import phonenumbers
from phonenumbers import carrier,geocoder,timezone

while True:
    mobile_Num = input("Enter Mobile Number With Country Code --> ")
    mobile_Num = phonenumbers.parse(mobile_Num)

    print(timezone.time_zones_for_number(mobile_Num))

    print(carrier.name_for_number(mobile_Num, "en"))

    print(geocoder.description_for_number(mobile_Num, "en"))

    print("Valid Mobile Number : ", phonenumbers.is_valid_number(mobile_Num))

    print("Checking Possibility Of Number : ",
        phonenumbers.is_possible_number(mobile_Num))
