# Тask4:
# Удалить все не ASCII символы из файла
# Удалить переводы строки в блоке BODY HTML-файла (сделать содержимое блока «inline»)
# Сохранить оба обновленных файла в созданную директорию на уровень выше текущей.

import os


def delete_not_ascii(file, pth):

    with open(file, 'r') as f:
        content = f.read().encode('ascii', errors='ignore')

    with open(os.path.join('..', pth, '_'.join(['no', 'ascii', file])), 'w') as f:
        f.write(content.decode('utf-8'))


def delete_newline(file, pth):

    with open(file, 'r') as f:
        content = f.read()

    body_start = content.find('<BODY>')+7
    body_end = content.rfind('</BODY>')-1
    newlines_amount = content[body_start:body_end].count('\n')

    with open(os.path.join('..', pth, '_'.join(['no', 'newlines', file])), 'w') as f:
        f.write(''.join([content[:body_start],
                         content[body_start:body_end].replace('\n', ''),
                         content[body_end + newlines_amount - 2:]]))


if __name__ == '__main__':
    uplvl_folder_name = 'test'
    os.mkdir(os.path.join('..', uplvl_folder_name))
    delete_not_ascii('day_1_task4_data.html', uplvl_folder_name)
    delete_newline('day_1_task4_data.html', uplvl_folder_name)


# Результат:
# $ python3 task4.py
# $ ls ../test
# no_ascii_day_1_task4_data.html  no_newlines_day_1_task4_data.html
# $ cat ../test/no_ascii_day_1_task4_data.html

# <!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
# <HTML>
#    <HEAD>
#       <TITLE>
#          A Small Hello.    .
#       </TITLE>
#    </HEAD>
# <BODY>
#    <H1>Hi   </H1>
#    <P>I want to be inline, in my source code</P>
#    <P>This is very minimal "hello world" HTML document.</P>
# </BODY>
# </HTML>

# $ cat ../test/no_newlines_day_1_task4_data.html

# <!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
# <HTML>
#    <HEAD>
#       <TITLE>
#          A Small Hello. Это по идеи заголовок.
#       </TITLE>
#    </HEAD>
# <BODY>
#    <H1>Hi я интерактивная страница</H1>   <P>I want to be inline, in my source c
# ode</P>   <P>This is very minimal "hello world" HTML document.</P>
# </BODY>
# </HTML>