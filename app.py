
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

admins = {"admin123": True}
users = {"user123": False}

courses = [
    {"title": "دورة أساسيات الأمن السيبراني", "description": "تعلم أساسيات الحماية وتأمين الأنظمة."},
    {"title": "اختبار الاختراق", "description": "دورة متقدمة في اختبار الاختراق."},
    {"title": "تشفير البيانات", "description": "مبادئ وتقنيات التشفير."}
]

@app.route('/', methods=['GET', 'POST'])
def home():
    error = ""
    if request.method == "POST":
        code = request.form.get("code")
        if code in admins:
            return redirect(url_for("admin_panel"))
        elif code in users:
            return redirect(url_for("user_panel"))
        else:
            error = "كود خاطئ، حاول مرة أخرى."
    return render_template_string("""
        <h2>تسجيل الدخول</h2>
        <form method="post">
            <input name="code" placeholder="أدخل كود الدخول" required>
            <button type="submit">دخول</button>
        </form>
        <p style="color:red;">{{error}}</p>
    """, error=error)

@app.route('/admin')
def admin_panel():
    return render_template_string("""
        <h2>لوحة تحكم الأدمن</h2>
        <ul>
            <li><a href="{{url_for('manage_courses')}}">إدارة الكورسات</a></li>
            <li><a href="{{url_for('manage_pages')}}">إدارة صفحات الويب</a></li>
            <li><a href="{{url_for('manage_settings')}}">الإعدادات</a></li>
        </ul>
        <a href="{{url_for('home')}}">تسجيل خروج</a>
    """)

@app.route('/admin/courses')
def manage_courses():
    return render_template_string("""
        <h2>إدارة الكورسات</h2>
        <ul>
        {% for course in courses %}
            <li><strong>{{course.title}}</strong>: {{course.description}}</li>
        {% endfor %}
        </ul>
        <a href="{{url_for('admin_panel')}}">رجوع</a>
    """, courses=courses)

@app.route('/admin/pages')
def manage_pages():
    return render_template_string("""
        <h2>إدارة صفحات الويب</h2>
        <p>هنا تقدر تضيف أو تعدل صفحات موقعك.</p>
        <a href="{{url_for('admin_panel')}}">رجوع</a>
    """)

@app.route('/admin/settings')
def manage_settings():
    return render_template_string("""
        <h2>الإعدادات</h2>
        <p>ضبط إعدادات الموقع هنا.</p>
        <a href="{{url_for('admin_panel')}}">رجوع</a>
    """)

@app.route('/user')
def user_panel():
    return render_template_string("""
        <h2>مرحبا بك في الموقع</h2>
        <h3>الكورسات المتاحة:</h3>
        <ul>
        {% for course in courses %}
            <li><strong>{{course.title}}</strong>: {{course.description}}</li>
        {% endfor %}
        </ul>
        <a href="{{url_for('home')}}">تسجيل خروج</a>
    """, courses=courses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
