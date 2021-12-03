# 2021kbo.txt 만들기

with open('2021kbo.txt', 'w') as f:
    team = ['NC', '키움', '기아', '삼성', '두산', '롯데']

    for i in team:
        f.write(i + '\n')