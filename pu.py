import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ICS.settings')
import django
django.setup()
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

#  Update the users in this list.
#  Each tuple represents the username, password, and email of a user.
users = [
    ('user_1','phgzHpXcnJ'),
    ('马尧新','812802'),
    ('陈帅','904119'),
    ('陈丽','550392'),
    ('赵蓬蓬','914655'),
    ('俞亦冰','186496'),
    ('张敏仪','272008'),
    ('庞洁神','930952'),
    ('陈环','947757'),
    ('朱佳敏','753988'),
    ('奚俊英','933288'),
    ('陈建伟','403669'),
    ('陈雅飞','492119'),
    ('陈琴','593944'),
    ('沈建芬','951502'),
    ('冯利芳','961201'),
    ('徐芮','656283'),
    ('蒋姚威','309715'),
    ('王颖','738458'),
    ('汤清峰','292601'),
    ('郑建栋','792980'),
    ('葛星程','369161'),
    ('王卡尔','486871'),
    ('肖爽','883614'),
    ('陈柏柱','952124'),
    ('封燕萍','962117'),
    ('周莉','634418'),
    ('王志伟','840274'),
    ('施雯雅','926682'),
    ('徐凌鹏','100258'),
    ('朱郦萍','619274'),
    ('潘国勇','544349'),
    ('王萍','984956'),
    ('娄茜','114687'),
    ('李燕娜','833258'),
    ('黄京霞','982506'),
    ('沈婵媛','720209'),
    ('乐仁贵','224888'),
    ('李大卫','994889'),
    ('吴钧涛','503369'),
    ('王雷霞','546331'),
    ('赵绿弟','610686'),
    ('汪蓓','339230'),
    ('吴振国','604792'),
    ('林朝霞','549072'),
    ('沈宏萍','209250'),
    ('厉万骁','655662'),
    ('周雅娟','347586'),
    ('汤海娣','872043'),
    ('叶亮','817524'),
    ('沈冬冬','193906'),
    ('朱敏敏','372166'),
    ('林琴','744152'),
    ('莫罗妮','974787'),
    ('王星星','453142'),
    ('金利','453677'),
    ('李清清','583240'),
    ('莫秋伟','365866'),
    ('宣佳卉','619576'),
    ('吴芬','302698'),
    ('滕菲','419097'),
    ('曹华娟','907719'),
    ('汪琦','970019'),
    ('葛晓玲','377480'),
    ('胡灶娟','341862'),
    ('潘梦怡','998710'),
    ('王琴','244720'),
    ('沃冬冬','682463'),
    ('杨彬','663689'),
    ('孔凯杰','517860'),
    ('沈珠慧','529152'),
]

for username, password in users:
    try:
        print ('Creating user {0}.'.format(username))
        user = User.objects.create_user(username=username)
        user.set_password(password)
        user.save()

        assert authenticate(username=username, password=password)
        print ('User {0} successfully created.'.format(username))

    except:
        print ('There was a problem creating the user: {0}.  Error: {1}.'.format(username, sys.exc_info()[1]))
