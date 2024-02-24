import subprocess


def main():
    a = subprocess.check_output('date', encoding='utf-8', shell=True)
    b = subprocess.check_output('hostname', encoding='utf-8', shell=True)
    c = subprocess.check_output('ip -br a | grep UP', encoding='utf-8', shell=True)
    e = subprocess.check_output('last -n 10 -i', encoding='utf-8', shell=True)
    d = subprocess.check_output('less ~/.bash_history | tail', encoding='utf-8', shell=True)
    n = subprocess.check_output('ps -a', encoding='utf-8', shell=True)
    m = subprocess.check_output('w', encoding='utf-8', shell=True)
    print(f' дата и время: {a}')
    print('***************************************************')
    print(f'имя хоста: {b}')
    print('***************************************************')
    print(f'ip address: {c}')
    print('***************************************************')
    print('***************************************************')
    print('10 последних входов в систему')
    print(e)
    print('***************************************************')
    print('***************************************************')
    print('10 последних команд в консоли')
    print(d)
    print('***************************************************')
    print('***************************************************')
    print('текущие фоновые процессы')
    print(n)
    print('***************************************************')
    print('***************************************************')
    print('текущие сессии')
    print(m)
    print('***************************************************')

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
