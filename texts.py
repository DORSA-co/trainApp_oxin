from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout as sQHBoxLayout

ERRORS = {

    'data_not_ready': {'fa': ' تصویری انتخاب نشده است',
                'en': ' Data Isnot Selected '},

    'ERROR': {'fa': ' خطا: ',
                'en': ' ERROR: '},
    'invalid_name': {'fa': ' نام پایپ لاین صحیح نمیباشد ',
                'en': ' Invalid Name '},

    'repeat_name': {'fa': ' نام پایپ لاین تکراری میباشد',
                'en': ' Name Already in Use '},

    'empty_name': {'fa': ' نام پایپ لاین نباید خالی باشد ',
                'en': ' Name can not Empty'},
    'BUILD_BINARYLIST_SLIDER_ERROR': {'fa': ' خطای ساخت اسلایدر تصاویر ',
                                      'en': ' Error while building slider(s) '},

    'READ_BINARYLIST_PARAMS_ERROR': {'fa': ' خطای دریافت اطلاعات دیتاست ',
                                     'en': ' Error while reading dataset parameters '},

    'READ_BINARYLIST_FOLDERS_ERROR': {'fa': ' خطای خواندن فولدر تصاویر معیوب/سالم ',
                                      'en': ' Error while reading defect/perfect folders '},

    'READ_BINARYLIST_IMAGES_ERROR': {'fa': ' خطای دریافت تصاویر معیوب/سالم ',
                                     'en': ' Error while reading defect/perfect images '},

    'MAXIMIZE_IMAGE_ERROR': {'fa': ' خطای نمایش تصویر ',
                             'en': ' Error while opening image '},

    'EPOCH_RANGE_INCORRECT': {'fa': ' بازه وارد شده برای اپوک صحیح نیست ',
                              'en': ' Epoch range is not correct '},

    'EPOCH_FORMAT_INVALID': {'fa': ' فرمت واردشده برای اپوک نامعتبر است ',
                             'en': ' Epoch format invalid '},

    'TEPOCH_RANGE_INCORRECT': {'fa': ' بازه وارد شده برای تیونینگ اپوک صحیح نیست ',
                               'en': ' Tuning epoch range is not correct '},

    'TEPOCH_FORMAT_INVALID': {'fa': ' فرمت واردشده برای تیونینگ اپوک نامعتبر است ',
                              'en': ' Tuning epoch format invalid '},

    'BATCHSIZE_RANGE_INCORRECT': {'fa': ' بازه وارد شده برای سایز بچ صحیح نیست ',
                                  'en': ' Batch-size range is not correct '},

    'BATCHSIZE_FORMAT_INVALID': {'fa': ' فرمت واردشده برای سایز بچ نامعتبر است ',
                                 'en': ' Batch-size format invalid '},

    'SPLITRATIO_RANGE_INCORRECT': {'fa': ' بازه وارد شده برای نسبت اسپلیت صحیح نیست ',
                                   'en': ' Split-ratio range is not correct '},

    'SPLITRATIO_FORMAT_INVALID': {'fa': ' فرمت واردشده برای نسبت اسپلیت نامعتبر است ',
                                  'en': ' Split-ratio format invalid '},

    'LOSS_RANGE_INCORRECT': {'fa': ' بازه وارد شده برای خطا صحیح نیست ',
                             'en': ' Loss range is not correct '},

    'LOSS_FORMAT_INVALID': {'fa': ' فرمت واردشده برای خطا نامعتبر است ',
                            'en': ' Loss format invalid '},

    'ACCU_RANGE_INCORRECT': {'fa': ' بازه وارد شده برای دقت صحیح نیست ',
                             'en': ' Accuracy range is not correct '},

    'ACCU_FORMAT_INVALID': {'fa': ' فرمت واردشده برای دقت نامعتبر است ',
                            'en': ' Accuracy format invalid '},

    'PREC_RANGE_INCORRECT': {'fa': ' بازه وارد شده برای پرسیژن صحیح نیست ',
                             'en': ' Precision range is not correct '},

    'PREC_FORMAT_INVALID': {'fa': ' فرمت واردشده برای پرسیژن نامعتبر است ',
                            'en': ' Precision format invalid '},

    'RECA_RANGE_INCORRECT': {'fa': ' بازه وارد شده برای ریکال صحیح نیست ',
                             'en': ' Recall range is not correct '},

    'RECA_FORMAT_INVALID': {'fa': ' فرمت وارد شده برای ریکال نامعتبر است ',
                            'en': ' Recall format invalid '},

    'IOU_RANGE_INCORRECT': {'fa': ' بازه‌ی وارد شده برای IOU صحیح نیست ',
                             'en': ' IOU range is not correct '},

    'IOU_FORMAT_INVALID': {'fa': ' فرمت وارد شده برای IOU نامعتبر است ',
                            'en': ' IOU format invalid '},

    'FSCORE_RANGE_INCORRECT': {'fa': ' بازه‌ی وارد شده برای FScore صحیح نیست ',
                             'en': ' FScore range is not correct '},

    'FSCORE_FORMAT_INVALID': {'fa': ' فرمت وارد شده برای FScore نامعتبر است ',
                            'en': ' FScore format invalid '},

    'YEAR_RANGE_INCORRECT': {'fa': ' مقدار وارد شده برای سال خارج از بازه است ',
                             'en': ' Start/end year not in range '},

    'YEAR_FORMAT_INVALID': {'fa': ' فرمت واردشده برای سال نامعتبر است و یا فیلدها خالی هستند ',
                            'en': ' Year format invalid/fields empty, Please check format of fill both fields '},

    'MONTH_RANGE_INCORRECT': {'fa': ' مقدار وارد شده برای ماه خارج از بازه است ',
                              'en': ' Start/end month not in range '},

    'MONTH_FORMAT_INVALID': {'fa': ' فرمت واردشده برای ماه نامعتبر است و یا فیلدها خالی هستند ',
                             'en': ' Month format invalid/fields empty, Please check format of fill both fields '},

    'DAY_RANGE_INCORRECT': {'fa': ' مقدار وارد شده برای روز خارج از بازه است ',
                            'en': ' Start/end day not in range '},

    'DAY_FORMAT_INVALID': {'fa': ' فرمت واردشده برای روز نامعتبر است و یا فیلدها خالی هستند ',
                           'en': ' Day format invalid/fields empty, Please check format of fill both fields '},

    'DATE_RANGE_INCORRECT': {'fa': ' بازه وارد شده برای تاریخ صحیح نیست ',
                             'en': ' Date range is not correct '},

    'database_load_defects_failed': {'fa': 'خطای دریافت لیست عیوب از دیتابیس',
                 'en': 'Failed to load defects from database'},

    'annotation_not_exist': {'fa': 'فایل انوتیشن وجود نداشته و یا قابل بارگزاری نیست',
                 'en': 'Annotation file doesnt exist or can not be loaded'},

    'load_masks_from_json_failed': {'fa': 'خطای بارگزاری ماسک عیوب از فایل انوتیشن',
                 'en': 'Failed to laod masks from annotation file'},

    'mask_overlay_to_image_failed': {'fa': 'خطای اعمال ماسک انوتیشن به تصویر اصلی',
                 'en': 'Failed to apply annotation mask overlay on image'},

    'set_image_to_slider_failed': {'fa': 'خطای نمایش تصاویر در اسلایدر',
                 'en': 'Failed to set images on slider'},

    'database_conection_failed': {'fa': 'خطای اتصال به دیتابیس',
                 'en': 'Database connection error'},

    'database_get_bmodels_failed': {'fa': 'خطای دریافت لیست مدل های باینری از دیتابیس',
                 'en': 'Failed to get binary models list from database'},

    'database_get_lmodels_failed': {'fa': 'خطای دریافت لیست مدل های جایابی از دیتابیس',
                 'en': 'Failed to get Localization models list from database'},

    'database_get_classmodels_failed': {'fa': 'خطای دریافت لیست مدل های دسته بندی از دیتابیس',
                 'en': 'Failed to get classification models list from database'},

    'database_get_datasets_failed': {'fa': 'خطای دریافت لیست دیتاست ها از دیتابیس',
                 'en': 'Failed to get datasets list from database'},

    'database_get_defects_failed': {'fa': 'خطای دریافت لیست عیوب از دیتابیس',
                 'en': 'Failed to get defects list from database'},

    'database_get_defect_groups_failed': {'fa': 'خطای دریافت لیست گروه عیوب از دیتابیس',
                 'en': 'Failed to get defect groups list from database'},

    'show_bmodels_failed': {'fa': 'خطای نمایش جدول مدل های باینری',
                 'en': 'Failed to show binary models on UI'},

    'show_datasets_on_ui_failed': {'fa': 'خطای نمایش جدول دیتاست ها',
                 'en': 'Failed to show datasets on UI'},

    'show_defefcts_on_ui_failed': {'fa': 'خطای نمایش جدول عیوب',
                 'en': 'Failed to show defects on UI'},

    'show_clsmodels_on_ui_failed': {'fa': 'خطای نمایش جدول مدل های دسته بندی',
                 'en': 'Failed to show classification models on UI'},

    'ui_get_bmodel_filter_params_failed': {'fa': 'خطای دریافت پارامترهای فیلتر مدل های باینری',
                 'en': 'Failed to get binary model filter params from UI'},

    'ui_get_lmodel_filter_params_failed': {'fa': 'خطای دریافت پارامترهای فیلتر مدل های جایابی',
                 'en': 'Failed to get localization model filter params from UI'},

    'update_binarylist_piechart_failed': {'fa': 'خطای آپدیت پای چارت صفحه دیتاست باینری',
                 'en': 'Failed to update binarylist piechart'},

    'update_classlist_piechart_failed': {'fa': 'خطای آپدیت پای چارت صفحه دیتاست دسته بندی',
                 'en': 'Failed to update classificationlist piechart'},

    'get_images_related_to_defect_failed': {'fa': 'خطای دریافت تصاویر مربوط به عیب',
                 'en': 'Failed to get images related to defect'},

    'get_binary_count_failed': {'fa': 'خطای دریافت تعداد تصاویر عیب و بدون عیب',
                 'en': 'Failed to get count of defect/perfect images'},

    'ui_get_clsmodel_filter_params_failed': {'fa': 'خطای دریافت پارامترهای فیلتر/جستج. برای جدول مدل های دسته بندی',
                 'en': 'Failed to get classification models filtering parameters from UI'},

    'database_get_filtered_cls_models_failed': {'fa': 'خطای دریافت لیست مدل های دسته بندی فیلترشده از دیتابیس',
                 'en': 'Failed to get filtered classification models list from database'},

    'piechart_create_failed': {'fa': 'خطای ایجاد پای چارت های موردنیاز',
                 'en': 'Failed to create needed piecharts on UI'},

    'database_add_bmodel_failed': {'fa': 'خطا در اضافه نمودن اطلاعات مدل باینری جدید در دیتابیس',
                 'en': 'Failed to add new binary model info to database'},

    'database_add_lmodel_failed': {'fa': 'خطا در اضافه نمودن اطلاعات مدل جایابی جدید در دیتابیس',
                 'en': 'Failed to add new localization model info to database'},

    'initialize_notif_ui_failed': {'fa': 'خطای ساخت کلاس اعلانات',
                 'en': 'Failed to initialize notification object.'},

    'notif_obj_clear_files_failed': {'fa': 'خطای پاکسازی فولدر اعلانات',
                 'en': 'Failed clear notification files in directory.'},

    'notif_obj_append_file_failed': {'fa': 'خطای ایجاد فایل اعلان جدید',
                 'en': 'Failed to create new notification file in directory.'},
    
    'notif_obj_pop_file_failed': {'fa': 'خطای حذف فایل اعلان یا نمایش اعلان',
                 'en': 'Failed to remove notification file/create notification.'},

    'error_notif': {'fa':'خطا',
            'en':'Error'},


    'plc_connection_apply_failed': {'fa': 'خطای اتصال به پی ال سی',
                'en': 'Failed to connect to PLC'},

    'database_set_plc_ip_failed': {'fa': 'خطای ذخیره آی پی در دیتابیس',
                'en': 'Failed to update PLC ip on database'},

    'database_get_plc_ip_failed': {'fa': 'خطای دریافت آی پی در دیتابیس',
                'en': 'Failed to get PLC ip on database'},

    'plc_disconnected_failed': {'fa': 'خطای قطع اتصال پی ال سی',
                'en': 'Failed to disconnect from PLC'},

    'plc_disconnected_by_error': {'fa': 'ارتباط با پی ال سی بصورت ناگهانی قطع شده است',
                'en': 'PLC is disconnected by erorr'},

    'plc_path_error': {'fa': 'خطای خواندن آدرس در پی ال سی',
                'en': 'Failed to read path from PLC'},

    'plc_write_json_failed': {'fa': 'خطای ثبت اطلاعات پی ال سی در فایل',
                'en': 'Failed to write PLC params to json file'},

    'plc_set_value_failed': {'fa': 'خطای آپدیت مقدار متغیر در پی ال سی',
                'en': 'Failed to set vaule on PLC'},

    'database_update_plc_params_failed': {'fa': 'خطای آپدیت پارامترهای پی ال سی در دیتابیس',
                'en': 'Failed to update PLC params on database'},

    'database_get_plc_params_failed': {'fa': 'خطای دریافت پارامترهای پی ال سی از دیتابیس',
                'en': 'Failed to get PLC params from database'},

    'UPDATE_BCHART_FAILED': {'fa': ' اپوک {}: .خطا در به روز رسانی نمودارهای آموزش باینری ',
                             'en': ' Epoch {}: Error while updating binary train charts. '},

    'UPDATE_LCHART_FAILED': {'fa': ' اپوک {}: .خطا در به روز رسانی نمودارهای آموزش جایابی ',
                             'en': ' Epoch {}: Error while updating localization train charts. '},
                    
    'SAVE_BMODEL_EPOCH_FAILED': {'fa': ' اپوک {}: .خطا در ذخیره سازی وزن های مدل آموزش باینری ',
                            'en': ' Epoch {}: Error while saving binary train model weightss. '},
                    
    'SAVE_LMODEL_EPOCH_FAILED': {'fa': ' اپوک {}: .خطا در ذخیره سازی وزن های مدل آموزش جایابی ',
                            'en': ' Epoch {}: Error while saving localization train model weightss. '},
                    
    'SAVE_BMODEL_FAILED': {'fa': ' خطا در ذخیره سازی وزن های مدل آموزش باینری. ',
                            'en': ' Error while saving binary train model weights. '},
                    
    'SAVE_LMODEL_FAILED': {'fa': ' خطا در ذخیره سازی وزن های مدل آموزش جایابی. ',
                            'en': ' Error while saving localization train model weights. '},
                    
    'SAVE_FTBMODEL_FAILED': {'fa': ' خطا در ذخیره سازی وزن های مدل آموزش باینری تنظیم دقیق.',
                            'en': ' Error while saving binary train fine tune model weights. '},
 
    'CREATE_BWPATH_FAILED': {'fa': ' خطا در ایجاد آدرس وزن های مدل آموزش باینری. ',
                            'en': ' Error while creating binary weights path. '},
 
    'SET_PROCESSOR_FAILED': {'fa': ' خطا در تنظیم پردازنده‌ی آموزش. ',
                            'en': ' Error while setting train processor. '},
 
    'CREATE_LWPATH_FAILED': {'fa': ' خطا در ایجاد آدرس وزن های مدل آموزش جایابی. ',
                            'en': ' Error while creating localization weights path. '},
 
    'CREATE_BINARY_GEN_FAILED': {'fa': ' خطا در آماده سازی داده ی آموزش باینری. ',
                            'en': ' Error preparing binary training data '},
 
    'CREATE_LOC_GEN_FAILED': {'fa': ' خطا در آماده سازی داده ی آموزش جایابی. ',
                            'en': ' Error preparing localization training data '},

    'PREPARE_DATA_FAILED': {'fa': ' خطا در آماده سازی داده ها برای آموزش. ',
                            'en': ' Error while preparing data for training. '},

    'CREATE_MODEL_FAILED': {'fa': ' خطا در ایجاد مدل برای الگوریتم {}. ',
                            'en': ' Error while creating model for {} algorithm. '},
                    
    'CALLBACK_CREATE_FAILED': {'fa': ' خطا در ایجاد شی CallBack ',
                    'en': ' Error while creating Callback object. '},

    'CREATE_FTMODEL_FAILED': {'fa': ' خطا در ایجاد مدل تنظیم دقیق برای الگوریتم {}. ',
                            'en': ' Error while creating fine tune model for {} algorithm. '},

    'FIT_MODEL_FAILED': {'fa': ' خطا در آموزش مدل. ',
                            'en': ' Error while model training. '},

    'FIT_FTMODEL_FAILED': {'fa': ' خطا در آموزش مدل تنظیم دقیق. ',
                            'en': ' Error while fine tune model training. '}, 

    'dataset_splitted_failed': {'fa': '(ها)خطا در تقسیم مجموعه داده.',
                        'en': 'Error while splitting Dataset(s)'}, 

    'path_not_exist': {'fa': ' پوشه ی تصاویر وجود ندارد. ',
                        'en': 'The images folder does not exist'},

    'sheet_not_exist': {'fa': 'فایل‌های مربوط به ورق با شناسه‌ی {} وجود ندارد.',
                        'en': 'The files related to sheet with ID {} not exists.'},

    'open_folder_failed': {'fa': ' خطا در باز کردن پوشه ی تصاویر. ',
                        'en': ' Error while openning images folder '},

    'refresh_failed': {'fa': ' خطا در به روز رسانی ',
                        'en': ' Error while refreshing '},

    'pipline_eror': {'fa': ' خطا در مدل یا دیتابیس ',
                        'en': ' Model/Dataset Eror '},

    'CREATE_DATASET_FAILED': {'fa': ' خطا در ایجاد مجموعه داده ',
                       'en': ' Error while creating dataset '},
                               
    'SET_DATASET_FAILED': {'fa': ' خطا در تنظیم مجموعه داده ی پیش فرض ',
                    'en': ' Error while setting default dataset '},
                               
    'REMOVE_PIP_FAILED': {'fa': ' خطا در حذف پایپ لاین ',
                    'en': ' Error while removing pipeline '},

    'Camera_serial_error': {'fa': ' شماره سریال دوربین {} در دسترس نیست ',
                        'en': ' Serial number of camera {} is not availabla '},

    'disconnect_error': {'fa': ' خطا در قطع اتصال دوربین {} ',
                'en': ' Disconnectiong Error for camera {} '},

    'no_connect': {'fa': ' اتصالی برای دوربین {} برقرار نمیباشد ',
                'en': ' There is no connection for camera {} '},

    'control_config_error': {'fa': ' دوربین {} توسط برنامه دیگری کنترل می شود یا خطای پیکربندی ',
                'en': ' Camera {} controlled by another application Or config error '},

    'date_empty': {'fa': 'فیلد تاریخ خالی است.',
                'en': ' There is no connection for camera {} '},

    'creator_user_name_empty': {'fa': 'فیلد نام کاربری سازنده خالی است.',
                'en': ' There is no connection for camera {} '},
                
    'dataset_name_empty': {'fa': 'فیلد نام مجموعه داده خالی است.',
                'en': ' There is no connection for camera {} '},

    'location_empty': {'fa': 'فیلد مسیر خالی است.',
                'en': ' There is no connection for camera {} '},

    'low_data': {'fa': 'داده‌های آموزشی کمتر از تعداد مورد نیاز است.',
        'en': 'Training data is less than required'},
}

