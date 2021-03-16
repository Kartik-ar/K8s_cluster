stdout = "{{ svc['stdout_lines'][1] }}"
start = stdout.find(':')
stop = stdout.find('/')
port = stdout[start:stop]
print(" http://{{ groups.Master.0 }}{0} ".format(port))
