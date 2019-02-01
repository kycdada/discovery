‏‎vcrypt(1)‎‏ - أداة لتشفير وفك تشفير مقدار صغير من البيانات
===============================================================

## المختصر

الاستخدام:‏‎ vcrypt --decrypt|-d  --encrypt|-e  --genkey|-g [ OPTIONS ]

## الوصف

`vcrypt` يتم استخدامه بشكل أولي لتشفير كلمات السرية للاستخدام بواسطة Connector Framework.

### ملحوظة هامة بشأن طول المفتاح

بصفة مفترضة، يجب أن يقوم تجهيز Java Virtual Machine بدعم المفاتيح ‏‎128-bit /16-byte AES‎‏. اذا تم تركيب ‏‎Java Cryptographic Extensions‎‏ للنظام، فيمكنه استخدام المفاتيح ‏‎256-bit/32-byte AES‎‏. سيعرض أحد الخطاء ما اذا كان يتم ادخال مفتاح 32-بايت لكن لا يتم دعمه بواسطة JVM المستخدم لبدء تشغيل `vcrypt`.

## الأوامر

### --encrypt | -e OPTIONS INPUT
يقوم بتشفير البيانات التي تم ادخالها في ملف أو في مدخلات قياسية.

### --decrypt | -d OPTIONS INPUT
يقوم بفك تشفير البيانات التي تم ادخالها في ملف أو في مدخلات قياسية.

### --genkey | -g
يقوم بتكوين مفتاح تشفير مناسب للاستخدام مع `vcrypt` للمخرجات القياسية.

## الاختيارات

### --keyfile|-k PATH/TO/ID_VCRYPT
تحديد مسار الملف الذي يتضمن مفتاح ‏‎Base64-encoded‎‏، غالبا ما يتم تكوينه باستخدام الأمر ‏‎`--genkey|-g`‎‏.

## INPUT

### نمط التشفير

    $FILE_CONTAINING_CLEARTEXT | -- $CLEARTEXT

### نمط فك التشفير

    $FILE_CONTAINING_CRYPTED_TEXT | -- $CRYPTED_TEXT

## أمثلة

تكوين مفتاح وضعه في ملف ‏‎`id_vcrypt`‎‏:

    vcrypt --genkey > id_vcrypt

تشفير كلمة سرية من مدخلات قياسية الى مخرجات قياسية، مكتوب هنا
بواسطة اعادة التوجيه الى ‏‎`my_secret_data.txt`‎‏:

    ./vcrypt --encrypt --keyfile id_vcrypt -- "my secret password" > my_secret_data.txt

يمكنك أيضا ارسال المخرجات بواسطة مسار الاتصال أحادي الاتجاه الى `xclip`، أو `pbcopy`، أو ما شابه لوضع المخرجات في مسودة نظام التشغيل الخاص بك.

فك تشفير كلمة السرية من أحد الملفات:

    vcrypt --decrypt --keyfile id_vcrypt my_secret_data.txt

## خصائص ومتغيرات بيئة التشغيل

### `VCRYPT_OPTS` متغير بيئة التشغيل
يمكن استخدام متغير بيئة التشغيل لتمرير الاختيارات الى الأمر `java` المستخدم لبدء `vcrypt`.

### الخاصية ‏‎`vcrypt.key`‎‏
يمكن تمرير هذا كخاصية `-D` في `VCRYPT_OPTS` باستخدام مجموعة حروف ذات 16- أو 32-بايت ليتم استخدام مفتاح في سطر الأمر، بدلا من تمرير الاختيار ‏‎`--keyfile | -k keyfile`‎‏.

مثال على الاستخدام:

    VCRYPT_OPTIONS="-Dvcrypt.key='1234qwerasdfzxcv'" vcrypt --encrypt file_to_encrypt

### `VIV_VCRYPT_KEY` متغير بيئة التشغيل
`vcrypt` يسمح باستخدام متغير بيئة التشغيل لاعداد المفتاح. يجب أن يكون 16 أو 32 بايت.

## يمكنك الاطلاع أيضا على

‏‎crawler(1)‎‏

‏‎crawler.conf(5)‎‏

‏‎crawler-options.conf(5)‎‏

‏‎crawler-seed.conf(5)‎‏

‏‎orchestration_service.conf(5)‎‏