WARNINGS = {
    
    'WARNING': {'fa': ' هشدار: ',
                'en': ' Warning: '},
    'Create_pipline': {'fa': ' آیا از ساخت پایپ لاین جدید مطمئن هستید ؟ نام (',
                'en': ' Are you sure want to create new Pilpline?  (Name : '},


    'Remove_pipline': {'fa': ' آیا از حذف پایپ لاین مطمئن هستید ؟ نام (',
                'en': ' Are you sure want to Remove Pilpline?  (Name : '},

    'details_pipline': {'fa': ' برای نمایش جزئیات پایپ لاین انتخاب شده به نرم افزار اپراتور مراجعه فرمایید',
                'en': ' For More Details of Pipline you should Use Operator Software '},

    'NO_CHOOSEN_IMG': {'fa': ' تصویری انتخاب نشده است ',
                       'en': ' No image selected '},

    'NO_SHEET': {'fa': ' ورقی بارگذاری نشده است ',
                 'en': ' No sheet loaded '},

    'IMAGE_STATUS': {'fa': ' وضعیت عیب تصویر مشخص نشده است ',
                     'en': ' defect status is not specified '},

    'IMAGE_STATUS_Format': {'fa': ' وضعیت عیب تصویر {} مشخص نشده است ',
                     'en': ' defect status of image {} is not specified '},

    'NO_IMAGE_LOADED': {'fa': ' تصویری بارگذاری نشده است ',
                        'en': ' No image loaded '},

    'ALREADY_SAVED': {'fa': ' تصویر قبلا ذخیره شده است ',
                      'en': ' Image already saved '},

    'question': {'fa': ' سوال ',
                            'en': ' Question '},

    'ALREADY_SAVED_DEFECT':{
            'fa': ' تصویر قبلا به عنوان معیوب ذخیره شده است. آیا مطمئنید که می‌خواهید آن را به عنوان سالم ذخیره کنید؟ ',
            'en': 'The image has already been saved as defective. Are you sure you want to save it as healthy?'},

    'ALREADY_SAVED_DEFECT_Format':{
            'fa': ' تصویر {} قبلا به عنوان معیوب ذخیره شده است. آیا مطمئنید که می‌خواهید آن را به عنوان سالم ذخیره کنید؟ ',
            'en': 'The image {} has already been saved as defective. Are you sure you want to save it as healthy?'},

    'ALREADY_SAVED_PERFECT': {
        'fa': ' تصویر قبلا به عنوان سالم ذخیره شده است. آیا مطمئنید که می‌خواهید آن را به عنوان معیوب ذخیره کنید؟ ',
        'en': 'The image has already been saved as healthy. Are you sure you want to save it as defective?'},

    'ALREADY_SAVED_PERFECT_Format': {
        'fa': ' تصویر {} قبلا به عنوان سالم ذخیره شده است. آیا مطمئنید که می‌خواهید آن را به عنوان معیوب ذخیره کنید؟ ',
        'en': 'The image {} has already been saved as healthy. Are you sure you want to save it as defective?'},

    'INVALID_DATASET': {'fa': ' آدرس مجموعه داده معتبر نیست ',
                        'en': ' Dataset address is invalid '},

    'DATASET_FORMAT': {'fa': ' قالب مجموعه داده صحیح نیست ',
                       'en': ' Dataset format is incorrect '},

    'IMAGE_SAVE_SUCCESSFULLY': {'fa': 'تصویر با موفقیت ذخیره شد',
                                'en': 'Image saved successfully'},

    'IMAGES_SAVE_SUCCESSFULLY': {'fa': 'تصاویر با موفقیت ذخیره شدند',
                                'en': 'Images saved successfully'},

    'DATASET_NUMBER': {'fa': ' شماره ی مجموعه داده خارج از محدوده است ',
                       'en': ' Dataset number is out of range '},

    'DATASET_EXIST': {'fa': ' آدرس وارد شده وجود دارد ',
                      'en': ' Address already exist '},

    'CONFIRM_LOGOUT': {'fa': ' آیا مطمئن هستید که خارج میشوید؟ ',
                       'en': ' Are you sure want to logout ? '},

    'Cmamera_successful': {'fa': ' دوربین متصل شد',
                           'en': ' Cmamera Connection successfuly '},

    'Cmamera_serial_eror': {'fa': ' شماره سریال متصل نیست',
                            'en': ' This camera Serial Not Connect '},

    'disconnect_eror': {'fa': ' خطا در قطع اتصال',
                        'en': ' Disconnectiong Eror '},

    'no_connect': {'fa': ' اتصالی برقرار نمیباشد',
                   'en': ' There is no connection '},

    'DATASET_NOT_SELECTED': {'fa': ' دیتاست انتخاب نشده است ',
                             'en': ' No dataset selected '},

    'CONFIRM_LOGOUT': {'fa': ' آیا مطمئن هستید که خارج میشوید؟ ',
                       'en': ' Are you sure want to logout ? '},

    'LOGIN_FIRST': {'fa': ' شما وارد حساب کاربری نشده اید ',
                    'en': ' You are not logged in '},

    'CREATE_DATABASE': {'fa': ' آیا از ایجاد دیتابیس جدید مطمئن هستید ؟ ',
                        'en': ' Are you sure want to create new database ? '},

    'EPOCH_RANGE_EMPTY': {'fa': ' لطفا هر دو فیلد مربوط به اپوک‌ها را مقدار دهید یا هر دو را خالی بگذارید ',
                          'en': ' Epoch range fields can not be empty, Please fill both them or leave them empty '},

    'TEPOCH_RANGE_EMPTY': {'fa': ' لطفا هر دو فیلد مربوط به اپوک‌های تنظیم را مقدار دهید یا هر دو را خالی بگذارید ',
                           'en': ' Tuning epoch range fields can not be empty, Please fill both them or leave them empty '},

    'BATCHSIZE_RANGE_EMPTY': {'fa': ' لطفا هر دو فیلد مربوط به اندازه‌ی دسته را مقدار دهید یا هر دو را خالی بگذارید ',
                              'en': ' Batch-size range fields can not be empty, Please fill both them or leave them empty '},

    'SPLITRATIO_RANGE_EMPTY': {'fa': ' لطفا هر دو فیلد مربوط به اندازه‌ی قطعه را مقدار دهید یا هر دو را خالی بگذارید ',
                               'en': ' Split-ratio range fields can not be empty, Please fill both them or leave them empty '},

    'LOSS_RANGE_EMPTY': {'fa': ' لطفا هر دو فیلد مربوط به خطا را مقدار دهید یا هر دو را خالی بگذارید ',
                         'en': ' Loss range fields can not be empty, Please fill both them or leave them empty '},

    'ACCU_RANGE_EMPTY': {'fa': ' لطفا هر دو فیلد مربوط به دقت را مقدار دهید یا هر دو را خالی بگذارید ',
                         'en': ' Accuracy range fields can not be empty, Please fill both them or leave them empty '},

    'PREC_RANGE_EMPTY': {'fa': ' لطفا هر دو فیلد مربوط به پرسیژن را مقدار دهید یا هر دو را خالی بگذارید ',
                         'en': ' Precision range fields can not be empty, Please fill both them or leave them empty '},

    'RECA_RANGE_EMPTY': {'fa': ' لطفا هر دو فیلد مربوط به ریکال را مقدار دهید یا هر دو را خالی بگذارید ',
                         'en': ' Recall range fields can not be empty, Please fill both them or leave them empty '},

    'IOU_RANGE_EMPTY': {'fa': ' لطفا هر دو فیلد مربوط به IOU را مقدار دهید یا هر دو را خالی بگذارید ',
                         'en': ' IOU range fields can not be empty, Please fill both them or leave them empty '},

    'FSCORE_RANGE_EMPTY': {'fa': ' لطفا هر دو فیلد مربوط به FScore را مقدار دهید یا هر دو را خالی بگذارید ',
                         'en': ' FScore range fields can not be empty, Please fill both them or leave them empty '},

    'SELECT_MORE_THAN_ONE_DEFECT_CLASS': {'fa': ' امکان انتخاب چند کلاس عیب به صورت همزمان وجود ندارد ',
                                          'en': ' can not select more than one defect class at same time '},

    'SELECT_NO_DEFECT_CLASS': {'fa': ' لطفا یک کلاس عیب انتخاب کنید  ',
                               'en': ' Please select a defect class '},

    'SELECT_NO_DATASET': {'fa': ' لطفا حداقل یک دیتاست انتخاب کنید  ',
                          'en': ' Please select at least on dataset '},

    'SELECT_SHEET': {'fa': ' لطفا یک ورق را انتخاب کنید  ',
                        'en': ' Please select one sheet '},
    'UNAV_ID': {'fa': ' شناسه ی وارد شده دردسترس نیست ',
                        'en': ' The entered ID is not available '},
    'UNAV_HEAT': {'fa': ' شماره سفارش وارد شده دردسترس نیست ',
                        'en': ' The entered HEAT number is not available '},
    'UNAV_PSN': {'fa': ' شماره سفارش وارد شده دردسترس نیست ',
                        'en': ' The entered PS number is not available '},
    'UNAV_PDLN': {'fa': ' شماره سفارش وارد شده دردسترس نیست ',
                        'en': ' The entered PDL number is not available '},

    'SET_DATASET_TITLE': {'fa': ' مجموعه داده پیش فرض ',
                          'en': ' Default dataset '},

    'CREATE_DATASET_TITLE': {'fa': ' وجود مجموعه داده ',
                             'en': ' Dataset exist '},

    'CREATE_DATASET_EXIST': {'fa': ' مجموعه داده با این آدرس و نام وجود دارد ',
                       'en': ' Dataset with this path and name already axist '},

    'SIDE_EMPTY': {'fa': ' فیلد جهت خالی است ',
                   'en': ' Side is empty '},

    'CAMERA_EMPTY': {'fa': ' فیلد شماره دوربین خالی است ',
                     'en': ' Camera number is empty '},

    'FRAME_EMPTY': {'fa': ' فیلد شماره فریم خالی است ',
                    'en': ' Frame number is empty '},

    'APPEND_SUCCESSFULLY': {'fa': ' با موفقیت اضافه شد ',
                            'en': ' Append successfully '},

    'REMOVE_SUCCESSFULLY': {'fa': ' با موفقیت حذف شد ',
                            'en': ' Remove successfully '},

    'WRONGE_MASK': {'fa': ' وضعیت یا ماسک اشتباه است ',
                    'en': ' Status or mask is wrong '},

    'WRONGE_MASK_Format': {'fa': ' وضعیت یا ماسک تصویر {} اشتباه است ',
                    'en': ' Status or mask of image {} is wrong '},

    'training_params_invalid': {'fa': 'پارامترهای آموزشی نامعتبرند',
                    'en': 'Training a arametrs are invalid'},
                    
    'no_defect_class_selected': {'fa': 'لطفا حداثل یک کلاس عیب انتخاب کنید',
                    'en': 'Please select at least one defect class'},

    'warning_notif': {'fa':'هشدار',
            'en':'Warning'},

    #  'en': ' Error while opening image '}
    'overhead_temp': {'fa':'دما بیش از حد مجاز فعالسازی سیستم سرمایشی',
            'en':'Overd Head Temperature Start Air Cooling'},  
    'overhead_temp': {'fa':'دما بیش از حد مجاز فعالسازی سیستم سرمایشی',
            'en':'Overd Head Temperature Start Air Cooling'},  


    'Training':{'fa':'در حال آموزش دیدن',
                        'en':'Training...'},

    'no_camera_selected': {'fa': ' دوربینی انتخاب نشده است. ',
                        'en': ' No camera selected '},

    'parameters_error': {'fa': 'پارامتر‌های ورودی به درستی مقدار دهی نشده‌اند.',
        'en': 'The input parameters are not set correctly.'},

    'image_not_exist': {'fa': 'فایل تصویر وجود ندارد.',
                        'en': 'The image file does not exist'},

    'invalid_date_range': {'fa': 'بازه‌ی تاریخ داده شده معتبر نیست.',
                        'en': 'The given date range is not valid.'},        
}

