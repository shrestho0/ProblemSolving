


# lines = []
# for line in range(int(input())):
#     lines.append(input())

lines = ['<head>', '<title>HTML</title>', '</head>', '<object type="application/x-flash" ', '  data="your-file.swf" ', '  width="0" height="0">', '  <!-- <param name="movie" value="your-file.swf" /> -->', '  <param name="quality" value="high"/>', '</object>']
for line in lines:
    splitted = line.split()
    if len(splitted) < 4:
        splitted = splitted[0][1:-1]
    
    
    print(splitted)