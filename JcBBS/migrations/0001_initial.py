# Generated by Django 3.2.6 on 2021-08-31 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article_msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nymph_name', models.CharField(blank=True, max_length=32, verbose_name='女神姓名/艺名')),
                ('num', models.PositiveIntegerField(default=1, verbose_name='数量')),
                ('look_score', models.FloatField(default=0, verbose_name='样貌评分')),
                ('server_score', models.FloatField(default=0, verbose_name='服务评分')),
                ('score', models.FloatField(default=0, verbose_name='整体评分')),
                ('contact', models.CharField(max_length=128, verbose_name='联系方式')),
                ('address', models.CharField(max_length=128, verbose_name='地址')),
                ('main_body', models.TextField(max_length=800, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articles_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('lf', '楼凤'), ('xy', '洗浴'), ('zy', '足浴'), ('zj', '站街'), ('qq', 'QQ'), ('hd', '黑店'), ('ktv', 'KTV')], max_length=8, verbose_name='类型')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='省份名称')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_ftc', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('passwd', models.CharField(max_length=128, verbose_name='用户密码')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('jc_coin', models.PositiveIntegerField(verbose_name='用户虚拟币')),
            ],
        ),
        migrations.CreateModel(
            name='Nymph_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('P', '一次'), ('PP', '两次'), ('BT', '半套'), ('BY', '包夜'), ('BH', '包时')], max_length=8, verbose_name='收费类型')),
                ('price', models.FloatField(default=0, verbose_name='价格')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('article_msg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='JcBBS.article_msg')),
            ],
        ),
        migrations.CreateModel(
            name='Nymph_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pthoto_path', models.CharField(blank=True, max_length=512, verbose_name='图片地址')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('article_msg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='JcBBS.article_msg')),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='城市名称')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_ftc', models.IntegerField(default=0)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JcBBS.provinces')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='城市名称')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JcBBS.cities')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='点赞数量')),
                ('conllection', models.PositiveIntegerField(default=0, verbose_name='收藏数量')),
                ('look', models.PositiveIntegerField(default=0, verbose_name='观看数量')),
                ('main_photo', models.CharField(max_length=512, verbose_name='主图地址')),
                ('buy_user_num', models.PositiveIntegerField(default=0, verbose_name='购买人数')),
                ('buy_num', models.PositiveIntegerField(default=0, verbose_name='购买次数')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('article_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JcBBS.articles_type')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JcBBS.block')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JcBBS.users')),
            ],
        ),
        migrations.AddField(
            model_name='article_msg',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='JcBBS.articles'),
        ),
    ]