MESSEGES = {
    'Data_Is_Ready' :{'fa': ' مجموعه داده ها آماده است',
                'en': ' Data is ready. '},
    'Data_Is_Not_Ready' :{'fa': 'مجموعه داده ها یافت نشد',
                'en': ' Data is not ready. '},
    'Customized Data is ready': {'fa':'مجموعه داده های سفارشی یافت شد',
                                'en':'Customized Data is ready'},
    'Customized Data is not ready': {'fa':'مجموعه داده های سفارشی یافت نشد',
                                'en':'Customized Data is not ready'},
    'Pipline_Is_Ready':{'fa':'پایپ لاین {} آماده است ',
                'en':'pipline {} is ready'},
    'Pipline_Is_Not_Ready':{'fa':'پایپ لاین آماده نیست',
                                'en':'the pipeline is not built, and not ready'},

    'UI_CREATED': {'fa': ' .شی رابط کاربری برای نرم افزار آموزشی ایجاد شد ',
                    'en': ' UI object for train app created. '},
                    
    'CALLBACK_CREATED': {'fa': ' .ایجاد شد Callback شی ',
                    'en': ' Callback object created. '},
                    
    'UPDATE_BCHART': {'fa': ' اپوک {}: .نمودار های آموزش باینری به روز شدند ',
                    'en': ' Epoch {}: Binary train charts updated. '},
                    
    'UPDATE_LCHART': {'fa': ' اپوک {}: .نمودار های آموزش جایابی به روز شدند ',
                    'en': ' Epoch {}: Localization train charts updated. '},
                    
    'SAVE_BMODEL_EPOCH': {'fa': ' اپوک {}: .وزن های مدل آموزش باینری ذخیره شدند ',
                    'en': ' Epoch {}: Binary train model weights saved. '},
                    
    'SAVE_LMODEL_EPOCH': {'fa': ' اپوک {}: .وزن های مدل آموزش جایابی ذخیره شدند ',
                    'en': ' Epoch {}: Localization train model weights saved. '},
                    
    'SAVE_BMODEL': {'fa': ' .وزن های مدل آموزش باینری ذخیره شدند ',
                    'en': ' Binary train model weights saved. '},
                    
    'SAVE_LMODEL': {'fa': ' .وزن های مدل آموزش جایابی ذخیره شدند ',
                    'en': ' Localization train model weights saved. '},

    'SAVE_FTBMODEL': {'fa': ' .وزن های مدل آموزش باینری تنظیم دقیق ذخیره شدند ',
                    'en': ' Binary train fine tune model weights saved. '},

    'SELECT_IMAGE': {'fa': 'دوربین: {} | فریم: {}',
                     'en': 'Camera: {} | Frame: {} '},

    'FILTERED_RESAULTS_SUCCUSSFULL': {'fa': ' نتایج اعمال فیلتر با موفقیت بازگردانده شد ',
                                      'en': ' Filtered resaults returened succussfully '},

    'FILTERED_RESAULTS_CLEAR': {'fa': ' فیلترهای اعمال شده پاک شدند ',
                                'en': ' Filters cleared '},

    'REFRESH_TABLE': {'fa': ' جدول(ها) رفرش شدند، فیلترهای اعمال شده پاک شدند ',
                      'en': ' Table(s) refreshed succussfully, Filters cleared  '},

    'LOAD_IMAGES_WITH_DEFECT': {'fa': ' تصاویر دارای کلاس عیب موردنظر بارگزاری شدند ',
                                'en': ' Image records containing this defect are loaded'},

    'LOAD_IMAGES_DATASETS': {'fa': ' تصاویر دیتاست های انتخاب شده بارگزاری شدند ',
                             'en': ' Image records belonging selected datasets are loaded'},

    'NO_IMAGE_AVAILABLE_WITH_DEFECT': {'fa': ' هیچ تصویر دارای کلاس موردنظر در دیتاست های انتخاب شده یافت نشد  ',
                                       'en': ' No image available with this defect class in selected datasets'},

    'NO_IMAGE_AVAILABLE_IN_DATASET': {'fa': ' هیچ تصویری در دیتاست های انتخاب شده یافت نشد  ',
                                      'en': ' No image available in selected datasets'},    
 
    'CREATE_BWPATH': {'fa': ' آدرس وزن های مدل آموزش باینری ایجاد شد. ',
                    'en': ' Binary weights path created. '},  
 
    'SET_PROCESSOR': {'fa': ' پردازنده‌ی آموزش تنظیم شد.',
                    'en': ' Training processor is set. '}, 

    'CREATE_LWPATH': {'fa': ' آدرس وزن های مدل آموزش جایابی ایجاد شد. ',
                    'en': ' Localization weights path created. '}, 
 
    'CREATE_BINARY_GEN': {'fa': ' داده‌ی آموزش باینری آماده شد. ',
                        'en': ' Binary training data is ready. '},
 
    'CREATE_LOC_GEN': {'fa': ' داده‌ی آموزش جایابی آماده شد. ',
                        'en': ' Localization training data is ready. '},

    'CREATE_MODEL': {'fa': ' مدل برای الگوریتم {} ایجاد شد. ',
                    'en': ' Model for {} algorithm created. '},

    'CREATE_FTMODEL': {'fa': ' مدل تنظیم دقیق برای الگوریتم {} ایجاد شد. ',
                        'en': ' Fine tune model for {} algorithm created. '},  

    'FIT_MODEL': {'fa': ' آموزش مدل با موفقیت انجام شد. ',
                    'en': ' Model trained successfully. '},

    'FIT_FTMODEL': {'fa': ' آموزش مدل تنظیم دقیق با موفقیت انجام شد. ',
                    'en': ' Fine tune model trained successfully. '},

    'plc_connection_apply': {'fa': 'اتصال به پی ال سی برقرار شد',
                'en': 'Connection to PLC established'},

    'plc_disconnected': {'fa': 'اتصال به پی ال سی قطع شد',
                'en': 'Disconnected from PLC'},

    'plc_start_connecting': {'fa': 'برقراری اتصال با پی ال سی',
                'en': 'Start Connecting to PLC'},

    
    'database_set_plc_ip': {'fa': 'آی پی پی ال سی در دیتابیس ذخیره شد',
                'en': 'PLC ip updated on database'},

    'database_get_plc_ip': {'fa': 'آی پی پی ال سی از دیتابیس دریافت شد',
                'en': 'PLC ip recieved from database'},

    'plc_set_value': {'fa': 'مقدار متغیر در پی ال سی آپدیت شد',
                'en': 'Vaule updated on PLC'},

    'database_update_plc_params': {'fa': 'پارامترهای پی ال سی در دیتابیس آپدیت شدند',
                'en': 'PLC params updated on database'},
    
    'database_get_plc_params': {'fa': 'پارامترهای پی ال سی از دیتابیس دریافت شد',
                'en': 'PLC params reciecved from database'},


    'BINARYLIST_SLIDER_build': {'fa': 'اسلایدرهای صفحه لیست باینری ایجاد شدند',
                                      'en': ' Binarylist sliders were built.'},

    'database_get_bmodels': {'fa': 'لیست مدل های باینری از دیتابیس دریافت شد',
                 'en': 'Binary models list were returned from database'},

    'database_get_lmodels': {'fa': 'لیست مدل های جایابی از دیتابیس دریافت شد',
                 'en': 'Localization models list were returned from database'},

    'database_get_classmodels': {'fa': 'لیست مدل های دسته بندی از دیتابیس دریافت شد',
                 'en': 'Classification models list were returned from database'},

    'database_get_datasets': {'fa': 'لیست دیتاست ها از دیتابیس دریافت شد',
                 'en': 'Datasets list were returned from database'},

    'database_get_defects': {'fa': 'لیست عیوب از دیتابیس دریافت شد',
                 'en': 'Defects list were returned from database'},

    'database_get_defect_groups': {'fa': 'لیست گروه عیوب از دیتابیس دریافت شد',
                 'en': 'Defect groups list were returned from database'},

    'database_get_filtered_cls_models': {'fa': 'لیست مدل های دسته بندی فیلترشده از دیتابیس دریافت شد',
                 'en': 'Filtered classification models list were returned from database'},

    'clslist_piechart_created': {'fa': 'پای چارت های صفحه لیست دسته بندی ایجاد شدند',
                 'en': 'Classification list piecharts created'},

    'binarylist_piechart_created': {'fa': 'پای چارت های صفحه لیست باینری ایجاد شدند',
                 'en': 'Binary list piecharts created'},

    'database_add_bmodel': {'fa': 'اطلاعات مدل باینری جدید در دیتابیس اضافه شدند',
                 'en': 'New binary model info record was added to database'},

    'database_add_lmodel': {'fa': 'اطلاعات مدل جایابی جدید در دیتابیس اضافه شدند',
                 'en': 'New localization model info record was added to database'},

    'bmodel_trained': {'fa': 'آموزش مدل باینری به اتمام رسید',
                 'en': 'Binary model training was finished'},

    'lmodel_trained': {'fa': 'آموزش مدل جایابی به اتمام رسید',
                 'en': 'Localization model training was finished'},

    'initialize_notif_ui': {'fa': 'ساخت کلاس اعلانات',
                 'en': 'Notficaion object initialized.'},

    'info_notif': {'fa':'اطلاعات',
            'en':'Information'},

        'success_notif': {'fa':'موفقیت',
            'en':'Success'},


    'user_logedin': {'fa':'کاربر با موفقیت وارد شد',
            'en':'User Logedin Successfully'},

    'user_logedout': {'fa':'کاربر از حساب کاربری خود خارج شد',
            'en':'User Logedout'},  

    'start_captring': {'fa':' شروع به تصویر برداری با تعداد دوربین ها و پرژکتورهای :',
            'en':'Start Capturing                                               Cameras-Projectors :'},  

    'save_sheet': {'fa':' ورق با موفقیت ذخیره شد',
            'en':'Sheet Saved Successfully '}, 

    'connection_failed': {'fa': 'اتصال به سطح ۲ انجام نشد.',
                        'en': 'Failed to connect to level 2.'}, 

    'dataset_splitted': {'fa': 'مجموعه داده(ها) با موفقیت تقسیم شد.',
                        'en': 'Dataset(s) was splitted successfully.'},

    'search_success': {'fa': ' جست و جو با موفقیت انجام شد ',
                        'en': ' The search was successful '},

    'refresh_success': {'fa': ' به روز رسانی با موفقیت انجام شد ',
                        'en': ' The refresh was successful '},

    'sheet_details': {'fa': ' ورق با شناسه ی {} در ساعت {} تاریخ {} توسط کاربر {} ذخیره شده است. تعداد فریم های ذخیره شده برابر با {} و تعداد دوربین ها برابر با {} است. ',
                        'en': ' The sheet with ID {} ​​was saved at time {} date {} by user {}. The number of saved frames is equal to {} and the number of cameras is equal to {}. '},

    'setting_applied': {'fa': 'تنظیمات {} اعمال شد',
                        'en': '{} settings Applied Successfully'},

    'CREATE_DATASET': {'fa': ' مجموعه داده با موفقیت ایجاد شد ',
                       'en': ' Dataset created successfully '},
                               
    'SET_DATASET': {'fa': ' مجموعه داده ی پیش فرض با موفقیت تنظیم شد ',
                    'en': ' Default dataset set successfully '},
                               
    'REMOVE_PIP': {'fa': ' پابپ لاین با موفقیت حذف شد ',
                    'en': ' Pipeline removed successfully '},

    'Camera_successful': {'fa': ' دوربین {} با موفقیت متصل شد ',
                           'en': ' Camera {} connected successfuly '},

    'Disconnect_camera_successful': {'fa':'قطع اتصال دوربین با موفقیت انجام شد',
                        'en':'Camera disconnected successfuly'},

    'changes_not_saved': {'fa': 'تغییرات ذخیره نشده است. میخواهید ادامه دهید؟', 
                        'en': 'Changes are not saved. Do you want to continue?'},

    'sure_delete': {'fa': 'آیا مطمئن هستید که می خواهید همه چند ضلعی ها را حذف کنید؟', 
                        'en': 'Are you sure you want to delete all polygons?'},

    'exit_confirm': {'fa': 'آیا مطمئن هستید که میخواهید خارج شوید؟',
                'en': 'Are you sure you want to exit?'},

    'train_successfuly': {'fa': 'آموزش با موفقیت به پایان رسید',
        'en': 'Training completed successfully'},
}

