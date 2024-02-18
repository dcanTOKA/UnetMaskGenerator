# UnetMaskGenerator'a Hoşgeldiniz

Bu araç, verilen anotasyonlar ve görseller üzerinden maskeleme işlemi yapmak için tasarlanmıştır. Aşağıdaki adımları takip ederek maskeleme işlemini başlatabilirsiniz.

## Gerekli Paketlerin Yüklenmesi

Gerekli paketlerin yüklenmesi için aşağıdaki komutu çalıştırın

```bash
pip install -r requirements.txt
```

## Adım 1: Dosyaların Hazırlanması

Lütfen anotasyon dosyanızı ve mask oluşturulacak görsellerinizi zip formatında `/data` klasörüne yerleştiriniz.

**Not:** Anotasyon dosyanızın formatı YOLO çıktısı formatında olmalıdır.

## Adım 2: Maskeleme İşleminin Başlatılması

Maskeleme işlemine başlamak için aşağıdaki komutu terminalinizde çalıştırınız. Bu komut, belirttiğiniz dosyaları kullanarak maskeleme işlemini gerçekleştirecek ve sonuçları `/masks` klasörüne kaydedecektir.

```bash
python main.py --zip_path="./data/FILE_NAME_WITH_ZIP_EXT" --images_zip_path="./data/FILE_NAME_WITH_ZIP_EXT" --output_dir="./masks/"
```

# Welcome to UnetMaskGenerator

This tool is designed to perform masking operations on given annotations and images. Follow the steps below to start the masking process.

## Install the necessary packages by using the command below

```bash
pip install -r requirements.txt
```

## Step 1: Preparing Your Files

Please place your annotation file and the images to be masked in zip format in the `/data` folder.

**Note:** The format of your annotation file should be in YOLO output format.

## Step 2: Starting the Masking Process

To start the masking process, run the following command in your terminal. This command will use the specified files to perform the masking operation and save the results in the `/masks` folder.

```bash
python main.py --zip_path="./data/FILE_NAME_WITH_ZIP_EXT" --images_zip_path="./data/FILE_NAME_WITH_ZIP_EXT" --output_dir="./masks/"
```
