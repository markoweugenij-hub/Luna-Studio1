import streamlit as st
import sqlite3
import os
from datetime import datetime

# --- 1. НАЛАШТУВАННЯ СТОРІНКИ ТА БАЗИ ДАНИХ ---
st.set_page_config(page_title="Luna Studio | Манікюр", page_icon="💅", layout="centered")

# Створення бази даних для заявок, відгуків та фотографій
conn = sqlite3.connect("luna_studio_db.sqlite", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments 
    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, service TEXT, date TEXT, time TEXT, status TEXT DEFAULT 'Нова')
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback 
    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, text TEXT, rating INTEGER, date TEXT)
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings 
    (key TEXT PRIMARY KEY, value TEXT)
""")
conn.commit()

# Пароль для доступу до адмінки (передайте його тому, хто керуватиме сайтом)
ADMIN_PASSWORD = "LunaAdmin2026"

# Директорія для збереження завантажених фотографій
UPLOAD_DIR = "uploaded_works"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# --- 2. ЕСТЕТИЧНИЙ АДАПТИВНИЙ ДИЗАЙН (РОЖЕВИЙ) ---
pink_style = """
    <style>
    .stApp { background-color: #FFF5F7; }
    h1, h2, h3 { color: #D14D72; font-family: 'Arial', sans-serif; text-align: center; }
    p, span, label { color: #4A3036 !important; }
    .service-card {
        background-color: #FFFFFF; padding: 20px; border-radius: 16px;
        margin-bottom: 15px; border: 1px solid #FFDEE5;
        box-shadow: 0 4px 12px rgba(209, 77, 114, 0.06);
    }
    .stButton>button {
        background-color: #FF8E9E; color: white !important;
        border-radius: 25px; border: none; padding: 12px 30px;
        font-weight: bold; width: 100%; box-shadow: 0 4px 10px rgba(255, 142, 158, 0.4);
    }
    .stButton>button:hover { background-color: #D14D72; }
    .feedback-box {
        background-color: #FFFFFF; padding: 15px; border-radius: 12px;
        border-left: 5px solid #FF8E9E; margin-bottom: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }
    </style>
"""
st.markdown(pink_style, unsafe_allow_html=True)

# --- 3. НАВІГАЦІЯ (Вгорі екрану) ---
page = st.selectbox("Перейти до розділу:", ["Головна сторінка", "Прайс та Запис", "Відгуки клієнтів", "👑 Панель Адміністратора"])

st.write("---")

# ==========================================
# РОЗДІЛ 1: ГОЛОВНА СТОРІНКА
# ==========================================
if page == "Головна сторінка":
    st.markdown("<h1>Luna Studio</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #885A65;'>Простір твого бездоганного стилю ✨</p>", unsafe_allow_html=True)
    
    st.markdown("### Наші роботи")
    st.write("Фото оновлюються адміністратором у реальному часі:")
    
    # Виведення фотографій, які завантажив адмін
    cols = st.columns(3)
    for i in range(1, 4):
        img_path = os.path.join(UPLOAD_DIR, f"work_{i}.jpg")
        with cols[i-1]:
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True, caption=f"Робота №{i}")
            else:
                st.image("https://placeholder.com", use_container_width=True, caption="Місце для фото")

    st.markdown("""
    <div style='text-align: center; margin-top: 30px;'>
        <p>📍 <b>Адреса:</b> м. Київ, вул. Центральна, 12</p>
        <p>📞 <b>Телефон:</b> +380 (93) 123-45-67</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# РОЗДІЛ 2: ПРАЙС ТА ОНЛАЙН-ЗАПИС
# ==========================================
elif page == "Прайс та Запис":
    st.markdown("<h2>Послуги та онлайн-запис</h2>")
    
    services = [
        {"title": "🌸 Комбінований манікюр", "desc": "Гігієнічна чистка, форма, догляд за кутикулою.", "price": "350 грн"},
        {"title": "✨ Манікюр + Покриття", "desc": "Вирівнювання пластини, однотонне покриття гель-лаком.", "price": "550 грн"},
        {"title": "💅 Нарощування нігтів", "desc": "Моделювання нігтів гелем + легкий дизайн.", "price": "від 750 грн"}
    ]
    
    for s in services:
        st.markdown(f"""
        <div class="service-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <strong style="color: #D14D72; font-size: 1.1rem;">{s['title']}</strong>
                <span style="background: #FFDEE5; padding: 4px 10px; border-radius: 12px; font-weight: bold; color: #D14D72;">{s['price']}</span>
            </div>
            <p style="margin-top: 8px; margin-bottom: 0; font-size: 0.9rem; color: #666;">{s['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("---")
    st.markdown("### Записатися на візит")
    
    with st.form("appointment_form", clear_on_submit=True):
        name = st.text_input("Ваше ім'я:")
        phone = st.text_input("Номер телефону для зв'язку (Viber/Telegram):")
        chosen_service = st.selectbox("Оберіть послугу:", [s["title"] for s in services])
        
        c1, c2 = st.columns(2)
        with c1:
            date = st.date_input("Дата візиту:")
        with c2:
            time = st.time_input("Бажаний час:")
            
        submit = st.form_submit_button("Підтвердити запис 💖")
        
        if submit:
            if name and phone:
                cursor.execute(
                    "INSERT INTO appointments (name, phone, service, date, time) VALUES (?, ?, ?, ?, ?)",
                    (name, phone, chosen_service, str(date), str(time))
                )
                conn.commit()
                st.balloons()
                st.success(f"✨ Дякуємо, {name}! Заявку надіслано. Майстер зв'яжеться з вами найближчим часом.")
            else:
                st.error("Будь ласка, заповніть поля Ім'я та Телефон!")

# ==========================================
# РОЗДІЛ 3: ЗВОРОТНІЙ ЗВ'ЯЗОК (ВІДГУКИ)
# ==========================================
elif page == "Відгуки клієнтів":
    st.markdown("<h2>Зворотній зв'язок</h2>")
    
    # Спеціальна кнопка-експандер для написання відгуку
    with st.expander("✍️ Залишити свій відгук студії"):
        with st.form("feedback_form", clear_on_submit=True):
            f_name = st.text_input("Ваше ім'я:")
            f_text = st.text_area("Ваші враження від візиту (що сподобалось?):")
            f_rating = st.slider("Ваша оцінка майстру:", 1, 5, 5)
            f_submit = st.form_submit_button("Опублікувати відгук ⭐")
            
            if f_submit:
                if f_name and f_text:
                    today = datetime.today().strftime('%d.%m.%Y')
                    cursor.execute("INSERT INTO feedback (name, text, rating, date) VALUES (?, ?, ?, ?)", (f_name, f_text, f_rating, today))
                    conn.commit()
                    st.success("Дякуємо! Ваш відгук успішно додано нижче.")
                else:
                    st.error("Будь ласка, вкажіть ваше ім'я та заповніть текст відгуку.")