Titles = {

        'sense': {'fa': "سنس",
                        'en': 'SENSE'},

        'trainer': {'fa': "نرم افزار آموزشی    ",
                        'en': '    Trainer App'},

        'message': {'fa': "پیغام",
                        'en': 'Message'},

        'persian': {'fa': "فارسی",
                        'en': 'Persian'},

        'english': {'fa': "انگلیسی",
                        'en': 'English'},

        'language': {'fa': "زبان",
                        'en': 'Language'},

        'font': {'fa': "فونت",
                'en': 'Font'},

        'manual': {'fa': "غیر خودکار",
                        'en': 'Manual'},

        'save_params': {'fa': "اعمال/ذخیره پارامترها",
                        'en': 'Apply/Save Parameters'},

        'save_params': {'fa': "اعمال/ذخیره پارامترها",
                        'en': 'Apply/Save Parameters'},

        'auto_wind': {'fa': "فشار‌هوای خودکار",
                        'en': 'Automatic wind'},

        'wind_duration': {'fa': ": مدت زمان فشار هوا",
                        'en': 'Wind duration :'},

        'automatic_wind_intervals': {'fa': ": فواصل فشار‌هوای خودکار",
                        'en': 'Automatic wind intervals :'},

        'update_time': {'fa': ": زمان به روز رسانی",
                        'en': 'Update time :'},

        'language_font': {'fa': 'زبان و فونت',
                       'en': 'language and font'},

        'plc': {'fa': "پی ال سی",
                        'en': 'PLC'},

        'cameras': {'fa': "دوربین ها",
                        'en': 'Cameras'},

        'appearance': {'fa': "ظاهر نرم افزار",
                        'en': 'App appearance'},

        'plc_ip': {'fa': ": آی پی پی ال سی",
                        'en': 'PLC IP :'},  

        'plc_status': {'fa': ': وضعیت پی ال سی',
                        'en': 'PLC Status :'},        

        'frame_rate': {'fa': ': نرخ تصویر‌برداری',
                        'en': 'Frame Rate :'},        

        'live_update': {'fa': ': زمان بروزرسانی نمایش زنده',
                        'en': 'Live show update time :'},             

        'Train Software': {'fa': "نرم افزار آموزشی",
                                'en': 'Train Software'},

        'Setting Software': {'fa': "نرم افزار تنظیمات",
                                'en': 'Setting Software'},

        'Data Auquzation': {'fa': "داده برداری",
                                'en': 'Data Auquzation'},

        'Label': {'fa': "برچسب گذاری",
                'en': 'Label'},

        'Label page': {'fa': "صفحه برچسب گذاری",
                'en': 'Label page'},

        ' Tuning': {'fa': "تیونینگ",
                        'en': ' Tuning'},

        'Pipline Build & Test': {'fa': "ساخت پایپ لاین و تست",
                                'en': 'Pipline Build and Test'},

        'show_logs': {'fa': "نمایش لاگ‌ها",
                        'en': 'Show Logs'},

        'Live': {'fa': 'نمایش زنده',
                'en': 'Live'},
        'Live tab': {'fa': ' تب نمایش زنده',
                'en': 'Live tab'},
        'Technical View': {'fa': 'نمای تکنیکال',
                        'en': 'Technical View'},
        'Technical View tab': {'fa': 'تب نمای تکنیکال',
                        'en': 'Technical View tab'},
        'TOP Side': {'fa': "سمت بالا",
                        'en': 'TOP Side'},

        'BOTTOM Side': {'fa': "سمت پایین",
                        'en': 'BOTTOM Side'},

        'position': {'fa': "موقعیت",
                        'en': 'Position'},

        'Load Sheet': {'fa': "بارگزاری ورق",
                        'en': 'Load Sheet'},

        'append': {'fa': "اضافه کردن",
                'en': 'Append'},

        'select all': {'fa': "انتخاب همه",
                        'en': 'Select All'},

        'all': {'fa': "همه",
                'en': 'All'},

        'cm': {'fa': "سانتی متر",
                'en': 'cm'},

        'Append with filter': {'fa': "اضافه کردن با فیلتر",
                                'en': 'Append with filter'},

        'Select with filter': {'fa': "انتخاب با فیلتر",
                                'en': 'Select with filter'},

        'side': {'fa': "سمت ورق",
                'en': 'Side'},

        'Frame Number': {'fa': "شماره فریم",
                        'en': 'Frame Number'},

        'Camera Number': {'fa': "شماره دوربین",
                        'en': 'Camera Number'},

        'creditsLabel': {'fa': "تهیه شده توسط : شرکت درصا",
                        'en': 'By: Dorsa-co'},

        'Sheet ID :': {'fa': " : شماره ورق",
                        'en': 'Sheet ID : '},

        'Heat Number :': {'fa': " : شماره سفارش",
                        'en': 'Heat Number : '},

        'Ps Number :': {'fa': " : شماره  سفارش",
                        'en': 'Ps Number : '},

        'Pdl Number :': {'fa': " : شماره  سفارش",
                        'en': 'Pdl Number : '},

        'length :': {'fa': " : طول",
                        'en': 'length :'},

        'Width :': {'fa': " : عرض",
                        'en': 'Width : '},

        'Thickness :': {'fa': " : ضخامت",
                        'en': 'Thickness : '},

        'start_capture': {'fa': 'شروع نمایش زنده',
                        'en': 'Start Capture'},

        'stop_capture': {'fa': 'پایان نمایش زنده',
                        'en': 'Stop Capture'},

        'save_images': {'fa': 'ذخیره تصاویر',
                        'en': 'Save Images'},

        'temperature': {'fa': ': دما',
                        'en': 'Temperature :'},

        'start': {'fa': 'شروع',
                'en': 'Start'},

        'seconds': {'fa': '{} ثانیه',
                'en': '{} Seconds'},

        'second': {'fa': '{} ثانیه',
                'en': '{} Second'},

        'reconnect': {'fa': 'اتصال مجدد {}',
                'en': 'Reconnect {}'},

        'connect': {'fa': 'متصل',
                'en': 'Connect'},

        'disconnect': {'fa': 'غیر متصل',
                'en': 'Diconnect'},

        'connect2': {'fa': 'وصل کردن',
                'en': 'Connect'},

        'disconnect2': {'fa': 'قطع کردن',
                'en': 'Diconnect'},

        'single_camera': {'fa': 'تک دوربین',
                        'en': 'Single Camera'},

        'top_cameras': {'fa': 'دوربین های بالا',
                        'en': 'Top Cameras'},

        'bottom_cameras': {'fa': 'دوربین های پایین',
                        'en': 'Bottom Cameras'},

        'all_cameras': {'fa': 'همه ی دوربین ها',
                        'en': 'All Cameras'},

        'camera_number': {'fa': 'شماره دوربین',
                        'en': 'Camera Number'},

        'detect sensor': {'fa': 'سنسور تشخیص',
                        'en': 'Detect sensor'},

        'air cleaning': {'fa': 'فشار هوا',
                        'en': 'Air cleaning'},

        'search by': {'fa': 'جست و جو براساس: ',
                        'en': 'Search By: '},

        'refresh': {'fa': 'به روز رسانی',
                        'en': 'Refresh'},

        'open_images': {'fa': 'باز کردن تصاویر',
                        'en': 'Open Images'},

        'load': {'fa': 'بارگذاری',
                'en': 'Load'},

        'detail': {'fa': 'جزئیات مجموعه داده',
                'en': 'Details Of Dataset'},

        'available_ids': {'fa': 'شماره شناسه های در دسترس :',
                        'en': 'Availabla ID Numbers :'},

        'available_heats': {'fa': 'شماره سفارش های در دسترس :',
                                'en': 'Availabl HEAT Numbers :'},

        'available_psns': {'fa': 'شماره سفارش های در دسترس :',
                                'en': 'Available Product Schedule Numbers :'},

        'available_pdlns': {'fa': 'شماره سفارش های در دسترس :',
                                'en': 'Available Product Drift Line Numbers :'},

        'number': {'fa': ': شماره',
                'en': 'Number :'},

        'user_login': {'fa': 'ورود کاربر',
                        'en': 'User Login'},

        'user_name': {'fa': 'نام کاربری',
                        'en': 'User Name'},

        'password': {'fa': '    رمز عبور',
                        'en': 'Password'},

        'login': {'fa': 'ورود',
                'en': 'Login'},

        'forget': {'fa': 'فراموشی نام کاربری/رمز عبور',
                'en': 'Forget Username/Password'},

        'user_name_2': {'fa': ':نام کاربری',
                        'en': 'User Name:'},

        'ID': {'fa': ':شناسه',
                'en': 'ID:'},

        'ID2': {'fa': 'شناسه',
                'en': 'ID'},

        'heatn': {'fa': 'ش. سفارش',
                'en': 'HEAT'},

        'psn': {'fa': 'ش. سفارش',
                'en': 'PSN'},

        'pdln': {'fa': 'ش. سفارش',
                'en': 'PDLN'},

        'role': {'fa': ':نقش',
                'en': 'Role:'},

        'date_created': {'fa': ':تاریخ ایجاد',
                        'en': 'Date Created:'},

        'default_sataset': {'fa': ':مجموعه داده پیش فرض',
                                'en': 'Default Dataset:'},

        'create_new_ds': {'fa': 'ایجاد مجموعه داده ی جدید',
                        'en': 'Create New Dataset'},

        'all_ds': {'fa': 'همه ی مجموعه داده ها',
                'en': 'All Datasets'},

        'my_ds': {'fa': 'مجموعه داده های من',
                'en': 'My Datasets'},

        'pipelines': {'fa': 'پایپ لاین ها',
                        'en': 'Pipelines'},

        'today_date': {'fa': ':تاریخ امروز',
                        'en': 'Today Date:'},

        'creator_username': {'fa': ':نام کاربری سازنده',
                        'en': 'Creator Username:'},

        'dataset_name': {'fa': ':نام مجموعه داده',
                        'en': 'Dataset Name:'},

        'location': {'fa': ':مکان',
                        'en': 'Location:'},

        'create': {'fa': 'ایجاد',
                'en': 'Create'},

        'select_ds': {'fa': ':انتخاب مجموعه داده',
                'en': 'Select Dataset:'},

        'owner_user': {'fa': ':کاربر مالک',
                'en': 'Owner User:'},

        'path': {'fa': ':مسیر',
                'en': 'Path:'},

        'set_default': {'fa': 'انتخاب به عنوان پیش فرض',
                        'en': 'Set As Default'},

        'my_pipelines': {'fa': ':پایپ لاین های من',
                        'en': 'My Pipelines:'},

        'all_pipelines': {'fa': ':همه ی پایپ لاین ها',
                        'en': 'All Pipelines:'},

        'show_details': {'fa': 'نمایش جزئیات',
                        'en': 'Show Details'},

        'df_piechart': {'fa': 'نمودار دایره ای معیوب/بدون عیب',
                        'en': 'Defect/Perfect PieChart'},

        'df_barchart': {'fa': 'نمودار میله ای تعداد معیوب/بدون عیب',
                        'en': 'Defect/Perfect Count BarChart'},

        'c_barchart': {'fa': 'نمودار میله ای کلاس های عیب',
                        'en': 'Defect Classes BarChart'},

        'date': {'fa': ': تاریخ',
                'en': 'Date :'},

        'coil_number': {'fa': ': شماره ورق',
                'en': 'Coil Number :'},

        'cam_number': {'fa': ': شماره دوربین',
                'en': 'Cam Number :'},

        'frame_number': {'fa': ': شماره فریم',
                'en': 'Frame Number :'},

        'show_neighbours': {'fa': 'نمایش تصاویر همسایه',
                'en': 'Show Neighbours'},

        'show_neighbours_labels': {'fa': 'نمایش برچسب تصاویر همسایه',
                'en': 'Show Neighbours labels'},

        'line_thickness': {'fa': ': ضخامت خط',
                'en': 'Line Thickness :'},

        'point_thickness': {'fa': ': ضخامت نقطه',
                'en': 'Point Thickness :'},

        'defect': {'fa': ':معیوب',
                'en': 'Defect:'},

        'defect2': {'fa': 'معیوب:',
                'en': 'Defect:'},

        'perfect': {'fa': 'سالم:',
                'en': 'Perfect:'},

        'yes': {'fa': 'بله',
                'en': 'Yes'},

        'no': {'fa': 'خیر',
                'en': 'No'},

        'save': {'fa': 'ذخیره',
                'en': 'Save'},

        'save_all': {'fa': 'ذخیره‌ی همه',
                'en': 'Save All'},

        'masks': {'fa': 'ماسک ها',
                'en': 'Masks'},

        'size': {'fa': 'اندازه',
                'en': 'Size'},

        'defect_id': {'fa': 'شناسه ی عیب',
                        'en': 'Defect ID'},

        'defect_name': {'fa': 'نام عیب',
                        'en': 'Defect Name'},

        'search_bar': {'fa': 'نوار جست و جو',
                        'en': 'Search Bar'},

        'ok': {'fa': 'تایید',
                'en': 'OK'},

        'cancel': {'fa': 'لغو',
                        'en': 'Cancel'},

        'binary_list': {'fa': 'لیست باینری',
                        'en': 'Binary list'},

        'Binary': {'fa': 'باینری',
                        'en': 'Binary'},

        'Localization': {'fa': 'جایابی',
                        'en': 'Localization'},

        'Classification': {'fa': 'دسته بندی',
                        'en': 'Classification'},

        'training': {'fa': 'آموزش',
                        'en': 'Training'},

        'binary_training': {'fa': 'آموزش باینری',
                                'en': 'Binary Training'},

        'localization_training': {'fa': 'آموزش جایابی',
                                        'en': 'Localization Training'},

        'classification_training': {'fa': 'آموزش کلاس بندی',
                                        'en': 'Classification Training'},

        'history': {'fa': 'تاریخچه',
                        'en': 'History'},

        'binary_history': {'fa': 'تاریخچه باینری',
                                'en': 'Binary History'},

        'localization_history': {'fa': 'تاریخچه جایابی',
                                        'en': 'Localization History'},

        'classification_history': {'fa': 'تاریخچه کلاس بندی',
                                        'en': 'Classification History'},

        'algorithm_name': {'fa': ':نام الگوریتم',
                        'en': 'Algorithm Name:'},

        'pretrained_weights_path': {'fa': ':آدرس وزن‌های آموزش دیده',
                        'en': 'Pretrained weights path:'},

        'algorithm_name_2': {'fa': 'نام الگوریتم',
                        'en': 'Algorithm Name'},

        'input_size': {'fa': ':اندازه ورودی',
                        'en': 'Input Size:'},

        'input_type': {'fa': ':نوع ورودی',
                        'en': 'Input Type:'},

        'resize': {'fa': 'تغییر اندازه',
                        'en': 'resize'},

        'split': {'fa': 'شکستن',
                        'en': 'split'},

        'epochs': {'fa': ':تعداد اپوک',
                        'en': 'Epochs:'},

        'batch_size': {'fa': ':اندازه ی دسته',
                        'en': 'Batch Size:'},

        'learning_rate': {'fa': ':نرخ یادگیری',
                        'en': 'Learning Rate:'},

        'tuning_epochs': {'fa': ':اپوک های تیونینگ',
                        'en': 'Tunning Epochs:'},

        'validation_split': {'fa': ' :% تقسیم داده',
                        'en': 'Validation Split %:'},

        'ds_path': {'fa': ':آدرس مجموعه داده',
                        'en': 'Dataset Path:'},

        'ds_path_2': {'fa': 'آدرس مجموعه داده',
                        'en': 'Dataset Path'},

        'ds_name': {'fa': 'نام مجموعه داده',
                        'en': 'Dataset Name'},

        'ds_owner': {'fa': 'کاربر مالک',
                        'en': 'Owner User'},

        'select_dataset': {'fa': 'انتخاب مجموعه داده',
                        'en': 'Select Dataset'},

        'delete': {'fa': 'حذف',
                        'en': 'Delete'},

        'add': {'fa': 'اضافه',
                        'en': 'Add'},

        'train_processor': {'fa': ':پردازنده‌ی آموزش',
                        'en': 'Train Processor:'},

        'train': {'fa': 'آموزش',
                        'en': 'Train'},

        'chart_full_view': {'fa': 'نمای کامل نمودار',
                        'en': 'Chart Full View'},

        'validation': {'fa': 'اعتبار سنجی',
                        'en': 'Validation'},

        'sf_training_records': {'fa': 'جست و جو/فیلتر رکوردهای آموزش دیده',
                        'en': 'Search/Filter Training Records'},

        'name': {'fa': 'نام',
                'en': 'Name'},

        'epochs_2': {'fa': 'اپوک ها',
                        'en': 'Epochs'},

        'tune_epochs': {'fa': 'اپوک های تنظیم',
                        'en': 'Tune Epochs'},

        'batch_size_2': {'fa': 'اندازه ی دسته',
                        'en': 'Batch Size'},

        'split_ratio': {'fa': 'نسبت تقسیم داده',
                        'en': 'Split Ratio'},
        
        'loss': {'fa': 'خطا', 
                'en': 'Loss'},

        'accuracy': {'fa': 'دقت', 
                'en': 'Accuracy'},
        
        'precision': {'fa': 'پرسیژن', 
                'en': 'Precision'},
        
        'recall': {'fa': 'ریکال', 
                'en': 'Recall'},
        
        'iou': {'fa': 'IOU', 
                'en': 'IOU'},
        
        'fscore': {'fa': 'FScore', 
                'en': 'FScore'},

        'min': {'fa': 'کمینه',
                'en': 'Min'},

        'max': {'fa': 'بیشینه',
                'en': 'Max'},

        'start_date': {'fa': 'تاریخ شروع',
                        'en': 'Start Date'},

        'end_date': {'fa': 'تاریخ پایان',
                        'en': 'End Date'},

        'search_filter': {'fa': 'جست و جو/فیلتر',
                        'en': 'Search/Filter'},

        'clear_filters': {'fa': 'حذف فیلترها',
                        'en': 'Clear Filters'},

        'statistic': {'fa': 'آمار',
                        'en': 'Statistic'},

        'search_tab': {'fa': 'برگه ی جست و جو',
                        'en': 'Search Tab'},

        'last_row': {'fa': 'آخرین ردیف',
                        'en': 'last row'},

        'request': {'fa': 'درخواست',
                        'en': 'Request'},

        'by_name': {'fa': ':بر اساس نام',
                        'en': 'by Name:'},

        'by_accuracy': {'fa': ':بر اساس Accuracy',
                        'en': 'by Accuracy:'},

        'by_recall': {'fa': ':بر اساس Recall',
                        'en': 'by Recall:'},

        'by_epoch': {'fa': ':بر اساس Epoch',
                        'en': 'by Epoch:'},

        'min_2': {'fa': ':کمینه',
                'en': 'Min:'},

        'max_2': {'fa': ':بیشینه',
                'en': 'Max:'},

        'classes_list': {'fa': 'لیست کلاس ها',
                        'en': 'Classes list'},

        'defect_classes': {'fa': 'کلاس های عیب',
                'en': 'Defect Classes'},

        'datasets': {'fa': 'مجموعه داده ها',
                'en': 'Datasets'},

        'including_class': {'fa': 'کلاس (ها) موجود',
                                'en': 'Including Class(s)'},



        'Pipline': {'fa': 'پایپ لاین',
                                'en': 'Pipline'},
        'Load Dataset': {'fa': 'بارگذاری داده',
                                'en': 'Load Dataset'},
        'History':{'fa':'تاریخچه',
                        'en':'History'},

        'binary_pbt':{'fa':' : دوتایی',
                        'en':'Binary : '},
        
        'localization_pbt':{'fa':' : جایابی',
                                'en':'Localization : '},
        
        'classification_pbt':{'fa':' : دسته بندی',
                                'en':'Classification :'},
        
        'pipline_name_pbt':{'fa':' : نام پایپ لاین',
                                'en':'Name of Pipiline  :'},
        
        'warn_of_valid_pipline_name':{'fa':'لطفا نام معتبری بنوسید',
                'en':'Please Enter Valid Name'},
                
        'example_of_pipline_name':{'fa':'برای مثال : تاریخ/ترکیبی از آدرس وزن....'
                                ,'en':'Example : Date/Mix of weights/....'},
        
        'apply_pbt':{'fa':'اعمال'
                  ,'en':'apply'},
        
        'refresh_pbt':{'fa':'بروزرسانی'
                        ,'en':'refresh'},
        
        'dataset_pbt':{'fa':'مجموعه دادگان'
                        ,'en':'dataset'},

        'title_of_gb_pbt':{'fa':'انتخاب مجموعه دادگان/تصویر',
                                'en':'Select Dataset / Image'},

        'perfect_pbt':{'fa':'سالم',
                        'en':'Perfect'},

        'defect_pbt':{'fa':'معیوب',
                        'en':'Defect'}, 

        'load_pbt':{'fa':'بارگذاری',
                        'en':'Load'},

        'load_img_pbt':{'fa':'بارگذاری تصاویر',
                        'en':'Load Image'},

        'select_pipline':{'fa':'انتخاب پایپ لاین',
                                'en':'Select Pipeline'},

        'set_pbt':{'fa':'بساز',
                        'en':'set'},

        'evaluate':{'fa':'ارزیابی',
                        'en':'Evaluate'},

        'Evaluated Details':{'fa':'نتیجه ارزیابی',
                        'en':'Evaluated Details'},

        'Orginal Images':{'fa':'تصاویر خام',
                        'en':'Orginal Images'},

        'Evaluated Images':{'fa':'نتیجه ازریابی',
                        'en':'Evaluated Images'},

        'binary model':{'fa':': مدل دوتایی','en':'binary model  :'},
        'binary acc':{'fa':': صحت دوتایی','en':'binary acc  :'},
        'binary precision':{'fa':': دقت دوتایی','en':'binary precision  :'},
        'binary recall':{'fa':': ریکال دوتایی','en':'binary recall  :'},
        'binary f1':{'fa':': اف یک دوتایی','en':'binary f1  :'},

        'localization model':{'fa':': مدل جایابی','en':'localization model  :'},
        'localization dice':{'fa':': دایس جایابی','en':'localization dice  :'},
        'localization iou':{'fa':': آی او یو جایایبی','en':'localization iou  :'},

        'classify model':{'fa':': مدل دسته بندی','en':'classify model  :'},
        'classify acc':{'fa':': صحت دسته بندی','en':'classify acc  :'},
        'classify precision':{'fa':'دقت دسته بندی','en':'classify precision  :'},
        'classify recall':{'fa':'ریکال دسته بندی','en':'classify recall  :'},
        'classify f1':{'fa':'اف یک دسته بندی','en':'classify f1  :'},
        'time_pbt':{'fa':': زمان','en':'Time  :'},
        'date_pbt':{'fa': ': تاریخ','en':'Date  :'},
        'Clear Filters':{'fa':'پاک کرن فیلتر','en':'Clear Filters'},
        'Search/Filter':{'fa':': جست و جو','en':'Search/Filter'},

        'User Profile': {'fa': 'صفحه کاربر',
                                'en': 'User Profile'},

        'settings': {'fa': 'تنظیمات',
                        'en': 'Settings'},

        'settings_page': {'fa': 'صفحه‌ی تنظیمات',
                        'en': 'Settings page'},
                                
        'connection_failed': {'fa': 'اتصال ناموفق',
                                'en': 'Connection failed'},  
                        
        'software_settings': {'fa': 'تنظیمات نرم افزار',
                                'en': 'Software Settings'},    
                        
        'user_profile': {'fa': 'پروفایل کاربر',
                        'en': 'User Profile'},  

        'show_suggested_defects': {'fa': 'نمایش عیوب پیشنهادی', 
                                'en': 'Show suggested defects'},
        
        'next_sheet': {'fa': 'ورق بعدی',
                'en': 'Next Sheet'},
        
        'prev_sheet': {'fa': 'ورق قبلی',
                'en': 'Previous Sheet'},
        
        'add_image': {'fa': 'اضافه کردن تصویر',
                'en': 'Add Image'},
        
        'remove_image': {'fa': 'حذف کردن تصویر',
                'en': 'Remove Image'},
        
        'next': {'fa': 'بعدی',
                'en': 'Next'},
        
        'previous': {'fa': 'قبلی',
                'en': 'Previous'},
        
        'zoom_in': {'fa': 'بزرگنمایی',
                'en': 'Zoom In'},
        
        'zoom_out': {'fa': 'کوچکنمایی',
                'en': 'Zoom Out'},
        
        'drag': {'fa': 'کشیدن',
                'en': 'Drag'},
        
        'polygon': {'fa': 'چند‌ضلعی',
                'en': 'Polygon'},
        
        'suggested_defects': {'fa': 'عیوب پیشنهادی',
                'en': 'Suggested Defects'},
        
        'suggested_defects_heatMap': {'fa': 'هیت‌مپ عیوب پیشنهادی',
                'en': 'Suggested Defects HeatMap'},
        
        'delete_polygons': {'fa': 'حذف چند‌ضلعی‌ها',
                'en': 'Delete Polygons'},

		'search_bar': {'fa': 'نوار جست و جو',
					'en': 'Search Bar'},

		'date': {'fa': 'تاریخ',
					'en': 'Date'},

        'all_dates': {'fa': 'همه‌ی تاریخ‌ها',
                'en': 'All Dates'},

        'from_date': {'fa': ':از تاریخ',
                'en': 'From Date:'},

        'to_date': {'fa': ':تا تاریخ',
                'en': 'To Date:'},

        'year': {'fa': ':سال',
                'en': 'Year:'},

        'month': {'fa': ':ماه',
                'en': 'Month:'},

        'day': {'fa': ':روز',
                'en': 'Day:'},

        'levels': {'fa': 'سطح‌ها',
                'en': 'Levels'},

        'all_levels': {'fa': 'همه‌ی سطح‌ها',
                'en': 'All Levels'},

        'types': {'fa': 'نوع‌ها',
                'en': 'Types'},

        'all_types': {'fa': 'همه‌ی نوع‌ها',
                'en': 'All Types'},

        'lines': {'fa': 'خط‌ها',
                'en': 'Lines'},

        'line': {'fa': 'خط‌',
                'en': 'Lines'},

        'from_first': {'fa': 'از ابتدا',
                'en': 'From First'},

        'from_last': {'fa': 'از انتها',
                'en': 'From Last'},

        'line': {'fa': 'خط‌',
                'en': 'Lines'},

        'search': {'fa': 'جست و جو',
                'en': 'Search'},

        'refresh': {'fa': 'به‌روز رسانی',
                'en': 'Refresh'},

        'logs': {'fa': 'لاگ‌ها',
                'en': 'Logs'},

#---------------------------------------------------------------------
#----------------------Setting Sofwtare-------------------------------
#---------------------------------------------------------------------

        'page_dashboard': {'fa': 'صفحه داشبورد',
                                'en': 'Dashboard'},  
        'page_camera': {'fa': 'صفحه دوربین',
                                'en': 'Camera'},  
        'page_defection': {'fa': 'صفحه عیوب',
                                'en': 'Defection'},  
        'page_level2': {'fa': 'صفحه ارتباطات',
                                'en': 'Level2'},  
        'page_calibration': {'fa': 'صفحه کالیبراسیون',
                                'en': 'Calibration'},  
        'page_settings': {'fa': 'صفحه تنظیمات',
                                'en': 'Setting'},  
        'page_users': {'fa': 'صفحه مدیریت کاربران',
                                'en': 'Users'},  
        'page_plc': {'fa': 'صفحه پی ال سی',
                                'en': 'PLC'},                        
        'page_storage': {'fa': 'صفحه حافظه',
                                'en': 'Storage'},                        
        'show_labels': {'fa': 'نمایش برچسب‌ها',
                                'en': 'Show Labels'},                       
}

