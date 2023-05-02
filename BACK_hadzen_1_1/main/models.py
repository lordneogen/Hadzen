from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
#
    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username
#

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)



class Ch(models.Model):
    name = models.TextField(blank=True, null=False, default='chanell')
    title = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    is_comm = models.BooleanField(blank=True, null=False,default=True)
    owner = models.ForeignKey(AuthUser,on_delete=models.CASCADE, db_column='owner', blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.pk)+' '+self.name

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'
        managed = True
        db_table = 'ch'

class Bl(models.Model):
    name = models.TextField(blank=True, null=True)
    text_in = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    creator = models.ForeignKey(AuthUser,on_delete=models.CASCADE, db_column='creator', blank=True, null=True)
    ch = models.ForeignKey(Ch,on_delete=models.CASCADE,null=True)
    img=models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.pk)+' '+ self.name

    class Meta:
        managed = True
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        db_table = 'bl'

class Subs(models.Model):
    ch=models.ForeignKey(Ch,on_delete=models.CASCADE,null=False)
    user=models.ForeignKey(AuthUser,on_delete=models.CASCADE, db_column='owner', blank=True, null=False)

    def __str__(self):
        return self.ch.name+' '+self.user.username

    class Meta:
        managed = True
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
        unique_together = (('user', 'ch'),)
        db_table = 'sub'





class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Comm(models.Model):
    id = models.BigAutoField(primary_key=True)
    text=models.TextField(null=True,default='text')
    user=models.ForeignKey(AuthUser,on_delete=models.CASCADE, blank=True, null=True)
    bl=models.ForeignKey(Bl,on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True,auto_now_add=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        managed = True
        db_table = 'Comm'

class LikeDisComm(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser,on_delete=models.CASCADE, blank=True, null=False)
    is_like = models.BooleanField(blank=True, null=True,default=False)
    is_dis = models.BooleanField(blank=True, null=True,default=False)
    comm = models.ForeignKey(Comm,on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = (('user', 'comm'),)
        verbose_name = 'Лайк,дизлайк для коментариев'
        verbose_name_plural = 'Лайк,дизлайк для коментариев'
        managed = True
        db_table = 'like_dis_comm'


class LikeDisShareBl(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser,on_delete=models.CASCADE)
    is_like = models.BooleanField(blank=True, null=True,default=False)
    is_dis = models.BooleanField(blank=True, null=True,default=False)
    is_share = models.BooleanField(blank=True, null=True,default=False)
    bl = models.ForeignKey(Bl,on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = (('user', 'bl'),)
        verbose_name = 'Лайк,дизлайк,поделится для блога'
        verbose_name_plural = 'Лайк,дизлайк,поделится для блога'
        managed = True
        db_table = 'like_dis_share_bl'


class Manager(models.Model):
    email = models.ForeignKey(AuthUser,on_delete=models.CASCADE, db_column='email', blank=True, null=True)
    create_field = models.BooleanField(db_column='create_', blank=True, null=True,default=False)  # Field renamed because it ended with '_'.
    update_field = models.BooleanField(db_column='update_', blank=True, null=True,default=False)  # Field renamed because it ended with '_'.
    delete_comm = models.BooleanField(blank=True, null=True,default=False)
    red_ch = models.BooleanField(blank=True, null=True,default=False)
    ch = models.ForeignKey(Ch,on_delete=models.CASCADE, related_name='manager_ch_set', blank=True, null=True)

    def __str__(self):
        return self.ch.name+':'+self.email.username+'''
        '''+ 'create:'+str(self.create_field)+'\nupdate blog:'+str(self.update_field)+'\ndelete comm:'+str(self.delete_comm)+'\nupdate chanell:'+str(self.red_ch)

    class Meta:
        unique_together = (('email','ch'),)
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'
        managed = True
        db_table = 'manager'

