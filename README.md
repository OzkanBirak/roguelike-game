# Roguelike Game

Bu proje, Python ve Pygame Zero kullanarak geliştirilen basit bir roguelike oyundur. Oyunda kahraman karakterini kontrol ederek düşmanlardan kaçmalı ve hayatta kalmalısınız.

## Özellikler
- **Roguelike Mekanikleri:** Kahraman ve düşmanlar belirli alanlarda hareket eder.
- **Sprite Animasyonları:** Hem kahraman hem de düşmanlar için hareket ve bekleme animasyonları bulunur.
- **Ses Efektleri ve Müzik:** Karakterin hareketleri ve saldırıları sırasında ses efektleri çalınır.
- **Ana Menü:** Oyunu başlatma, sesleri açma/kapatma ve çıkış seçenekleri bulunur.

## Kurulum
Bu oyunu çalıştırmak için Python'un kurulu olması gerekmektedir. Aşağıdaki adımları takip ederek oyunu çalıştırabilirsiniz:

```sh
# Python'ı ve pip'i güncelleyin
python -m ensurepip --default-pip
python -m pip install --upgrade pip

# Gerekli bağımlılığı yükleyin
pip install pgzero

# Oyunu başlatın
python game.py
```

## Oynanış
- **Yön Tuşları:** Kahramanı hareket ettirir.
- **Ana Menü:** Başlangıçta seçim yapmak için 1, 2 ve 3 tuşları kullanılır.
- **Düşmanlardan Kaçın:** Düşmanlar belirli bölgelerde hareket eder ve çarpışmalardan kaçınmanız gerekir.