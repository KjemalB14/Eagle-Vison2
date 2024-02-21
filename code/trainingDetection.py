#Importing os library
import os
import object_detection

#Defining constants
CUSTOM_MODEL_NAME = 'my_ssd_mobnet'
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
LABEL_MAP_NAME = 'label_map.pbtxt'

#Define folder pathing
paths = {
    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
    'SCRIPTS_PATH': os.path.join('Tensorflow','scripts'),
    'APIMODEL_PATH': os.path.join('Tensorflow','models'),
    'ANNOTATION_PATH': os.path.join('Tesorflow','workspace','annotations'),
    'IMAGE_PATH': os.path.join('Tensorflow','workspace','images',),
    'MODEL_PATH': os.path.join('Tensorflow','workspace','models'),
    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow','workspace','pre-trained-model'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow','workspace','models',CUSTOM_MODEL_NAME),
    'OUTPUT_PATH': os.path.join('Tensorflow','workspace','models',CUSTOM_MODEL_NAME,'export'),
    'TFJS_PATH': os.path.join('Tensorflow','workspace','models',CUSTOM_MODEL_NAME,'tfjsexport'),
    'TFLITE_PATH': os.path.join('Tensorflow','workspace','models',CUSTOM_MODEL_NAME,'tfliteexport'),
    'PROTOC_PATH': os.path.join('Tensorflow','protoc')
}

#Define file paths
files = {
    'PIPELINE_CONFIG': os.path.join('Tensorflow','workspace','models',CUSTOM_MODEL_NAME,'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'],TF_RECORD_SCRIPT_NAME),
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'],LABEL_MAP_NAME)
}

#Verfifys all packages needed are had ????????????????????
VERIFICATION_SCRIPT = os.path.join(paths['APIMODEL_PATH'],'research','object_detection','builders','model_builder_tf2_test.py')

import object_detection


