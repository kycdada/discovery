# توصيف Data Crawler

`crawler` يتطلب ملف توصيف للاختيارات الخاصة به. تتوافر أمثلة على التوصيف في دليل `المشاركة` في دليل تركيب `crawler`. يمكن نسخ هذه الأمثلة وتعديلها. *لا تقوم بتعديل الأمثلة في مكانها.*

يتضمن الملف ‏‎`crawler.conf`‎‏ معلومات تقوم باخبار أداة البحث أي ملفات يتم استخدامها لعمليات بحث صفحات الانترنت الخاصة بها (موفق المدخلات)، ومكان ارسال ارسال مجموعة الملفات التي تم بحثها بمجرد اتمام عملية بحث صفحات الانترنت (موفق المخرجات)، واختيارات أخرى خاصة بادارة بحث صفحات الانترنت.

**ملحوظة**: كل مسارات الملفات تعد متعلقة بالدليل `config`، عدا الحالات المشار اليها.

الاختيار التي يمكن تحديدها في هذا الملف هي:

## موفق المدخلات
*  **الفئة** - الاستخدام الداخلي فقط، يقوم بتعريف فئة موفق مدخلات Data Crawler. القيمة المفترضة هي: ‏‎`com.ibm.watson.crawler.connectorframeworkinputadapter.Crawl`‎‏.
*  **التوصيف** - الاستخدام الداخلي فقط، يقوم بتعريف توصيف Connector Framework. مفتاح التوصيف المفترض الذي في هذه الكتلة والمستخدم للتمرير لموفق المدخلات الذي تم اختياره هو: ‏‎`connector_framework`‎‏. **ملحوظة** - يعد Connector framework هو ما يسمح لك بالتحدث الى البيانات الخاصة بك. قد تكون بيانات داخلية في المشروع، أو قد تكون بيانات خارجية على شبكة الانترنت أو في وحدة شارات التعليم المجمعة. تسمح الموصلات بالتوصل الى عدد من مصادر البيانات المختلفة، بينما يتم التحكم في الاتصال فعليا بواسطة عملية بحث صفحات الانترنت.
  -  **هام** - البيانات التي تم استرجاعها بواسطة Framework Input Adapter تم تسجيلها في الذاكرة الوسيطة محليا. ولا يتم تخزينها بشكل مشفر. بصفة مفترضة، يتم تسجيل البيانات في الذاكرة الوسيطة بدليل مؤقت يجب محوه عند اعادة التحميل الأولي، ويجب أن تكون قابلة للقراءة فقط بواسطة المستخدم الذي قام بتنفيذ أمر أداة البحث. هناك فرصة أن ينجو هذا الدليل من أداة البحث  اذا انتهى عمل connector framework قبل أن يتمكن من اعادة تنظيم نفسه. يمكنك الأخذ في الاعتبار بعناية مكان البيانات التي تم تسجيلها في الذاكرة الوسيطة الخاصة بك - يمكنك وضعها بنظام ملفات مشفر، لكن كن على حذر من الأثار المترتبة على الأداء من القيام بذلك. يمكنك أنت فقط أن تقرر التوازن المناسب بين السرعة والسرية فيما يتعلق بعمليات بحث صفحات الانترنت الخاصة بك.
*  **crawl_config_file** - هو ملف التوصيف المستخدم لبحث صفحات الانترنت. القيمة المفترضة هي: ‏‎`connectors/filesystem.conf`‎‏.
*  **crawl_seed_file** - هو ملف الخاص بأساس الترقيم الآلى المستخدم لبحث صفحات الانترنت. القيمة المفترضة هي: ‏‎`seeds/filesystem-seed.conf`‎‏.
*  **id_vcrypt_file** - هو ملف المفاتيح المستخدم لتشفير البيانات بواسطة أداة البحث؛ المفتاح المفترض الذي تم تضمينه مع أداة البحث هو ‏‎`id_vcrypt`‎‏.
يمكن استخدام البرنامج النصي vcrypt في حافظة `bin` اذا كنت بحاجة لتكوين ملف ‏‎id_vcrypt_file‎‏ جديد
*  **crawler_temp_dir** - هو حافظة Crawler المؤقتة الخاصة بسجلات الموصل. تم ادخال القيمة المفترضة، `tmp`. اذا لم تكن موجودة بالفعل، فسيتم تكوين الحافظة  `tmp` في دليل العمل الحالي.
*  **extra_jars_dir** - الاستخدام الداخلي فقط؛ حيث يتم اضافة المزيد من ملفات تخزين JAVA الى مسار فئة Connector Framework.
يجب أن تكون هذه القيمة `oakland` عند استخدام الموصل SharePoint، و `database` عند استخدام موصل قاعدة البيانات. يمكنك تركها خالية (على سبيل المثال، مجموعة حروف خالية "") عند استخدام موصلات أخرى.
  **ملحوظة**: وفقا لدليل connector framework ‏‎`lib/java`‎‏.