HELPS = {
    'MAIN_HELP': {'fa': """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p align="center" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt; font-weight:600;">به نرم‌افزار آموزشی سنس خوش آمدید</span></p>
<p align="right" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt;">برای شروع کار با نرم‌افزار از منوی سمت چپ بر روی کلید مورد نظر کلیک کنید</span><span style=" font-family:'Segoe UI'; font-size:12pt;">. </span><span style=" font-family:'B Nazanin'; font-size:12pt;">برای دیدن جزئیات هر کلید روی آيکون سه نقطه کلیک کنید یا نشانگر موس را روی کلید مورد نظر نگه دارید</span><span style=" font-family:'Segoe UI'; font-size:12pt;">.</span></p>
<p align="right" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt;">در ابتدا روی کلید داده برداری کلیک کنید</span><span style=" font-family:'Segoe UI'; font-size:12pt;">. </span><span style=" font-family:'B Nazanin'; font-size:12pt;">از تب نمایش زنده، اتصال دوربین ها را بررسی کنید و تصاویر گرفته شده از ورق ها را به صورت زنده مشاهده و ذخیره کنید</span><span style=" font-family:'Segoe UI'; font-size:12pt;">. </span></p>
<p align="right" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt;">سپس در تب نمای تکنیکال، ورق هایی که تصاویر آن‌ها ذخیره شده‌اند را بارگذاری کنید و تصاویر مورد نظر خود را برای برچسب زدن اضافه کنید</span><span style=" font-family:'Segoe UI'; font-size:12pt;">. </span><span style=" font-family:'B Nazanin'; font-size:12pt;">با کلیک بر روی کلید برچسب گذاری در این صفحه وارد صفحه ی برچسب گذاری شوید</span><span style=" font-family:'Segoe UI'; font-size:12pt;">.</span></p>
<p align="right" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt;">در صفحه ی برچسب گذاری، عیوب تصاویر انتخاب شده و نوع عیوب را مشخص کنید و تصاویر را ذخیره کنید</span><span style=" font-family:'Segoe UI'; font-size:12pt;">.</span></p>
<p align="right" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt;">با کلیک بر روی کلید تیونینگ، یکی از سه کلید باینری، جایابی یا کلاس بندی را انتخاب کنید و با کلیک روی آن به صفحه ی مربوطه بروید و مدل مورد نظر خود را آموزش دهید</span><span style=" font-family:'Segoe UI'; font-size:12pt;">.</span></p>
<p align="right" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt;">در صفحه ی ساخت پایپ لاین و تست، با استفاده از مدل های آموزش داده شده پایپ لاین مورد نظر خود را تنظیم و تست کنید.</span></p>
<p align="right" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt;">در نوار بالایی صفحه با کلیک بر روی آیکون چرخ‌دنده کلید‌های مربوط به تنظیمات نرم‌افزار و پروفایل کاربر(صفحه‌ی جاری) را مشاهده کنید و با کلیک بر روی هر کلید به صفحه‌ی مورد نظر بروید.</span></p>
<p dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'B Nazanin'; font-size:12pt;">در صفحه‌ی تنظیمات نرم‌افزار، تنظیمات مربوط برنامه، پی ال سی و دوربین‌ها را انجام دهید.</span></p>
<p align="right" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt;">در صفحه ی پروفایل کاربر، مجموعه داده‌های ایجاد شده را مشاهده کنید و مجموعه داده ی خود را برای ذخیره ی تصاویر انتخاب کنید </span><span style=" font-family:'Segoe UI'; font-size:12pt;">(</span><span style=" font-family:'B Nazanin'; font-size:12pt;">در غیر این صورت تصاویر در مجموعه داده ی پیش‌فرض ذخیره می‌شوند).</span></p>
<p align="right" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt;">با کلیک بر روی آیکون لاگین در نوار بالای صفحه با استفاده از نام کاربری و رمزعبور خود به برنامه وارد یا از آن خارج شوید.</span></p>
<p align="right" dir='rtl' style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'B Nazanin'; font-size:12pt;">در هر یک از صفحات با کلیک بر روی آیکون علامت سؤال در بالای صفحه، جزئیات نحوه ی کار با آن صفحه را مشاهده کنید.</span></p></body></html>""",

                'en': """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; font-weight:600; background-color:transparent;">Welcome to SENS TRAINER App</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">To start working with the software, click on the desired key from the left menu. To see the details of each key, click on the three dots icon or hold the mouse pointer over the desired key.</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">First, click on the Data Auquzation button. From the Live tab, check the connection of the cameras and view and save the images taken from the sheets live.</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">Then, in the Technical View tab, load the sheets whose images are saved and add the images you want for labeling. Enter the labeling page by clicking on the Label button on this page.</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">On the Label page, specify the defects of the selected images and the type of defects and save the images.</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">By clicking on the Tuning key, select one of the three keys, Binary, Localization or Classification, and by clicking on it, go to the corresponding page and train your desired model.</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">On the Pipeline Build &amp; Test page, set up and test your desired pipeline using the trained models.</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">On the top bar of the page, click on the gear icon to see the keys related to software settings and user profile (current page) and go to the desired page by clicking on each key.</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">On the software settings page, make settings for the program, PLC and cameras.</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">On the user profile page, view the created datasets and select your dataset to save the images (otherwise the images will be saved in the default dataset).</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">Log in or out of the program using your username and password by clicking the login icon on the top bar.</span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;"><span style=" font-family:'Segoe UI'; font-size:10pt; background-color:transparent;">On each of the pages, click on the question mark icon at the top of the page to see the details of how to work with that page.</span></p></body></html>"""},


#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Trainig Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

    'SETTINGS_PAGE': {'fa': 'صفحه‌ی تنظیمات \n این صفحه مربوط به تنظیمات نرم افزار از جمله تنظیمات ظاهری، تنظیمات پی ال سی و تنظیمات تصویربرداری است.',
                'en': 'Settings Page \n This page is related to software settings including appearance settings, PLC settings and cameras settings.'},

    'LIVE_PAGE': {'fa': 'صفحه ی نمایش زنده \n این صفحه مربوط به مدیریت اتصال دوربین ها و ذخیره سازی و نمایش زنده ی تصاویر گرفته شده توسط آن هاست.',
                'en': 'Live Page \n This page is related to the management of the connection of cameras and the storage and live display of the images taken by them.'},
    'TECHNICAL_PAGE': {'fa': 'صفحه ی نمای فنی \n این صفحه مربوط به بارگذاری ورق و مشاهده ی تصاویر مربوط به آن و همچنین انتخاب تصاویر برای برچسب زدن است.',
                'en': 'Thechnical View Page \n This page is about loading the sheet and viewing related images as well as selecting images for labeling.'},
    'LABEL_PAGE': {'fa': 'صفحه ی برچسب زدن \n این صفحه مربوط به برچسب زدن تصاویر ورق ها است.',
                'en': 'Label Page \n This page is about labeling sheet images.'},
    'PROFILE_CREATEDS_PAGE': {'fa': 'صفحه ی پروفایل کاربر \n این صفحه مربوط به اطلاعات کاربر و مجموعه داده ها است.',
                            'en': 'User Profile Page \n This page is about user information and datasets.'},
    'PROFILE_ALLDS_PAGE': {'fa': 'صفحه ی پروفایل کاربر \n این صفحه مربوط به اطلاعات کاربر و مجموعه داده ها است.',
                            'en': 'User Profile Page \n This page is about user information and datasets.'},
    'PROFILE_MYDS_PAGE': {'fa': 'صفحه ی پروفایل کاربر \n این صفحه مربوط به اطلاعات کاربر و مجموعه داده ها است.',
                            'en': 'User Profile Page \n This page is about user information and datasets.'},
    'PROFILE_MYPIP_PAGE': {'fa': 'صفحه ی پروفایل کاربر \n این صفحه مربوط به اطلاعات کاربر و مجموعه داده ها است.',
                            'en': 'User Profile Page \n This page is about user information and datasets.'},
    'BINARY_TRAINING_PAGE': {'fa': 'صفحه ی آموزش باینری \n این صفحه مربوط به آموزش مدل‌های باینری است.',
                            'en': 'Binary Training Page \n This page is about training binary models.'},
    'BINARY_HISTORY_PAGE': {'fa': 'صفحه ی تاریخچه ی آموزش باینری \n این صفحه مربوط به تاریخچه ی آموزش مدل‌های باینری است.',
                            'en': 'Binary History Page \n This page is about history of training binary models.'},
    'BINARYLIST_PAGE': {'fa': 'صفحه ی لیست باینری \n این صفحه مربوط به مشاهده ی جزئیات مجموعه داده های باینری موجود است.',
                            'en': 'Binary List Page \n This page is about viewing the details of the available binary data sets.'},
    'LOC_TRAINING_PAGE': {'fa': 'صفحه ی آموزش جایابی \n این صفحه مربوط به آموزش مدل‌های جایابی است.',
                            'en': 'Localization Training Page \n This page is about training localization models.'},
    'LOC_HISTORY_PAGE': {'fa': 'صفحه ی تاریخچه ی آموزش جایابی \n این صفحه مربوط به تاریخچه ی آموزش مدل‌های جایابی است.',
                            'en': 'Localization History Page \n This page is about history of training localization models.'},

    'PBT_PIPLINE_PAGE':{'fa':'این صفحه برای ساخت پایپ لاین سفارشی شده است\nبه این صورت که با استفاده از سه لیست زیر ،مدل های از قبل آموزش دیده شده موجود در نرم افزار  را براساس معماری آنها فیلتر کرده\nو در جدول زیر لیست ها  عملکرد هر مدل  بر اساس معماری انتخاب شده نمایش داده میشود\nو از طریق جدول، مدل هر جز از پایپ لاین را انتخاب کرده \nو در پایان،در جای خالی زیر صفحه یک نام برای پایپ لاین انتخاب کرده و با زدن دکمه اعمال پایپ لاین راساخته.',
                        'en':'this page is for a customized pipline. \nIn such a way that: useing the following three list,fliter the pre-trained models in the software based on their architecture,\nthe performace of each model is shown in the table blow the lists, \nuseing the model table,select each part, \nfinaly choose a suitable name for pipeline in the empty space below and hit the apply buttom and build the pipline '},
    'PBT_LOADDATASET_PAGE' :{'fa':'این صفحه برای اعتبار سنجی پایپ لاین های موجود در نرم افزار بر روی مجموعه داده های موجود است.\n به این صورت که،ابتدا از قسمت بالا سمت چپ نرم افزار تنظیمات مربوط به بارگذاری مجموعه داده ها را انجام داده\n سپس با استفاده از لیست سمت راست،پایپ لاین مورد نظر را انتخاب کرده\n با فشردن دکمه اعتبار سنجی عملیات را انجام داده.',
                              'en':'This page is for validating pipelines in the software on existing data sets.\nIn this way, first of all, from the upper left part of the software, the settings related to loading the data set have been made\nThen, using the list on the right, select the desired pipeline\nBy pressing the evaluate button, the evaluating operation is done'},
    'PBT_HISTORY_PAGE':{'fa':' این صفحه برای مشاهده تاریخچه تمامی اعتبار سنجی های انجام شده در نرم افزار است،\nکه این تاریخچه با استفاده ابزار سمت چپ صفحه قابل فیلتر است.',
                        'en':'This page is for viewing the history of all evaluating , done in the software.\nThis history can be filtered using the tool on the left side of the page.'},

#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Setting Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


    'page_dashboard': {'fa': 'در این صفحه تمام پارامتر به اختصار نمایش داده میشوند و برای دسترسی به نرم افزار نیاز به لاگین میباشد \n این صفحه اولین صفحه نرم افزار است.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_camera': {'fa': 'در این صفحه تمام تنظیمات مربوط به دوربین صورت میگیرد و هر دوربین به صورت مجزا یا گروهی مقادیر خود را میگیرد و در نهایت در دیتابیس ذخیره میشود.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_users': {'fa': 'در این صفحه کاربران نرم افزار تعریف میشوند این کاربران در هر سه نرم افزار دسترسی دارند و سطح دسترسی آنها مشخص میشود.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_settings': {'fa': 'در این صفحه تنظیمات کلی مربوط به نزم افزار تنظیمات مشخص میشود .',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_calibration': {'fa': 'در این صفحه پارامتر های مروبط به الگوریتم پردازش تصویر و عرض سنج مشخص میشود.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_level2': {'fa': 'در این صفحه نوع ارتباط و پارامتر های ارتباط نرم افزار تنظیمات با کارخانه مشخص و اعمال میشود.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},

    'page_defection': {'fa': 'در این صفحه عیوب و دسته بندی ورق تعریف میشوند .',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_plc': {'fa': 'در این صفحه آی پی پی ال سی و حافظه های آن نمایش و ذخیره میشوند.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_storage': {'fa': 'در این صفحه تنظیمات مربوط به حافظه برای حذف داده های قدیمی اعمال میشود.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},




}

HELPS_ADDRESS = {
#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Training Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
    'SETTINGS_PAGE': {'fa': 'images/helps/settings_page_fa.png',
                    'en': 'images/helps/settings_page.png'},
    'LIVE_PAGE': {'fa': 'images/helps/live_page_fa.png',
                    'en': 'images/helps/live_page.png'},
    'TECHNICAL_PAGE': {'fa': 'images/helps/technical_page_fa.png',
                    'en': 'images/helps/technical_page.png'},
    'LABEL_PAGE': {'fa': 'images/helps/label_page_fa.png',
                    'en': 'images/helps/label_page.png'},
    'PROFILE_CREATEDS_PAGE': {'fa': 'images/helps/profile_createds_fa.png',
                            'en': 'images/helps/profile_createds.png'},
    'PROFILE_ALLDS_PAGE': {'fa': 'images/helps/profile_allds_fa.png',
                            'en': 'images/helps/profile_allds.png'},
    'PROFILE_MYDS_PAGE': {'fa': 'images/helps/profile_myds_fa.png',
                            'en': 'images/helps/profile_myds.png'},
    'PROFILE_MYPIP_PAGE': {'fa': 'images/helps/profile_mypip_fa.png',
                            'en': 'images/helps/profile_mypip.png'},
    'BINARY_TRAINING_PAGE': {'fa': 'images/helps/binary_training_page_fa.png',
                            'en': 'images/helps/binary_training_page.png'},
    'BINARY_HISTORY_PAGE': {'fa': 'images/helps/binary_history_page_fa.png',
                            'en': 'images/helps/binary_history_page.png'},
    'BINARYLIST_PAGE': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'},
    'LOC_TRAINING_PAGE': {'fa': 'images/helps/loc_training_page_fa.png',
                            'en': 'images/helps/loc_training_page.png'},
    'LOC_HISTORY_PAGE': {'fa': 'images/helps/loc_history_page_fa.png',
                            'en': 'images/helps/loc_history_page.png'},
    'PBT_PIPLINE_PAGE':{'fa':'images/helps/PBT_pipline_page.png',
                        'en':'images/helps/PBT_pipline_page.png'},
    'PBT_LOADDATASET_PAGE' :{'fa':'images/helps/PBT_loaddataset_page.png',
                              'en':'images/helps/PBT_loaddataset_page.png'},
    'PBT_HISTORY_PAGE':{'fa':'images/helps/PBT_history_page.png',
                        'en':'images/helps/PBT_history_page.png'},

#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Setting Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

    'page_dashboard': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'},
    'page_camera': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'},
    'page_defection': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'},
    'page_level2': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'},                        
    'page_calibration': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'}, 
    'page_settings': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'}, 
    'page_users': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'}, 
    'page_plc': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'}, 
    'page_storage': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'}, 
}

def set_title(self, lang):
    self.titleLeftApp.setText(Titles['sense'][lang])
    self.titleLeftDescription.setText(Titles['trainer'][lang])

    self.Data_auquzation_btn.setText(Titles['Data Auquzation'][lang])
    self.Data_auquzation_btn.setToolTip(Titles['Data Auquzation'][lang])
    self.label_btn.setText(Titles['Label'][lang])
    self.label_btn.setToolTip(Titles['Label'][lang])
    self.tuning_btn.setText(Titles[' Tuning'][lang])
    self.tuning_btn.setToolTip(Titles[' Tuning'][lang])
    self.pbt_btn.setText(Titles['Pipline Build & Test'][lang])
    self.pbt_btn.setToolTip(Titles['Pipline Build & Test'][lang])
    self.log_btn.setText(Titles['show_logs'][lang])
    self.log_btn.setToolTip(Titles['show_logs'][lang])

    self.Binary_btn.setText(Titles['Binary'][lang])
    self.Localization_btn.setText(Titles['Localization'][lang])
    self.Classification_btn.setText(Titles['Classification'][lang])

    self.btn_software_setting.setText(Titles['software_settings'][lang])
    self.btn_user_profile.setText(Titles['user_profile'][lang])

    # Data Page

    self.tabWidget_2.setTabText(0, Titles['Live'][lang])
    self.tabWidget_2.setTabText(1, Titles['Technical View'][lang])
    self.label_1291.setText('40 ' + Titles['cm'][lang])
    self.label_124.setText('40 ' + Titles['cm'][lang])
    self.label_6_1.setText(Titles['TOP Side'][lang])
    self.label_119.setText(Titles['BOTTOM Side'][lang])
    self.label_45.setText(Titles['position'][lang])
    self.load_coil_btn.setText(Titles['Load Sheet'][lang])
    self.label_btn_SI.setText(Titles['Label'][lang])
    self.label_2.setText(Titles['append'][lang])
    self.checkBox_select.setText(Titles['select all'][lang])
    self.label_222.setText(Titles['cm'][lang])
    self.label_47.setText(Titles['cm'][lang])
    self.checkBox_all_imgs_SI.setText(Titles['select all'][lang])
    self.checkBox_all_camera_SI.setText(Titles['all'][lang])
    self.checkBox_all_frame_SI.setText(Titles['all'][lang])
    self.add_filter_btn_SI.setText(Titles['Append with filter'][lang])
    self.select_filter_btn_SI.setText(Titles['Select with filter'][lang])
    self.label_48.setText(Titles['side'][lang])
    self.label_49.setText(Titles['Camera Number'][lang])
    self.label_50.setText(Titles['Frame Number'][lang])
    self.creditsLabel.setText(Titles['creditsLabel'][lang])

    self.label_226.setText(Titles['Sheet ID :'][lang])
    self.label_156.setText(Titles['Sheet ID :'][lang])
    self.label_heat_number_3.setText(Titles['Heat Number :'][lang])
    self.label_heat_number_5.setText(Titles['Heat Number :'][lang])
    self.label_228.setText(Titles['Ps Number :'][lang])
    self.label_159.setText(Titles['Ps Number :'][lang])
    self.label_229.setText(Titles['Pdl Number :'][lang])
    self.label_132.setText(Titles['Pdl Number :'][lang])
    self.label_230.setText(Titles['length :'][lang])
    self.label_223.setText(Titles['length :'][lang])
    self.label_231.setText(Titles['Width :'][lang])
    self.label_227.setText(Titles['Width :'][lang])
    self.label_232.setText(Titles['Thickness :'][lang])
    self.label_225.setText(Titles['Thickness :'][lang])

    self.checkBox_suggested_defects.setText(Titles['show_suggested_defects'][lang])
    self.next_coil_btn.setToolTip(Titles['next_sheet'][lang])
    self.prev_coil_btn.setToolTip(Titles['prev_sheet'][lang])
    self.add_btn_SI.setToolTip(Titles['add_image'][lang])
    self.remove_btn_SI.setToolTip(Titles['remove_image'][lang])

    self.start_capture_btn.setText(Titles['start_capture'][lang])
    self.stop_capture_btn.setText(Titles['stop_capture'][lang])

    self.checkBox_top.setText(Titles['top_cameras'][lang])
    self.checkBox_bottom.setText(Titles['bottom_cameras'][lang])
    self.checkBox_all.setText(Titles['all_cameras'][lang])
    self.connect_camera_btn.setText(Titles['connect2'][lang])
    self.disconnect_camera_btn.setText(Titles['disconnect2'][lang])

    self.checkBox_save_images.setText(Titles['save_images'][lang])
    self.label_236.setText(Titles['temperature'][lang])
    self.label_237.setText(Titles['plc_status'][lang])

#     strings = [str(x) for x in range(1, 25)]
#     strings.append(Titles['all'][lang])
#     self.comboBox_cam_select.clear()
#     self.comboBox_cam_select.addItems(strings)
#     self.comboBox_cam_select.setCurrentIndex(24)

    self.live_tabWidget.setTabText(0, Titles['single_camera'][lang])
    self.live_tabWidget.setTabText(1, Titles['top_cameras'][lang])
    self.live_tabWidget.setTabText(2, Titles['bottom_cameras'][lang])
    self.live_tabWidget.setTabText(3, Titles['all_cameras'][lang])

    self.label_166.setText(Titles['camera_number'][lang])
    self.label_27.setText(Titles['detect sensor'][lang])
    self.label_235.setText(Titles['air cleaning'][lang])

    
    self.load_sheets_win.groupBox.setTitle(Titles['search by'][lang])
    self.load_sheets_win.btn_id_search.setText(Titles['search'][lang])
    self.load_sheets_win.btn_pdln_search.setText(Titles['search'][lang])
    self.load_sheets_win.btn_psn_search.setText(Titles['search'][lang])
    self.load_sheets_win.btn_heat_search.setText(Titles['search'][lang])

    self.load_sheets_win.btn_refresh.setText(Titles['refresh'][lang])
    self.load_sheets_win.open_folder_image.setText(Titles['open_images'][lang])
    self.load_sheets_win.load_btn.setText(Titles['load'][lang])

    self.load_sheets_win.groupBox_2.setTitle(Titles['detail'][lang])

    self.load_sheets_win.label_13.setText(Titles['available_ids'][lang])
    self.load_sheets_win.label_5.setText(Titles['available_heats'][lang])
    self.load_sheets_win.label_6.setText(Titles['available_psns'][lang])
    self.load_sheets_win.label_9.setText(Titles['available_pdlns'][lang])

    self.load_sheets_win.label_12.setText(Titles['ID'][lang])
    self.load_sheets_win.label_4.setText(Titles['number'][lang])
    self.load_sheets_win.label_7.setText(Titles['number'][lang])
    self.load_sheets_win.label_8.setText(Titles['number'][lang])
    self.load_sheets_win.show_dataset()

    self.load_sheets_win.coil_search.setTabText(0, Titles['ID2'][lang])
    self.load_sheets_win.coil_search.setTabText(1, Titles['heatn'][lang])
    self.load_sheets_win.coil_search.setTabText(2, Titles['psn'][lang])
    self.load_sheets_win.coil_search.setTabText(3, Titles['pdln'][lang])


    # User Profile Page
    self.label_6.setText(Titles['user_name_2'][lang])
    self.label_15.setText(Titles['ID'][lang])
    self.label_16.setText(Titles['role'][lang])
    self.label_17.setText(Titles['date_created'][lang])
    self.label_79.setText(Titles['default_sataset'][lang])

    self.create_new_database.setText(Titles['create_new_ds'][lang])
    self.all_databases.setText(Titles['all_ds'][lang])
    self.my_databases_2.setText(Titles['my_ds'][lang])
    self.my_databases_3.setText(Titles['pipelines'][lang])

    self.label_78.setText(Titles['today_date'][lang])
    self.label_129.setText(Titles['creator_username'][lang])
    self.label_8.setText(Titles['dataset_name'][lang])
    self.label_157.setText(Titles['path'][lang])
    self.create_database_btn.setText(Titles['create'][lang])

    self.label_24.setText(Titles['select_ds'][lang])
    self.label_14.setText(Titles['ID'][lang])
    self.label_20.setText(Titles['dataset_name'][lang])
    self.label_25.setText(Titles['owner_user'][lang])
    self.label_26.setText(Titles['path'][lang])

    self.label_219.setText(Titles['select_ds'][lang])
    self.label_154.setText(Titles['ID'][lang])
    self.label_131.setText(Titles['dataset_name'][lang])
    self.label_218.setText(Titles['owner_user'][lang])
    self.label_155.setText(Titles['path'][lang])
    self.set_default_database_btn.setText(Titles['set_default'][lang])

    self.label_28.setText(Titles['all_pipelines'][lang])
    self.label_61.setText(Titles['my_pipelines'][lang])
    self.show_details_pipline.setText(Titles['show_details'][lang])
    self.remove_pipline.setText(Titles['delete'][lang])

    self.binary_chart_frame_profile.setTitle(Titles['df_piechart'][lang])
    self.classlist_chart_frame_profile.setTitle(Titles['c_barchart'][lang])
    self.mainHelp.setHtml(HELPS['MAIN_HELP'][lang])

    self.label_278.setText(Titles['message'][lang])

    # Label Page
    self.label_13.setText(Titles['date'][lang])
    self.label_22.setText(Titles['coil_number'][lang])
    self.label_121.setText(Titles['cam_number'][lang])
    self.label_288.setText(Titles['frame_number'][lang])
    self.label_285.setText(Titles['line_thickness'][lang])
    self.label_286.setText(Titles['point_thickness'][lang])
    self.checkBox_show_neighbours.setText(Titles['show_neighbours'][lang])
    self.checkBox_show_neighbours_labels.setText(Titles['show_neighbours_labels'][lang])

    self.label_111.setText(Titles['defect'][lang])
    self.no_defect.setText(Titles['no'][lang])
    self.yes_defect.setText(Titles['yes'][lang])
    self.label_220.setText(Titles['masks'][lang])
    self.save_dataset_btn.setText(Titles['save'][lang])
    self.save_all_dataset_btn.setText(Titles['save_all'][lang])
    self.binary_chart_frame_label.setTitle(Titles['df_piechart'][lang])

    self.mask_table_widget.horizontalHeader().setVisible(True)
    self.mask_table_widget.setHorizontalHeaderLabels([Titles['defect_id'][lang], Titles['defect_name'][lang], Titles['size'][lang]])

    self.next_img_label_btn.setToolTip(Titles['next'][lang])
    self.prev_img_label_btn.setToolTip(Titles['previous'][lang])
    self.zoomIn_btn.setToolTip(Titles['zoom_in'][lang])
    self.zoomOut_btn.setToolTip(Titles['zoom_out'][lang])
    self.drag_btn.setToolTip(Titles['drag'][lang])
    self.polygon_btn.setToolTip(Titles['polygon'][lang])
    self.suggested_defects_btn.setToolTip(Titles['suggested_defects'][lang])
    self.heatmap_btn.setToolTip(Titles['suggested_defects_heatMap'][lang])
    self.delete_btn.setToolTip(Titles['delete_polygons'][lang])

    # binary train page

    self.binary_list.setText(Titles['binary_list'][lang])
    self.binary_training.setText(Titles['training'][lang])
    self.binary_history.setText(Titles['history'][lang])

    ## binary list

    self.binary_list_show_btn.setText(Titles['search'][lang])
    self.binarylist_chart_frame.setTitle(Titles['df_piechart'][lang])
    self.binarylist_chart_frame_2.setTitle(Titles['df_barchart'][lang])

    ## training

    self.label_137.setText(Titles['algorithm_name'][lang])
    self.label_144.setText(Titles['input_size'][lang])
    self.label_7.setText(Titles['input_type'][lang])
    self.input_type_resize.setText(Titles['resize'][lang])
    self.input_type_split.setText(Titles['split'][lang])
    self.label_138.setText(Titles['epochs'][lang])
    self.label_139.setText(Titles['batch_size'][lang])
    self.label_140.setText(Titles['learning_rate'][lang])
    self.label_141.setText(Titles['tuning_epochs'][lang])
    self.label_142.setText(Titles['validation_split'][lang])
    self.label_143.setText(Titles['ds_path'][lang])
    self.b_select_dp.setText(Titles['select_dataset'][lang])
    self.b_delete_ds.setText(Titles['delete'][lang])
    self.b_add_ds.setText(Titles['add'][lang])
    self.b_add_cancel.setText(Titles['cancel'][lang])
    self.b_add_ok.setText(Titles['ok'][lang])
    self.b_add_ds_lineedit.setPlaceholderText(Titles['ds_path_2'][lang])
    self.label_130.setText(Titles['train_processor'][lang])
    self.binary_train.setText(Titles['train'][lang])
    self.binary_chart_checkbox.setText(Titles['chart_full_view'][lang])
    self.label_8_2.setText(Titles['train'][lang])
    self.label_11.setText(Titles['validation'][lang])

    ## history

    self.groupBox_33.setTitle(Titles['sf_training_records'][lang])
    self.label_102.setText(Titles['algorithm_name_2'][lang])
    self.label_109.setText(Titles['epochs_2'][lang])
    self.label_134_2.setText(Titles['tune_epochs'][lang])
    self.label_134.setText(Titles['batch_size_2'][lang])
    self.label_145.setText(Titles['split_ratio'][lang])
    self.label_148.setText(Titles['loss'][lang])
    self.label_150.setText(Titles['accuracy'][lang])
    self.label_153.setText(Titles['precision'][lang])
    self.label_309.setText(Titles['recall'][lang])
    self.label_312.setText(Titles['start_date'][lang])
    self.label_315.setText(Titles['end_date'][lang])
    self.binary_filter_btn.setText(Titles['search_filter'][lang])
    self.binary_clearfilter_btn.setText(Titles['clear_filters'][lang])

    self.label_112.setText(Titles['min'][lang])
    self.label_120.setText(Titles['max'][lang])
    self.label_85_2.setText(Titles['min'][lang])
    self.label_133.setText(Titles['max'][lang])
    self.label_135.setText(Titles['min'][lang])
    self.label_136.setText(Titles['max'][lang])
    self.label_146.setText(Titles['min'][lang])
    self.label_147.setText(Titles['max'][lang])
    self.label_132_2.setText(Titles['min'][lang])
    self.label_149.setText(Titles['max'][lang])
    self.label_151.setText(Titles['min'][lang])
    self.label_152.setText(Titles['max'][lang])
    self.label_158.setText(Titles['min'][lang])
    self.label_308.setText(Titles['max'][lang])
    self.label_310.setText(Titles['min'][lang])
    self.label_311.setText(Titles['max'][lang])

    # localization train page

    self.localization_training.setText(Titles['training'][lang])
    self.localization_history.setText(Titles['history'][lang])

    ## training

    self.label_242.setText(Titles['algorithm_name'][lang])
    self.label_301.setText(Titles['pretrained_weights_path'][lang])
    self.label_243.setText(Titles['input_size'][lang])
    self.label_33.setText(Titles['input_type'][lang])
    self.l_input_type_resize.setText(Titles['resize'][lang])
    self.l_input_type_split.setText(Titles['split'][lang])
    self.label_244.setText(Titles['epochs'][lang])
    self.label_245.setText(Titles['batch_size'][lang])
    self.label_246.setText(Titles['learning_rate'][lang])
    self.label_248.setText(Titles['validation_split'][lang])
    self.label_250.setText(Titles['ds_path'][lang])
    self.l_select_dp.setText(Titles['select_dataset'][lang])
    self.l_delete_ds.setText(Titles['delete'][lang])
    self.l_add_ds.setText(Titles['add'][lang])
    self.l_add_cancel.setText(Titles['cancel'][lang])
    self.l_add_ok.setText(Titles['ok'][lang])
    self.l_add_ds_lineedit.setPlaceholderText(Titles['ds_path_2'][lang])
    self.label_249.setText(Titles['train_processor'][lang])
    self.localization_train.setText(Titles['train'][lang])
    self.localization_chart_checkbox.setText(Titles['chart_full_view'][lang])
    self.label_8_3.setText(Titles['train'][lang])
    self.label_19.setText(Titles['validation'][lang])

    ## history

    self.groupBox_35.setTitle(Titles['sf_training_records'][lang])
    self.label_90.setText(Titles['algorithm_name_2'][lang])
    self.label_91.setText(Titles['epochs_2'][lang])
    self.label_2471.setText(Titles['batch_size_2'][lang])
    self.label_95.setText(Titles['split_ratio'][lang])
    self.label_110.setText(Titles['loss'][lang])
    self.label_254.setText(Titles['accuracy'][lang])
    self.label_257.setText(Titles['iou'][lang])
    self.label_260.setText(Titles['fscore'][lang])
    self.label_263.setText(Titles['start_date'][lang])
    self.label_266.setText(Titles['end_date'][lang])
    self.localization_filter_btn.setText(Titles['search_filter'][lang])
    self.localization_clearfilter_btn.setText(Titles['clear_filters'][lang])
    self.label_92.setText(Titles['min'][lang])
    self.label_93.setText(Titles['max'][lang])
    self.label_2511.setText(Titles['min'][lang])
    self.label_252.setText(Titles['max'][lang])
    self.label_96.setText(Titles['min'][lang])
    self.label_97.setText(Titles['max'][lang])
    self.label_132_4.setText(Titles['min'][lang])
    self.label_253.setText(Titles['max'][lang])
    self.label_255.setText(Titles['min'][lang])
    self.label_256.setText(Titles['max'][lang])
    self.label_258.setText(Titles['min'][lang])
    self.label_259.setText(Titles['max'][lang])
    self.label_261.setText(Titles['min'][lang])
    self.label_262.setText(Titles['max'][lang])

    # classification training

    self.classification_class_list.setText(Titles['classes_list'][lang])
    self.classification_training.setText(Titles['training'][lang])
    self.classification_history.setText(Titles['history'][lang])

    ## classes list

    self.groupBox_80.setTitle(Titles['defect_classes'][lang])
    self.groupBox_88.setTitle(Titles['datasets'][lang])
    self.classlist_show_related_img_btn.setText(Titles['search'][lang])
    self.binary_chart_frame.setTitle(Titles['df_piechart'][lang])
    self.classlist_chart_frame.setTitle(Titles['c_barchart'][lang])

    ## history

    self.groupBox_34.setTitle(Titles['sf_training_records'][lang])
    self.label_160.setText(Titles['name'][lang])
    self.label_161.setText(Titles['epochs_2'][lang])
    self.label_164.setText(Titles['tune_epochs'][lang])
    self.label_167.setText(Titles['batch_size_2'][lang])
    self.label_170.setText(Titles['split_ratio'][lang])
    self.label_186.setText(Titles['start_date'][lang])
    self.label_185.setText(Titles['end_date'][lang])
    self.cls_filter_btn.setText(Titles['search_filter'][lang])
    self.cls_clearfilter_btn.setText(Titles['clear_filters'][lang])
    self.label_39.setText(Titles['including_class'][lang])
    self.label_162.setText(Titles['min'][lang])
    self.label_163.setText(Titles['max'][lang])
    self.label_165.setText(Titles['min'][lang])
    self.label_86_3.setText(Titles['max'][lang])
    self.label_168.setText(Titles['min'][lang])
    self.label_169.setText(Titles['max'][lang])
    self.label_171.setText(Titles['min'][lang])
    self.label_172.setText(Titles['max'][lang])
    self.label_132_3.setText(Titles['min'][lang])
    self.label_174.setText(Titles['max'][lang])
    self.label_176.setText(Titles['min'][lang])
    self.label_177.setText(Titles['max'][lang])
    self.label_179.setText(Titles['min'][lang])
    self.label_180.setText(Titles['max'][lang])
    self.label_182.setText(Titles['min'][lang])
    self.label_183.setText(Titles['max'][lang])

    ## setting

    self.label_5.setText(Titles['language'][lang])
    self.label_281.setText(Titles['font'][lang])
    self.groupBox_5.setTitle(Titles['plc'][lang])
    self.groupBox_9.setTitle(Titles['cameras'][lang])
    self.groupBox_10.setTitle(Titles['appearance'][lang])
    self.connect_plc_btn.setText(Titles['connect2'][lang])
    self.disconnect_plc_btn.setText(Titles['disconnect2'][lang])
    self.manual_plc_check.setText(Titles['manual'][lang])
    self.manual_cameras_check.setText(Titles['manual'][lang])
    self.label_29.setText(Titles['wind_duration'][lang])
    self.auto_wind_check.setText(Titles['auto_wind'][lang])
    self.label_299.setText(Titles['automatic_wind_intervals'][lang])
    self.label.setText(Titles['update_time'][lang])
    self.label_10.setText(Titles['plc_ip'][lang])
    self.label_4.setText(Titles['plc_status'][lang])
    self.label_46.setText(Titles['frame_rate'][lang])
    self.label_197.setText(Titles['live_update'][lang])
    self.appearance_btn.setText(Titles['save_params'][lang])
    self.plc_btn.setText(Titles['save_params'][lang])
    self.cameras_btn.setText(Titles['save_params'][lang])
    self.label_277.setText(Titles['message'][lang])

    
    #................................PBT..................................
    #Pipline:
    self.pipeline_pbt_btn.setText(Titles['Pipline'][lang])
    
    self.label_12_3.setText(Titles['binary_pbt'][lang])
    self.label_122.setText(Titles['localization_pbt'][lang])
    self.label_123.setText(Titles['classification_pbt'][lang])
    
    self.label_12_4.setText(Titles['binary_pbt'][lang])
    self.label_247.setText(Titles['classification_pbt'][lang])
    self.label_251.setText(Titles['localization_pbt'][lang])
    self.label_9.setText(Titles['pipline_name_pbt'][lang])
    
    self.pipline_name_status.setText(Titles['warn_of_valid_pipline_name'][lang])
    self.pipline_name.setPlaceholderText(Titles['example_of_pipline_name'][lang])
    self.BTN_apply_of_binary_classifaction_in_PBT_page.setText(Titles['apply_pbt'][lang])
    self.BTN_refreshing_pipline_page_in_PBT.setText(Titles['refresh_pbt'][lang])

    #load dataset
    self.load_dataset_pbt_btn.setText(Titles['Load Dataset'][lang])
    self.groupBox_6.setTitle(Titles['title_of_gb_pbt'][lang])
    self.label_35.setText(Titles['dataset_pbt'][lang])
    self.chbox_prefectdata_in_PBT_page.setText(Titles['perfect_pbt'][lang])
    self.chbox_defectdata_in_PBT_page.setText(Titles['defect_pbt'][lang])  
    self.BTN_load_in_PBT_page.setText(Titles['load_pbt'][lang])
    self.BTN_load_image_in_PBT_page.setText(Titles['load_img_pbt'][lang])
    self.groupBox_7.setTitle(Titles['select_pipline'][lang])
    self.BTN_set_pipline_in_PBT_page.setText(Titles['set_pbt'][lang])
    self.label_36.setText(Titles['Pipline'][lang])
    self.BTN_set_pipline_in_PBT_page.setText(Titles['set_pbt'][lang])
    self.BTN_evaluate_image_in_PBT_page_2.setText(Titles['evaluate'][lang])
    self.GBox_model_evaluation_details.setTitle(Titles['Evaluated Details'][lang])
    self.label_37.setText(Titles['Orginal Images'][lang])
    self.label_40.setText(Titles['Evaluated Images'][lang])

    self.history_pbt_btn.setText(Titles['History'][lang])
    self.LBL_piplines_name_in_PBT_page.setText(Titles['pipline_name_pbt'][lang])
    self.LBL_binary_model_in_PBT_page.setText(Titles['binary_pbt'][lang])
    self.LBL_binary_accuracy_in_PBT_page.setText(Titles['binary acc'][lang])
    self.label_103.setText(Titles['min'][lang])
    self.label_104.setText(Titles['max'][lang])
    self.LBL_binary_precision_in_PBT_page_2.setText(Titles['binary precision'][lang])
    self.label_105.setText(Titles['min'][lang])
    self.label_106.setText(Titles['max'][lang])
    self.LBL_binary_recall_in_PBT_page_3.setText(Titles['binary recall'][lang])
    self.label_107.setText(Titles['min'][lang])
    self.label_108.setText(Titles['max'][lang])
    self.LBL_binary_f1_in_PBT_page_5.setText(Titles['binary f1'][lang])
    self.label_113.setText(Titles['min'][lang])
    self.label_114.setText(Titles['max'][lang])
    self.LBL_localization_model_in_PBT_page.setText(Titles['localization_pbt'][lang])
    self.LBL_localiztion_dice_in_PBT_page.setText(Titles['localization dice'][lang])
    self.label_115.setText(Titles['min'][lang])
    self.label_116.setText(Titles['max'][lang])
    self.LBL_localiztion_iou_in_PBT_page.setText(Titles['localization iou'][lang])
    self.label_117.setText(Titles['min'][lang])
    self.label_118.setText(Titles['max'][lang])
    self.LBL_classification_model_in_PBT_page.setText(Titles['classify model'][lang])
    self.LBL_classification_accuracy_in_PBT_page.setText(Titles['classify acc'][lang])
    self.label_269.setText(Titles['min'][lang])
    self.label_270.setText(Titles['max'][lang])
    self.LBL_classification_precision_in_PBT_page.setText(Titles['classify precision'][lang])
    self.label_271.setText(Titles['min'][lang])
    self.label_272.setText(Titles['max'][lang])
    self.LBL_classification_recall_in_PBT_page.setText(Titles['classify recall'][lang])
    self.label_273.setText(Titles['min'][lang])
    self.label_274.setText(Titles['max'][lang])
    self.LBL_classification_f1_in_PBT_page.setText(Titles['classify f1'][lang])
    self.label_275.setText(Titles['min'][lang])
    self.label_276.setText(Titles['max'][lang])
    self.label_291.setText(Titles['time_pbt'][lang])
    self.label_294.setText(Titles['date_pbt'][lang])
    self.BTN_clear_filter_in_PBT.setText(Titles['Clear Filters'][lang])
    self.BTN_search_and_filter_in_PBT.setText(Titles['Search/Filter'][lang])
    
    set_alignment(self, lang)

def set_title_login(self, lang):
    self.login_window.label.setText(Titles['user_login'][lang])
    self.login_window.user_name.setPlaceholderText(Titles['user_name'][lang])
    self.login_window.password.setPlaceholderText(Titles['password'][lang])
    self.login_window.login_btn.setText(Titles['login'][lang])

def set_title_ds_selection(self, lang):
    self.select_ds_dialog.ok_btn.setText(Titles['ok'][lang])
    self.select_ds_dialog.cancel_btn.setText(Titles['cancel'][lang])

    self.select_ds_dialog.table.horizontalHeader().setVisible(True)
    self.select_ds_dialog.table.setHorizontalHeaderLabels([Titles['ds_name'][lang], Titles['ds_owner'][lang], Titles['ds_path_2'][lang]])

def set_title_labeling(self, lang):
    self.labeling_win.save_btn.setText(Titles['ok'][lang])
    self.labeling_win.cancel_btn.setText(Titles['cancel'][lang])

def set_moving_title(self, lang):
    text = self.plc_status_line.text()
    if text == Titles['connect']['fa'] or text == Titles['connect']['en']:
        self.plc_status_line.setText(Titles['connect'][lang])
    if text == Titles['disconnect']['fa'] or text == Titles['disconnect']['en']:
        self.plc_status_line.setText(Titles['disconnect'][lang])

    text = self.plc_warnings.text()
    if text == Titles['connect']['fa'] or text == Titles['connect']['en']:
        self.plc_warnings.setText(Titles['connect'][lang])
    if text == Titles['disconnect']['fa'] or text == Titles['disconnect']['en']:
        self.plc_warnings.setText(Titles['disconnect'][lang])

    text = self.start_wind_btn.text()
    if text == Titles['start']['fa'] or text == Titles['start']['en']:
        self.start_wind_btn.setText(Titles['start'][lang])     
    
    text = self.user_name.text()
    if text!='':
        user = text[text.find(':'):]
        self.user_name.setText(Titles['user_name'][lang] + user)

def set_alignment(self, lang):
    if lang == 'fa':
        self.titleLeftApp.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.titleLeftDescription.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_237.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_48.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_49.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_50.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_15.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_16.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_17.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_79.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_78.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_129.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_8.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_157.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_24.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_14.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_20.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_25.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_26.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_219.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_154.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_131.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_218.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_155.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_28.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_61.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_278.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_13.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_22.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_121.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_288.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_285.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_286.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_137.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_144.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_138.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_139.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_140.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_141.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_142.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_143.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_130.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_90.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_91.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_2471.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_95.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_110.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_254.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.label_257.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.label_260.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_263.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_266.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_242.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_301.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_243.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_33.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_244.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_245.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_246.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_248.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_249.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_250.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_186.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_185.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_39.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_160.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.help_win.textEdit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_281.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_29.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_299.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_10.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_277.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_46.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_197.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_102.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_109.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_134_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_134.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_145.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_148.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_150.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_153.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_309.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_312.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_315.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        #..................PBT....................
        self.label_12_3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_122.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_123.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_12_4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_247.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_251.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_9.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.pipline_name_status.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.pipline_name.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.load_dataset_pbt_btn.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.groupBox_6.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_35.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.chbox_prefectdata_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.chbox_defectdata_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.BTN_load_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.BTN_load_image_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.groupBox_7.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.BTN_set_pipline_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_36.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.BTN_set_pipline_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.BTN_evaluate_image_in_PBT_page_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.GBox_model_evaluation_details.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_37.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignVCenter)


        # self.history_pbt_btn.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_piplines_name_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_binary_model_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_binary_accuracy_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_103.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_104.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_binary_precision_in_PBT_page_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_105.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_106.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_binary_recall_in_PBT_page_3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_107.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_108.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_binary_f1_in_PBT_page_5.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_113.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_114.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_localization_model_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_localiztion_dice_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_115.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_116.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_localiztion_iou_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_117.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_118.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_classification_model_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_classification_accuracy_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_269.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_270.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_classification_precision_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_271.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_272.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_classification_recall_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_273.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_274.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.LBL_classification_f1_in_PBT_page.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_275.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_276.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_291.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.pipline_year_lineedit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.pipline_month_lineedit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.pipline_day_lineedit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_294.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.pipline_hour_lineedit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.pipline_minut_lineedit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.BTN_clear_filter_in_PBT.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.BTN_search_and_filter_in_PBT.setAlignment(Qt.AlignRight | Qt.AlignVCenter)


    elif lang == 'en':
        self.titleLeftApp.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.titleLeftDescription.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_237.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.label_48.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_49.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_50.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.label_6.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_15.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_16.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_17.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_79.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_78.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_129.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_8.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_157.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_24.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_14.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_20.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_25.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_26.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_219.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_154.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_131.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_218.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_155.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_28.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_61.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_278.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_13.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_22.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_121.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_288.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_285.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_286.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_137.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_144.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_7.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_138.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_139.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_140.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_141.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_142.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_143.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_130.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # self.label_80.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.label_191.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.label_194.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.label_90.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_91.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_2471.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_95.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_110.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_254.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.label_257.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.label_260.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_263.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_266.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_242.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_301.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_243.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_33.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_244.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_245.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_246.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_248.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_249.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_250.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_186.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_185.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_39.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_160.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_5.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_281.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_29.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_299.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_10.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_277.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_4.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_46.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_197.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.help_win.textEdit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label_102.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_109.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_134_2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_134.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_145.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_148.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_150.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_153.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_309.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_312.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_315.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        #..................PBT....................
        self.label_12_3.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_122.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_123.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_12_4.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_247.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_251.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_9.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.pipline_name_status.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.pipline_name.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.load_dataset_pbt_btn.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.groupBox_6.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_35.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.chbox_prefectdata_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.chbox_defectdata_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.BTN_load_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.BTN_load_image_in_PBT_pag.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.groupBox_7.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.groupBox_7.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.BTN_set_pipline_in_PBT_pag.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_36.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.BTN_set_pipline_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.BTN_evaluate_image_in_PBT_page_2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.GBox_model_evaluation_detail.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_37.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_40.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)


        # self.history_pbt_btn.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_piplines_name_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_binary_model_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_binary_accuracy_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_103.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_104.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_binary_precision_in_PBT_page_2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_105.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_106.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_binary_recall_in_PBT_page_3.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_107.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_108.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_binary_f1_in_PBT_page_5.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_113.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_114.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_localization_model_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_localiztion_dice_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_115.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_116.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_localiztion_iou_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_117.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_118.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_classification_model_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_classification_accuracy_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_269.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_270.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_classification_precision_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_271.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_272.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_classification_recall_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_273.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_274.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.LBL_classification_f1_in_PBT_page.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_275.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_276.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_291.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.pipline_year_lineedit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.pipline_month_lineedit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.pipline_day_lineedit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_294.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.pipline_hour_lineedit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.pipline_minut_lineedit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.BTN_clear_filter_in_PBT.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.BTN_search_and_filter_in_PBT.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    
    set_alignment

def set_show_log(self, lang):
	self.show_log_win.groupBox.setTitle(Titles['search_bar'][lang])
	self.show_log_win.groupBox_3.setTitle(Titles['date'][lang])

	self.show_log_win.checkBox_allDates.setText(Titles['all_dates'][lang])
	self.show_log_win.label.setText(Titles['from_date'][lang])
	self.show_log_win.label_2.setText(Titles['to_date'][lang])
	self.show_log_win.label_5.setText(Titles['year'][lang])
	self.show_log_win.label_8.setText(Titles['year'][lang])
	self.show_log_win.label_6.setText(Titles['month'][lang])
	self.show_log_win.label_9.setText(Titles['month'][lang])
	self.show_log_win.label_7.setText(Titles['day'][lang])
	self.show_log_win.label_10.setText(Titles['day'][lang])

	self.show_log_win.groupBox_5.setTitle(Titles['levels'][lang])
	self.show_log_win.checkBox_allLevels.setText(Titles['all_levels'][lang])

	self.show_log_win.groupBox_6.setTitle(Titles['types'][lang])
	self.show_log_win.checkBox_allTypes.setText(Titles['all_types'][lang])

	self.show_log_win.groupBox_4.setTitle(Titles['lines'][lang])
	self.show_log_win.label_12.setText(Titles['line'][lang])
	self.show_log_win.comboBox_linesFL.clear()
	self.show_log_win.comboBox_linesFL.addItems([Titles['from_last'][lang], Titles['from_first'][lang]])
	
	self.show_log_win.search_btn.setText(Titles['search'][lang])
	self.show_log_win.refresh_btn.setText(Titles['refresh'][lang])

	self.show_log_win.groupBox_2.setTitle(Titles['logs'][lang])

	if lang == 'fa':
		self.show_log_win.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
		self.show_log_win.label_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
	elif lang == 'en':
		self.show_log_win.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
		self.show_log_win.label_2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

# def set_help_title(self):
#     self.Data_auquzation_btn.setText(Titles['Data Auquzation'][lang])
#     self.label_btn.setText(Titles['Label'][lang])
#     self.tuning_btn.setText(Titles[' Tuning'][lang])
#     self.pbt_btn.setText(Titles['Pipline Build & Test'][lang])