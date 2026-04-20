# Retail Big Data Analiz Projesi

Perakende sektöründe satış tahmini ve veri analizi için geliştirilmiş kapsamlı bir Big Data projesidir. PySpark ile çok ülkeli veri setlerini işleyerek machine learning modelleri ile satış öngörüsü yapmaktadır.

## 📋 Proje Özellikleri

- **Veri Kaynakları**: Türkiye, Romanya, Azerbaycan, KKTC ve Libya perakende verileri
- **Machine Learning Model**: LightGBM algoritması ile satış tahmini
- **API Sunucusu**: FastAPI ile REST API hizmeti
- **Containerization**: Docker ile kolay dağıtım
- **Veri İşleme**: PySpark ile büyük veri analizi ve dönüşümleri

## 📊 Veri Seti

Proje aşağıdaki ülkelerin perakende verilerini içermektedir:

| Ülke | Dosya |
|------|-------|
| 🇹🇷 Türkiye | `turkiye.csv` |
| 🇷🇴 Romanya | `romanya.csv` |
| 🇦🇿 Azerbaycan | `azerbaycan.csv` |
| 🇨🇾 KKTC | `kktc.csv` |
| 🇱🇾 Libya | `libya.csv` |

Veriler `Datas/` dizininde saklanmaktadır.

## 🔍 Tahmin Özellikleri

Model aşağıdaki özellikleri kullanarak satış tahmini yapmaktadır:

- **Ürün Bilgileri**: Ürün sınıflandırması, mal grubu, alt grup
- **Satış Verileri**: Geçen yıl satışları, indirim oranları
- **Zaman Bilgileri**: Haftanın günü, ayın adı, hafta numarası, haftasonu bayrağı
- **Hava Durumu**: Minimum, ortalama ve maksimum sıcaklık
- **Depo Bilgileri**: Günsonunda toplam stok, üreyonun stoğu
- **Mağaza Bilgileri**: Mağaza kodu, açık kalma süresi
- **Özel Günler**: Tatil ve özel gün bayrakları

## 🚀 Kurulum

### Gereksinimler

- Python 3.10+
- Docker (opsiyonel, containerized çalıştırma için)
- uv paket yöneticisi

### Yerel Kurulum

1. **Depoyu klonlayın**
```bash
git clone <repository-url>
cd retail_bigdata_project
```

2. **Bağımlılıkları yükleyin**
```bash
uv sync
```

3. **Modeli indirin**
LightGBM model dosyası (`lightgbm_model.pkl`) proje dizinine yerleştirilmelidir.

## 📦 Proje Yapısı

```
retail_bigdata_project/
├── 📋 Backend (API Sunucusu)
│   ├── main.py                      # FastAPI sunucusu ve tahmin API'si
│   ├── lightgbm_model.pkl           # Eğitilmiş LightGBM modeli
│   ├── pyproject.toml               # Proje bağımlılıkları (uv)
│   ├── uv.lock                      # Sürüm kilitlemesi
│   ├── Dockerfile                   # Backend containerı
│   └── .python-version              # Python sürümü belirtimi
│
├── 🎨 Frontend (Web Arayüzü)
│   ├── frontend/
│   │   ├── index.html               # İnteraktif form arayüzü
│   │   └── Dockerfile               # Frontend containerı
│   │
├── 📊 Veri İşleme & Analiz
│   ├── pyspark_analiz.ipynb         # Jupyter Notebook: Veri analizi ve EDA
│   ├── Datas/
│   │   ├── turkiye.csv              # Türkiye perakende verileri
│   │   ├── romanya.csv              # Romanya perakende verileri
│   │   ├── azerbaycan.csv           # Azerbaycan perakende verileri
│   │   ├── kktc.csv                 # KKTC perakende verileri
│   │   └── libya.csv                # Libya perakende verileri
│   │
├── 📚 Sürüm Kontrol
│   ├── .git/                        # Git deposu
│   ├── .github/                     # GitHub Actions
│   ├── .gitignore                   # Git ignore dosyası
│   │
├── 🐍 Çevre
│   ├── .venv/                       # Sanal ortam
│   ├── __pycache__/                 # Python cache
│   │
└── 📄 Dokümantasyon
    └── README.md                    # Bu dosya
```

## 🛠️ Bağımlılıklar

### Production Bağımlılıkları
- `fastapi[standard]` - Web framework
- `uvicorn` - ASGI sunucusu
- `lightgbm` - Machine learning modeli
- `scikit-learn` - ML araçları
- `pandas` - Veri işleme
- `numpy` - Sayısal hesaplamalar
- `joblib` - Model yükleme

### Geliştirme Bağımlılıkları
- `pyspark` - Büyük veri işleme
- `jupyter/ipykernel` - Notebook ortamı
- `xgboost`, `catboost` - Alternatif ML modelleri
- `optuna` - Hiperparametre optimizasyonu
- `shap` - Model açıklanabilirliği
- `seaborn` - Veri görselleştirme
- `polars` - Hızlı veri işleme
- `pyarrow` - Veri formatları

## 💻 Kullanım

### 1. 📊 Jupyter Notebook ile Veri Analizi

