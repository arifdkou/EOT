import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow

st.set_page_config(page_title="Arduino Elektro-Optik Deneyleri", layout="wide")

# ============================================================
# Yardımcı: Basit düzenek çizim fonksiyonları
# ============================================================

def draw_setup_1():
    """Deney 1: Lazer modülasyonu + fotodiyot düzenek çizimi"""
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")

    # Arduino
    ard = Rectangle((0.2, 0.5), 2, 1.5, fill=False)
    ax.add_patch(ard)
    ax.text(1.2, 1.25, "Arduino", ha="center", va="center")

    # Transistor kutusu
    tr = Rectangle((3, 0.8), 1, 1, fill=False)
    ax.add_patch(tr)
    ax.text(3.5, 1.3, "Transistor", ha="center", va="center", fontsize=8)

    # Lazer diyot
    laser = Rectangle((5, 1.0), 1.2, 0.8, fill=False)
    ax.add_patch(laser)
    ax.text(5.6, 1.4, "Lazer\nDiyot", ha="center", va="center", fontsize=8)

    # Fotodiyot
    pd = Rectangle((8, 1.0), 1.2, 0.8, fill=False)
    ax.add_patch(pd)
    ax.text(8.6, 1.4, "Fotodiyot", ha="center", va="center", fontsize=8)

    # Bağlantı okları
    ax.add_patch(FancyArrow(2.2, 1.25, 0.7, 0, width=0.05, length_includes_head=True))
    ax.add_patch(FancyArrow(4.0, 1.25, 0.8, 0, width=0.05, length_includes_head=True))
    ax.add_patch(FancyArrow(6.2, 1.4, 1.6, 0, width=0.02, length_includes_head=True))
    ax.text(7.0, 1.6, "Işık", ha="center", fontsize=8)

    return fig


def draw_setup_2():
    """Deney 2: Triangulation mesafe ölçümü düzenek çizimi"""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    # Lazer
    laser = Rectangle((1, 2.2), 1.2, 0.8, fill=False)
    ax.add_patch(laser)
    ax.text(1.6, 2.6, "Lazer", ha="center", va="center", fontsize=8)

    # Nesne
    obj = Rectangle((4, 1.5), 0.6, 2, fill=False)
    ax.add_patch(obj)
    ax.text(4.3, 2.6, "Nesne", ha="center", va="center", fontsize=8)

    # Sensör (line sensör)
    sens = Rectangle((7, 1.5), 1.5, 0.4, fill=False)
    ax.add_patch(sens)
    ax.text(7.75, 1.9, "Sensör\n(dizi)", ha="center", va="bottom", fontsize=8)

    # Lazer ışını
    ax.add_patch(FancyArrow(2.2, 2.6, 1.7, 0.3, width=0.02, length_includes_head=True))
    ax.add_patch(FancyArrow(4.6, 2.2, 2.2, -0.5, width=0.02, length_includes_head=True))
    ax.text(3.5, 3.1, "yansıma", fontsize=8)

    return fig


def draw_setup_3():
    """Deney 3: Optik yoğunluk ölçümü düzenek çizimi"""
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3)
    ax.axis("off")

    # Lazer
    laser = Rectangle((0.5, 1.0), 1.2, 0.8, fill=False)
    ax.add_patch(laser)
    ax.text(1.1, 1.4, "Lazer", ha="center", va="center", fontsize=8)

    # Numune
    sample = Rectangle((4, 0.8), 1.2, 1.2, fill=False)
    ax.add_patch(sample)
    ax.text(4.6, 1.4, "Numune", ha="center", va="center", fontsize=8)

    # Fotodiyot
    pd = Rectangle((8, 1.0), 1.2, 0.8, fill=False)
    ax.add_patch(pd)
    ax.text(8.6, 1.4, "Fotodiyot", ha="center", va="center", fontsize=8)

    # Işık okları
    ax.add_patch(FancyArrow(1.7, 1.4, 2.0, 0, width=0.03, length_includes_head=True))
    ax.add_patch(FancyArrow(5.2, 1.4, 2.4, 0, width=0.03, length_includes_head=True))

    ax.text(3, 1.7, "I0", fontsize=8)
    ax.text(7, 1.7, "I", fontsize=8)

    return fig


