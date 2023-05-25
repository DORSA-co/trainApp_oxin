from PySide6.QtCharts import QChart as sQChart, QBarCategoryAxis, QBarSet, QValueAxis, QPieSlice
from PySide6.QtCharts import QChartView as sQChartView
from PySide6.QtCharts import QPieSeries as sQPieSeries
from PySide6.QtCharts import QLineSeries as sQLineSeries
from PySide6.QtCharts import QScatterSeries as sQScatterSeries
from PySide6.QtCharts import QBarSeries as sQBarSeries
from PySide6.QtCharts import QHorizontalPercentBarSeries as sQHorizontalPercentBarSeries
from PySide6.QtCharts import QBarSet as sQBarSet
from PySide6.QtCharts import QValueAxis as sQValueAxis
from PySide6.QtCore import QPointF as sQPointF
from PySide6.QtCore import QMargins as sQMargins
from PySide6.QtWidgets import QVBoxLayout as sQVBoxLayout
from PySide6 import QtCore as sQtCore
from PySide6.QtGui import QBrush as sQBrush
from PySide6.QtGui import QColor as sQColor
from PySide6.QtGui import QPen as sQPen
from PySide6.QtGui import QPainter as sQPainter
from PySide6.QtGui import QFont as sQFont
from PySide6.QtCore import Qt

import cv2
import numpy as np
import random

from backend import dataset
import texts, texts_codes


# chart colors and appearance
train_color = '#1564FF'
val_color = '#FF0000'
bar_color = '#f8b41c'
pen_width = 3
marker_size = 10
animation_duration = 1000
# for test
global numepoch
numepoch = 10
global epochitr
epochitr = 0
global axisX_range
axisX_range = 10
axisY_range = 100
load = np.arange(numepoch)
eff_train = [random.randint(0, 100) for _ in range(numepoch)]
eff_val = [random.randint(0, 100) for _ in range(numepoch)]



