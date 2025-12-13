"""App name to package name mapping for supported applications.

This mapping supports both Chinese and English app names to accommodate users
in different regions. Chinese apps like WeChat (微信) and Taobao (淘宝) are
widely used and should be supported by their native names.
"""

APP_PACKAGES: dict[str, str] = {
    # Social & Messaging
    "微信": "com.tencent.mm",  # WeChat (Chinese name)
    "QQ": "com.tencent.mobileqq",
    "微博": "com.sina.weibo",  # Weibo (Chinese name)
    # E-commerce
    "淘宝": "com.taobao.taobao",  # Taobao (Chinese name)
    "京东": "com.jingdong.app.mall",  # JD.com (Chinese name)
    "拼多多": "com.xunmeng.pinduoduo",  # Pinduoduo (Chinese name)
    "淘宝闪购": "com.taobao.taobao",  # Taobao Flash Sale (Chinese name)
    "京东秒送": "com.jingdong.app.mall",  # JD Express (Chinese name)
    # Lifestyle & Social
    "小红书": "com.xingin.xhs",  # Xiaohongshu / RedNote (Chinese name)
    "豆瓣": "com.douban.frodo",  # Douban (Chinese name)
    "知乎": "com.zhihu.android",  # Zhihu (Chinese name)
    # Maps & Navigation
    "高德地图": "com.autonavi.minimap",  # Amap (Chinese name)
    "百度地图": "com.baidu.BaiduMap",  # Baidu Maps (Chinese name)
    # Food & Services
    "美团": "com.sankuai.meituan",  # Meituan (Chinese name)
    "大众点评": "com.dianping.v1",  # Dianping (Chinese name)
    "饿了么": "me.ele",  # Ele.me (Chinese name)
    "肯德基": "com.yek.android.kfc.activitys",  # KFC (Chinese name)
    # Travel
    "携程": "ctrip.android.view",  # Ctrip (Chinese name)
    "铁路12306": "com.MobileTicket",  # China Railway 12306 (Chinese name)
    "12306": "com.MobileTicket",
    "去哪儿": "com.Qunar",  # Qunar (Chinese name)
    "去哪儿旅行": "com.Qunar",  # Qunar Travel (Chinese name)
    "滴滴出行": "com.sdu.did.psnger",  # DiDi (Chinese name)
    # Video & Entertainment
    "bilibili": "tv.danmaku.bili",
    "抖音": "com.ss.android.ugc.aweme",  # Douyin / TikTok China (Chinese name)
    "快手": "com.smile.gifmaker",  # Kuaishou (Chinese name)
    "腾讯视频": "com.tencent.qqlive",  # Tencent Video (Chinese name)
    "爱奇艺": "com.qiyi.video",  # iQiyi (Chinese name)
    "优酷视频": "com.youku.phone",  # Youku (Chinese name)
    "芒果TV": "com.hunantv.imgo.activity",  # Mango TV (Chinese name)
    "红果短剧": "com.phoenix.read",  # HongGuo Short Drama (Chinese name)
    # Music & Audio
    "网易云音乐": "com.netease.cloudmusic",  # NetEase Cloud Music (Chinese name)
    "QQ音乐": "com.tencent.qqmusic",  # QQ Music (Chinese name)
    "汽水音乐": "com.luna.music",  # Qishui Music (Chinese name)
    "喜马拉雅": "com.ximalaya.ting.android",  # Ximalaya (Chinese name)
    # Reading
    "番茄小说": "com.dragon.read",  # Tomato Novel (Chinese name)
    "番茄免费小说": "com.dragon.read",  # Tomato Free Novel (Chinese name)
    "七猫免费小说": "com.kmxs.reader",  # QiMao Free Novel (Chinese name)
    # Productivity
    "飞书": "com.ss.android.lark",  # Feishu / Lark (Chinese name)
    "QQ邮箱": "com.tencent.androidqqmail",  # QQ Mail (Chinese name)
    # AI & Tools
    "豆包": "com.larus.nova",  # Doubao (Chinese name)
    # Health & Fitness
    "keep": "com.gotokeep.keep",
    "美柚": "com.lingan.seeyou",  # Meiyou (Chinese name)
    # News & Information
    "腾讯新闻": "com.tencent.news",  # Tencent News (Chinese name)
    "今日头条": "com.ss.android.article.news",  # Toutiao (Chinese name)
    # Real Estate
    "贝壳找房": "com.lianjia.beike",  # Beike (Chinese name)
    "安居客": "com.anjuke.android.app",  # Anjuke (Chinese name)
    # Finance
    "同花顺": "com.hexin.plat.android",  # Tonghuashun (Chinese name)
    # Games
    "星穹铁道": "com.miHoYo.hkrpg",  # Honkai: Star Rail (Chinese name)
    "崩坏：星穹铁道": "com.miHoYo.hkrpg",  # Honkai: Star Rail (Chinese name, full)
    "恋与深空": "com.papegames.lysk.cn",  # Love and Deepspace (Chinese name)
    # System and Common Apps
    "AndroidSystemSettings": "com.android.settings",
    "Android System Settings": "com.android.settings",
    "Android  System Settings": "com.android.settings",
    "Android-System-Settings": "com.android.settings",
    "Settings": "com.android.settings",
    "AudioRecorder": "com.android.soundrecorder",
    "audiorecorder": "com.android.soundrecorder",
    # International Apps - Finance & Productivity
    "Bluecoins": "com.rammigsoftware.bluecoins",
    "bluecoins": "com.rammigsoftware.bluecoins",
    "Broccoli": "com.flauschcode.broccoli",
    "broccoli": "com.flauschcode.broccoli",
    # International Apps - Travel & Booking
    "Booking.com": "com.booking",
    "Booking": "com.booking",
    "booking.com": "com.booking",
    "booking": "com.booking",
    "BOOKING.COM": "com.booking",
    "Expedia": "com.expedia.bookings",
    "expedia": "com.expedia.bookings",
    "Trip.com": "ctrip.english",
    "trip.com": "ctrip.english",
    # International Apps - Browsers & Tools
    "Chrome": "com.android.chrome",
    "chrome": "com.android.chrome",
    "Google Chrome": "com.android.chrome",
    "Clock": "com.android.deskclock",
    "clock": "com.android.deskclock",
    "Contacts": "com.android.contacts",
    "contacts": "com.android.contacts",
    # International Apps - Education & Learning
    "Duolingo": "com.duolingo",
    "duolingo": "com.duolingo",
    # International Apps - Files & Storage
    "Files": "com.android.fileexplorer",
    "files": "com.android.fileexplorer",
    "File Manager": "com.android.fileexplorer",
    "file manager": "com.android.fileexplorer",
    # International Apps - Email & Communication (Google)
    "gmail": "com.google.android.gm",
    "Gmail": "com.google.android.gm",
    "GoogleMail": "com.google.android.gm",
    "Google Mail": "com.google.android.gm",
    "GoogleFiles": "com.google.android.apps.nbu.files",
    "googlefiles": "com.google.android.apps.nbu.files",
    "FilesbyGoogle": "com.google.android.apps.nbu.files",
    "Files by Google": "com.google.android.apps.nbu.files",
    "GoogleCalendar": "com.google.android.calendar",
    "Google-Calendar": "com.google.android.calendar",
    "Google Calendar": "com.google.android.calendar",
    "google-calendar": "com.google.android.calendar",
    "google calendar": "com.google.android.calendar",
    "GoogleChat": "com.google.android.apps.dynamite",
    "Google Chat": "com.google.android.apps.dynamite",
    "Google-Chat": "com.google.android.apps.dynamite",
    "GoogleClock": "com.google.android.deskclock",
    "Google Clock": "com.google.android.deskclock",
    "Google-Clock": "com.google.android.deskclock",
    "GoogleContacts": "com.google.android.contacts",
    "Google-Contacts": "com.google.android.contacts",
    "Google Contacts": "com.google.android.contacts",
    "google-contacts": "com.google.android.contacts",
    "google contacts": "com.google.android.contacts",
    "GoogleDocs": "com.google.android.apps.docs.editors.docs",
    "Google Docs": "com.google.android.apps.docs.editors.docs",
    "googledocs": "com.google.android.apps.docs.editors.docs",
    "google docs": "com.google.android.apps.docs.editors.docs",
    "Google Drive": "com.google.android.apps.docs",
    "Google-Drive": "com.google.android.apps.docs",
    "google drive": "com.google.android.apps.docs",
    "google-drive": "com.google.android.apps.docs",
    "GoogleDrive": "com.google.android.apps.docs",
    "Googledrive": "com.google.android.apps.docs",
    "googledrive": "com.google.android.apps.docs",
    "GoogleFit": "com.google.android.apps.fitness",
    "googlefit": "com.google.android.apps.fitness",
    "Google Fit": "com.google.android.apps.fitness",
    "GoogleKeep": "com.google.android.keep",
    "googlekeep": "com.google.android.keep",
    "Google Keep": "com.google.android.keep",
    "GoogleMaps": "com.google.android.apps.maps",
    "Google Maps": "com.google.android.apps.maps",
    "googlemaps": "com.google.android.apps.maps",
    "google maps": "com.google.android.apps.maps",
    "Google Play Books": "com.google.android.apps.books",
    "Google-Play-Books": "com.google.android.apps.books",
    "google play books": "com.google.android.apps.books",
    "google-play-books": "com.google.android.apps.books",
    "GooglePlayBooks": "com.google.android.apps.books",
    "googleplaybooks": "com.google.android.apps.books",
    "GooglePlayStore": "com.android.vending",
    "Google Play Store": "com.android.vending",
    "Google-Play-Store": "com.android.vending",
    "Play Store": "com.android.vending",
    "GoogleSlides": "com.google.android.apps.docs.editors.slides",
    "Google Slides": "com.google.android.apps.docs.editors.slides",
    "Google-Slides": "com.google.android.apps.docs.editors.slides",
    "GoogleTasks": "com.google.android.apps.tasks",
    "Google Tasks": "com.google.android.apps.tasks",
    "Google-Tasks": "com.google.android.apps.tasks",
    # International Apps - Notes & Organization
    "Joplin": "net.cozic.joplin",
    "joplin": "net.cozic.joplin",
    # International Apps - Food & Services
    "McDonald": "com.mcdonalds.app",
    "mcdonald": "com.mcdonalds.app",
    "McDonalds": "com.mcdonalds.app",
    "McDonald's": "com.mcdonalds.app",
    # International Apps - Navigation & Maps
    "Osmand": "net.osmand",
    "osmand": "net.osmand",
    "OsmAnd": "net.osmand",
    "OpenTracks": "de.dennisguse.opentracks",
    "opentracks": "de.dennisguse.opentracks",
    # International Apps - Music & Media
    "PiMusicPlayer": "com.Project100Pi.themusicplayer",
    "pimusicplayer": "com.Project100Pi.themusicplayer",
    "RetroMusic": "code.name.monkey.retromusic",
    "retromusic": "code.name.monkey.retromusic",
    "VLC": "org.videolan.vlc",
    "vlc": "org.videolan.vlc",
    # International Apps - Social & Communication
    "Quora": "com.quora.android",
    "quora": "com.quora.android",
    "Reddit": "com.reddit.frontpage",
    "reddit": "com.reddit.frontpage",
    "Telegram": "org.telegram.messenger",
    "telegram": "org.telegram.messenger",
    "Tiktok": "com.zhiliaoapp.musically",
    "tiktok": "com.zhiliaoapp.musically",
    "TikTok": "com.zhiliaoapp.musically",
    "Twitter": "com.twitter.android",
    "twitter": "com.twitter.android",
    "X": "com.twitter.android",
    "x": "com.twitter.android",
    "WeChat": "com.tencent.mm",  # English name for 微信
    "wechat": "com.tencent.mm",
    "Whatsapp": "com.whatsapp",
    "WhatsApp": "com.whatsapp",
    "whatsapp": "com.whatsapp",
    "Facebook": "com.facebook.katana",
    "facebook": "com.facebook.katana",
    "FacebookMessenger": "com.facebook.orca",
    "Facebook Messenger": "com.facebook.orca",
    "Messenger": "com.facebook.orca",
    "messenger": "com.facebook.orca",
    "Instagram": "com.instagram.android",
    "instagram": "com.instagram.android",
    # International Apps - E-commerce & Shopping
    "Amazon": "com.amazon.mShop.android.shopping",
    "amazon": "com.amazon.mShop.android.shopping",
    "Amazon Shopping": "com.amazon.mShop.android.shopping",
    "eBay": "com.ebay.mobile",
    "ebay": "com.ebay.mobile",
    "Ebay": "com.ebay.mobile",
    "temu": "com.einnovation.temu",
    "Temu": "com.einnovation.temu",
    "TEMU": "com.einnovation.temu",
    # International Apps - Utilities
    "SimpleSMSMessenger": "com.simplemobiletools.smsmessenger",
}


def get_package_name(app_name: str) -> str | None:
    """
    Get the package name for an app.

    Args:
        app_name: The display name of the app.

    Returns:
        The Android package name, or None if not found.
    """
    return APP_PACKAGES.get(app_name)


def get_app_name(package_name: str) -> str | None:
    """
    Get the app name from a package name.

    Args:
        package_name: The Android package name.

    Returns:
        The display name of the app, or None if not found.
    """
    for name, package in APP_PACKAGES.items():
        if package == package_name:
            return name
    return None


def list_supported_apps() -> list[str]:
    """
    Get a list of all supported app names.

    Returns:
        List of app names.
    """
    return list(APP_PACKAGES.keys())
