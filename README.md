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
├── main.py                      # FastAPI sunucusu ve tahmin API'si
├── pyspark_analiz.ipynb         # Jupyter Notebook: Veri analizi ve EDA
├── pyproject.toml               # Proje bağımlılıkları (uv)
├── Dockerfile                   # Docker containerı için yapılandırma
├── Datas/                        # Veri setleri
│   ├── turkiye.csv
│   ├── romanya.csv
│   ├── azerbaycan.csv
│   ├── kktc.csv
│   └── libya.csv
├── lightgbm_model.pkl           # Eğitilmiş LightGBM modeli
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

### 1. Jupyter Notebook ile Analiz

```bash
uv run jupyter notebook pyspark_analiz.ipynb
```

Bu notebook'ta:
- Veri keşfi ve temizleme
- PySpark ile dağıtık veri işleme
- Özellik mühendisliği
- Model eğitimi ve değerlendirmesi

### 2. FastAPI Sunucusunu Başlatma

```bash
uv run uvicorn main:app --reload
```

Sunucu `http://localhost:8000` adresinde çalışacaktır.

#### API Endpoints

- **POST** `/predict` - Satış tahmin endpointi
  ```json
  {
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
  }
  ```

- **GET** `/docs` - API dokumentasyonu (Swagger UI)
- **GET** `/redoc` - ReDoc dokumentasyonu

### 3. Docker ile Çalıştırma

```bash
# Docker image'ı oluştur
docker build -t retail-bigdata:latest .

# Container'ı çalıştır
docker run -p 8000:8000 retail-bigdata:latest
```

Sunucu `http://localhost:8000` adresinde hizmet verecektir.

## 🧪 Test Etme

```bash
# Tahmin API'sini test et
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "urunklasmankod": 101,
    "satisadet_lfl_gy": 5000,
    ...
  }'
```

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