def create_train_chart_on_ui(ui_obj, frame_obj, checkbox_obj, scroll_obj, chart_postfix, chart_title='chart', legend_train='legend1', legend_val='legend2',
                            axisX_title='epoch', axisY_title='Accuracy', axisX_visible = False, legend_visible=False, axisY_set_range = True):
    # define chart
    chart = sQChart()
    #chart.setTitle(chart_title)
    chart.legend().setVisible(legend_visible)
    chart.setBackgroundBrush(sQBrush(sQColor(255, 255, 255)))
    chart.setAnimationOptions(sQChart.AnimationOption.SeriesAnimations)
    chart.setAnimationDuration(animation_duration)
    chart.createDefaultAxes()
    chart.setMargins(sQMargins(0,0,0,0))
    chart.setBackgroundRoundness(0)
    # set chart to ui
    eval("exec('ui_obj.chart_%s = chart')" % chart_postfix)
    # ---------------------------------------------------------------------------
    # define training series
    #self.series = sQLineSeries()
    train_line_series = sQLineSeries()
    train_line_series.setName(legend_train)
    pen = sQPen()
    pen.setStyle(sQtCore.Qt.SolidLine)
    pen.setWidth(pen_width)
    pen.setColor(sQColor(train_color))
    train_line_series.setPen(pen)
    # scatterseries (for data points)
    train_scatter_series_1 = sQScatterSeries()
    train_scatter_series_1.setMarkerShape(sQScatterSeries.MarkerShapeCircle) #Circular point
    train_scatter_series_1.setBorderColor(sQColor(train_color)) #Discrete point border color
    train_scatter_series_1.setBrush(sQBrush(sQColor(train_color))) # Discrete point background color
    train_scatter_series_1.setMarkerSize(marker_size) # Discrete point size
    # scatterseries (for center of data points)
    train_scatter_series_2 = sQScatterSeries()
    train_scatter_series_2.setMarkerShape(sQScatterSeries.MarkerShapeCircle) # Circular point
    train_scatter_series_2.setBorderColor(sQColor(255, 255, 255)) # Border color
    train_scatter_series_2.setBrush(sQBrush(sQColor(255, 255, 255))) # background color 
    train_scatter_series_2.setMarkerSize(marker_size//2) # Point size
    # set series to ui
    eval("exec('ui_obj.train_line_series_%s = train_line_series')" % chart_postfix)
    eval("exec('ui_obj.train_scatter_series_1_%s = train_scatter_series_1')" % chart_postfix)
    eval("exec('ui_obj.train_scatter_series_2_%s = train_scatter_series_2')" % chart_postfix)
    # ---------------------------------------------------------------------------------
    # define validation series
    #self.series = sQLineSeries()
    val_line_series = sQLineSeries()
    val_line_series.setName(legend_val)
    pen = sQPen()
    pen.setStyle(sQtCore.Qt.SolidLine)
    pen.setWidth(pen_width)
    pen.setColor(sQColor(val_color))
    val_line_series.setPen(pen)
    # scatterseries (for data points)
    val_scatter_series_1 = sQScatterSeries()
    val_scatter_series_1.setMarkerShape(sQScatterSeries.MarkerShapeCircle) #Circular point
    val_scatter_series_1.setBorderColor(sQColor(val_color)) #Discrete point border color
    val_scatter_series_1.setBrush(sQBrush(sQColor(val_color))) # Discrete point background color
    val_scatter_series_1.setMarkerSize(marker_size) # Discrete point size
    # scatterseries (for center of data points)
    val_scatter_series_2 = sQScatterSeries()
    val_scatter_series_2.setMarkerShape(sQScatterSeries.MarkerShapeCircle) # Circular point
    val_scatter_series_2.setBorderColor(sQColor(255, 255, 255)) # Border color
    val_scatter_series_2.setBrush(sQBrush(sQColor(255, 255, 255))) # background color 
    val_scatter_series_2.setMarkerSize(marker_size//2) # Point size
    # set series to ui
    eval("exec('ui_obj.val_line_series_%s = val_line_series')" % chart_postfix)
    eval("exec('ui_obj.val_scatter_series_1_%s = val_scatter_series_1')" % chart_postfix)
    eval("exec('ui_obj.val_scatter_series_2_%s = val_scatter_series_2')" % chart_postfix)
    # --------------------------------------------------------------------------------------
    # define axis
    # X
    axisX = sQValueAxis()
    axisX.setRange(1, axisX_range)
    axisX.setLabelsFont(sQFont("Times", 6, sQFont.Bold))
    axisX.setLabelFormat("%d")
    axisX.setTickCount(axisX_range)
    if axisX_visible:
        axisX.setTitleText(axisX_title)
    eval("exec('ui_obj.axisX_%s = axisX')" % chart_postfix)
    # Y
    axisY = sQValueAxis()
    if axisY_set_range:
        axisY.setRange(0, axisY_range)
    axisY.setLabelsFont(sQFont("Times", 6, sQFont.Bold))
    axisY.setLabelFormat("%.1f")
    axisY.setTickCount(axisY_range//10+1)
    axisY.setTitleText(axisY_title)
    eval("exec('ui_obj.axisY_%s = axisY')" % chart_postfix)
    # add axis to chart
    eval('ui_obj.chart_%s' % chart_postfix).addAxis(eval('ui_obj.axisX_%s' % chart_postfix), sQtCore.Qt.AlignBottom)
    eval('ui_obj.chart_%s' % chart_postfix).addAxis(eval('ui_obj.axisY_%s' % chart_postfix), sQtCore.Qt.AlignLeft)
    # --------------------------------------------------------------------------------------------------
    # define chartview
    chartview = sQChartView(eval('ui_obj.chart_%s' % chart_postfix))
    chartview.setContentsMargins(0,0,0,0)
    chartview.setRenderHint(sQPainter.Antialiasing)
    # -------------------------------------------------------------------------------------------------
    # add series to chart
    eval('ui_obj.chart_%s' % chart_postfix).addSeries(eval('ui_obj.train_line_series_%s' % chart_postfix))
    eval('ui_obj.chart_%s' % chart_postfix).addSeries(eval('ui_obj.train_scatter_series_1_%s' % chart_postfix))
    eval('ui_obj.chart_%s' % chart_postfix).addSeries(eval('ui_obj.train_scatter_series_2_%s' % chart_postfix))
    eval('ui_obj.chart_%s' % chart_postfix).addSeries(eval('ui_obj.val_line_series_%s' % chart_postfix))
    eval('ui_obj.chart_%s' % chart_postfix).addSeries(eval('ui_obj.val_scatter_series_1_%s' % chart_postfix))
    eval('ui_obj.chart_%s' % chart_postfix).addSeries(eval('ui_obj.val_scatter_series_2_%s' % chart_postfix))
    # attach axis
    eval('ui_obj.train_line_series_%s' % chart_postfix).attachAxis(eval('ui_obj.axisX_%s' % chart_postfix))
    eval('ui_obj.train_line_series_%s' % chart_postfix).attachAxis(eval('ui_obj.axisY_%s' % chart_postfix))
    eval('ui_obj.train_scatter_series_1_%s' % chart_postfix).attachAxis(eval('ui_obj.axisX_%s' % chart_postfix))
    eval('ui_obj.train_scatter_series_1_%s' % chart_postfix).attachAxis(eval('ui_obj.axisY_%s' % chart_postfix))
    eval('ui_obj.train_scatter_series_2_%s' % chart_postfix).attachAxis(eval('ui_obj.axisX_%s' % chart_postfix))
    eval('ui_obj.train_scatter_series_2_%s' % chart_postfix).attachAxis(eval('ui_obj.axisY_%s' % chart_postfix))
    eval('ui_obj.val_line_series_%s' % chart_postfix).attachAxis(eval('ui_obj.axisX_%s' % chart_postfix))
    eval('ui_obj.val_line_series_%s' % chart_postfix).attachAxis(eval('ui_obj.axisY_%s' % chart_postfix))
    eval('ui_obj.val_scatter_series_1_%s' % chart_postfix).attachAxis(eval('ui_obj.axisX_%s' % chart_postfix))
    eval('ui_obj.val_scatter_series_1_%s' % chart_postfix).attachAxis(eval('ui_obj.axisY_%s' % chart_postfix))
    eval('ui_obj.val_scatter_series_2_%s' % chart_postfix).attachAxis(eval('ui_obj.axisX_%s' % chart_postfix))
    eval('ui_obj.val_scatter_series_2_%s' % chart_postfix).attachAxis(eval('ui_obj.axisY_%s' % chart_postfix))
    # --------------------------------------------------------------------------------------------------------
    # hide legends of scatter series
    eval('ui_obj.chart_%s' % chart_postfix).legend().markers(eval('ui_obj.train_scatter_series_1_%s' % chart_postfix))[0].setVisible(False)
    eval('ui_obj.chart_%s' % chart_postfix).legend().markers(eval('ui_obj.train_scatter_series_2_%s' % chart_postfix))[0].setVisible(False)
    eval('ui_obj.chart_%s' % chart_postfix).legend().markers(eval('ui_obj.val_scatter_series_1_%s' % chart_postfix))[0].setVisible(False)
    eval('ui_obj.chart_%s' % chart_postfix).legend().markers(eval('ui_obj.val_scatter_series_2_%s' % chart_postfix))[0].setVisible(False)
    # ----------------------------------------------------------------------------------------------------------
    # define hbox layout
    hbox = sQVBoxLayout()
    hbox.addWidget(chartview)
    hbox.setContentsMargins(0, 0, 0, 0)
    # add to frame
    frame_obj.setLayout(hbox)
    frame_obj.layout().setContentsMargins(0, 0, 0, 0)
    # -------------------------------------------------------------------------------------------------------------
    # define actions
    scroll_obj.valueChanged.connect(lambda: recalculate_range(ui_obj=ui_obj, scrolbaer_obj=scroll_obj, checkbox_obj=checkbox_obj, chart_postfix=chart_postfix))
    #                                                              
    checkbox_obj.stateChanged.connect(lambda: state_changed(checkbox_obj=checkbox_obj, ui_obj=ui_obj,
                                        scrolbaer_obj=scroll_obj, axisX_obj=eval('ui_obj.axisX_%s' % chart_postfix)))
    

# clear series
def clear_series_date(chart_postfixes, ui_obj):
    for chart_postfix in chart_postfixes:
        eval('ui_obj.train_line_series_%s' % chart_postfix).clear()
        eval('ui_obj.train_scatter_series_1_%s' % chart_postfix).clear()
        eval('ui_obj.train_scatter_series_2_%s' % chart_postfix).clear()
        eval('ui_obj.val_line_series_%s' % chart_postfix).clear()
        eval('ui_obj.val_scatter_series_1_%s' % chart_postfix).clear()
        eval('ui_obj.val_scatter_series_2_%s' % chart_postfix).clear()


# reset axisX range
def recalculate_range(ui_obj, checkbox_obj, scrolbaer_obj, chart_postfix):
    if not checkbox_obj.isChecked():
        scrollbar_obj = scrolbaer_obj
        axisX_obj = eval('ui_obj.axisX_%s' % chart_postfix)
        xmin = scrollbar_obj.value()
        xmax = scrollbar_obj.value() + axisX_range
        axisX_obj.setRange(xmin+1, xmax)
    else:
        scrolbaer_obj.setMaximum(0)
        scrolbaer_obj.setValue(0)


# append new data to chart
def append_data_to_chart(ui_obj, chart_postfix, train_x_series, train_y_series, val_x_series, val_y_series):
    # append the last comming history (data) to chart
    eval('ui_obj.train_line_series_%s' % chart_postfix).append(sQPointF(float(train_x_series), float(train_y_series)))
    eval('ui_obj.train_scatter_series_1_%s' % chart_postfix).append(sQPointF(float(train_x_series), float(train_y_series)))
    eval('ui_obj.train_scatter_series_2_%s' % chart_postfix).append(sQPointF(float(train_x_series), float(train_y_series)))
    eval('ui_obj.val_line_series_%s' % chart_postfix).append(sQPointF(float(val_x_series), float(val_y_series)))
    eval('ui_obj.val_scatter_series_1_%s' % chart_postfix).append(sQPointF(float(val_x_series), float(val_y_series)))
    eval('ui_obj.val_scatter_series_2_%s' % chart_postfix).append(sQPointF(float(val_x_series), float(val_y_series)))


# function to change chart view
def state_changed(ui_obj, checkbox_obj, scrolbaer_obj, axisX_obj):
    nepoch, last_epoch = get_nepochs_and_lastepoch()
    if checkbox_obj.isChecked():
        scrolbaer_obj.setMaximum(0)
        scrolbaer_obj.setValue(0)
        axisX_obj.setRange(1, nepoch)
        axisX_obj.setTickCount(nepoch)
        # axisX_obj.setLabelsFont(sQFont("Times", 4, sQFont.Normal))
    else:
        axisX_obj.setTickCount(axisX_range)
        if (last_epoch//axisX_range - 1)*axisX_range + (last_epoch%axisX_range) >= 0:
            scrolbaer_obj.setMaximum((last_epoch//axisX_range - 1)*axisX_range + (last_epoch%axisX_range)+1)
            scrolbaer_obj.setValue((last_epoch//axisX_range - 1)*axisX_range + (last_epoch%axisX_range)+1)
        else:
            axisX_obj.setRange(1, axisX_range)
            scrolbaer_obj.setMaximum(0)
            scrolbaer_obj.setValue(0)


def get_nepochs_and_lastepoch():
    return numepoch, epochitr


def update_axisX_range(ui_obj, nepoch):
    global numepoch
    numepoch = nepoch
    global epochitr
    epochitr = 0


def update_chart_test(ui_obj, chart_postfixes, scroll_obj):
    nepoch, last_epoch = get_nepochs_and_lastepoch()
    while last_epoch <= nepoch-1:
        #
        if last_epoch >= axisX_range and not ui_obj.binary_chart_checkbox.isChecked(): 
            scroll_obj.setMaximum(((last_epoch+1)//axisX_range - 1)*axisX_range + ((last_epoch+1)%axisX_range))
            scroll_obj.setValue(((last_epoch+1)//axisX_range - 1)*axisX_range + ((last_epoch+1)%axisX_range))
        #
        cv2.waitKey(1000)
        for chart_postfix in chart_postfixes:
            append_data_to_chart(ui_obj=ui_obj, chart_postfix=chart_postfix, train_x_series=load[last_epoch], train_y_series=eff_train[last_epoch],
                                    val_x_series=load[last_epoch], val_y_series=eff_val[last_epoch])
        #
        global epochitr
        epochitr += 1
        nepoch, last_epoch = get_nepochs_and_lastepoch()


def update_chart(ui_obj, chart_postfixes, last_epoch, logs, scroll_obj, chart_type='binary'):
    if chart_type == 'binary':
        params = [logs['loss'], logs['accuracy']*100, logs['Recall']*100, logs['Precision']*100, logs['val_loss'], logs['val_accuracy']*100, logs['val_Recall']*100, logs['val_Precision']*100]
    elif chart_type == 'localization':
        params = [logs['loss'], logs['accuracy']*100, logs['iou_score']*100, logs['f1-score']*100, logs['val_loss'], logs['val_accuracy']*100, logs['val_iou_score']*100, logs['val_f1-score']*100]
    elif chart_type == 'yolo':
        params = [logs['train/box_loss'], logs['train/obj_loss'], logs['train/cls_loss'],
                  110, 110, 110,
                  logs['val/box_loss'], logs['val/obj_loss'], logs['val/cls_loss'],
                  logs['metrics/recall']*100, logs['metrics/precision']*100, logs['metrics/mAP_0.5']*100]

    if last_epoch >= axisX_range and not ui_obj.binary_chart_checkbox.isChecked():
        scroll_obj.setMaximum(((last_epoch+1)//axisX_range - 1)*axisX_range + ((last_epoch+1)%axisX_range))
        scroll_obj.setValue(((last_epoch+1)//axisX_range - 1)*axisX_range + ((last_epoch+1)%axisX_range))
    #
    for i, chart_postfix in enumerate(chart_postfixes):
        append_data_to_chart(ui_obj=ui_obj, chart_postfix=chart_postfix, train_x_series=last_epoch, train_y_series=params[i],
                                val_x_series=last_epoch, val_y_series=params[i+len(chart_postfixes)])
    #

    global epochitr
    epochitr = last_epoch


#_____________________________________________________________________________________________________________________
perfect_color = '#4dbf4d'
defect_color = '#ff0000'
pie_background_color = '#282c34'
pie_label_color = '#FFFFFF'
pie_label_color2 = '#000000'
pie_pen_width = 8

# pie chart for class list page
def create_classlist_piechart_on_ui(ui_obj, frame_obj_binary, frame_obj_classlist, chart_title='Chart', binary_hole_size=0.2):
    """this function is used to create classification list page picharts (one for binary and one for defects)

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param frame_obj_binary: frame object of binary chart
    :type frame_obj_binary: _type_
    :param frame_obj_classlist: frame object of classification/defects chart
    :type frame_obj_classlist: _type_
    :param chart_title: _description_, defaults to 'Chart'
    :type chart_title: str, optional
    :param binary_hole_size: center hole size of the piechart, defaults to 0.2
    :type binary_hole_size: float, optional
    """

    # creat chart
    # binary
    ui_obj.binary_piechart = sQChart()
    ui_obj.binary_piechart.setAnimationOptions(sQChart.SeriesAnimations)
    ui_obj.binary_piechart.setMargins(sQMargins(0,0,0,0))
    #ui_obj.binary_piechart.setTitle(chart_title)
    #ui_obj.binary_piechart.setTheme(sQChart.ChartThemeDark)
    ui_obj.binary_piechart.legend().setVisible(False)
    ui_obj.binary_piechart.setBackgroundBrush(sQColor(pie_background_color))

    # classes
    ui_obj.classlist_piechart = sQChart()
    ui_obj.classlist_piechart.setAnimationOptions(sQChart.SeriesAnimations)
    ui_obj.classlist_piechart.setMargins(sQMargins(0,0,0,0))
    #ui_obj.classlist_piechart.setTitle(chart_title)
    #ui_obj.classlist_piechart.setTheme(sQChart.ChartThemeDark)
    ui_obj.classlist_piechart.legend().setVisible(False)
    ui_obj.classlist_piechart.setBackgroundBrush(sQColor(pie_background_color))

    # binary series
    ui_obj.classlist_pie_binary_series = sQPieSeries()
    ui_obj.classlist_pie_binary_series.setHoleSize(binary_hole_size)
    #ui_obj.pseries.setPieSize(0.2)
    # classlist series
    ui_obj.classlist_pie_cls_series = sQPieSeries()
    ui_obj.classlist_pie_cls_series.setHoleSize(binary_hole_size)
    # a = ui_obj.classlist_pie_cls_series.append('a', 1)
    # a.setLabelFont
    
    # add series to chart
    ui_obj.binary_piechart.addSeries(ui_obj.classlist_pie_binary_series)
    ui_obj.classlist_piechart.addSeries(ui_obj.classlist_pie_cls_series)
    
    # set to ui
    ui_obj.binary_piechartview = sQChartView(ui_obj.binary_piechart)
    ui_obj.binary_piechartview.setContentsMargins(0,0,0,0)
    ui_obj.classlist_piechartview = sQChartView(ui_obj.classlist_piechart)
    ui_obj.classlist_piechartview.setContentsMargins(0,0,0,0)
    #
    pievbox = sQVBoxLayout()
    pievbox.addWidget(ui_obj.binary_piechartview)
    pievbox.setContentsMargins(0, 0, 0, 0)
    #
    pievbox2 = sQVBoxLayout()
    pievbox2.addWidget(ui_obj.classlist_piechartview)
    pievbox2.setContentsMargins(0, 0, 0, 0)
    #
    frame_obj_binary.setLayout(pievbox)
    frame_obj_binary.layout().setContentsMargins(0, 0, 0, 0)
    #
    frame_obj_classlist.setLayout(pievbox2)
    frame_obj_classlist.layout().setContentsMargins(0, 0, 0, 0)

    ui_obj.logger.create_new_log(message=texts.MESSEGES['clslist_piechart_created']['en'],
                                code=texts_codes.SubTypes['clslist_piechart_created'],
                                level=1
                                )


# update pie chart
def update_classlist_piechart(ui_obj, binary_len, classes_len, classes_list):
    """this function is used to update classificationlist piechart

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param binary_len: count of perfect and defect images
    :type binary_len: dict
    :param classes_len: count of images related to each defect
    :type classes_len: dict
    :param classes_list: _description_
    :type classes_list: _type_
    """

    ui_obj.classlist_pie_binary_series.clear()
    ui_obj.classlist_pie_cls_series.clear()

    try:
        # binary
        # convert len to percentage
        perfect_percentage = binary_len[dataset.PERFECT_FOLDER] / (binary_len[dataset.PERFECT_FOLDER] + binary_len[dataset.DEFECT_FOLDER])
        defect_percentage = binary_len[dataset.DEFECT_FOLDER] / (binary_len[dataset.PERFECT_FOLDER] + binary_len[dataset.DEFECT_FOLDER])

        # append to series
        my_slice = ui_obj.classlist_pie_binary_series.append("defect: {} ({:.1f}%)".format(binary_len[dataset.DEFECT_FOLDER], defect_percentage*100), defect_percentage)
        if defect_percentage != 0.0:
            my_slice.setLabelVisible(True)
            my_slice.setLabelColor(sQColor(pie_label_color))
            my_slice.setPen(sQPen(sQColor(pie_background_color), pie_pen_width))
            my_slice.setBrush(sQColor(defect_color))

        my_slice = ui_obj.classlist_pie_binary_series.append("perfect: {} ({:.1f}%)".format(binary_len[dataset.PERFECT_FOLDER], perfect_percentage*100), perfect_percentage)
        if perfect_percentage != 0.0:
            my_slice.setLabelVisible(True)
            my_slice.setLabelColor(sQColor(pie_label_color))
            my_slice.setPen(sQPen(sQColor(pie_background_color), pie_pen_width))
            my_slice.setBrush(sQColor(perfect_color))

        # classes
        # convert len to percentage
        ##print('defects', classes_list)
        for cls in classes_list:
            cls_id = str(cls['defect_ID'])
            #

            if cls_id in classes_len.keys():
                percentage = classes_len[cls_id] / sum(classes_len.values())
            else:
                percentage = 0.0
            #
            
            try:
                my_slice = ui_obj.classlist_pie_cls_series.append(cls['short_name']+': {} ({:.1f}%)'.format(classes_len[cls_id], percentage*100), percentage)
            except:
                my_slice = ui_obj.classlist_pie_cls_series.append(cls['short_name']+': {} ({:.1f}%)'.format(0, 0.0), percentage)
            #
            if percentage != 0.0:
                my_slice.setLabelVisible(True)
                my_slice.setLabelColor(sQColor(pie_label_color))
                my_slice.setPen(sQPen(sQColor(pie_background_color), pie_pen_width))
                my_slice.setBrush(sQColor(cls['color']))


            # my_slice = series.append("Fat 15.6%", 15.6)
            # my_slice.setExploded(True)
            # my_slice.setLabelVisible(True)
    
    except Exception as e:
        ui_obj.logger.create_new_log(message=texts.ERRORS['update_classlist_piechart_failed']['en'],
                                    code=texts_codes.SubTypes['update_classlist_piechart_failed'],
                                    level=5)
        return


# pie chart for binarylist page
def create_binarylist_piechart_on_ui(ui_obj, frame_obj_binary, chart_title='Chart', binary_hole_size=0.2):
    """this function is used to create binary list page pichart

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param frame_obj_binary: frame object of binary chart
    :type frame_obj_binary: _type_
    :param chart_title: _description_, defaults to 'Chart'
    :type chart_title: str, optional
    :param binary_hole_size: center hole size of the piechart, defaults to 0.2
    :type binary_hole_size: float, optional
    """
    
    # creat chart
    # binary
    ui_obj.binarylist_piechart = sQChart()
    ui_obj.binarylist_piechart.setAnimationOptions(sQChart.SeriesAnimations)
    ui_obj.binarylist_piechart.setMargins(sQMargins(0,0,0,0))
    #ui_obj.binary_piechart.setTitle(chart_title)
    #ui_obj.binary_piechart.setTheme(sQChart.ChartThemeDark)
    ui_obj.binarylist_piechart.legend().setVisible(False)
    ui_obj.binarylist_piechart.setBackgroundBrush(sQColor(pie_background_color))

    # binary series
    ui_obj.pie_binarylist_series = sQPieSeries()
    ui_obj.pie_binarylist_series.setHoleSize(binary_hole_size)
    #ui_obj.pseries.setPieSize(0.2)
    # a = ui_obj.classlist_pie_cls_series.append('a', 1)
    # a.setLabelFont
    
    # add series to chart
    ui_obj.binarylist_piechart.addSeries(ui_obj.pie_binarylist_series)
    
    # set to ui
    ui_obj.binarylist_piechartview = sQChartView(ui_obj.binarylist_piechart)
    ui_obj.binarylist_piechartview.setContentsMargins(0,0,0,0)
    #
    bpievbox = sQVBoxLayout()
    bpievbox.addWidget(ui_obj.binarylist_piechartview)
    bpievbox.setContentsMargins(0, 0, 0, 0)
    #
    frame_obj_binary.setLayout(bpievbox)
    frame_obj_binary.layout().setContentsMargins(0, 0, 0, 0)

    ui_obj.logger.create_new_log(message=texts.MESSEGES['binarylist_piechart_created']['en'],
                                code=texts_codes.SubTypes['binarylist_piechart_created'],
                                level=1)

# update binarylist pie chart
def update_binarylist_piechart(ui_obj, binary_len):
    """this function is used to update binarylist piechart

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param binary_len: count of defect/perfect images
    :type binary_len: list of dicts
    """
    ui_obj.pie_binarylist_series.clear()

    try:
        # binary
        # convert len to percentage
        if (binary_len[dataset.PERFECT_FOLDER] + binary_len[dataset.DEFECT_FOLDER]) != 0:
            perfect_percentage = binary_len[dataset.PERFECT_FOLDER] / (binary_len[dataset.PERFECT_FOLDER] + binary_len[dataset.DEFECT_FOLDER])
            defect_percentage = binary_len[dataset.DEFECT_FOLDER] / (binary_len[dataset.PERFECT_FOLDER] + binary_len[dataset.DEFECT_FOLDER])
        else:
            perfect_percentage = 0
            defect_percentage = 0

        # append to series
        my_slice = ui_obj.pie_binarylist_series.append("{:.1f}%".format(defect_percentage*100), defect_percentage)
        if defect_percentage != 0.0:
            my_slice.setLabelVisible(True)
            my_slice.setLabelColor(sQColor(pie_label_color2))
            my_slice.setPen(sQPen(sQColor(pie_background_color), pie_pen_width))
            my_slice.setBrush(sQColor(defect_color))

        my_slice = ui_obj.pie_binarylist_series.append("{:.1f}%".format(perfect_percentage*100), perfect_percentage)
        if perfect_percentage != 0.0:
            my_slice.setLabelVisible(True)
            my_slice.setLabelColor(sQColor(pie_label_color2))
            my_slice.setPen(sQPen(sQColor(pie_background_color), pie_pen_width))
            my_slice.setBrush(sQColor(perfect_color))
        
        ui_obj.pie_binarylist_series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
    
    except Exception as e:
        ui_obj.logger.create_new_log(message=texts.ERRORS['update_binarylist_piechart_failed']['en'],
                                    code=texts_codes.SubTypes['update_binarylist_piechart_failed'],
                                    level=5)
        return


def create_binarylist_barchart_on_ui(ui_obj, frame_obj_binary, chart_title='Chart'):
    # creat chart
    # binary
    ui_obj.binary_barchart_bl = sQChart()
    ui_obj.binary_barchart_bl.setAnimationOptions(sQChart.SeriesAnimations)
    ui_obj.binary_barchart_bl.setMargins(sQMargins(0, 0, 0, 0))
    # ui_obj.binary_barchart.setTitle(chart_title)
    # ui_obj.binary_barchart.setTheme(sQChart.ChartThemeDark)
    ui_obj.binary_barchart_bl.legend().setVisible(False)
    ui_obj.binary_barchart_bl.setBackgroundBrush(sQColor(pie_background_color))

    # binary series
    ui_obj.bar_binary_series_bl = sQBarSeries()
    # ui_obj.bar_binary_series_pro.setHoleSize(binary_hole_size)
    # ui_obj.pseries.setbarSize(0.2)
    # a = ui_obj.classlist_bar_cls_series.append('a', 1)
    # a.setLabelFont

    # add series to chart
    ui_obj.binary_barchart_bl.addSeries(ui_obj.bar_binary_series_bl)

    # set to ui
    ui_obj.binary_barchartview_bl = sQChartView(ui_obj.binary_barchart_bl)
    ui_obj.binary_barchartview_bl.setContentsMargins(0, 0, 0, 0)
    #
    bbarvbox = sQVBoxLayout()
    bbarvbox.addWidget(ui_obj.binary_barchartview_bl)
    bbarvbox.setContentsMargins(0, 0, 0, 0)
    #
    frame_obj_binary.setLayout(bbarvbox)
    frame_obj_binary.layout().setContentsMargins(0, 0, 0, 0)


def update_binarylist_barchart(ui_obj, binary_len):
    ui_obj.bar_binary_series_bl.clear()
    m = max(binary_len.values())
    categories = ['معیوب', 'سالم'] if ui_obj.language=='fa' else list(binary_len.keys())
    ui_obj.axisX = QBarCategoryAxis()
    ui_obj.axisX.append(categories)
    ui_obj.binary_barchart_bl.setAxisX(ui_obj.axisX, ui_obj.bar_binary_series_bl)
    ui_obj.axisX.setLabelsColor(sQColor(pie_label_color))

    ui_obj.axisY = QValueAxis()
    ui_obj.binary_barchart_bl.setAxisY(ui_obj.axisY, ui_obj.bar_binary_series_bl)
    ui_obj.axisY.setRange(0, m)
    ui_obj.axisY.setTickInterval(2)
    ui_obj.axisY.setLabelsColor(sQColor(pie_label_color))

    set0 = QBarSet('defects')

    for d in binary_len:
        p = binary_len[d]
        set0.append(p)
        
    set0.setBrush(sQColor(bar_color))

    ui_obj.bar_binary_series_bl.append(set0)


def create_userprofile_piechart_on_ui(ui_obj, frame_obj_binary, chart_title='Chart', binary_hole_size=0.2):
    # creat chart
    # binary
    ui_obj.binary_piechart_pro = sQChart()
    ui_obj.binary_piechart_pro.setAnimationOptions(sQChart.SeriesAnimations)
    ui_obj.binary_piechart_pro.setMargins(sQMargins(0, 0, 0, 0))
    # ui_obj.binary_piechart.setTitle(chart_title)
    # ui_obj.binary_piechart.setTheme(sQChart.ChartThemeDark)
    ui_obj.binary_piechart_pro.legend().setVisible(False)
    ui_obj.binary_piechart_pro.setBackgroundBrush(sQColor(pie_background_color))

    # binary series
    ui_obj.pie_binary_series_pro = sQPieSeries()
    ui_obj.pie_binary_series_pro.setHoleSize(binary_hole_size)
    # ui_obj.pseries.setPieSize(0.2)
    # a = ui_obj.classlist_pie_cls_series.append('a', 1)
    # a.setLabelFont

    # add series to chart
    ui_obj.binary_piechart_pro.addSeries(ui_obj.pie_binary_series_pro)

    # set to ui
    ui_obj.binary_piechartview_pro = sQChartView(ui_obj.binary_piechart_pro)
    ui_obj.binary_piechartview_pro.setContentsMargins(0, 0, 0, 0)
    #
    bpievbox = sQVBoxLayout()
    bpievbox.addWidget(ui_obj.binary_piechartview_pro)
    bpievbox.setContentsMargins(0, 0, 0, 0)
    #
    frame_obj_binary.setLayout(bpievbox)
    frame_obj_binary.layout().setContentsMargins(0, 0, 0, 0)


def update_userprofile_piechart(ui_obj, binary_len):
    ui_obj.pie_binary_series_pro.clear()

    try:
        # binary
        # convert len to percentage
        perfect_percentage = binary_len[dataset.PERFECT_FOLDER] / (
                    binary_len[dataset.PERFECT_FOLDER] + binary_len[dataset.DEFECT_FOLDER])
        defect_percentage = binary_len[dataset.DEFECT_FOLDER] / (
                    binary_len[dataset.PERFECT_FOLDER] + binary_len[dataset.DEFECT_FOLDER])
        # append to series
        my_slice = ui_obj.pie_binary_series_pro.append(
            "{} {} ({:.1f}%)".format(texts.Titles['defect2'][ui_obj.language], binary_len[dataset.DEFECT_FOLDER], defect_percentage * 100),
            defect_percentage)
        if defect_percentage != 0.0:
            my_slice.setLabelVisible(True)
            my_slice.setLabelColor(sQColor(pie_label_color))
            my_slice.setPen(sQPen(sQColor(pie_background_color), pie_pen_width))
            my_slice.setBrush(sQColor(defect_color))

        my_slice = ui_obj.pie_binary_series_pro.append(
            "{} {} ({:.1f}%)".format(texts.Titles['perfect'][ui_obj.language], binary_len[dataset.PERFECT_FOLDER], perfect_percentage * 100),
            perfect_percentage)
        if perfect_percentage != 0.0:
            my_slice.setLabelVisible(True)
            my_slice.setLabelColor(sQColor(pie_label_color))
            my_slice.setPen(sQPen(sQColor(pie_background_color), pie_pen_width))
            my_slice.setBrush(sQColor(perfect_color))

    except:
        return


def create_userprofile_barchart_on_ui(ui_obj, frame_obj_binary, chart_title='Chart'):
    # creat chart
    # binary
    ui_obj.binary_barchart_pro = sQChart()
    ui_obj.binary_barchart_pro.setAnimationOptions(sQChart.SeriesAnimations)
    ui_obj.binary_barchart_pro.setMargins(sQMargins(0, 0, 0, 0))
    # ui_obj.binary_barchart.setTitle(chart_title)
    # ui_obj.binary_barchart.setTheme(sQChart.ChartThemeDark)
    ui_obj.binary_barchart_pro.legend().setVisible(False)
    ui_obj.binary_barchart_pro.setBackgroundBrush(sQColor(pie_background_color))

    # binary series
    ui_obj.bar_binary_series_pro = sQBarSeries()
    # ui_obj.bar_binary_series_pro.setHoleSize(binary_hole_size)
    # ui_obj.pseries.setbarSize(0.2)
    # a = ui_obj.classlist_bar_cls_series.append('a', 1)
    # a.setLabelFont

    # add series to chart
    ui_obj.binary_barchart_pro.addSeries(ui_obj.bar_binary_series_pro)

    # set to ui
    ui_obj.binary_barchartview_pro = sQChartView(ui_obj.binary_barchart_pro)
    ui_obj.binary_barchartview_pro.setContentsMargins(0, 0, 0, 0)
    #
    bbarvbox = sQVBoxLayout()
    bbarvbox.addWidget(ui_obj.binary_barchartview_pro)
    bbarvbox.setContentsMargins(0, 0, 0, 0)
    #
    frame_obj_binary.setLayout(bbarvbox)
    frame_obj_binary.layout().setContentsMargins(0, 0, 0, 0)


def update_userprofile_barchart(ui_obj, classification_len):
    ui_obj.bar_binary_series_pro.clear()

    total = classification_len['total']
    if total == 0:
        return
    del (classification_len['total'])

    categories = list(classification_len.keys())
    ui_obj.axisX = QBarCategoryAxis()
    ui_obj.axisX.append(categories)
    ui_obj.binary_barchart_pro.setAxisX(ui_obj.axisX, ui_obj.bar_binary_series_pro)
    ui_obj.axisX.setLabelsColor(sQColor(pie_label_color))

    ui_obj.axisY = QValueAxis()
    ui_obj.binary_barchart_pro.setAxisY(ui_obj.axisY, ui_obj.bar_binary_series_pro)
    ui_obj.axisY.setRange(0, 100)
    ui_obj.axisY.setLabelsColor(sQColor(pie_label_color))

    set0 = QBarSet('defects')

    for d in classification_len:
        p = (classification_len[d] / total) * 100
        set0.append(p)
        
    set0.setBrush(sQColor(bar_color))

    ui_obj.bar_binary_series_pro.append(set0)


def clear_userprofile_barchart(ui_obj):
    try:
        ui_obj.binary_barchart_pro.removeAxis(ui_obj.axisX)
        ui_obj.binary_barchart_pro.removeAxis(ui_obj.axisY)
        ui_obj.bar_binary_series_pro.clear()
        ui_obj.pie_binary_series_pro.clear()
    except:
        pass


def create_label_piechart_on_ui(ui_obj, frame_obj_binary, chart_title='Chart', binary_hole_size=0.2):
    # creat chart
    # binary
    ui_obj.binary_piechart_label = sQChart()
    ui_obj.binary_piechart_label.setAnimationOptions(sQChart.SeriesAnimations)
    ui_obj.binary_piechart_label.setMargins(sQMargins(0, 0, 0, 0))
    # ui_obj.binary_piechart.setTitle(chart_title)
    # ui_obj.binary_piechart.setTheme(sQChart.ChartThemeDark)
    ui_obj.binary_piechart_label.legend().setVisible(False)
    ui_obj.binary_piechart_label.setBackgroundBrush(sQColor(pie_background_color))

    # binary series
    ui_obj.pie_binary_series_label = sQPieSeries()
    ui_obj.pie_binary_series_label.setHoleSize(binary_hole_size)
    # ui_obj.pseries.setPieSize(0.2)
    # a = ui_obj.classlist_pie_cls_series.append('a', 1)
    # a.setLabelFont

    # add series to chart
    ui_obj.binary_piechart_label.addSeries(ui_obj.pie_binary_series_label)

    # set to ui
    ui_obj.binary_piechartview_label = sQChartView(ui_obj.binary_piechart_label)
    ui_obj.binary_piechartview_label.setContentsMargins(0, 0, 0, 0)
    #
    bpievbox = sQVBoxLayout()
    bpievbox.addWidget(ui_obj.binary_piechartview_label)
    bpievbox.setContentsMargins(0, 0, 0, 0)
    #
    frame_obj_binary.setLayout(bpievbox)
    frame_obj_binary.layout().setContentsMargins(0, 0, 0, 0)


def update_label_piechart(ui_obj, binary_len):
    ui_obj.pie_binary_series_label.clear()

    try:
        # binary
        # convert len to percentage
        perfect_percentage = binary_len[dataset.PERFECT_FOLDER] / (
                    binary_len[dataset.PERFECT_FOLDER] + binary_len[dataset.DEFECT_FOLDER])
        defect_percentage = binary_len[dataset.DEFECT_FOLDER] / (
                    binary_len[dataset.PERFECT_FOLDER] + binary_len[dataset.DEFECT_FOLDER])
        # append to series
        my_slice = ui_obj.pie_binary_series_label.append(
            "{:.1f}%".format(defect_percentage * 100),
            defect_percentage)
        if defect_percentage != 0.0:
            my_slice.setLabelVisible(True)
            my_slice.setLabelColor(sQColor(pie_label_color2))
            my_slice.setPen(sQPen(sQColor(pie_background_color), pie_pen_width))
            my_slice.setBrush(sQColor(defect_color))

        my_slice = ui_obj.pie_binary_series_label.append(
            "{:.1f}%".format(perfect_percentage * 100),
            perfect_percentage)
        if perfect_percentage != 0.0:
            my_slice.setLabelVisible(True)
            my_slice.setLabelColor(sQColor(pie_label_color2))
            my_slice.setPen(sQPen(sQColor(pie_background_color), pie_pen_width))
            my_slice.setBrush(sQColor(perfect_color))


        ui_obj.pie_binary_series_label.setLabelsPosition(QPieSlice.LabelInsideHorizontal)

    except:
        return


def create_storage_barchart_on_ui(ui_obj, frame_obj_storage, storage_type, chart_title='Storage Status'):
    # creat chart
    # binary
    exec('ui_obj.{}_storage_barchart = sQChart()'.format(storage_type))
    # ui_obj.storage_barchart.setAnimationOptions(sQChart.SeriesAnimations)
    exec('ui_obj.{}_storage_barchart.setMargins(sQMargins(0, 0, 0, 0))'.format(storage_type))
    exec('ui_obj.{}_storage_barchart.layout().setContentsMargins(0, 0, 0, 0)'.format(storage_type))
    # ui_obj.binary_barchart.setTitle(chart_title)
    # ui_obj.binary_barchart.setTheme(sQChart.ChartThemeDark)
    exec('ui_obj.{}_storage_barchart.legend().setVisible(False)'.format(storage_type))
    # exec('ui_obj.{}_storage_barchart.legend().setAlignment(Qt.AlignRight)'.format(storage_type))
    # exec('ui_obj.{}_storage_barchart.legend().setLabelBrush(sQColor(pie_label_color))'.format(storage_type))
    exec('ui_obj.{}_storage_barchart.setBackgroundBrush(sQColor("#14165c"))'.format(storage_type))
    exec('ui_obj.{}_storage_barchart.setBackgroundRoundness(0)'.format(storage_type))

    # binary series
    exec('ui_obj.bar_{}_storage_series = sQHorizontalPercentBarSeries()'.format(storage_type))

    # add series to chart
    exec('ui_obj.{}_storage_barchart.addSeries(ui_obj.bar_{}_storage_series)'.format(storage_type, storage_type))

    # set to ui
    exec('ui_obj.{}_storage_barchartview = sQChartView(ui_obj.{}_storage_barchart)'.format(storage_type, storage_type))
    exec('ui_obj.{}_storage_barchartview.setContentsMargins(0, 0, 0, 0)'.format(storage_type))
    #
    
    exec('frame_obj_storage.layout().addWidget(ui_obj.{}_storage_barchartview)'.format(storage_type, storage_type))


def update_storage_barchart(ui_obj, storage_type, storage_status):
    exec('ui_obj.bar_{}_storage_series.clear()'.format(storage_type))
    
    categories = list(storage_status.keys())
    # ui_obj.axisX = QBarCategoryAxis()
    # ui_obj.axisX.append(categories)
    # exec('ui_obj.{}_storage_barchart.setAxisY(ui_obj.axisX, ui_obj.bar_{}_storage_series)'.format(storage_type, storage_type))
    # ui_obj.axisX.setLabelsColor(sQColor(pie_label_color))
    # ui_obj.axisX.setLabelsVisible(False)

    # ui_obj.axisY = QValueAxis()
    # exec('ui_obj.{}_storage_barchart.setAxisX(ui_obj.axisY, ui_obj.bar_{}_storage_series)'.format(storage_type, storage_type))
    # ui_obj.axisY.setRange(0, 100)
    # ui_obj.axisY.setLabelsColor(sQColor(pie_label_color))
    # ui_obj.axisY.setLabelsFont(sQFont("Times", 5, sQFont.Normal))

    set0 = QBarSet('Used')
    set1 = QBarSet('Free')

    for k in categories:
        set0.append(storage_status[k]['Used'])
        set1.append(storage_status[k]['Free'])

    set0.setBrush(sQColor(defect_color))
    set1.setBrush(sQColor(perfect_color))

    exec('ui_obj.bar_{}_storage_series.append(set0)'.format(storage_type))
    exec('ui_obj.bar_{}_storage_series.append(set1)'.format(storage_type))


# # chart (must be add in main_ui.py)
# # chart ---------------------------------------------------------------------------------------------
# chart_funcs.create_train_chart_on_ui(ui_obj=self, frame_obj=self.frame_chart, hover_label_obj=self.label_chart, chart_postfix='accuracy', chart_title='chart', legend_train='legend1', legend_val='legend2',
#                     axisX_title='epoch', axisY_title='Accuracy', checkbox_obj=self.checkBox)

# self.pushButton.clicked.connect(partial(lambda: chart_funcs.update_chart(ui_obj=self, chart_postfix='accuracy')))

    

    
    

    
    

    

    

    

    