*  **urls_to_filter** - كشف سماح مفصول بسطر جديد لعناوين URL المراد بحثها، في نموذج التعبير معتاد. يقوم Data Crawler فقط ببحث صفحات الانترنت لعناوين URL التي تتوافق مع أحدى التعبيرات المعتادة التي تم ادخالها. يتضمن كشف النطاق أكثر النطاقات الشائعة ذات المستوى الرئيسي؛ ويمكن الاضافه اليه اذا لازم الأمر. يتضمن كشف نوع لاحقة الملف لاحقات الملفات التي تقوم Orchestration Service بدعمها، كهذا الاصدار من Data Crawler. تأكد من أنه تم السماح بنطاق عنوان URL أساس الترقيم الآلى الخاص بك بواسطة مرشح البيانات. على سبيل المثال، اذا كان أساس الترقيم الآلى يبدو وكأنه ‏‎`http://testdomain.test.in`‎‏، قم باضافة "`in`" الى مرشح بيانات النطاق. تأكد من أنه لن يتم استبعاد عنوان URL أساس الترقيم الآلى الخاص بك بواسطة مرشح البيانات، أو أن Crawler قد يصبح معلق.
*  **max_text_size** - الحد الأقصى للحجم، بالبايت، الخاص بالوثيقة قبل أن يتم كتابتها على قرص بواسطة Connector Framework. يؤدي ضبط ذلك بقيمة أعلى الى تخفيض كمية الوثائق التي يتم كتابتها الى القرص، ولكن سيؤدي الى زيادة متطلبات الذاكرة.
*  **extra_vm_params** - يسمح لك باضافة الكثير من معاملات Java الى الأمر المستخدم لبدء تشغيل Connector Framework.
*  **bootstrap_logging** - يقوم بكتابة سجل بدء تشغيل connector framework، وهو مفيد لتصحيح أخطاء المتقدم فقط. القيم هي `true` أو `false`. وسيتم كتابة ملف السجل الى ‏‎`crawler_temp_dir`‎‏.

## موفق مساحة التخزين

يسمح بتخزين الحالة الداخلية لأداة البحث بقاعدة بيانات. هذه المحددات ضرورية للاختيارات `restart` و `resume` الخاصة ببحث صفحات الانترنت لتعمل بشكل صحيح.

```javascript
storage_adapter {
 config = "storage_in_db"
  storage_in_db {
    include "storage/database_storage.conf"
  } 
}
```
الملف المشار اليه، ‏‎`storage/database_storage.conf`‎‏، بصفة مفترضة يقوم باستخدام قاعدة بيانات H2‎. يمكن استخدام أي قاعدة بيانات باستخدام مشغل JDBC، بدلا من المفترضات التي تم ادخالها. يرجع الى المطبوعات الفنية الخاصة بمشغل JDBC الخاص بك لايجاد معلومات معينة عن بعض هذه المحددات. يمكن تغيير الاختيارات المفترضة مباشرة بواسطة فتح ملف ‏‎`config/storage/database_storage.conf`‎‏، وتعديل القيم التالية الخاصة بحالة الاستخدام الخاص بك:
*  **class** - تشير هذه الفئة لفئة موفق قاعدة البيانات المراد استخدامه. القيمة المفترض هي ‏‎`com.ibm.watson.crawler.storageadapters.DatabasePersistAdapter`‎‏
*  **driver** - فئة مشغل JDBC. القيمة المفترض هي ‏‎`org.h2.Driver`‎‏ لاستخدام H2‎
*  **url** - ارجع الى اختيارات JDBC للحصول على برنامج المشغل الخاص بك. يعد هذا هو بادئة عنوان URL الخاص بمجموعة حروف وصلة JDBC. المفترض هو ‏‎`jdbc:h2:file:`‎‏
*  **database_location** - هو المكان الذي تريد به قاعدة البيانات الخاصة بك. يتم تطبيق هذا فقط على قواعد البيانات المبنية على أساس الملفات مثل sqlite و H2. القيمة المفترض هي ‏‎`./storage/database`‎‏
*  **database_name** - اسم قاعدة البيانات. القيمة المفترض هي ‏‎`ActivityDB`‎‏
*  **table_name** - اسم الجدول المراد استخدامه. القيمة المفترض هي ‏‎`Ledger`‎‏
*  **اسم المستخدم** - اسم المستخدم للاتصال بقاعدة البيانات
*  **كلمة السرية** - كلمة السرية للاتصال بقاعدة البيانات

يعد التوصيف المفترض كافي لمعظم الأنشطة.

