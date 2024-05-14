info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info_list = info.split(':')
new_info = '+'.join(info_list)

new_info2 = info.replace(':', '+')
print(new_info2)