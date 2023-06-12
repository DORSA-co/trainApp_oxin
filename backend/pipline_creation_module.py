# ui module
from PySide6.QtCore import QObject, QThread, Signal

# custom module
from backend import pipelines
from backend.binary_list_funcs import PIPLINES_PATH
from backend.binary_model_funcs import (
    strInputSize_2_intInputSize,
    translate_binary_algorithm_id_to_name,
    translate_model_algorithm_id_to_creator_function,
)
from Train_modules.model_creator import translate_model_database_info_to_modelOBJ


# _______Threading Management Class_______#
class ModelsCreation_worker(QObject):
    # vars for handling thread
    finished = Signal()
    pipline_info_signal = Signal(str)
    model_creation_signal = Signal(int, bool)

    def set_params(self, pipline_name, database, login_user_name):
        self.pipline_name = pipline_name
        self.db = database
        self.login_user_name = login_user_name

    def load_pipline_info_from_database(self):
        """load required data for database"""

        flag = True  # indicate data fetched correctly
        pipline_info, binary_model_info = None, None
        LC_model_info = {"yolo": None, "segmentation": None, "classification": None}

        # load pipline info
        _, pipline_info = self.db.get_selected_pipline_record(value=self.pipline_name)

        if pipline_info != []:
            pipline_type = pipline_info[0]["pipline_type"]
            self.pipline_type = pipline_type
            # load binary model info
            _, binary_model_info = self.db.get_model(
                self.db.binary_model, pipline_info[0]["binary_weight_path"]
            )

            if binary_model_info != []:
                # get input type of pipline e.g. splited or resized
                self.inputtype = binary_model_info[0]["input_type"]
                # convert binary input size in str format to tuple of int
                self.inputsize = strInputSize_2_intInputSize(
                    string=binary_model_info[0]["input_size"]
                )
            else:
                flag = False

            if "S" in pipline_type:
                # load segmnetion model
                _, localiztion_model_info = self.db.get_model(
                    self.db.localiztion, pipline_info[0]["localization_weight_path"]
                )
                if localiztion_model_info != []:
                    LC_model_info["segmentation"] = localiztion_model_info
                else:
                    flag = False

            if "C" in pipline_type:
                _, classification_model_info = self.db.get_model(
                    self.db.classification,
                    pipline_info[0]["classification_weight_path"],
                )
                if classification_model_info != []:
                    LC_model_info["classification"] = classification_model_info
            if "Y" in pipline_type:
                _, yolo_model_info = self.db.get_model(
                    self.db.yolo, pipline_info[0]["yolo_weight_path"]
                )
                if yolo_model_info != []:
                    LC_model_info["yolo"] = yolo_model_info
                else:
                    flag = False

        return flag, pipline_type, binary_model_info, LC_model_info

    def build_pipline(self):
        # creating pipline object
        self.pipline_OBJ = pipelines.Pipeline(
            pipeline_root=PIPLINES_PATH,
            pipeline_name=self.pipline_name,
        )
        # set values of owner and username in pipline obj
        self.pipline_OBJ.set(key=pipelines.OWNER, value=self.login_user_name)

        # load data from database:
        (
            flag,
            pipline_type,
            binary_model_info,
            LC_model_info,
        ) = self.load_pipline_info_from_database()

        if flag:
            # create binary model object
            # try:
            self.b_model = translate_model_database_info_to_modelOBJ(
                info_dict={
                    "algo_name": binary_model_info[0]["algo_name"],
                    "input_size": self.inputsize,
                    "num_class": 1,
                    "mode": "binary",
                },
                weights_path=binary_model_info[0]["weights_path"],
                model_type="binary",
            )
            # send signal for updataing progress bar
            self.model_creation_signal.emit(
                1,
                True,
            )
            self.pipline_OBJ.set_binary_model(
                key=pipelines.MODEL_ID, value=binary_model_info[0]["algo_name"]
            )
            self.pipline_OBJ.set_binary_model(
                key=pipelines.MODEL_WEIGHTS_PATH,
                value=binary_model_info[0][pipelines.MODEL_WEIGHTS_PATH],
            )

            # except:
            #     # send notif of there is problem in creating models of pipline(here binary)
            #     self.model_creation_signal.emit(1, False)

            if "S" in pipline_type:
                try:
                    # create segmention model object
                    self.l_model = translate_model_database_info_to_modelOBJ(
                        info_dict={
                            "algo_name": LC_model_info["segmentation"][0]["algo_name"],
                            "input_size": self.inputsize,
                            "num_class": 1,
                            "mode": "binary",
                        },
                        weights_path=LC_model_info["segmentation"][0]["weights_path"],
                        model_type="localization",
                    )
                    # send signal for updataing progress bar
                    self.model_creation_signal.emit(2, True)
                    self.pipline_OBJ.set_localization_model(
                        key=pipelines.MODEL_ID,
                        value=LC_model_info["segmentation"][0]["algo_name"],
                    )
                    self.pipline_OBJ.set_localization_model(
                        key=pipelines.MODEL_WEIGHTS_PATH,
                        value=LC_model_info["segmentation"][0]["weights_path"],
                    )
                except:
                    # send notif of there is problem in creating models of pipline(here segmention)
                    self.model_creation_signal.emit(2, False)

            if "C" in pipline_type:
                (
                    self.classes_num,
                    _,
                ) = strInputSize_2_intInputSize(
                    string=LC_model_info["classification"][0]["classes"],
                    use_for_other_parameter=True,
                )
                try:
                    # create segmention model object
                    self.c_model = translate_model_database_info_to_modelOBJ(
                        info_dict={
                            "algo_name": LC_model_info["classification"][0][
                                "algo_name"
                            ],
                            "input_size": self.inputsize,
                            "num_class": self.classes_num,
                            "mode": "categorical",
                        },
                        weights_path=LC_model_info["classification"][0]["weights_path"],
                        model_type="classification",
                    )
                    # send signal for updataing progress bar
                    self.model_creation_signal.emit(3, True)
                    self.pipline_OBJ.set_classification_model(
                        key=pipelines.MODEL_ID,
                        value=LC_model_info["classification"][0]["algo_name"],
                    )
                    self.pipline_OBJ.set_classification_model(
                        key=pipelines.MODEL_WEIGHTS_PATH,
                        value=LC_model_info["classification"][0]["weights_path"],
                    )
                except:
                    # send notif of there is problem in creating models of pipline(here segmention)
                    self.model_creation_signal.emit(3, False)

            if "Y" in pipline_type:
                (
                    self.classes_num,
                    _,
                ) = strInputSize_2_intInputSize(
                    string=LC_model_info["yolo"][0]["classes"],
                    use_for_other_parameter=True,
                )
                try:
                    # create yolo model object
                    self.yolo_model = translate_model_database_info_to_modelOBJ(
                        info_dict={
                            "algo_name": LC_model_info["yolo"][0]["algo_name"],
                            "device": "",
                            "batch_size": LC_model_info["yolo"][0]["batch_size"],
                        },
                        weights_path=LC_model_info["yolo"][0]["weights_path"],
                        model_type="yolo",
                    )
                    # send signal for updataing progress bar
                    self.model_creation_signal.emit(4, True)
                    self.pipline_OBJ.set_yolo_model(
                        key=pipelines.MODEL_ID,
                        value=LC_model_info["yolo"][0]["algo_name"],
                    )
                    self.pipline_OBJ.set_yolo_model(
                        key=pipelines.MODEL_WEIGHTS_PATH,
                        value=LC_model_info["yolo"][0]["weights_path"],
                    )
                    self.pipline_OBJ.set(pipelines.USE_YOLO, value=True)
                except:
                    # send notif of there is problem in creating models of pipline(here yolo)
                    self.model_creation_signal.emit(4, False)

            if pipline_type == "BS":
                self.classes_num = 1
        else:
            self.model_creation_signal.emit(
                0,
                False,
            )
        self.pipline_info_signal.emit(pipline_type)
        self.finished.emit()
