import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# PySerial opsiyonel – yoksa sadece simülasyon modunda çalışır
try:
    import serial
except ImportError:
    serial = None

# =========================================================
#  GENEL AYARLAR
# =========================================================
st.set_page_config(
    page_title="Elektro-Optik Teknolojilere Giriş",
    page_icon="🔦",
    layout="wide"
)

# =========================================================
#  BAŞLIK
# =========================================================
st.title("🔦 Elektro-Optik Teknolojilere Giriş")
st.markdown(
"""
**Elektro-Optik Teknolojilere Giriş**

Bu uygulama, elektro-optik teknolojilerini tanıtmak, temel denklemleri göstermek ve bazı basit simülasyonlar ile kavramların daha iyi anlaşılmasını sağlamak için hazırlandı. 
Optik bilimi, fotonik, lazer sistemleri, sensörler ve akıllı ölçüm teknolojilerinin kesişiminde yer alan bu alan; bugün savunmadan uzay teknolojilerine, tıptan endüstriyel kalite kontrol sistemlerine kadar geniş bir etki alanı oluşturuyor.

Bu interaktif eğitim aracı, **Ostim Teknik Üniversitesi Elektro-Optik Topluluğu’nda** kendini geliştirmek isteyen **genç araştırmacılar** için **Prof. Dr. Arif Demir** tarafından hazırlanmıştır.  
Amacımız, elektro-optik sistemlerin mantığını yalnızca teorik bir çerçevede değil; deneysel düşünme, problem çözme, simülasyon ve gerçek devre uygulamalarıyla birlikte öğrenmenizi sağlamaktır.

Sol menüden bölüm ve simülasyon seçerek etkileşimli olarak inceleyebilir, elektro-optik dünyasına adım adım hâkim olabilirsiniz.
"""
)


# =========================================================
#  SIDEBAR MENÜ
# =========================================================
st.sidebar.header("⚙️ Ayarlar")

section = st.sidebar.selectbox(
    "Bölüm Seç:",
    [
        "1️⃣ Teorik Bilgi",
        "2️⃣ Simülasyonlar"
    ]
)

if section == "2️⃣ Simülasyonlar":
    sim_choice = st.sidebar.radio(
        "Simülasyon Seç:",
        [
            "Snell Kırılma Yasası",
            "Fotodiyot Cevabı",
            "Gauss Işın Demeti (Beam Propagation)",
            "Arduino Seri Port – Fotodiyot (Gerçek/Sanal)"
        ]
    )
else:
    sim_choice = None

