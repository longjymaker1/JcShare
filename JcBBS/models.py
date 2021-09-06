from django.db import models

# Create your models here.


class Provinces(models.Model):
    """省份表"""
    name = models.CharField(max_length=32, verbose_name="省份名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_ftc = models.IntegerField(default=0)

    class Meta:
        verbose_name = '省份表'
        verbose_name_plural = verbose_name


class Cities(models.Model):
    """城市表"""
    name = models.CharField(max_length=32, verbose_name="城市名称")
    province = models.ForeignKey(Provinces, on_delete=models.CASCADE, verbose_name='省份id')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_ftc = models.IntegerField(default=0)

    class Meta:
        verbose_name = '城市表'
        verbose_name_plural = verbose_name


class Block(models.Model):
    """城市街区"""
    name = models.CharField(max_length=32, verbose_name="城市-区")
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, verbose_name='城市id')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '城市区'
        verbose_name_plural = verbose_name


class Users(models.Model):
    """用户表"""
    name = models.CharField(max_length=64, verbose_name="用户名")
    email = models.EmailField(verbose_name="用户邮箱")
    passwd = models.CharField(max_length=128, verbose_name="用户密码")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    jc_coin = models.PositiveIntegerField(verbose_name="用户虚拟币")

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class Articles_type(models.Model):
    """信息类型"""
    article_type = (
        (u'lf', u'楼凤'),
        (u'xy', u'洗浴'),
        (u'zy', u'足浴'),
        (u'zj', u'站街'),
        (u'qq', u'QQ'),
        (u'hd', u'黑店'),
        (u'ktv', u'KTV'),
    )
    types = models.CharField(max_length=8, choices=article_type, verbose_name='类型')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '信息类型'
        verbose_name_plural = verbose_name


class Articles(models.Model):
    """帖子主表"""
    title = models.CharField(max_length=128, blank=False, verbose_name="标题")
    like = models.PositiveIntegerField(default=0, blank=False, verbose_name="点赞数量")
    conllection = models.PositiveIntegerField(default=0, blank=False, verbose_name="收藏数量")
    look = models.PositiveIntegerField(default=0, blank=False, verbose_name="观看数量")
    main_photo = models.CharField(max_length=512, verbose_name="主图地址")
    buy_user_num = models.PositiveIntegerField(default=0, verbose_name="购买人数")
    buy_num = models.PositiveIntegerField(default=0, verbose_name="购买次数")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='用户id')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name='城市-区id')
    article_type = models.ForeignKey(Articles_type, on_delete=models.CASCADE, verbose_name='帖子类型')

    class Meta:
        verbose_name = '帖子主表'
        verbose_name_plural = verbose_name


class Article_msg(models.Model):
    """帖子信息"""
    nymph_name = models.CharField(max_length=32, blank=True, verbose_name="女神姓名/艺名")
    num = models.PositiveIntegerField(default=1, blank=False, verbose_name="数量")
    look_score = models.FloatField(default=0, blank=False, verbose_name="样貌评分")
    server_score = models.FloatField(default=0, blank=False, verbose_name="服务评分")
    score = models.FloatField(default=0, blank=False, verbose_name="整体评分")
    contact = models.CharField(max_length=128, blank=False, verbose_name="联系方式")
    address = models.CharField(max_length=128, blank=False, verbose_name="地址")
    main_body = models.TextField(max_length=800, verbose_name="描述")
    article = models.OneToOneField(Articles, on_delete=models.CASCADE, verbose_name='帖子id')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '帖子信息表'
        verbose_name_plural = verbose_name


class Nymph_price(models.Model):
    """价格"""
    server_type = (
        (u'P', u'一次'),
        (u'PP', u'两次'),
        (u'BT', u'半套'),
        (u'BY', u'包夜'),
        (u'BH', u'包时'),
    )
    types = models.CharField(max_length=8, choices=server_type, verbose_name='收费类型')
    price = models.FloatField(default=0, blank=False, verbose_name='价格')
    article_msg = models.OneToOneField(Article_msg, on_delete=models.CASCADE, verbose_name='帖子详情id')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '价格表'
        verbose_name_plural = verbose_name


class Nymph_photo(models.Model):
    """照片"""
    pthoto_path = models.CharField(max_length=512, blank=True, verbose_name="图片地址")
    article_msg = models.OneToOneField(Article_msg, on_delete=models.CASCADE, verbose_name='帖子详情id')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '照片表'
        verbose_name_plural = verbose_name

