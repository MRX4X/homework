from threading import Thread
from datetime import datetime
start_time = datetime.now()
def replace_id(path_file):
    print(path_file)
    with open(path_file, 'r') as file:
        a=file.read()
        print(a)
        s_text=a.split(':')
        s_text[0]='id'

    with open(path_file, 'w') as file_1:
        ind_1=str(s_text[0])
        ind_2=str(s_text[1])
        b = file_1.write(ind_1)
        c=file_1.write(':')
        d=file_1.write(ind_2)


t1=Thread(target=replace_id('/Users/denis/homework/Task_25_Flow/Files/file0.txt'))
t1.start()
print(datetime.now() - start_time)

