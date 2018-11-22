from APP04.models import *
import xadmin
from xadmin import  views
# Register your models here.
class TypeAdmin():
    # 在admin中显⽰顺序
    list_display = ["id", "name"]
    # 给admin添加搜索功能
    search_fields = ["id", "name"]
    # 筛选字段
    list_filter = ["id", "name"]
    # 排序字段
    ordering = ["id"]


# class UserInfoAdmin():
#     # 在admin中显⽰顺序
#     list_display = ["username", "gender", "mobile", "email", "is_staff", "is_superuser"]
#     # 给admin添加搜索功能
#     search_fields = ["username", "gender", "mobile", "email"]
#     # 筛选字段
#     list_filter = ["username", "gender", "mobile", "email"]
#     # 直接编辑字段
#     list_editable = ["is_staff", "is_superuser"]
#     # 排序字段
#     ordering = ["id"]


class ContentAdmin():
    # 在admin中显⽰顺序
    list_display = ["id", "title", "picture"]
    # 给admin添加搜索功能
    search_fields = ["id", "publish_time", "title", "picture"]
    # 排序字段
    ordering = ["-publish_time"]


class CommentAdmin():
    # 在admin中显⽰顺序
    list_display = ["id", "content", "user_id", "news_id"]
    # 给admin添加搜索功能
    search_fields = ["id", "publish_time", "user_id", "news_id"]
    # 直接编辑字段

    # 排序字段
    ordering = ["-publish_time"]

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    # 后台管理系统的标题
    site_title = "后台管理系统"
    # 底部显示信息
    site_footer = "底部信息"
    menu_style = "accordion"




xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Type, TypeAdmin)
# xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(Content, ContentAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)