## موفق المخرجات

هناك زوج من *موفقات المخرجات* الذي يمكنك الاختيار من بينهما. يمكنك تحديد موفق المخرجات بواسطة تحديد ‏‎`output_adapter.class`‎‏ في ‏‎`crawler.conf`‎‏. الاختيارات هي:

*  **class** - يقوم بتعريف فئة موفق المخرجات Data Crawler. القيمة المفترض هي ‏‎`com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter`‎‏
*  **config** - يقوم بتعريف مفتاح التوصيف للتمرير للموفق المخرجات. يجب أن تقوم مجموعة الحروف بمقابلة مفتاح في عنصر التوصيف هذا. في مثال الكود التالي:
```javascript
  orchestration_service {
    include "orchestration_service.conf"
  },
  test {
    output_directory = "/tmp/crawler-test-output"
  }
}
```
مفتاح التوصيف هو ‏‎`orchestration_service`‎‏. القيمة المفترضة هي `discovery_service`.يجب تحديد موفق مخرجات بواسطة تحديد معامل `class` الخاص به و المفتاح `config`.

* **موفق مخرجات Orchestration Service**: يقوم بتحميل الوثائق التي تم بحثها الى ‏‎Watson Developer Cloud's Orchestration Service‎‏. يمكنك تحديد هذا الموفق بواسطة تحديد المعامل `class` والمفتاح `config` كما يلي: 
```javascript
  class = "com.ibm.watson.crawler.orchestrationserviceoutputadapter.oneatatime.OrchestrationServiceOutputAdapter"
  config = "orchestration_service"
  orchestration_service {
    include "orchestration/orchestration_service.conf"
  }
```
* **موفق مخرجات Discovery Service**: يقوم بتحميل الوثائق التي تم بحثها الى ‏‎Watson Developer Cloud's Discovery Service‎‏. يمكنك تحديد هذا الموفق بواسطة تحديد المعامل `class` والمفتاح `config` كما يلي:
```javascript
  class = "com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter"
  config = "discovery_service"
  discovery_service {
    include "discovery/discovery_service.conf"
  }
```
* **موفق مخرجات Watson Test**: يقوم بكتابة تمثيل للملفات التي تم بحثها الى قرص في المكان المحدد. يمكنك
تحديد هذا الموفق بواسطة تحديد المعامل `class` والمفتاح `config` كما يلي:

**ملحوظة** - يقوم المعامل الاضافي، `output_directory`، بتحديد الدليل الذي يجب كتابة تمثيل البيانات التي تم بحثها اليه.
```javascript
  class = "com.ibm.watson.crawler.testoutputadapter.TestOutputAdapter"
  config = "test"
  output_directory = "/tmp/crawler-test-output"
```
* **retry** - يقوم بتحديد اختيارات اعادة المحاولة في حالة فشل محاولات الدفع الى موفق المخرجات.
  * max_attempts - الحد الأقصى لعدد مرات اعادة المحاولة. القيمة المفترض هي `10`
  * delay - الحد الأدنى للتأخير بين المحاولات، بالثانية. القيمة المفترض هي `2`
  * exponent_base - هو المعامل الذي يقوم بتحديد زيادة وقت التأخير بعد كل محاولة غير ناجحة. القيمة المفترض هي `2`

 المعادلة هي:
```
 d(nth_retry) = delay * (exponent_base ^ nth_retry)
```

 على سبيل المثال، المحددات ذات التأخير لمدة 1 ثانية و قاعدة أس بالقيمة 2، سيؤدي الى تأخير اعادة المحاولة الثانية - المحاولة الثالثة - لمدة 2 ثانية بدلا من 1، وتأخير التالية الى 4 ثانية.
 ```
 d(0) = 1 * (2 ^ 0) = 1 second
 d(1) = 1 * (2 ^ 1) = 2 seconds
 d(2) = 1 * (2 ^ 2) = 4 seconds
```
 وبالتالي، باستخدام المحددات المفترضة، سيتم محاولة الاحالة حتى 10 مرات، والانتظار تقريبا 1,022 ثانية ( أكثر بقليل من 17 دقيقة). يعد هذا الوقت تقريبا لأن هناك وقت اضافي يتم اضافته لتجنب حدوث تنفيذ عمليات اعادة احالة متعددة في نفس الوقت. يعد هذا الوقت "غير الدقيق" هو حتى 10%, لذا أخر اعادة محاولة في المثال السابق قد تتأخر حتى 4.4 ثانية. لا يتضمن وقت الانتظار الوقت المستغرق للاتصال بالخدمة، أو تحميل البيانات، أو انتظار الاستجابة.

 *تحذير:* قد يؤدي تخفيض وقت الانتظار بواسطة تخفيض أي من هذه القيم المفترضة الى عدم تحميل الوثائق بنجاح بواسطة موفق المخرجات الذي تم توصيفه. الدليل على ذلك عند استخدام خدمات Watson Developer Cloud سيكون هناك الرسائل RetryFailure في سجل الاقتباس "429 Too Many Requests" تقوم بتقييم الحد.
 
