#Write a python script to determine whether a string contains a specific substring.

string=input('Enter a String : ')
sub_string=input('Enter a Sub-String, Which You Want To Find : ')

print('Yes, Sub-String in String',string.count(sub_string),'Times.') if sub_string in string else print("No, This Sub-String Doesn't Exists in String...")