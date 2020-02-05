from datetime import datetime
import datetime

def check_birthdate(year, month, day):
	if datetime.date.today()>datetime.date(year,month,day):
		return True
	return False
	# write code here

def calculate_age(year, month, day):
	age = datetime.date.today() -datetime.date(year,month,day)
	age_in_years=age.days/365
	print ("You are "+ str(int(age_in_years))+" years old")
    # write code here

def main():
        year=input("Enter year of birth: ")
        month=input("Enter month of birth: ")
        day=input("Enter day of birth: ")
        if(check_birthdate(int(year), int(month), int(day))):
                calculate_age(int(year), int(month), int(day))
	# write main code here


if __name__ == '__main__':
	main()
