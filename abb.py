from flask import Flask, render_template_string

app = Flask(__name__)

# كود التصميم (HTML) مدمج لتسهيل التشغيل في ملف واحد حالياً
html_content = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>موقعي الشخصي كمطور بايثون</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            text-align: center;
            max-width: 500px;
            width: 100%;
        }
        h1 {
            color: #4a90e2;
            margin-bottom: 10px;
        }
        .badge {
            background-color: #3776ab;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            display: inline-block;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.1em;
            line-height: 1.6;
            color: #666;
        }
        .btn {
            background-color: #4a90e2;
            color: white;
            padding: 10px 25px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            text-decoration: none;
            display: inline-block;
            margin-top: 15px;
            transition: 0.3s;
        }
        .btn:hover {
            background-color: #357abd;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>مرحباً بك في موقع مهند! 👋</h1>
        <div class="badge">مطور بايثون مستقبلي</div>
        <p>لقد قمت ببناء هذا الموقع بنجاح باستخدام لغة <strong>بايثون</strong> وإطار عمل <strong>Flask</strong>.</p>
        <p>هذه هي الخطوة الأولى في رحلتي البرمجية لإنشاء مواقع وتطبيقات ويب ذكية.</p>
        <a href="#" class="btn" onclick="alert('أحسنت! الكود يعمل والتفاعل ناجح 🚀')">اضغط للتفاعل</a>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    # تمرير التصميم ليعرضه المتصفح
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
