import streamlit as st
import datetime

# 1. НАЛАШТУВАННЯ СТОРІНКИ
st.set_page_config(
    page_title="Luna Studio | Nail Esthetic", 
    page_icon="🌙", 
    layout="centered"
)

# Ініціалізація стану кнопок (щоб сайт пам'ятав, яку вкладку відкрито)
if 'menu_selection' not in st.session_state:
    st.session_state.menu_selection = "main"

# 2. СТИЛІЗАЦІЯ (CSS) ДЛЯ СТВОРЕННЯ РОЖЕВОЇ ЕСТЕТИКИ LUNA STUDIO
pink_design = """
<style>
    /* Головний фон сайту — ніжний пастельно-рожевий */
    .stApp {
        background-color: #FFF5F7;
    }
    
    /* Головний логотип Luna Studio */
    .logo-title {
        color: #C71585;
        font-family: 'Playfair Display', 'Georgia', serif;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
        letter-spacing: 2px;
    }
    
    /* Заголовки блоків */
    h2, h3 {
        color: #D2143A;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }
    
    /* Текст підзаголовка */
    .subtitle {
        text-align: center;
        color: #C71585;
        font-size: 16px;
        font-style: italic;
        margin-bottom: 35px;
        letter-spacing: 1px;
    }

    /* Контейнер для фото — біла картка, яка НЕ зливається з фоном */
    .photo-container {
        background-color: #FFFFFF;
        padding: 12px;
        border-radius: 18px;
        box-shadow: 0 6px 20px rgba(219, 112, 147, 0.12);
        text-align: center;
        margin-bottom: 25px;
        border: 2px solid #FFB6C1;
        position: relative;
    }
    
    /* Ефект магічних зірочок навколо рамки фото */
    .photo-container::before {
        content: "✨ 🌙 ✨";
        position: absolute;
        top: -14px;
        left: 50%;
        transform: translateX(-50%);
        background: #FFF5F7;
        padding: 0 10px;
        color: #FF69B4;
        font-size: 13px;
    }
    
    /* Стиль для великих рожевих кнопок */
    .stButton > button {
        width: 100%;
        background-color: #FF69B4;
        color: white !important;
        border-radius: 25px;
        border: 2px solid #FFB6C1;
        padding: 12px 20px;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(255, 105, 180, 0.2);
    }
    
    /* Ефект при наведенні мишки на кнопку */
    .stButton > button:hover {
        background-color: #C71585;
        border-color: #C71585;
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(199, 21, 133, 0.3);
    }
    
    /* Інформаційні картки для списків */
    .info-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #FF69B4;
        margin-bottom: 15px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
    }
</style>
"""
st.markdown(pink_design, unsafe_allow_html=True)

# 3. ШАПКА САЙТУ З НОВИМ ЛОГОТИПОМ
st.markdown("<div class='logo-title'>LUNA STUDIO</div>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>🌙 Твій магічний простір ідеального манікюру ✨</p>", unsafe_allow_html=True)

# 4. БЛОК ФОТОГРАФІЙ (ГАЛЕРЕЯ РОБІТ)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="photo-container">', unsafe_allow_html=True)
    st.image("photo1.jpg", use_container_width=True)
    st.markdown("<small style='color:#C71585; font-weight:bold;'>Елегантний Нюд</small>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="photo-container">', unsafe_allow_html=True)
    st.image("photo2.jpg", use_container_width=True)
    st.markdown("<small style='color:#C71585; font-weight:bold;'>Ідеальний Френч</small>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="photo-container">', unsafe_allow_html=True)
    st.image("photo3.jpg", use_container_width=True)
    st.markdown("<small style='color:#C71585; font-weight:bold;'>Сяючі Тренди</small>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---") 

# 5. БЛОК ТРЬОХ ГОЛОВНИХ КНОПОК
btn_col1, btn_col2, btn_col3 = st.columns(3)

with btn_col1:
    if st.button("📅 Запис на манікюр"):
        st.session_state.menu_selection = "zapis"

with btn_col2:
    if st.button("✨ Каталог ідей"):
        st.session_state.menu_selection = "catalog"

with btn_col3:
    if st.button("🛡️ Гарантія безпеки"):
        st.session_state.menu_selection = "safety"

st.write("") 

# 6. ЛОГІКА КНОПОК

# --- КНОПКА 1: ЗАПИС НА МАНІКЮР ---
if st.session_state.menu_selection == "zapis":
    st.markdown("### 📝 Онлайн-запис в Luna Studio")
    with st.form("booking_form"):
        client_name = st.text_input("Ваше ім'я:")
        client_phone = st.text_input("Номер телефону (Viber/Telegram):")
        chosen_service = st.selectbox("Оберіть послугу:", ["Манікюр з покриттям", "Укріплення та дизайн", "Нарощування нігтів", "Педикюр"])
        chosen_date = st.date_input("Оберіть зручний день:", min_value=datetime.date.today())
        
        submit_btn = st.form_submit_button("Надіслати заявку")
        if submit_btn:
            if client_name and client_phone:
                st.success(f"🌙 Дякуємо, {client_name}! Заявку прийнято на {chosen_date.strftime('%d.%m.%Y')}. Студія Luna зв'яжеться з вами найближчим часом!")
            else:
                st.error("Будь ласка, вкажіть ваше ім'я та телефон для зв'язку.")

# --- КНОПКА 2: КАТАЛОГ ДИЗАЙН-ІДЕЙ ---
elif st.session_state.menu_selection == "catalog":
    st.markdown("### ✨ Топ-дизайни від Luna Studio")
    st.markdown('<div class="info-card"><b>⭐ Місячний манікюр:</b> Наш фірмовий дизайн із витонченими блискітками біля основи нігтя.</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card"><b>💎 Глазуровані нігті:</b> Трендова втирка, що створює ефект дорогого перлинного сяйва.</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card"><b>🎨 Акварельні мазки:</b> Абстрактні ніжні розмиви у рожевих та пастельних тонах.</div>', unsafe_allow_html=True)

# --- КНОПКА 3: ГАРАНТІЯ БЕЗПЕКИ ---
elif st.session_state.menu_selection == "safety":
    st.markdown("### 🛡️ Твоя безпека в Luna Studio")
    st.write("Ми дбаємо про твою красу та здоров'я, тому використовуємо виключно стерильний інструмент:")
    st.markdown('<div class="info-card"><b>🧼 1. Дезінфекція:</b> Замочування інструментів у розчині преміум-класу одразу після клієнта.</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card"><b>💧 2. Очищення:</b> Ретельне промивання та сушка перед термічною обробкою.</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card"><b>🔥 3. Стерилізація:</b> Випікання в сертифікованому сухожарі. Крафт-пакет відкриваємо тільки при тобі!</div>', unsafe_allow_html=True)

# 7. ПІДВАЛ (ФУТЕР) САЙТУ
st.markdown("💅 Luna Studio 2026")