import requests
import json
import time
from urllib.parse import quote
import random

def search_aparat(query, page=1):
    """
    جستجو در آپارات با API رسمی و برگرداندن نتایج
    """
    encoded_query = quote(query)
    # URL دقیق API جستجوی آپارات
    url = f"https://www.aparat.com/etc/api/videoBySearch/text/{encoded_query}/page/{page}"
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            # کلید پاسخ API، 'videoBySearch' است
            videos = data.get('videoBySearch', [])
            return videos
        else:
            print(f"  ⚠️ خطا در دریافت: وضعیت {response.status_code}")
            return []
    except Exception as e:
        print(f"  ⚠️ خطا در اتصال: {str(e)[:50]}")
        return []

def collect_real_animations():
    """
    جمع‌آوری انیمیشن‌ها با کلمات کلیدی مختلف
    """
    all_videos = []
    seen_urls = set()
    
    # کلمات کلیدی هدفمند برای پیدا کردن انیمیشن‌های متنوع
    search_queries = [
        "انیمیشن سینمایی", "کارتون", "پویانمایی",
        "انیمیشن جدید", "انیمیشن دوبله فارسی",
        "انیمیشن خارجی", "انیمیشن ایرانی",
        "سریال انیمیشنی", "انیمیشن کودکانه"
    ]
    
    print("="*60)
    print("🎬 شروع جمع‌آوری لینک‌های واقعی انیمیشن از آپارات")
    print("="*60)
    
    for query in search_queries:
        print(f"\n🔍 جستجو برای: {query}")
        page = 1
        # برای هر کلمه کلیدی، ۳ صفحه اول را بررسی کن
        while page <= 3:
            print(f"   📄 صفحه {page}...", end=" ")
            videos = search_aparat(query, page)
            
            if not videos:
                print("❌ خالی یا خطا")
                break
                
            print(f"✅ {len(videos)} ویدیو")
            
            for video in videos:
                # استخراج اطلاعات از پاسخ API
                title = video.get('title', 'بدون عنوان').strip()
                video_id = video.get('uid', '')
                
                if not video_id:
                    continue
                
                # ساخت لینک صحیح آپارات
                url = f"https://www.aparat.com/v/{video_id}"
                
                # جلوگیری از تکراری شدن لینک‌ها
                if url in seen_urls:
                    continue
                seen_urls.add(url)
                
                # گرفتن توضیحات (اگر موجود باشد)
                description = video.get('description', '')
                if not description or len(description) < 5:
                    description = f"انیمیشن {title[:30]}"
                
                all_videos.append({
                    "title": title,
                    "url": url,
                    "description": description[:100]  # خلاصه کردن توضیحات
                })
            
            page += 1
            # تاخیر بین درخواست‌ها برای جلوگیری از مسدود شدن
            time.sleep(1 + random.random())
    
    print("\n" + "="*60)
    print(f"✅ جمع‌آوری شد: {len(all_videos)} انیمیشن با لینک‌های واقعی")
    return all_videos

def save_to_json(animations, filename='animations.json'):
    """
    ذخیره لیست در فایل JSON
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(animations, f, ensure_ascii=False, indent=2)
    print(f"💾 لیست در فایل '{filename}' ذخیره شد.")

if __name__ == '__main__':
    # اجرای جمع‌آوری
    real_animations = collect_real_animations()
    
    if real_animations:
        save_to_json(real_animations)
        print("\n🎉 کار تمام است! حالا می‌توانید سایت را اجرا کنید.")
    else:
        print("\n❌ هیچ انیمیشنی جمع‌آوری نشد. ممکن است به اینترنت یا VPN نیاز باشد.")