```bash
uv run jupyter notebook pyspark_analiz.ipynb
```

Bu notebook'ta yapılabilecek işlemler:
- Veri keşfi ve temizleme
- PySpark ile dağıtık veri işleme
- Özellik mühendisliği
- Model eğitimi ve değerlendirmesi
- Ülkeler arası karşılaştırmalar

### 2. 🚀 Backend API Sunucusunu Başlatma

```bash
# Terminal 1: Backend sunucusu
cd /home/emre/gtu/BIG-DATA/retail_bigdata_project
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Sunucu `http://localhost:8000` adresinde çalışacaktır.

**API Endpoints:**

- **POST** `/predict` - Satış tahmin endpointi (JSON payload)
- **GET** `/docs` - Swagger UI API Dokumentasyonu
- **GET** `/redoc` - ReDoc interaktif dokumentasyonu
- **GET** `/openapi.json` - OpenAPI şeması

### 3. 🎨 Frontend Web Arayüzü

**Seçenek A: Yerel Dosya Açma**
```bash
# Firefox, Chrome veya Safari'de açın
open frontend/index.html
```

**Seçenek B: Live Server ile Çalıştırma (VS Code)**
1. VS Code'da "Live Server" extension'ı yükleyin
2. `frontend/index.html` dosyasına sağ tıkla
3. "Open with Live Server" seçeneğini tıkla

**Seçenek C: Python HTTP Server**
```bash
cd frontend
python3 -m http.server 3000
# http://localhost:3000 adresinde erişin
```

Frontend arayüzü, backend API'ye bağlanarak tahmin sonuçları gösterir.

#### Frontend Özellikleri:
- ✅ Responsive tasarım (mobil uyumlu)
- ✅ Real-time form doğrulaması
- ✅ Önceden doldurulmuş test değerleri
- ✅ Hata yönetimi ve kullanıcı geri bildirimi
- ✅ CSS Grid tabanlı profesyonel layout

### 4. 🐳 Docker ile Full Stack Çalıştırma

#### Backend Container
```bash
# Backend image'ı oluştur
docker build -t retail-backend:latest .

# Backend container'ı çalıştır
docker run -p 8000:8000 --name retail-api retail-backend:latest
```

#### Frontend Container
```bash
# Frontend image'ı oluştur
cd frontend
docker build -t retail-frontend:latest .

# Frontend container'ı çalıştır
docker run -p 80:80 --name retail-web retail-frontend:latest
```

#### Docker Compose (Tüm Sistem)
```bash
# Her iki container'ı birlikte çalıştır (gelecek: docker-compose.yml)
docker-compose up -d
```

**Sonuç:**
- Backend API: `http://localhost:8000`
- Frontend Web: `http://localhost` veya `http://localhost/80`

### 5. 🧪 Test Etme

#### API Test (cURL)
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "urunklasmankod": 101,
    "satisadet_lfl_gy": 5000,
    "indirimorani": 0.15,
    "gunlukminimumsicaklik": 5.2,
    "gunlukortalamasicaklik": 12.3,
    "gunlukmaksimumsicaklik": 18.5,
    "ozelgunflag": 0,
    "gunsonutoplamstok": 15000,
    "gunsonureyonstok": 3000,
    "Haftanin_Gunu": 3,
    "Yilin_Ayi": 6,
    "Yilin_Haftasi": 25,
    "Acik_Kalma_Suresi_Saat": 14.5,
    "ulke_Index": 1,
    "magazakod_Index": 5,
    "merchmarkayasgrupkod_Index": 2,
    "merchaltgrupkod_Index": 8,
    "depoyerlesimtip_Index": 1,
    "Haftasonu_Mu": 0,
    "Indirim_x_Haftasonu": 0.0
  }'
```

#### Web Arayüzü Test
1. `frontend/index.html` dosyasını tarayıcıda açın
2. Değerler önceden doldurulmuştur
3. "Modeli Çalıştır 🚀" düğmesine tıklayın
4. Tahmin sonucunu görün

## 📈 Model Performansı

LightGBM modeli aşağıdaki metriklerle değerlendirilmiştir:
- Eğitim süresi: Optimize edilmiş
- Özellik sayısı: 20 temel özellik
- Zaman serisi avantajı: Sezonsallık ve trend analizi

## 🔧 Teknik Detaylar

### Docker Optimizasyonları
- Slim Python image kullanarak boyut azaltma
- Multi-stage build yapısı
- uv paket yöneticisi ile hızlı kurulum
- Production bağımlılıklarına odaklanma

### Veri İşleme
- PySpark ile dağıtık veri işleme
- Kategorik değişkenlerin index'lenmesi
- Zaman serisi özellikleri oluşturma
- Eksik veri işleme ve normalizasyon

## 📚 Kaynaklar

- [FastAPI Dokumentasyonu](https://fastapi.tiangolo.com/)
- [LightGBM Dokumentasyonu](https://lightgbm.readthedocs.io/)
- [PySpark Dokumentasyonu](https://spark.apache.org/docs/latest/api/python/)
- [Uvicorn Dokumentasyonu](https://www.uvicorn.org/)

## 📝 Lisans

Bu proje eğitim amaçlıdır.


