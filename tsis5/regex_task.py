import re

with open('row.txt', 'r') as file:
    text = file.read()

# 1
# match = re.findall(r'a+b*',text)
# if match:
#     print(f"matches and is {match}")
# else:
#     print("not matches")

# 2
# match = re.findall(r'a(bb|bbb)', text)
# if match:
#     print(f"matches and is {match}")
# else:
#     print("not matches")

# 3
# match = re.findall(r'[a-z]+_[a-z]+', text)
# if match:
#     print(f"matches and is {match}")
# else:
#     print("not matches")

# 4
# match = re.findall(r'[A-Z][a-z]+', text)
# if match:
#     print(f"matches and is {match}")
# else:
#     print("not matches")

# 5
# match = re.findall(r'a.*b$', text)
# if match:
#     print(f"matches and is {match}")
# else:
#     print("not matches")

# 6
# new_text = re.sub(r'[ ,.]', ':', text)

# 7
# camel_text = re.sub(r'_(\w)', lambda match: match.group(1).upper(), text)

# 8
# text = "AidarNurkin"
# split_string = re.findall('[A-Z][^A-Z]*', text)

# 9
# text = "AidarNurkin"
# spaces_string = re.sub(r'(?<=\w)([A-Z])', r' \1', text)
# print(spaces_string)

# 10
# text = 'AidarNurkin'
# snake_string = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
# print(snake_string)