# =========================================================
#  1) TEORİK BİLGİ BÖLÜMÜ
# =========================================================
if section == "1️⃣ Teorik Bilgi":
    st.header("1️⃣ Elektro-Optik Sistemlere Genel Bakış")

    st.markdown(
    """
Elektro-optik teknolojiler; **ışığın üretilmesi, yönlendirilmesi, algılanması ve elektriksel sinyallerle işlenmesini** 
kapsayan kritik bir alandır. Lazerler, mercekler, aynalar, fiber optik kablolar ve fotodetektörler gibi bileşenler 
bir araya gelerek iletişimden savunmaya, tıptan endüstriyel kalite kontrole kadar pek çok uygulamada kullanılır.

Aşağıda bazı temel kavramları ve Türkiye / dünyadan örnekleri özetliyoruz.
"""
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔧 Temel Bileşenler")
        st.markdown(
        """
- **Işık Kaynakları:** Lazerler (Nd:YAG, fiber lazer, CO₂, UV), LED'ler, SLD’ler  
- **Optik Elemanlar:** Mercek, ayna, prizma, difraksiyon ızgarası, filtre  
- **Dedektörler:** Fotodiyot, CCD/CMOS kamera, APD, InGaAs dedektörler  

Bu elemanların kombinasyonu ile **lazer işleme, spektroskopi, görüntüleme ve haberleşme** sistemleri kurulur.
"""
        )

    with col2:
        st.subheader("🌍 Türkiye ve Dünya Örnekleri")
        st.markdown(
        """
**Türkiye:**
- ASELSAN – Termal kameralar, elektro-optik keşif sistemleri  
- ROKETSAN – Lazer güdüm ve optik arayıcı başlıklar  
- OSTİM ekosistemi – LIBS, spektroskopi, lazer–plazma sistemleri  

**Dünya:**
- ASML & ARCNL (Hollanda) – EUV litografi, çip üretiminde fotonik  
- Fraunhofer (Almanya) – Endüstriyel lazer sistemleri  
- MIT, Stanford (ABD) – Kuantum optik, entegre fotonik devreler  
"""
        )

    st.markdown("---")
    st.header("2️⃣ Temel Denklemler")

    st.subheader("📐 2.1 Snell Kırılma Yasası")
    st.latex(r"n_1 \sin\theta_1 = n_2 \sin\theta_2")
    st.markdown(
    """
- \( n_1, n_2 \): kırılma indisleri  
- \( \theta_1 \): gelme açısı  
- \( \theta_2 \): kırılma açısı  
"""
    )

    st.subheader("💡 2.2 Fotodiyot Akımı")
    st.latex(r"I_{pd} = R(\lambda)\, P_{optik}")
    st.markdown(
    """
- \( I_{pd} \): fotodiyot akımı (A)  
- \( R(\lambda) \): dalga boyuna bağlı responsivite (A/W)  
- \( P_{optik} \): fotodiyoda gelen optik güç (W)  
"""
    )

    st.subheader("🔦 2.3 Gauss Işın Demeti")
    st.latex(r"w(z) = w_0 \sqrt{1 + \left( \frac{z}{z_R} \right)^2 }")
    st.latex(r"z_R = \frac{\pi w_0^2}{\lambda}")
    st.markdown(
    """
Bu formül, lazer odaklama, malzeme işleme ve mikroskopi uygulamalarında kritik öneme sahiptir.
"""
    )

    st.markdown("---")
    st.header("3️⃣ Arduino ile Elektro-Optik Uygulamalar")

    st.markdown(
    """
Arduino, **düşük maliyetli ve kolay programlanabilir** bir platform olduğu için elektro-optik deneyler için ideal:

- Fotodiyot çıkışını **ADC** ile ölçer.  
- **PWM** ile lazer diyot/LED sürücüyü kontrol eder.  
- Step/servo ile optik hizalama yapılabilir.  
- Seri port ile PC’ye veri gönderilir, burada Python–Streamlit ile grafiklenir.

Aşağıdaki simülasyonlardan biri doğrudan Arduino’dan seri port ile veri okumayı hedefler.
"""
    )

# =========================================================
#  2) SİMÜLASYONLAR
# =========================================================
if section == "2️⃣ Simülasyonlar":

    # -----------------------------------------------------
    #  SIM 1: Snell Kırılma Yasası
    # -----------------------------------------------------
    if sim_choice == "Snell Kırılma Yasası":
        st.header("🔍 Snell Kırılma Yasası Simülasyonu")

        st.markdown(
        """
Bu simülasyon, iki ortam arasındaki **kırılma** olayını görselleştirir.  
Kırılma indisi ve gelme açısını değiştirerek, kırılan ışının açısını ve çizimini görebilirsin.
"""
        )

        col_inputs, col_plot = st.columns([1, 2])

        with col_inputs:
            n1 = st.number_input("n₁ (Birinci ortam kırılma indisi)", 0.1, 5.0, 1.0, 0.01)
            n2 = st.number_input("n₂ (İkinci ortam kırılma indisi)", 0.1, 5.0, 1.5, 0.01)
            theta1_deg = st.slider("Gelme Açısı θ₁ (derece)", 0.0, 89.0, 30.0, 1.0)

            theta1 = np.deg2rad(theta1_deg)

            # Kritik açı kontrolü
            if n1 > n2:
                sin_crit = n2 / n1
                if sin_crit <= 1.0:
                    theta_crit = np.rad2deg(np.arcsin(sin_crit))
                else:
                    theta_crit = None
            else:
                theta_crit = None

            # Kırılma açısını hesapla
            sin_theta2 = (n1 / n2) * np.sin(theta1)
            total_internal_reflection = False
            if abs(sin_theta2) > 1.0:
                total_internal_reflection = True
                theta2_deg = None
            else:
                theta2 = np.arcsin(sin_theta2)
                theta2_deg = np.rad2deg(theta2)

            st.markdown("### Sonuçlar")
            st.latex(r"n_1 \sin\theta_1 = n_2 \sin\theta_2")
            st.write(f"Seçilen gelme açısı: **θ₁ = {theta1_deg:.2f}°**")
            st.write(f"Kırılma indisleri: **n₁ = {n1:.3f}, n₂ = {n2:.3f}**")

            if total_internal_reflection:
                st.error("Toplam iç yansıma gerçekleşti! (Kırılan ışın yok)")
                if theta_crit is not None:
                    st.write(f"Kritik açı ≈ **{theta_crit:.2f}°**")
            else:
                st.success(f"Kırılan ışın açısı: **θ₂ ≈ {theta2_deg:.2f}°**")

        with col_plot:
            fig, ax = plt.subplots()
            ax.axhline(0, linewidth=1)

            # Gelme ışını
            x0, y0 = -1.0, np.tan(theta1)
            ax.plot([x0, 0], [y0, 0], linewidth=2)

            if not total_internal_reflection:
                theta2_rad = np.deg2rad(theta2_deg)
                x1, y1 = 1.0, -np.tan(theta2_rad)
                ax.plot([0, x1], [0, y1], linewidth=2)
            else:
                x1, y1 = -1.0, -np.tan(theta1)
                ax.plot([0, x1], [0, y1], linewidth=2, linestyle='--')

            ax.axvline(0, linestyle='--', linewidth=1)

            ax.set_aspect('equal', 'box')
            ax.set_xlim(-1.2, 1.2)
            ax.set_ylim(-1.2, 1.2)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title("Snell Kırılma Görselleştirmesi")
            ax.grid(True)

            st.pyplot(fig)

    # -----------------------------------------------------
    #  SIM 2: Fotodiyot Cevabı
    # -----------------------------------------------------
    if sim_choice == "Fotodiyot Cevabı":
        st.header("📡 Fotodiyot Cevabı Simülasyonu")

        st.markdown(
        """
Bu simülasyon, bir fotodiyotun **optik güç–akım** ve **optik güç–gerilim** ilişkilerini gösterir.  
Arduino ile **Rf** (geri besleme direnci) üzerinden bir transimpedans yükselteci kurduğunu ve çıkış gerilimini okuduğunu varsayıyoruz.

Temel denklemler:
"""
        )
        st.latex(r"I_{pd} = R(\lambda)\, P_{optik}")
        st.latex(r"V_{out} = - I_{pd} R_f")

        col_left, col_right = st.columns([1, 2])

        with col_left:
            R_lambda = st.number_input("Responsivite R(λ) (A/W)", 0.01, 1.0, 0.5, 0.01)
            Rf = st.number_input("Geri besleme direnci R_f (Ohm)", 1e3, 1e7, 1e5, 1e4, format="%.0f")
            P_min = st.number_input("Min. Optik Güç (mW)", 0.0, 10.0, 0.0, 0.1)
            P_max = st.number_input("Max. Optik Güç (mW)", 0.1, 50.0, 10.0, 0.5)
            num_points = st.slider("Örnek Sayısı", 5, 200, 50, 5)

        with col_right:
            P_mW = np.linspace(P_min, P_max, num_points)
            P_W = P_mW * 1e-3
            I_pd = R_lambda * P_W
            V_out = -I_pd * Rf

            fig1, ax1 = plt.subplots()
            ax1.plot(P_mW, I_pd * 1e3)
            ax1.set_xlabel("Optik Güç (mW)")
            ax1.set_ylabel("Fotodiyot Akımı (mA)")
            ax1.set_title("Optik Güç – Fotodiyot Akımı")
            ax1.grid(True)
            st.pyplot(fig1)

            fig2, ax2 = plt.subplots()
            ax2.plot(P_mW, V_out)
            ax2.set_xlabel("Optik Güç (mW)")
            ax2.set_ylabel("Çıkış Gerilimi V_out (V)")
            ax2.set_title("Optik Güç – Çıkış Gerilimi")
            ax2.grid(True)
            st.pyplot(fig2)

        st.markdown(
        """
Bu grafikler, Arduino ile ölçtüğün **V_out** değerlerinin teorik davranışını gösterir.
Gerçekte ADC ile ölçtüğün gerilimlerden yola çıkarak, **optik güç** ve **I_pd** hakkında hesaplama yapabilirsin.
"""
        )

    # -----------------------------------------------------
    #  SIM 3: Gauss Işın Demeti
    # -----------------------------------------------------
    if sim_choice == "Gauss Işın Demeti (Beam Propagation)":
        st.header("🔦 Gauss Işın Demeti (Beam Propagation) Simülasyonu")

        st.markdown(
        """
Bu simülasyon, Gauss ışın demetinin **uzunluk boyunca nasıl genişlediğini** gösterir.

Denklemler:
"""
        )
        st.latex(r"z_R = \frac{\pi w_0^2}{\lambda}")
        st.latex(r"w(z) = w_0 \sqrt{1 + \left( \frac{z}{z_R} \right)^2 }")

        col_left, col_right = st.columns([1, 2])

        with col_left:
            wavelength_nm = st.number_input("Dalga boyu λ (nm)", 200.0, 2000.0, 1064.0, 1.0)
            w0_um = st.number_input("Beam waist w₀ (µm)", 5.0, 1000.0, 50.0, 5.0)
            z_max_mm = st.number_input("Maksimum Mesafe (mm)", 1.0, 500.0, 100.0, 5.0)
            num_points = st.slider("Örnek Sayısı", 50, 1000, 200, 50)

            wavelength = wavelength_nm * 1e-9
            w0 = w0_um * 1e-6
            z_max = z_max_mm * 1e-3

            z = np.linspace(-z_max, z_max, num_points)
            z_R = np.pi * w0**2 / wavelength
            w_z = w0 * np.sqrt(1 + (z / z_R)**2)

        with col_right:
            fig, ax = plt.subplots()
            ax.plot(z * 1e3, w_z * 1e6)
            ax.set_xlabel("z (mm)")
            ax.set_ylabel("Işın yarıçapı w(z) (µm)")
            ax.set_title("Gauss Işın Demeti Genişlemesi")
            ax.grid(True)
            st.pyplot(fig)

        st.markdown(
        f"""
**Rayleigh uzunluğu** yaklaşık:  

\\[
z_R \\approx {z_R * 1e3:.2f}~\\text{{mm}}
\\]
"""
        )

    # -----------------------------------------------------
    #  SIM 4: Arduino Seri Port – Fotodiyot (Gerçek/Sanal)
    # -----------------------------------------------------
    if sim_choice == "Arduino Seri Port – Fotodiyot (Gerçek/Sanal)":
        st.header("🧪 Arduino Seri Port – Fotodiyot (Gerçek/Zamanlı veya Simülasyon)")

      