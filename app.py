import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Luna Studio | Манікюр", page_icon="💅", layout="centered")

# Пам'ять для збереження заявок та відгуків (тепер список відгуків спочатку повністю порожній)
if "appointments" not in st.session_state:
    st.session_state.appointments = []
if "feedbacks" not in st.session_state:
    st.session_state.feedbacks = []

ADMIN_PASSWORD = "LunaAdmin2026"

# Акуратний рожевий дизайн
st.markdown("""
    <style>
    .stApp { background-color: #FFF5F7; }
    h1, h2, h3 { color: #D14D72; font-family: 'Arial', sans-serif; text-align: center; }
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
    }
    </style>
""", unsafe_allow_html=True)

page = st.selectbox("Перейти до розділу:", ["Головна сторінка", "Прайс та Запис", "Відгуки клієнтів", "👑 Панель Адміністратора"])
st.write("---")

# --- 1. ГОЛОВНА СТОРІНКА ---
if page == "Головна сторінка":
    st.markdown("<h1>Luna Studio</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #885A65;'>Простір твого бездоганного стилю ✨</p>", unsafe_allow_html=True)
    
    st.markdown("### Наші роботи")
    cols = st.columns(3)
    with cols[0]:
        st.image("photo1.jpg", caption="Galaxy Pink")
    with cols[1]:
        st.image("photo2.jpg", caption="Love & Stars")
    with cols[2]:
        st.image("photo3.jpg", caption="Elegant French")

    st.markdown("<div style='text-align: center; margin-top: 30px;'><p>📍 <b>Адреса:</b> м. Київ, вул. Центральна, 12</p><p>📞 <b>Телефон:</b> +380 (93) 123-45-67</p></div>", unsafe_allow_html=True)

# --- 2. ПРАЙС ТА ЗАПИС ---
elif page == "Прайс та Запис":
    st.markdown("<h2>Послуги та онлайн-запис</h2>")
    services = [
        {"title": "🌸 Комбінований манікюр", "desc": "Гігієнічна чистка, форма, догляд за кутикулою.", "price": "350 грн"},
        {"title": "✨ Манікюр + Покриття", "desc": "Вирівнювання пластини, покриття гель-лаком.", "price": "550 грн"},
        {"title": "💅 Нарощування нігтів", "desc": "Моделювання нігтів гелем + легкий дизайн.", "price": "від 750 грн"}
    ]
    
    for s in services:
        st.markdown(f'<div class="service-card"><strong style="color: #D14D72;">{s["title"]}</strong> — <b>{s["price"]}</b><p style="font-size:0.9rem; color:#666;">{s["desc"]}</p></div>', unsafe_allow_html=True)
        
    st.write("---")
    with st.form("appointment_form", clear_on_submit=True):
        name = st.text_input("Ваше ім'я:")
        phone = st.text_input("Номер телефону:")
        chosen_service = st.selectbox("Оберіть послугу:", [s["title"] for s in services])
        date = st.date_input("Дата:")
        time = st.time_input("Час:")
        
        if st.form_submit_button("Підтвердити запис 💖"):
            if name and phone:
                st.session_state.appointments.append({
                    "name": name, "phone": phone, "service": chosen_service, "date": str(date), "time": str(time)
                })
                st.balloons()
                st.success("✨ Заявку надіслано майстру! Перевірте її в адмінці.")
            else:
                st.error("Будь ласка, заповніть ім'я та номер телефону!")

# --- 3. ВІДГУКИ КЛІЄНТІВ ---
elif page == "Відгуки клієнтів":
    st.markdown("<h2>Зворотній зв'язок</h2>")
    
    with st.expander("✍️ Залишити свій відгук студії"):
        with st.form("feedback_form", clear_on_submit=True):
            f_name = st.text_input("Ваше ім'я:")
            f_text = st.text_area("Ваші враження:")
            f_rating = st.slider("Оцінка:", 1, 5, 5)
            if st.form_submit_button("Опублікувати ⭐"):
                if f_name and f_text:
                    st.session_state.feedbacks.insert(0, {
                        "name": f_name, "text": f_text, "rating": f_rating, "date": datetime.today().strftime('%d.%m.%Y')
                    })
                    st.success("Відгук додано!")
                    st.rerun()

    st.write("---")
    
    # Якщо відгуків немає — виводимо чесний напис
    if not st.session_state.feedbacks:
        st.info("Відгуків ще немає. Будьте першою, хто залишить відгук!")
    else:
        for fb in st.session_state.feedbacks:
            st.markdown(f'<div class="feedback-box"><b>{fb["name"]}</b> ({fb["date"]})<br>{"⭐"*fb["rating"]}<p>{fb["text"]}</p></div>', unsafe_allow_html=True)

# --- 4. ПАНЕЛЬ АДМІНІСТРАТОРА ---
elif page == "👑 Панель Адміністратора":
    st.markdown("<h2>Вхід для керівника</h2>")
    password_input = st.text_input("Введіть секретний пароль:", type="password")
    
    if password_input == ADMIN_PASSWORD:
        st.success("Доступ дозволено!")
        
        st.markdown("### 📥 Нові заявки від клієнтів")
        if st.session_state.appointments:
            for idx, ap in enumerate(st.session_state.appointments):
                with st.expander(f"📋 Заявка від {ap['name']} (Послуга: {ap['service']})"):
                    st.write(f"📞 **Telephone:** {ap['phone']}")
                    st.write(f"📅 **When:** {ap['date']} at {ap['time']}")
                    if st.button("Видалити заявку", key=f"del_{idx}"):
                        st.session_state.appointments.pop(idx)
                        st.rerun()
        else:
            st.info("Нових заявок наразі немає.")
    elif password_input != "":
        st.error("Невірний пароль!")
