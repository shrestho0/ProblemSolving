

import re
pattern = "AABBAAAABBBB"

print(re.findall("\w{2}", pattern))