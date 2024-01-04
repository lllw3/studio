#搜索晋献春医生列表，截至2020/7/30日可以无限刷新,不会屏蔽接口。可以更换搜索的医生姓名
SEARCHDOCTOR_URL = 'https://dyh.xqyy.com.cn/reservegh?cls=yygh&m=searchDoctor&funcId=function03&is_searchdept=1&is_searchspecial=1&searchvalue=晋献春'
# SEARCHDOCTOR_URL = 'https://dyh.xqyy.com.cn/reservegh?cls=yygh&m=searchDoctor&funcId=function03&is_searchdept=1&is_searchspecial=1&searchvalue=陈勇鹏'

#排班地址
CHOOSEDATEEXT_URL = 'https://dyh.xqyy.com.cn/reservegh?cls=yygh&m=choosedateext&deptCode={deptCode}&doctorNo={doctorNo}&funcId=function03'

#余号地址,需要提供排班的id
SCHEDULETIME_URL = 'https://dyh.xqyy.com.cn/reservegh?cls=yygh&m=scheduleTime&funcId=function03&scheduleid={}'

####晋献春，专家号
DOCTORNO_212820 = '2baf47ce661741e2b54a2bde72051411'
DEPTCODE_212820 = 212820
DOCTORNO_70='57dc7270631b46a49656a1e20bbdfbaf'
DEPTCODE_70 = 70
##添加测试医生
# DOCTORNO_212820 = 'e8d75990ac5a4a89937b3a58bc1b3383'
# DEPTCODE_212820 = 212820

##依赖库
#schedule,grequests

#配置微信点击位置
# POSITIONS = [((19,522),'任巧云'),((610,519),'郭梦圆'),((1160,518),'钟俊非')]
POSITIONS = {'任巧云':(629,515),'郭梦圆':(1155,522),'钟俊飞':(90,523)}