## اختيار تصحيح الأخطاء
*  **full_node_debugging** - يقوم بتفعيل نمط تصحيح الأخطاء؛ القيم المحتملة هي `true` أو `false`. **تحذير**: سيقوم بوضع البيانات الكاملة الخاصة بكل وثيقة تم بحثها في السجلات.
*  **heartbeat_wait_time** - الفترة الزمنية، بالملي ثانية، بين تسجيل احصائيات استيعاب وثيقة (نمط تصحيح الأخطاء فقط). القيمة المفترضة هي 1000 ملي ثانية.

## اختيارات التسجيل
*  **configuration_file** - ملف التوصيف ليتم استخدامه للتسجيل. في ملف النموذج ‏‎`crawler.conf`‎‏، تم تعريف هذا الاختيار في ‏‎`logging.log4j`‎‏ والقيمة المفترضة الخاصة به هي ‏‎`log4j_custom.properties`‎‏.
يجب تعريف هذا الاختيار بطريقة مماثلة سواء باستخدام ملف ‏‎`.properties`‎‏ أو ‏‎`.conf`‎‏.

## اختيارات اضافية لادارة بحث صفحات الانترنت
*  **shutdown_timeout** - يقوم بتحديد قيمة انتهاء الوقت، بالدقائق، قبل اغلاق التطبيق. القيمة المفترض هي `10`.
*  **output_limit** - هو أعلى عدد من البنود المفهرسة التي سيحاول Crawler ارساله في نفس الوقت الى موفق المخرجات. قد يتم حد هذا بشكل أكبر بواسطة عدد الأجزاء المركزية المتاحة للقيام بالعمل. وفي أية نقطة محددة لن يكون هناك أكثر من "x" بند قابل للفهرسة يتم ارساله الى موفق المخرجات وينتظر رجوعه. القيمة المفترض هي `10`. 
*  **input_limit** - يقوم بحد عدد عناوين URL التي يمكن طلبها من الموصل في نفس الوقت.القيمة المفترض هي `3`.
*  **output_timeout** هو مقدار الوقت، بالثانية، قبل تخلي Data Crawler عن ارسال طلب الى موفق المخرجات، ثم ازالة البند من صف موفق المخرجات، للسماح بالمزيد من عمليات التشغيل. القيمة المفترض هي `1200`.MD:STRONG>ملحوظة** - يجب الاهتمام بالقيود التي يتم فرضها بواسطة موفق المخرجات، حيث قد تتعلق تلك القيود بالحدود التي يتم تعريفها هنا. `output_limit` الذي تم تعريفه بأعلى يتعلق فقط بعدد العناصر القابلة للفهرسة التي يمكن ارسالها الى موفق المخرجات فورا. بمجرد ارسال عنصر قابل للفهرسة الى موفق المخرجات، يبدأ "العد الزمني،" كما هو معرف بواسطة المتغير `output_timeout`. من الممكن أن يتوافر لموفق المخرجات نفسه خاصية تضيق الاختيارات مما يمنعه من القدرة على تشغيل نفس عدد المدخلات الذي يقوم باستلامه. على سبيل المثال، قد يتوافر لموفق مخرجات التنسيق مستودع وصلات، قابل للتوصيف لاتصالات HTTP بالخدمة. اذا كان المفترض 8، على سبيل المثال، واذا تم اعداد `output_limit` ليكون رقم أكبر من 8، فسيتوافر لديك عمليات، على مدار الساعة، في انتظار دورها ليتم تنفيذها. ويمكنك مواجهة حالات انتهاء الوقت.
*  **num_threads** - عدد سلاسل العمليات المتوازية التي ي مكن تشغيلها في وقت واحد. يمكن أن تكون هذه القيمة اما رقم صحيح، وهي التي تقوم بتحديد عدد سلاسل العمليات المتوازية مباشرة، أو أن تكون مجموعة حروف، بالنسق "xNUM"، مما يحدد عامل الضرب لعدد وحدات التشغيل المتاحة، على سبيل المثال، ‏‎"x1.5"‎‏. القيم المفترضة هي `"30"`.

## يمكنك الاطلاع أيضا على

‏‎crawler(1)‎‏

‏‎vcrypt(1)‎‏

‏‎crawler-options.conf(5)‎‏

‏‎crawler-seed.conf(5)‎‏

‏‎orchestration_service.conf(5)‎‏