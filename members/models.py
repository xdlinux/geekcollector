from django.db import models

class Group(models.Model):
    """小组，包括WDT，android，Video，Newbie"""
    name = models.CharField(max_length=20)
    describe = models.CharField(max_length=140, blank=True) #小组简介限制字数一百四，大家都懂的，回来让各个小组的负责人写，WDT的畜松你自己搞定吧~
    def __unicode__(self):
        return self.name

class Member(models.Model):
    """成员的DRM"""
    #基本信息
    name = models.CharField(max_length=10)
    student_num = models.IntegerField()
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=75, blank=True)

    #小组选择信息，每人可以选择多个小组，设定related_name为groups就可以通过Group.members直接访问某个小组所有报名的人了
    groups = models.ManyToManyField(Group, related_name='members', through='MenberGroup')

    #个人感兴趣或者了解的科技相关的关键字,每个人都可以选很多个，所以直接以字符串储存，后期在做处理,
    kw = models.TextField(blank=True)
    def __unicode__(self):
        return self.name
    
class MemberGroup(models.Model):
    """用于连接用户类Member和小组类Group"""
    Member = models.ForeignKey(Member)
    Group = models.ForeignKey(Group)