def draw_setup_4():
    """Deney 4: Optik kapı hız ölçümü düzenek çizimi"""
    fig, ax = plt.subplots(figsize=(6, 2.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    # Lazer verici
    laser = Rectangle((1, 1.5), 1.2, 0.8, fill=False)
    ax.add_patch(laser)
    ax.text(1.6, 1.9, "Lazer", ha="center", va="center", fontsize=8)

    # Fotodiyot alıcı
    pd = Rectangle((8, 1.5), 1.2, 0.8, fill=False)
    ax.add_patch(pd)
    ax.text(8.6, 1.9, "Fotodiyot", ha="center", va="center", fontsize=8)

    # Nesne
    obj = Rectangle((4.5, 1.2), 1, 1.4, fill=False)
    ax.add_patch(obj)
    ax.text(5, 2.6, "Geçen\nnesne", ha="center", va="center", fontsize=8)

    # Işık yolu
    ax.add_patch(FancyArrow(2.2, 1.9, 2.0, 0, width=0.02, length_includes_head=True))
    ax.add_patch(FancyArrow(6.0, 1.9, 1.9, 0, width=0.02, length_includes_head=True))
    ax.text(4, 2.2, "Işık bariyeri", ha="center", fontsize=8)

    return fig


def draw_setup_5():
    """Deney 5: RGB sensör + lazerler düzenek çizimi"""
    fig, ax = plt.subplots(figsize=(6, 2.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)
    ax.axis("off")

    # Farklı lazerler
    l1 = Rectangle((1, 2.4), 1.1, 0.6, fill=False)
    l2 = Rectangle((1, 1.3), 1.1, 0.6, fill=False)
    l3 = Rectangle((1, 0.2), 1.1, 0.6, fill=False)
    ax.add_patch(l1)
    ax.add_patch(l2)
    ax.add_patch(l3)
    ax.text(1.55, 2.7, "Kırmızı", ha="center", fontsize=7)
    ax.text(1.55, 1.6, "Yeşil", ha="center", fontsize=7)
    ax.text(1.55, 0.5, "Mavi/Mor", ha="center", fontsize=7)

    # RGB Sensör
    sensor = Rectangle((8, 1.3), 1.6, 1.0, fill=False)
    ax.add_patch(sensor)
    ax.text(8.8, 1.8, "RGB\nSensör", ha="center", va="center", fontsize=8)

    # Işık okları
    ax.add_patch(FancyArrow(2.1, 2.7, 5.4, -0.5, width=0.02, length_includes_head=True))
    ax.add_patch(FancyArrow(2.1, 1.6, 5.4, 0.0, width=0.02, length_includes_head=True))
    ax.add_patch(FancyArrow(2.1, 0.5, 5.4, 0.8, width=0.02, length_includes_head=True))

    return fig

# ============================================================
# Deney 1: Lazer modülasyonu ve fotodiyot
# ============================================================

def experiment_1():
    st.header("Deney 1 – Lazer Modülasyonu ve Fotodiyot ile Sinyal Tespiti")

    st.markdown(
        "Bu deneyde Arduino ile lazer diyot kare dalga modülasyonu yapılır ve fotodiyot ile bu modülasyon algılanır. "
        "Band genişliği, transimpedans yükselteç ve RC filtre etkisi gözlemlenir."
    )

    st.subheader("Düzenek Şeması")
    fig = draw_setup_1()
    st.pyplot(fig)

    st.subheader("Temel Denklemler")

    st.latex(r"""
    I_{\text{laser}} = \frac{V_s - V_{\text{laser}}}{R_{\text{limit}}}
    """)
    st.latex(r"""
    I_{\text{pd}} = R_{\lambda} \, P_{\text{opt}}
    """)
    st.latex(r"""
    V_{\text{out}} = - I_{\text{pd}} \, R_f
    """)
    st.latex(r"""
    f_{\text{cutoff}} = \frac{1}{2\pi R_f C_d}
    """)

    st.subheader("Simülasyon: Lazer Darbesi → Fotodiyot Çıkışı")

    col1, col2 = st.columns(2)
    with col1:
        freq = st.slider("Lazer Darbe Frekansı (Hz)", 1, 5000, 500, key="exp1_freq")
        duty = st.slider("Görev Oranı (%)", 1, 99, 50, key="exp1_duty")
        power_mw = st.slider("Optik Güç (mW)", 1, 50, 10, key="exp1_power")
    with col2:
        responsivity = st.slider("Responsivity (A/W)", 0.1, 1.0, 0.5, key="exp1_resp")
        Rf_k = st.slider("Rf (kΩ)", 10, 500, 100, key="exp1_Rf")
        Cd_pf = st.slider("Cd (pF)", 1.0, 200.0, 20.0, key="exp1_Cd")

    T = 0.01
    fs = 200_000
    t = np.linspace(0, T, int(T * fs))

    duty_f = duty / 100.0
    laser_mw = (((t * freq) % 1) < duty_f).astype(float) * power_mw
    laser_W = laser_mw / 1000.0
    Ipd = responsivity * laser_W

    Rf = Rf_k * 1000
    Vout_ideal = -Ipd * Rf

    Cd = Cd_pf * 1e-12
    tau = Rf * Cd
    dt = 1.0 / fs
    alpha = dt / (tau + dt)
    Vout = np.zeros_like(Vout_ideal)
    for i in range(1, len(Vout)):
        Vout[i] = Vout[i-1] + alpha * (Vout_ideal[i] - Vout[i-1])

    fig2, ax2 = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    ax2[0].plot(t * 1000, laser_mw)
    ax2[0].set_ylabel("Lazer (mW)")
    ax2[0].set_title("Lazer Darbe Sinyali")

    ax2[1].plot(t * 1000, Vout)
    ax2[1].set_xlabel("Zaman (ms)")
    ax2[1].set_ylabel("Vout (V)")
    ax2[1].set_title("Fotodiyot Çıkışı")

    st.pyplot(fig2)

    f_c = 1.0 / (2 * np.pi * Rf * Cd)
    st.markdown(
        f"- Kesim frekansı: **{f_c:.1f} Hz**  \n"
        f"- İdeal çıkış min.: **{np.min(Vout_ideal):.2f} V**  \n"
        f"- RC filtreli çıkış min.: **{np.min(Vout):.2f} V**"
    )

# ============================================================
# Deney 2: Triangulation ile mesafe ölçümü
# ============================================================

def experiment_2():
    st.header("Deney 2 – Lazer Triangulation ile Mesafe Ölçümü")

    st.markdown(
        "Bu deneyde lazer beam bir nesneye çarpar, yansıyan nokta bir line sensör üzerinde kayar. "
        "Bu kayma kullanılarak nesnenin mesafesi hesaplanır (triangulation prensibi)."
    )

    st.subheader("Düzenek Şeması")
    fig = draw_setup_2()
    st.pyplot(fig)

    st.subheader("Temel Geometri")
    st.latex(r"""
    d = \frac{b \, f}{x}
    """)
    st.markdown(
        "Burada:  \n"
        "- d: nesne mesafesi  \n"
        "- b: lazer ile sensör arasındaki taban mesafesi  \n"
        "- f: optik sistemin odak uzaklığı  \n"
        "- x: sensör üzerindeki görüntü kayması"
    )

    st.subheader("Simülasyon: Mesafe → Piksel Konumu")

    b = st.slider("Taban Mesafesi b (cm)", 2.0, 15.0, 5.0, key="exp2_b")
    f = st.slider("Odak Uzaklığı f (cm)", 1.0, 10.0, 3.0, key="exp2_f")
    d_min, d_max = 5.0, 50.0
    d_vals = np.linspace(d_min, d_max, 200)

    x_vals = b * f / d_vals
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.plot(d_vals, x_vals)
    ax2.set_xlabel("Mesafe d (cm)")
    ax2.set_ylabel("Sensör Kayması x (cm)")
    ax2.set_title("Mesafe–Sensör Kayması İlişkisi")
    st.pyplot(fig2)

    d0 = st.slider("Ölçmek istediğiniz mesafe d0 (cm)", d_min, d_max, 25.0, key="exp2_d0")
    x0 = b * f / d0
    st.markdown(
        f"Seçilen d0 = **{d0:.1f} cm** için beklenen sensör kayması: **x0 = {x0:.2f} cm**"
    )

# ============================================================
# Deney 3: Optik yoğunluk (attenuation) ölçümü
# ============================================================

def experiment_3():
    st.header("Deney 3 – Optik Yoğunluk (Attenuation) Ölçümü")

    st.markdown(
        "Bu deneyde lazer ışığı bir numuneden geçirilir, giriş ve çıkış şiddetleri ölçülerek "
        "Beer–Lambert yasası ile soğurma katsayısı hesaplanır."
    )

    st.subheader("Düzenek Şeması")
    fig = draw_setup_3()
    st.pyplot(fig)

    st.subheader("Beer–Lambert Yasası")
    st.latex(r"""
    I = I_0 e^{-\alpha L}
    """)
    st.latex(r"""
    \alpha = \frac{1}{L} \ln\left(\frac{I_0}{I}\right)
    """)

    st.subheader("Simülasyon: Farklı Kalınlıklar için I(L)")

    I0 = st.slider("Giriş şiddeti I0 (mW)", 1.0, 20.0, 10.0, key="exp3_I0")
    alpha = st.slider("Soğurma katsayısı α (1/cm)", 0.01, 1.0, 0.2, key="exp3_alpha")
    L_vals = np.linspace(0, 5, 200)
    I_vals = I0 * np.exp(-alpha * L_vals)

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.plot(L_vals, I_vals)
    ax2.set_xlabel("Kalınlık L (cm)")
    ax2.set_ylabel("I (mW)")
    ax2.set_title("Numune Kalınlığına Göre Işık Şiddeti")
    st.pyplot(fig2)

    Lm = st.slider("Seçilen numune kalınlığı Lm (cm)", 0.1, 5.0, 1.0, key="exp3_Lm")
    Im = I0 * np.exp(-alpha * Lm)
    st.markdown(
        f"Seçilen Lm = **{Lm:.2f} cm** için çıkış şiddeti: **I = {Im:.2f} mW**"
    )

# ============================================================
# Deney 4: Optik kapı ile hız ölçümü
# ============================================================

def experiment_4():
    st.header("Deney 4 – Optik Kapı ile Nesne Hızı Ölçümü")

    st.markdown(
        "Bu deneyde lazer ve fotodiyot ile bir ışık bariyeri kurulur. "
        "Nesne ışık yolunu kestiği süre ölçülerek hız hesaplanır."
    )

    st.subheader("Düzenek Şeması")
    fig = draw_setup_4()
    st.pyplot(fig)

    st.subheader("Temel Denklem")
    st.latex(r"""
    v = \frac{L}{\Delta t}
    """)
    st.markdown(
        "L: bariyeri kateden nesnenin boyu,  Δt: ışığın kesildiği süre."
    )

    st.subheader("Simülasyon: Dijital Sinyal ve Hız Hesabı")

    L_obj = st.slider("Nesne boyu L (cm)", 1.0, 20.0, 5.0, key="exp4_L")
    v_obj = st.slider("Gerçek hız v (cm/s)", 10.0, 200.0, 50.0, key="exp4_v")
    dt = L_obj / v_obj

    # Simüle zaman ekseni
    T = 2 * dt
    t = np.linspace(0, T, 1000)
    signal = np.ones_like(t)
    # Ortada nesne geçişi
    t_start = 0.5 * (T - dt)
    t_end = t_start + dt
    signal[(t >= t_start) & (t <= t_end)] = 0

    fig2, ax2 = plt.subplots(figsize=(7, 3))
    ax2.plot(t * 1000, signal, drawstyle="steps-post")
    ax2.set_xlabel("Zaman (ms)")
    ax2.set_ylabel("Fotodiyot çıkışı (norm.)")
    ax2.set_ylim(-0.2, 1.2)
    ax2.set_title("Optik Bariyer Sinyali (1: açık, 0: kapalı)")
    st.pyplot(fig2)

    st.markdown(
        f"Hesaplanan kesilme süresi Δt = **{dt*1000:.1f} ms**  \n"
        f"Bu süreyi ölçerseniz, v = L / Δt ile hız: **{v_obj:.1f} cm/s**"
    )

# ============================================================
# Deney 5: RGB sensör ile lazer spektrumu algılama
# ============================================================

def experiment_5():
    st.header("Deney 5 – RGB Sensör ile Farklı Lazerlerin Spektral Analizi")

    st.markdown(
        "Bu deneyde RGB renk sensörü kullanarak kırmızı, yeşil ve mor/mavi lazerlerin "
        "hangi kanalda daha güçlü sinyal ürettiğini gözlemleriz. "
        "Bu, 3 bantlı basit bir mini spektrometre gibi düşünülebilir."
    )

    st.subheader("Düzenek Şeması")
    fig = draw_setup_5()
    st.pyplot(fig)

    st.subheader("RGB Sensör Mantığı")
    st.markdown(
        "RGB sensör üç ayrı filtreli fotodiyot barındırır: R, G ve B. "
        "Lazerin dalga boyuna göre bu kanallardan biri baskın olur."
    )

    st.subheader("Simülasyon: Dalga Boyuna Göre RGB Tepkisi")

    wavelength = st.slider("Lazer Dalga Boyu (nm)", 400, 700, 650, key="exp5_lambda")

    lam = wavelength
    # Çok basit üç gauss benzeri tepki
    R = np.exp(-0.5 * ((lam - 630) / 30) ** 2)
    G = np.exp(-0.5 * ((lam - 540) / 30) ** 2)
    B = np.exp(-0.5 * ((lam - 460) / 25) ** 2)

    channels = ["R", "G", "B"]
    values = [R, G, B]

    fig2, ax2 = plt.subplots(figsize=(5, 3))
    ax2.bar(channels, values)
    ax2.set_ylim(0, 1.1)
    ax2.set_ylabel("Normalize Kanal Sinyali")
    ax2.set_title(f"{lam} nm için RGB kanal tepkisi (normalize)")
    st.pyplot(fig2)

    st.markdown(
        f"Seçilen dalga boyu: **{lam} nm**  \n"
        f"- R kanalı: **{R:.2f}**  \n"
        f"- G kanalı: **{G:.2f}**  \n"
        f"- B kanalı: **{B:.2f}**"
    )

# ============================================================
# ANA ARAYÜZ
# ============================================================

st.title("Arduino Tabanlı 5 Elektro-Optik Deney")

selection = st.selectbox(
    "Deney seçin:",
    [
        "1 - Lazer Modülasyonu ve Fotodiyot ile Sinyal Tespiti",
        "2 - Lazer Triangulation ile Mesafe Ölçümü",
        "3 - Optik Yoğunluk (Attenuation) Ölçümü",
        "4 - Optik Kapı ile Hız Ölçümü",
        "5 - RGB Sensör ile Lazer Spektrumu Analizi",
    ]
)

if selection.startswith("1"):
    experiment_1()
elif selection.startswith("2"):
    experiment_2()
elif selection.startswith("3"):
    experiment_3()
elif selection.startswith("4"):
    experiment_4()
elif selection.startswith("5"):
    experiment_5()
