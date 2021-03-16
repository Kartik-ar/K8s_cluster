stdout = "{{ svc['stdout_lines'][2] }}"
start = stdout.find(':')
stop = stdout.find('/')
port = [start,stop]
print(f" http://{{ groups.Master.0 }}{ stdout[{start}:{stop}] } ")
