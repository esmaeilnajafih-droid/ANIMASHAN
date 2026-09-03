from flask import Flask, render_template, request

app = Flask(__name__)

# لیست ۱۶ انیمیشن از فایل PDF
animations = [
    {
        "title": "شکارچیان شیطان کی پاپ (دوبله فارسی)",
        "url": "https://www.aparat.com/v/isc04sq",
        "description": "انیمیشن دوبله فارسی با ۳۱۲,۹۲۷ بازدید"
    },
    {
        "title": "بچهمرشد ۲ (ماجراهای نوید)",
        "url": "https://www.aparat.com/v/dhh5g3x",
        "description": "پویانمایی ایرانی جدید با ۱۹۸,۲۱۷ بازدید"
    },
    {
        "title": "گروه شب نقاب",
        "url": "https://www.aparat.com/v/kjmgeh5",
        "description": "انیمیشن با ۱۳۱,۱۸۷ بازدید"
    },
    {
        "title": "کارتون موزیکال ماشین ها",
        "url": "https://www.aparat.com/v/vlrw569",
        "description": "کارتون موزیکال با ۱۰۱,۲۰۸ بازدید"
    },
    {
        "title": "انیمیشن جدید دوست (دوبله فارسی ۲۰۲۵)",
        "url": "https://www.aparat.com/v/gvzgs3s",
        "description": "انیمیشن دوبله فارسی با ۸۷,۲۹۰ بازدید"
    },
    {
        "title": "لوراکس (دوبله فارسی)",
        "url": "https://www.aparat.com/v/o5713f0",
        "description": "انیمیشن سینمایی محبوب"
    },
    {
        "title": "شرک ۱ (دوبله فارسی)",
        "url": "https://www.aparat.com/v/kud96x1",
        "description": "انیمیشن سینمایی محبوب با ۸۵,۷۲۶ بازدید"
    },
    {
        "title": "توییت ها (دوبله فارسی ۲۰۲۶)",
        "url": "https://www.aparat.com/v/hnhbspi",
        "description": "انیمیشن کمدی با ۱۵,۵۲۵ بازدید"
    },
    {
        "title": "دهکده حیوانات (کارتون دهه شصت)",
        "url": "https://www.aparat.com/v/oR357",
        "description": "کارتون قدیمی با ۱۳,۹۰۹ بازدید"
    },
    {
        "title": "انیمیشن شیر",
        "url": "https://www.aparat.com/v/y58oi63",
        "description": "انیمیشن با ۹,۲۵۳ بازدید"
    },
    {
        "title": "ضرب اعداد اعشاری (انیمیشن آموزشی)",
        "url": "https://www.aparat.com/v/8IAZP",
        "description": "آموزشی ریاضی با ۶,۹۰۷ بازدید"
    },
    {
        "title": "کارتون موش کوهستان",
        "url": "https://www.aparat.com/v/s638w9i",
        "description": "کارتون دهه شصتی با ۳,۳۱۲ بازدید"
    },
    {
        "title": "آناستازیا (دوبله فارسی)",
        "url": "https://www.aparat.com/v/x629mjq",
        "description": "انیمیشن سینمایی کلاسیک"
    },
    {
        "title": "پینوکیو (دوبله فارسی)",
        "url": "https://www.aparat.com/v/a62gl9p",
        "description": "انیمیشن کلاسیک ۱۹۴۰"
    },
    {
        "title": "افسانه جومونگ (سریال) - قسمت ۶",
        "url": "https://www.aparat.com/v/q322453",
        "description": "سریال انیمیشنی دوبله فارسی با ۳۱۷,۲۸۵ بازدید"
    },
    {
        "title": "تام سخنگو",
        "url": "https://www.aparat.com/v/mnn72k1",
        "description": "کارتون گربه سخنگو با ۲۹,۲۴۹ بازدید"
    }
]

@app.route('/')
def index():
    search_query = request.args.get('search', '').strip()
    
    if search_query:
        filtered = [
            anim for anim in animations 
            if search_query.lower() in anim['title'].lower() 
            or search_query.lower() in anim['description'].lower()
        ]
    else:
        filtered = animations
    
    return render_template('index.html', 
                         animations=filtered,
                         total_count=len(animations),
                         result_count=len(filtered),
                         search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)