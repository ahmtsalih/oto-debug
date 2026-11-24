# 🚀 oto-debug

Terminalinizde çöken Python kodlarını anında analiz eden ve Google Gemini AI gücüyle çözüm önerilerini doğrudan terminalinize basan otonom hata ayıklayıcı (CLI Debugger).

![PyPI](https://img.shields.io/pypi/v/oto-debug)
![Python Version](https://img.shields.io/pypi/pyversions/oto-debug)
![License](https://img.shields.io/github/license/ahmtsalih/oto-debug)

## 🌟 Özellikler

- **🤖 Yapay Zeka Destekli Analiz:** Hataları sadece göstermez, neden kaynaklandığını ve nasıl çözüleceğini Türkçe olarak açıklar.
- **🎨 Zengin Terminal Arayüzü:** Markdown formatı, sözdizimi renklendirmesi (syntax highlighting) ve modern paneller ile okunabilirliği artırır.
- **⚡ Akıllı Model Seçimi:** Kota dostu "Yedekleme" (Fallback) mimarisi ile her zaman en stabil ve hızlı Gemini modelini (1.5-flash vb.) otomatik seçer.
- **🖥️ Çapraz Platform Desteği:** Windows, macOS ve Linux üzerinde sorunsuz çalışır.

## 📦 Kurulum

Paketi PyPI üzerinden pip aracılığıyla global olarak kurabilirsiniz:

```bash
pip install oto-debug
```

## ⚙️ Yapılandırma

Aracı kullanabilmek için ücretsiz bir [Google Gemini API Anahtarı](https://aistudio.google.com/app/apikey) almanız gerekmektedir. 

API anahtarınızı aldıktan sonra terminalinizde şu komutu çalıştırarak sisteme kaydedin:

```bash
oto-debug kur <API_ANAHTARINIZ>
```
*(Bu işlem anahtarınızı bilgisayarınızda güvenli bir şekilde `~/.oto-debug-config.json` dosyasına kaydeder.)*

## 🚀 Kullanım

Çalıştırmak istediğiniz herhangi bir kodu veya komutu `oto-debug run` komutunun sonuna eklemeniz yeterlidir. 

Örneğin, hata fırlatan bir Python dosyanız varsa:

```bash
oto-debug run python script.py
```

### 💡 Nasıl Çalışır?

1. Komutunuz standart olarak çalıştırılır. Eğer bir hata yoksa, normal çıktıları görürsünüz.
2. Kodunuz çöküp bir hata (Exception/Traceback) fırlatırsa, `oto-debug` bu hatayı anında yakalar.
3. Hata çıktısı arka planda yapay zekaya gönderilir (terminalde şık bir bekleme animasyonu belirir).
4. Saniyeler içinde hatanın nedeni ve çözümünü içeren kod bloğu ekranınıza basılır.

## 👨‍💻 Geliştirici

**ahmtsalih**
Projeye katkıda bulunmak veya sorun bildirmek için GitHub reposunu ziyaret edebilirsiniz.

## 📝 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.