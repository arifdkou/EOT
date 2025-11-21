import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Elektro-Optik: Arduino + Lazer + Fotodiyot", layout="wide")

# ===============================================================
#  TITLE & LEARNING OUTCOMES
# ===============================================================
st.title("Elektro-Optik Uygulama: Arduino + Lazer Diyot + Fotodiyot")

st.subheader("Dersin Öğrenme Çıktıları")

st.markdown(
"""
Bu ders sonunda öğrenci:

- Arduino ile lazer diyot sürmeyi öğrenir  
- Lazer akım sınırlama mantığını açıklar  
- Fotodiyodun optik güce bağlı akım üretimini açıklar  
- Transimpedans yükselteç yapısını analiz eder  
- Streamlit üzerinde lazer darbe → fotodiyod çıkış simülasyonu yapar  
"""
)

# ===============================================================
# 1. SISTEM TANIMI
# ===============================================================
st.header("1. Sistem Bileşenleri ve Genel Yapı")

st.markdown(
"""
Sistem 3 ana bileşenden oluşur:

1. **Arduino + Transistor ile lazer sürme**  
2. **Optik yol (lazer → fotodiyot)**  
3. **Fotodiyot + transimpedans yükselteci**
"""
)

st.latex(r"""
I_{\text{laser}} = \frac{V_s - V_{\text{laser}}}{R_{\text{limit}}}
""")

st.latex(r"""
V_{\text{out}} = - I_{\text{pd}} \, R_f
""")

# ===============================================================
# 2. LAZER DIYOT SURME
# ===============================================================
st.header("2. Lazer Diyotun Arduino ile Sürülmesi")

st.markdown(
"""
Lazer diyot Arduino pinine doğrudan bağlanmaz.  

- Arduino pin akımı sınırlıdır  
- Lazer diyot yüksek akım gerektirir  
- Ani akım darbeleri lazer diyotu yakabilir  

Bu nedenle **NPN transistor + akım sınırlama direnci** gereklidir.
"""
)

st.latex(r"""
I_{\text{laser}} = \frac{V_s - V_{\text{laser}}}{R_{\text{limit}}}
""")

# ===============================================================
# 3. FOTODIYOT & TRANSIMPEDANS
# ===============================================================
st.header("3. Fotodiyot ve Transimpedans Yükselteci")

st.markdown(
"""
Fotodiyot ışığı akıma çevirir. Bu ilişki:

"""
)

st.latex(r"""
I_{\text{pd}} = R_{\lambda} \, P_{\text{opt}}
""")

st.markdown(
"""
Transimpedans yükselteci bu akımı gerilime dönüştürür:
"""
)

st.latex(r"""
V_{\text{out}} = - I_{\text{pd}} \, R_f
""")

st.markdown(
"""
Bant genişliği ise fotodiyot kapasitansı ve geri besleme direncine bağlıdır:
"""
)

st.latex(r"""
f_{\text{cutoff}} = \frac{1}{2\pi R_f C_d}
""")

# ===============================================================
# 4. SIMULASYON
# ===============================================================
st.header("4. Simülasyon: Lazer Darbesi → Fotodiyod Çıkışı")

col1, col2 = st.columns(2)

with col1:
    freq = st.slider("Lazer Darbe Frekansı (Hz)", 1, 5000, 200)
    duty = st.slider("Görev Oranı (%)", 1, 99, 50)
    power_mw = st.slider("Optik Güç (mW)", 1, 50, 10)

with col2:
    responsivity = st.slider("Responsivity (A/W)", 0.1, 1.0, 0.5)
    Rf_k = st.slider("Rf (kΩ)", 10, 500, 100)
    Cd_pf = st.slider("Cd (pF)", 1.0, 200.0, 20.0)

# -------------------------
# TIME AXIS
# -------------------------
T = 0.01
fs = 200_000
t = np.linspace(0, T, int(T*fs))

# -------------------------
# LASER SIGNAL
# -------------------------
duty_f = duty / 100.0
laser_mw = (((t * freq) % 1) < duty_f).astype(float) * power_mw
laser_W = laser_mw / 1000.0

# -------------------------
# PHOTODIODE CURRENT
# -------------------------
Ipd = responsivity * laser_W

# -------------------------
# TRANSIMPEDANCE
# -------------------------
Rf = Rf_k * 1000
Vout_ideal = -Ipd * Rf

Cd = Cd_pf * 1e-12
tau = Rf * Cd
dt = 1.0 / fs
alpha = dt / (tau + dt)

Vout = np.zeros_like(Vout_ideal)
for i in range(1, len(Vout)):
    Vout[i] = Vout[i-1] + alpha * (Vout_ideal[i] - Vout[i-1])

# -------------------------
# PLOT
# -------------------------
fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax[0].plot(t*1000, laser_mw)
ax[0].set_ylabel("Lazer (mW)")
ax[0].set_title("Lazer Darbesi")

ax[1].plot(t*1000, Vout)
ax[1].set_xlabel("Zaman (ms)")
ax[1].set_ylabel("Vout (V)")
ax[1].set_title("Fotodiyod Çıkışı")

st.pyplot(fig)

# -------------------------
# NUMERIC SUMMARY
# -------------------------
f_c = 1.0 / (2*np.pi*Rf*Cd)

st.subheader("Sayısal Sonuçlar")

st.markdown(
f"""
- Kesim frekansı: **{f_c:.1f} Hz**  
- İdeal çıkış min.: **{np.min(Vout_ideal):.2f} V**  
- RC filtreli çıkış min.: **{np.min(Vout):.2f} V**  
"""
)

# ===============================================================
# 5. ARDUINO KODLARI
# ===============================================================
