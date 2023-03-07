import re

# with open('row.txt', 'r') as file:
#     text = file.read()

text = "AAaAaASabbD_S Aada_dabb_asd_sdAS123fasdb"

# 1 
# match = re.findall(r'a+b*',text)
# if match:
#     print(f"matches and is {match}")
# else:
#     print("not matches")

# 2
# match = re.findall(r'a+[b]{2,3}', text)
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
# match = re.findall(r'[A-Z]{1}[a-z]+', text)
# if match:
#     print(f"matches and is {match}")
# else:
#     print("not matches")

# 5
# match = re.findall(r'a.*b', text)
# if match:
#     print(f"matches and is {match}")
# else:
#     print("not matches")

# 6
# new_text = re.sub(r'[ ,.]', ':', text)
# print(new_text)
# 7
# A Match object represents a matched part of the target string. It may be parametrized as Match[str]
# text = "foo_bar_fff"
# camel_text =  re.sub(r'(.*?)_([a-zA-Z])', lambda x: x.group(1)+x.group(2).upper(), text)
# print(camel_text)

# 8
# text = "AidarNurkin"
# split_string = re.findall('[A-Z][^A-Z]*', text)
# print(split_string)
# 9
# text = "AidarAasdNurkinAidar"
# spaces_string = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
# print(spaces_string)

# 10
# text = 'AidarNurkinSha'
# snake_string = re.sub(r"(.+?)([A-Z])", lambda x: (x.group(1) + "_" + x.group(2)).lower(), text)
# print(snake_string)