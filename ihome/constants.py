# 保存常量数据

# 图片验证码的redis的有效期 单位秒
IMAGE_CODE_REDIS_EXPIRES =180

# 短信验证码的redis的有效期 单位秒
SMS_CODE_REDIS_EXPIRES = 600

# 发送短信验证码的问题， 单位秒
SEND_SMS_CODE_INTERVAL = 100

# 登录错误尝试次数
LOGIN_ERROR_MAX_TIMES = 5

# 登录错误限制的时间， 单位秒
LOGIN_ERROR_FORBID_TIME = 600

# 七牛的域名
QINIU_URL_DOMAIN = "https://qvyo4b3rp.hd-bkt.clouddn.com/"

# 用户上传图片的保存地址域名
UPLOAD_IMAGE_URL = 'http://127.0.0.1:5000/static/images/'

# 城区信息的缓存时间，单位：秒
AREA_INFO_REDIS_EXPIRE = 7200

# 首页显示的图片数量，单位：个
HOME_PAGE_INDEX_IMAGES = 10

# 首页信息的缓存时间，单位：秒
HOME_PAGE_REDIS_EXPIRE = 3600

# 房屋详情信息的缓存时间，单位：秒
HOUSE_DETAIL_REDIS_EXPIRE = 3600

# 房屋列表页面每页数据容量
HOUSE_LIST_PER_PAGE_CAPACITY = 2

# 列表页缓存的有效期，单位：秒
HOUSE_LIST_PAGE_REDIS_EXPIRE = 3600

# 详情页面显示的评论条目数
HOUSE_DETAIL_COMMENT_DISPLAY_COUNTS = 20

# 支付宝的网关地址
API_PAY_ADDRESS = "https://openapi.alipaydev.com/gateway.do?"
