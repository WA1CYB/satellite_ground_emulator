#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Ground Test 1
# Author: WA1CYB
# Description: Ground Test 1
# Generated: Sun Oct 22 11:38:00 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from math import sqrt
from optparse import OptionParser
import ConfigParser
import osmosdr
import sip
import sys
import threading
import time


class ground_test_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Ground Test 1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ground Test 1")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ground_test_1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self._sr2_sq_thres_config_config = ConfigParser.ConfigParser()
        self._sr2_sq_thres_config_config.read('default')
        try: sr2_sq_thres_config = self._sr2_sq_thres_config_config.getfloat('main', 'Min Squelch Level sr2')
        except: sr2_sq_thres_config = -12
        self.sr2_sq_thres_config = sr2_sq_thres_config
        self._sr1_sq_thres_config_config = ConfigParser.ConfigParser()
        self._sr1_sq_thres_config_config.read('default')
        try: sr1_sq_thres_config = self._sr1_sq_thres_config_config.getfloat('main', 'Min Squelch Level sr1')
        except: sr1_sq_thres_config = -12
        self.sr1_sq_thres_config = sr1_sq_thres_config
        self.samp_rate_sr1 = samp_rate_sr1 = 100.e6/100
        self.samp_rate = samp_rate = 32000
        self.lo_xmit = lo_xmit = 4.8105e9
        self.atten_in_dB_gr2 = atten_in_dB_gr2 = -70
        self.atten_in_dB = atten_in_dB = -65
        self.test_signal_input = test_signal_input = 0
        self.st1_gain = st1_gain = 25.0
        self.st1_freq = st1_freq = 849.5e6+lo_xmit
        self.sr2_sq_thres_min = sr2_sq_thres_min = sr2_sq_thres_config
        self.sr2_rcv_tun_freq = sr2_rcv_tun_freq = 9896520000
        self.sr2_rcv_rf_tun_gain_if = sr2_rcv_rf_tun_gain_if = 20.0
        self.sr2_rcv_rf_tun_gain = sr2_rcv_rf_tun_gain = 30
        self.sr2_ppm = sr2_ppm = 18.0
        self.sr2_freq_offset = sr2_freq_offset = -9000
        self.sr1_sq_thres_min = sr1_sq_thres_min = sr1_sq_thres_config
        self.sr1_rit = sr1_rit = 0
        self.sr1_gain = sr1_gain = 1.0
        self.sr1_freq = sr1_freq = 446.4e6
        self.sr1_atten_linear = sr1_atten_linear = 1/(10**(-atten_in_dB/20.))
        self.samp_rate_sr2_0 = samp_rate_sr2_0 = samp_rate
        self.samp_rate_sr2 = samp_rate_sr2 = samp_rate_sr1
        self.samp_rate_UHD = samp_rate_UHD = samp_rate_sr1
        self.pseudo_doppler = pseudo_doppler = 0
        self.probed_det_freq_error_with_old = probed_det_freq_error_with_old = 0
        self.probed_det_freq_error = probed_det_freq_error = 0
        self.offset_tone_freq = offset_tone_freq = 0
        self.offset_temp = offset_temp = 0
        
        self.lpf_taps = lpf_taps = firdes.low_pass(1.0, samp_rate_sr1/4, samp_rate_sr1/64, 0.1*samp_rate_sr1/64, firdes.WIN_HAMMING, 6.76)
          
        self.lnb_lo = lnb_lo = 9.75e9
        self.gr2_atten_linear = gr2_atten_linear = 1/(10**(-atten_in_dB_gr2/20.))
        self.enable_feedback = enable_feedback = 0
        self.audio_rate = audio_rate = 48000

        ##################################################
        # Blocks
        ##################################################
        self.sdr_st1_controls = Qt.QTabWidget()
        self.sdr_st1_controls_widget_0 = Qt.QWidget()
        self.sdr_st1_controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_st1_controls_widget_0)
        self.sdr_st1_controls_grid_layout_0 = Qt.QGridLayout()
        self.sdr_st1_controls_layout_0.addLayout(self.sdr_st1_controls_grid_layout_0)
        self.sdr_st1_controls.addTab(self.sdr_st1_controls_widget_0, 'GT1 Transmit Frequency')
        self.sdr_st1_controls_widget_1 = Qt.QWidget()
        self.sdr_st1_controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_st1_controls_widget_1)
        self.sdr_st1_controls_grid_layout_1 = Qt.QGridLayout()
        self.sdr_st1_controls_layout_1.addLayout(self.sdr_st1_controls_grid_layout_1)
        self.sdr_st1_controls.addTab(self.sdr_st1_controls_widget_1, 'GT1 Transmit Gain')
        self.sdr_st1_controls_widget_2 = Qt.QWidget()
        self.sdr_st1_controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_st1_controls_widget_2)
        self.sdr_st1_controls_grid_layout_2 = Qt.QGridLayout()
        self.sdr_st1_controls_layout_2.addLayout(self.sdr_st1_controls_grid_layout_2)
        self.sdr_st1_controls.addTab(self.sdr_st1_controls_widget_2, 'Pseudo Doppler')
        self.sdr_st1_controls_widget_3 = Qt.QWidget()
        self.sdr_st1_controls_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_st1_controls_widget_3)
        self.sdr_st1_controls_grid_layout_3 = Qt.QGridLayout()
        self.sdr_st1_controls_layout_3.addLayout(self.sdr_st1_controls_grid_layout_3)
        self.sdr_st1_controls.addTab(self.sdr_st1_controls_widget_3, 'Test Signals')
        self.top_grid_layout.addWidget(self.sdr_st1_controls, 0,3,1,1)
        self.sdr_sr1_controls = Qt.QTabWidget()
        self.sdr_sr1_controls_widget_0 = Qt.QWidget()
        self.sdr_sr1_controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_sr1_controls_widget_0)
        self.sdr_sr1_controls_grid_layout_0 = Qt.QGridLayout()
        self.sdr_sr1_controls_layout_0.addLayout(self.sdr_sr1_controls_grid_layout_0)
        self.sdr_sr1_controls.addTab(self.sdr_sr1_controls_widget_0, 'GR1 Local Receiver Frequency')
        self.sdr_sr1_controls_widget_1 = Qt.QWidget()
        self.sdr_sr1_controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_sr1_controls_widget_1)
        self.sdr_sr1_controls_grid_layout_1 = Qt.QGridLayout()
        self.sdr_sr1_controls_layout_1.addLayout(self.sdr_sr1_controls_grid_layout_1)
        self.sdr_sr1_controls.addTab(self.sdr_sr1_controls_widget_1, 'GR1 Local Receiver RIT')
        self.sdr_sr1_controls_widget_2 = Qt.QWidget()
        self.sdr_sr1_controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_sr1_controls_widget_2)
        self.sdr_sr1_controls_grid_layout_2 = Qt.QGridLayout()
        self.sdr_sr1_controls_layout_2.addLayout(self.sdr_sr1_controls_grid_layout_2)
        self.sdr_sr1_controls.addTab(self.sdr_sr1_controls_widget_2, 'GR1 Local Receiver Gain')
        self.sdr_sr1_controls_widget_3 = Qt.QWidget()
        self.sdr_sr1_controls_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_sr1_controls_widget_3)
        self.sdr_sr1_controls_grid_layout_3 = Qt.QGridLayout()
        self.sdr_sr1_controls_layout_3.addLayout(self.sdr_sr1_controls_grid_layout_3)
        self.sdr_sr1_controls.addTab(self.sdr_sr1_controls_widget_3, 'GR1 Local Squelch')
        self.top_grid_layout.addWidget(self.sdr_sr1_controls, 0,1,1,1)
        self.rtl_sdr_1_controls = Qt.QTabWidget()
        self.rtl_sdr_1_controls_widget_0 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_0)
        self.rtl_sdr_1_controls_grid_layout_0 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_0.addLayout(self.rtl_sdr_1_controls_grid_layout_0)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_0, 'GR2 X-band Receiver Frequency ')
        self.rtl_sdr_1_controls_widget_1 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_1)
        self.rtl_sdr_1_controls_grid_layout_1 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_1.addLayout(self.rtl_sdr_1_controls_grid_layout_1)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_1, 'GR2 RIT')
        self.rtl_sdr_1_controls_widget_2 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_2)
        self.rtl_sdr_1_controls_grid_layout_2 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_2.addLayout(self.rtl_sdr_1_controls_grid_layout_2)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_2, 'GR2 Receiver Gain')
        self.rtl_sdr_1_controls_widget_3 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_3)
        self.rtl_sdr_1_controls_grid_layout_3 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_3.addLayout(self.rtl_sdr_1_controls_grid_layout_3)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_3, 'GR2 Receiver IF Gain')
        self.rtl_sdr_1_controls_widget_4 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_4)
        self.rtl_sdr_1_controls_grid_layout_4 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_4.addLayout(self.rtl_sdr_1_controls_grid_layout_4)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_4, 'GR2 PPM')
        self.rtl_sdr_1_controls_widget_5 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_5)
        self.rtl_sdr_1_controls_grid_layout_5 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_5.addLayout(self.rtl_sdr_1_controls_grid_layout_5)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_5, 'GR2 Squelch')
        self.top_grid_layout.addWidget(self.rtl_sdr_1_controls, 0,2,1,1)
        self.freq_error_det_0 = blocks.probe_signal_f()
        self.freq_error_det = blocks.probe_signal_f()
        self._test_signal_input_options = (0, 1, 2, )
        self._test_signal_input_labels = ('No Test Signal', 'Wide Band Noise ~ -20 dB', 'Sweep Across Band', )
        self._test_signal_input_tool_bar = Qt.QToolBar(self)
        self._test_signal_input_tool_bar.addWidget(Qt.QLabel('Test Input'+": "))
        self._test_signal_input_combo_box = Qt.QComboBox()
        self._test_signal_input_tool_bar.addWidget(self._test_signal_input_combo_box)
        for label in self._test_signal_input_labels: self._test_signal_input_combo_box.addItem(label)
        self._test_signal_input_callback = lambda i: Qt.QMetaObject.invokeMethod(self._test_signal_input_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._test_signal_input_options.index(i)))
        self._test_signal_input_callback(self.test_signal_input)
        self._test_signal_input_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_test_signal_input(self._test_signal_input_options[i]))
        self.sdr_st1_controls_grid_layout_3.addWidget(self._test_signal_input_tool_bar,  0,0,1,1)
        self._st1_freq_tool_bar = Qt.QToolBar(self)
        self._st1_freq_tool_bar.addWidget(Qt.QLabel('Frequency'+": "))
        self._st1_freq_line_edit = Qt.QLineEdit(str(self.st1_freq))
        self._st1_freq_tool_bar.addWidget(self._st1_freq_line_edit)
        self._st1_freq_line_edit.returnPressed.connect(
        	lambda: self.set_st1_freq(eng_notation.str_to_num(str(self._st1_freq_line_edit.text().toAscii()))))
        self.sdr_st1_controls_grid_layout_0.addWidget(self._st1_freq_tool_bar,  0,0,1,1)
        self._sr2_sq_thres_min_range = Range(-100, 0, 1, sr2_sq_thres_config, 200)
        self._sr2_sq_thres_min_win = RangeWidget(self._sr2_sq_thres_min_range, self.set_sr2_sq_thres_min, 'SR2 min SQ in dB', "counter_slider", float)
        self.rtl_sdr_1_controls_grid_layout_5.addWidget(self._sr2_sq_thres_min_win,  0,0,1,1)
        self._sr2_rcv_tun_freq_range = Range(70e6+lnb_lo, 1700.0e6+lnb_lo, 1, 9896520000, 200)
        self._sr2_rcv_tun_freq_win = RangeWidget(self._sr2_rcv_tun_freq_range, self.set_sr2_rcv_tun_freq, 'SR2 Rcvr Freq (Hz)', "counter", float)
        self.rtl_sdr_1_controls_grid_layout_0.addWidget(self._sr2_rcv_tun_freq_win,  0,0,1,1)
        self._sr2_rcv_rf_tun_gain_if_range = Range(0.0, 45.0, 1, 20.0, 200)
        self._sr2_rcv_rf_tun_gain_if_win = RangeWidget(self._sr2_rcv_rf_tun_gain_if_range, self.set_sr2_rcv_rf_tun_gain_if, 'SR2 Receiver IF Gain', "counter", float)
        self.rtl_sdr_1_controls_grid_layout_3.addWidget(self._sr2_rcv_rf_tun_gain_if_win,  0,0,1,1)
        self._sr2_rcv_rf_tun_gain_range = Range(0, 45, 1, 30, 200)
        self._sr2_rcv_rf_tun_gain_win = RangeWidget(self._sr2_rcv_rf_tun_gain_range, self.set_sr2_rcv_rf_tun_gain, 'SR2 Receiver Gain', "counter", float)
        self.rtl_sdr_1_controls_grid_layout_2.addWidget(self._sr2_rcv_rf_tun_gain_win,  0,0,1,1)
        self._sr2_ppm_range = Range(-100, 100, 1, 18.0, 200)
        self._sr2_ppm_win = RangeWidget(self._sr2_ppm_range, self.set_sr2_ppm, 'SR2 ppm', "counter", float)
        self.rtl_sdr_1_controls_grid_layout_4.addWidget(self._sr2_ppm_win,  0,0,1,1)
        self._sr2_freq_offset_range = Range(-20000, 20000, 1, -9000, 200)
        self._sr2_freq_offset_win = RangeWidget(self._sr2_freq_offset_range, self.set_sr2_freq_offset, "SR2 RIT ", "counter_slider", float)
        self.rtl_sdr_1_controls_grid_layout_1.addWidget(self._sr2_freq_offset_win,  0,0,1,1)
        self._sr1_sq_thres_min_range = Range(-100, 0, 1, sr1_sq_thres_config, 200)
        self._sr1_sq_thres_min_win = RangeWidget(self._sr1_sq_thres_min_range, self.set_sr1_sq_thres_min, 'SR1 min SQ in dB', "counter_slider", float)
        self.sdr_sr1_controls_grid_layout_3.addWidget(self._sr1_sq_thres_min_win,  0,0,1,1)
        self._sr1_rit_range = Range(-30000, 30000, 5.0, 0, 200)
        self._sr1_rit_win = RangeWidget(self._sr1_rit_range, self.set_sr1_rit, "SR1 Receiver RIT", "counter_slider", float)
        self.sdr_sr1_controls_grid_layout_1.addWidget(self._sr1_rit_win,  0,0,1,1)
        self._sr1_gain_range = Range(0.0, 50, 1.0, 1.0, 200)
        self._sr1_gain_win = RangeWidget(self._sr1_gain_range, self.set_sr1_gain, 'RF Gain', "counter_slider", float)
        self.sdr_sr1_controls_grid_layout_2.addWidget(self._sr1_gain_win,  0,0,1,1)
        self._sr1_freq_tool_bar = Qt.QToolBar(self)
        self._sr1_freq_tool_bar.addWidget(Qt.QLabel('Frequency'+": "))
        self._sr1_freq_line_edit = Qt.QLineEdit(str(self.sr1_freq))
        self._sr1_freq_tool_bar.addWidget(self._sr1_freq_line_edit)
        self._sr1_freq_line_edit.returnPressed.connect(
        	lambda: self.set_sr1_freq(eng_notation.str_to_num(str(self._sr1_freq_line_edit.text().toAscii()))))
        self.sdr_sr1_controls_grid_layout_0.addWidget(self._sr1_freq_tool_bar,  0,0,1,1)
        self._pseudo_doppler_options = (0, 1, 2, 3, )
        self._pseudo_doppler_labels = ('Zero Doppler', 'MEO+ +/- 50 kHz', 'MEO  +/- 150 kHz', 'LEO  +/- 250 kHz', )
        self._pseudo_doppler_tool_bar = Qt.QToolBar(self)
        self._pseudo_doppler_tool_bar.addWidget(Qt.QLabel('Pseudo Doppler'+": "))
        self._pseudo_doppler_combo_box = Qt.QComboBox()
        self._pseudo_doppler_tool_bar.addWidget(self._pseudo_doppler_combo_box)
        for label in self._pseudo_doppler_labels: self._pseudo_doppler_combo_box.addItem(label)
        self._pseudo_doppler_callback = lambda i: Qt.QMetaObject.invokeMethod(self._pseudo_doppler_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._pseudo_doppler_options.index(i)))
        self._pseudo_doppler_callback(self.pseudo_doppler)
        self._pseudo_doppler_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_pseudo_doppler(self._pseudo_doppler_options[i]))
        self.sdr_st1_controls_grid_layout_2.addWidget(self._pseudo_doppler_tool_bar,  0,0,1,1)
        
        def _probed_det_freq_error_with_old_probe():
            while True:
                val = self.freq_error_det.level()
                try:
                    self.set_probed_det_freq_error_with_old(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (200))
        _probed_det_freq_error_with_old_thread = threading.Thread(target=_probed_det_freq_error_with_old_probe)
        _probed_det_freq_error_with_old_thread.daemon = True
        _probed_det_freq_error_with_old_thread.start()
            
        
        def _probed_det_freq_error_probe():
            while True:
                val = self.freq_error_det_0.level()
                try:
                    self.set_probed_det_freq_error(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (200))
        _probed_det_freq_error_thread = threading.Thread(target=_probed_det_freq_error_probe)
        _probed_det_freq_error_thread.daemon = True
        _probed_det_freq_error_thread.start()
            
        self._enable_feedback_options = (0, 1, )
        self._enable_feedback_labels = ('Un-Lock', 'Lock Frequency', )
        self._enable_feedback_group_box = Qt.QGroupBox('Enable Feedback')
        self._enable_feedback_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._enable_feedback_button_group = variable_chooser_button_group()
        self._enable_feedback_group_box.setLayout(self._enable_feedback_box)
        for i, label in enumerate(self._enable_feedback_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._enable_feedback_box.addWidget(radio_button)
        	self._enable_feedback_button_group.addButton(radio_button, i)
        self._enable_feedback_callback = lambda i: Qt.QMetaObject.invokeMethod(self._enable_feedback_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._enable_feedback_options.index(i)))
        self._enable_feedback_callback(self.enable_feedback)
        self._enable_feedback_button_group.buttonClicked[int].connect(
        	lambda i: self.set_enable_feedback(self._enable_feedback_options[i]))
        self.top_grid_layout.addWidget(self._enable_feedback_group_box, 2,3,1,1)
        self.uhd_usrp_source_0_0_0 = uhd.usrp_source(
        	",".join(('', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0_0_0.set_subdev_spec('A:0', 0)
        self.uhd_usrp_source_0_0_0.set_samp_rate(samp_rate_sr1)
        self.uhd_usrp_source_0_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0_0_0.set_center_freq(sr1_freq+sr1_rit, 0)
        self.uhd_usrp_source_0_0_0.set_gain(sr1_gain, 0)
        self.uhd_usrp_source_0_0_0.set_antenna('RX2', 0)
        self._st1_gain_range = Range(0.0, 50, 1.0, 25.0, 200)
        self._st1_gain_win = RangeWidget(self._st1_gain_range, self.set_st1_gain, 'RF Gain', "counter_slider", float)
        self.sdr_st1_controls_grid_layout_1.addWidget(self._st1_gain_win,  0,0,1,1)
        self.sr2_dc_iq_offset_0_1_1 = analog.sig_source_c(samp_rate_sr1, analog.GR_CONST_WAVE, -9000., 1, 0)
        self.rational_resampler_xxx_6 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=int(samp_rate_sr1/16)/5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_4_0_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate_sr2),
                decimation=int(samp_rate_sr2/4),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_4_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate_sr1/4),
                decimation=int(samp_rate_sr1),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_4 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate_sr1/4),
                decimation=int(samp_rate_sr1),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_3_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_3 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=25,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0_0_0_0_0_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate_sr1),
                decimation=int(samp_rate_sr1/16),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=audio_rate,
                decimation=int(samp_rate_sr2/4/4)/2,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate_sr2, #bw
        	"LNB Received", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_0_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-80, 0)
        
        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 3,3,1,1)
        self.qtgui_freq_sink_x_3_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate_sr1/4/4, #bw
        	"LNB RF nbfm", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_3_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_3_1.set_y_axis(-140, -20)
        self.qtgui_freq_sink_x_3_1.set_y_label('Relative Gain in dB', '')
        self.qtgui_freq_sink_x_3_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_3_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_3_1.enable_grid(True)
        self.qtgui_freq_sink_x_3_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_3_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_3_1.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_3_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_3_1.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_3_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_3_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_3_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_3_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_3_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_3_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_3_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_3_1_win, 6,3,1,1)
        self.qtgui_freq_sink_x_2_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	st1_freq, #fc
        	samp_rate_sr1, #bw
        	"Uplink Xmtr Input Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_2_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_2_0.set_y_axis(-90, 0)
        self.qtgui_freq_sink_x_2_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_2_0.enable_grid(False)
        self.qtgui_freq_sink_x_2_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_2_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_2_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_2_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_2_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_2_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_2_0_win, 6,0,1,3)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate_sr2/4/25, #bw
        	"Center Lock", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-100, 0)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 1,3,1,1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	sr2_rcv_tun_freq+sr2_freq_offset, #fc
        	samp_rate_sr2, #bw
        	"GR2 (LNB) Input", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 1,1,1,2)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	sr1_freq+sr1_rit, #fc
        	samp_rate_sr1/4, #bw
        	"GR1 Local Input", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 3,1,1,2)
        self.pseudo_doppler_source_0 = analog.sig_source_f(samp_rate_sr2, analog.GR_TRI_WAVE, (1./60)/2, 1, -.5)
        self.pseudo_doppler_source = analog.sig_source_f(samp_rate_sr2, analog.GR_TRI_WAVE, (1./8000), 1, -.5)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate_sr2)
        self.osmosdr_source_0.set_center_freq(sr2_rcv_tun_freq-sr2_freq_offset-offset_temp-lnb_lo, 0)
        self.osmosdr_source_0.set_freq_corr(sr2_ppm, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(sr2_rcv_rf_tun_gain, 0)
        self.osmosdr_source_0.set_if_gain(sr2_rcv_rf_tun_gain_if, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0_2_0_2_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, int(samp_rate_sr1/16), 7500*2, 400, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_2_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, audio_rate, 5e3, 500, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate_sr2/4, 10e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(4, (lpf_taps), -9e3, samp_rate_sr1/4)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        self.blocks_vco_c_0_2_0 = blocks.vco_c(samp_rate_sr2/4, -(22/7)*(502./3), 1)
        self.blocks_vco_c_0_2 = blocks.vco_c(samp_rate_sr1, 2*(22/7)*(2*130e3), .05)
        self.blocks_vco_c_0_1 = blocks.vco_c(samp_rate_sr2, 2*(22/7)*(2*250e3), 1)
        self.blocks_vco_c_0_0 = blocks.vco_c(samp_rate_sr2, 2*(22/7)*(2*150e3), 1)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate_sr2, 2*(22/7)*(2*50e3), 1)
        self.blocks_sample_and_hold_xx_0 = blocks.sample_and_hold_ff()
        self.blocks_null_source_1 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_2 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_1_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_4 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_vcc((1, ))
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_vff((1.0, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc((sr1_atten_linear, ))
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_vff((1, ))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((gr2_atten_linear, ))
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_vff((1, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.1, ))
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_4 = blocks.add_vcc(1)
        self.blks2_selector_1 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=3,
        	num_outputs=1,
        	input_index=test_signal_input,
        	output_index=0,
        )
        self.blks2_selector_0_1 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=enable_feedback,
        	output_index=0,
        )
        self.blks2_selector_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=4,
        	num_outputs=1,
        	input_index=pseudo_doppler,
        	output_index=0,
        )
        self.audio_sink_0_1 = audio.sink(48000, '', True)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self._atten_in_dB_gr2_range = Range(-120, 0, 1, -70, 200)
        self._atten_in_dB_gr2_win = RangeWidget(self._atten_in_dB_gr2_range, self.set_atten_in_dB_gr2, "LNB GR2 Input Atten", "counter_slider", float)
        self.top_grid_layout.addWidget(self._atten_in_dB_gr2_win, 2,2,1,1)
        self._atten_in_dB_range = Range(-120, 0, 1, -65, 200)
        self._atten_in_dB_win = RangeWidget(self._atten_in_dB_range, self.set_atten_in_dB, "GR1 Input Atten", "counter_slider", float)
        self.top_grid_layout.addWidget(self._atten_in_dB_win, 2,1,1,1)
        self.analog_sig_source_x_1_1_0 = analog.sig_source_c(samp_rate_sr1/4, analog.GR_CONST_WAVE, offset_temp, 1, 0)
        self.analog_sig_source_x_1_1 = analog.sig_source_c(samp_rate_sr1, analog.GR_CONST_WAVE, +2**16, .00001, 0)
        self.analog_sig_source_x_0_0_0_0_0 = analog.sig_source_c(samp_rate_sr2/4, analog.GR_CONST_WAVE, offset_tone_freq, 1e-2, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate_sr2/4, analog.GR_CONST_WAVE, -offset_tone_freq, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate_sr2, analog.GR_CONST_WAVE, 0, 1, 0)
        self.analog_rail_ff_0_1 = analog.rail_ff(-1., +1.)
        self.analog_rail_ff_0_0 = analog.rail_ff(-10000, 10000)
        self.analog_rail_ff_0 = analog.rail_ff(-1., +1.)
        self.analog_pwr_squelch_xx_0_0_1 = analog.pwr_squelch_cc((sr2_sq_thres_min), .001, 1, False)
        self.analog_pwr_squelch_xx_0_0_0 = analog.pwr_squelch_cc((sr1_sq_thres_min), .001, 1, False)
        self.analog_nbfm_tx_0_0 = analog.nbfm_tx(
        	audio_rate=int(samp_rate_sr1/16)/5,
        	quad_rate=int(samp_rate_sr1/16),
        	tau=75e-6,
        	max_dev=5.0e3,
        	fh=-1.0,
                )
        self.analog_nbfm_rx_2_0 = analog.nbfm_rx(
        	audio_rate=int(samp_rate_sr1/16)/5,
        	quad_rate=int(samp_rate_sr1/16),
        	tau=75e-6,
        	max_dev=5e3,
          )
        self.analog_nbfm_rx_2 = analog.nbfm_rx(
        	audio_rate=int(samp_rate_sr2/4/4)/2,
        	quad_rate=int(samp_rate_sr2/4/4),
        	tau=75e-6,
        	max_dev=5.e3,
          )
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=samp_rate_sr2/4,
        	audio_decim=8,
        	deviation=10000,
        	audio_pass=1400,
        	audio_stop=3000,
        	gain=1000,
        	tau=0.0,
        )
        self.analog_fastnoise_source_x_1 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, 1, 0, 8192)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, probed_det_freq_error)
        self.analog_const_source_x_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, probed_det_freq_error_with_old)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_agc2_xx_0_0_0_2 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_0_0_2.set_max_gain(16)
        self.analog_agc2_xx_0_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_0.set_max_gain(16)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0_0, 0), (self.analog_pwr_squelch_xx_0_0_0, 0))    
        self.connect((self.analog_agc2_xx_0_0_0_2, 0), (self.analog_pwr_squelch_xx_0_0_1, 0))    
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.analog_const_source_x_0_0, 0), (self.blks2_selector_0_1, 1))    
        self.connect((self.analog_const_source_x_0_0_0_0, 0), (self.blocks_vco_c_0_2_0, 0))    
        self.connect((self.analog_const_source_x_0_0_1, 0), (self.blocks_sample_and_hold_xx_0, 0))    
        self.connect((self.analog_const_source_x_0_1, 0), (self.blks2_selector_0_1, 0))    
        self.connect((self.analog_fastnoise_source_x_1, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.analog_fm_demod_cf_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))    
        self.connect((self.analog_nbfm_rx_2, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.analog_nbfm_rx_2_0, 0), (self.analog_nbfm_tx_0_0, 0))    
        self.connect((self.analog_nbfm_rx_2_0, 0), (self.rational_resampler_xxx_6, 0))    
        self.connect((self.analog_nbfm_tx_0_0, 0), (self.low_pass_filter_0_2_0_2_0_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0_0_0, 0), (self.analog_nbfm_rx_2_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0_0_1, 0), (self.analog_nbfm_rx_2, 0))    
        self.connect((self.analog_rail_ff_0, 0), (self.blocks_float_to_complex_1, 0))    
        self.connect((self.analog_rail_ff_0_0, 0), (self.blocks_multiply_const_vxx_1_1, 0))    
        self.connect((self.analog_rail_ff_0_1, 0), (self.blocks_float_to_complex_1, 1))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blks2_selector_0_0, 0))    
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_1, 1))    
        self.connect((self.analog_sig_source_x_0_0_0_0_0, 0), (self.blocks_multiply_xx_2, 1))    
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blks2_selector_1, 0))    
        self.connect((self.analog_sig_source_x_1_1_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blks2_selector_0_0, 0), (self.rational_resampler_xxx_2, 0))    
        self.connect((self.blks2_selector_0_1, 0), (self.blocks_float_to_char_0, 0))    
        self.connect((self.blks2_selector_1, 0), (self.blocks_add_xx_4, 2))    
        self.connect((self.blocks_add_xx_4, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.analog_rail_ff_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.analog_rail_ff_0_1, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_sample_and_hold_xx_0, 1))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_multiply_xx_4, 1))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blks2_selector_1, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.audio_sink_0_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_freq_sink_x_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_waterfall_sink_x_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.rational_resampler_xxx_3_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.analog_agc2_xx_0_0_0_2, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.qtgui_freq_sink_x_3_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.freq_error_det_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.analog_rail_ff_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_multiply_xx_2, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.qtgui_freq_sink_x_2_0, 0))    
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.analog_fm_demod_cf_0, 0))    
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_null_sink_1_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_multiply_xx_3, 0))    
        self.connect((self.blocks_multiply_xx_2, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_xx_3, 0), (self.rational_resampler_xxx_4_0_0, 0))    
        self.connect((self.blocks_multiply_xx_4, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.blocks_null_source_1, 0), (self.blocks_add_xx_4, 1))    
        self.connect((self.blocks_sample_and_hold_xx_0, 0), (self.freq_error_det, 0))    
        self.connect((self.blocks_vco_c_0, 0), (self.blks2_selector_0_0, 1))    
        self.connect((self.blocks_vco_c_0_0, 0), (self.blks2_selector_0_0, 2))    
        self.connect((self.blocks_vco_c_0_1, 0), (self.blks2_selector_0_0, 3))    
        self.connect((self.blocks_vco_c_0_2, 0), (self.blks2_selector_1, 2))    
        self.connect((self.blocks_vco_c_0_2_0, 0), (self.blocks_multiply_xx_3, 1))    
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0_1, 0))    
        self.connect((self.low_pass_filter_0_2_0, 0), (self.blocks_multiply_const_vxx_0_0_1, 0))    
        self.connect((self.low_pass_filter_0_2_0, 0), (self.blocks_null_sink_2, 0))    
        self.connect((self.low_pass_filter_0_2_0_2_0_0, 0), (self.rational_resampler_xxx_0_0_0_0_0_0_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.rational_resampler_xxx_4_0, 0))    
        self.connect((self.pseudo_doppler_source, 0), (self.blocks_vco_c_0, 0))    
        self.connect((self.pseudo_doppler_source, 0), (self.blocks_vco_c_0_0, 0))    
        self.connect((self.pseudo_doppler_source, 0), (self.blocks_vco_c_0_1, 0))    
        self.connect((self.pseudo_doppler_source_0, 0), (self.blocks_vco_c_0_2, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0_2_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0_0_0_0_0_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.analog_agc2_xx_0_0, 0))    
        self.connect((self.rational_resampler_xxx_2, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.rational_resampler_xxx_3, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.rational_resampler_xxx_3_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))    
        self.connect((self.rational_resampler_xxx_3_0, 0), (self.rational_resampler_xxx_3, 0))    
        self.connect((self.rational_resampler_xxx_4, 0), (self.blocks_add_xx_4, 0))    
        self.connect((self.rational_resampler_xxx_4_0, 0), (self.blocks_multiply_const_vxx_3, 0))    
        self.connect((self.rational_resampler_xxx_4_0_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.rational_resampler_xxx_6, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.sr2_dc_iq_offset_0_1_1, 0), (self.blocks_multiply_xx_4, 0))    
        self.connect((self.uhd_usrp_source_0_0_0, 0), (self.rational_resampler_xxx_4, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ground_test_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sr2_sq_thres_config(self):
        return self.sr2_sq_thres_config

    def set_sr2_sq_thres_config(self, sr2_sq_thres_config):
        self.sr2_sq_thres_config = sr2_sq_thres_config
        self.set_sr2_sq_thres_min(self.sr2_sq_thres_config)

    def get_sr1_sq_thres_config(self):
        return self.sr1_sq_thres_config

    def set_sr1_sq_thres_config(self, sr1_sq_thres_config):
        self.sr1_sq_thres_config = sr1_sq_thres_config
        self.set_sr1_sq_thres_min(self.sr1_sq_thres_config)

    def get_samp_rate_sr1(self):
        return self.samp_rate_sr1

    def set_samp_rate_sr1(self, samp_rate_sr1):
        self.samp_rate_sr1 = samp_rate_sr1
        self.set_samp_rate_sr2(self.samp_rate_sr1)
        self.uhd_usrp_source_0_0_0.set_samp_rate(self.samp_rate_sr1)
        self.sr2_dc_iq_offset_0_1_1.set_sampling_freq(self.samp_rate_sr1)
        self.set_samp_rate_UHD(self.samp_rate_sr1)
        self.qtgui_freq_sink_x_3_1.set_frequency_range(0, self.samp_rate_sr1/4/4)
        self.qtgui_freq_sink_x_2_0.set_frequency_range(self.st1_freq, self.samp_rate_sr1)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.sr1_freq+self.sr1_rit, self.samp_rate_sr1/4)
        self.low_pass_filter_0_2_0_2_0_0.set_taps(firdes.low_pass(1, int(self.samp_rate_sr1/16), 7500*2, 400, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1_1_0.set_sampling_freq(self.samp_rate_sr1/4)
        self.analog_sig_source_x_1_1.set_sampling_freq(self.samp_rate_sr1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_sr2_0(self.samp_rate)

    def get_lo_xmit(self):
        return self.lo_xmit

    def set_lo_xmit(self, lo_xmit):
        self.lo_xmit = lo_xmit
        self.set_st1_freq(849.5e6+self.lo_xmit)

    def get_atten_in_dB_gr2(self):
        return self.atten_in_dB_gr2

    def set_atten_in_dB_gr2(self, atten_in_dB_gr2):
        self.atten_in_dB_gr2 = atten_in_dB_gr2
        self.set_gr2_atten_linear(1/(10**(-self.atten_in_dB_gr2/20.)))

    def get_atten_in_dB(self):
        return self.atten_in_dB

    def set_atten_in_dB(self, atten_in_dB):
        self.atten_in_dB = atten_in_dB
        self.set_sr1_atten_linear(1/(10**(-self.atten_in_dB/20.)))

    def get_test_signal_input(self):
        return self.test_signal_input

    def set_test_signal_input(self, test_signal_input):
        self.test_signal_input = test_signal_input
        self._test_signal_input_callback(self.test_signal_input)
        self.blks2_selector_1.set_input_index(int(self.test_signal_input))

    def get_st1_gain(self):
        return self.st1_gain

    def set_st1_gain(self, st1_gain):
        self.st1_gain = st1_gain

    def get_st1_freq(self):
        return self.st1_freq

    def set_st1_freq(self, st1_freq):
        self.st1_freq = st1_freq
        Qt.QMetaObject.invokeMethod(self._st1_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.st1_freq)))
        self.qtgui_freq_sink_x_2_0.set_frequency_range(self.st1_freq, self.samp_rate_sr1)

    def get_sr2_sq_thres_min(self):
        return self.sr2_sq_thres_min

    def set_sr2_sq_thres_min(self, sr2_sq_thres_min):
        self.sr2_sq_thres_min = sr2_sq_thres_min
        self._sr2_sq_thres_config_config = ConfigParser.ConfigParser()
        self._sr2_sq_thres_config_config.read('default')
        if not self._sr2_sq_thres_config_config.has_section('main'):
        	self._sr2_sq_thres_config_config.add_section('main')
        self._sr2_sq_thres_config_config.set('main', 'Min Squelch Level sr2', str(self.sr2_sq_thres_min))
        self._sr2_sq_thres_config_config.write(open('default', 'w'))
        self.analog_pwr_squelch_xx_0_0_1.set_threshold((self.sr2_sq_thres_min))

    def get_sr2_rcv_tun_freq(self):
        return self.sr2_rcv_tun_freq

    def set_sr2_rcv_tun_freq(self, sr2_rcv_tun_freq):
        self.sr2_rcv_tun_freq = sr2_rcv_tun_freq
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.sr2_rcv_tun_freq+self.sr2_freq_offset, self.samp_rate_sr2)
        self.osmosdr_source_0.set_center_freq(self.sr2_rcv_tun_freq-self.sr2_freq_offset-self.offset_temp-self.lnb_lo, 0)

    def get_sr2_rcv_rf_tun_gain_if(self):
        return self.sr2_rcv_rf_tun_gain_if

    def set_sr2_rcv_rf_tun_gain_if(self, sr2_rcv_rf_tun_gain_if):
        self.sr2_rcv_rf_tun_gain_if = sr2_rcv_rf_tun_gain_if
        self.osmosdr_source_0.set_if_gain(self.sr2_rcv_rf_tun_gain_if, 0)

    def get_sr2_rcv_rf_tun_gain(self):
        return self.sr2_rcv_rf_tun_gain

    def set_sr2_rcv_rf_tun_gain(self, sr2_rcv_rf_tun_gain):
        self.sr2_rcv_rf_tun_gain = sr2_rcv_rf_tun_gain
        self.osmosdr_source_0.set_gain(self.sr2_rcv_rf_tun_gain, 0)

    def get_sr2_ppm(self):
        return self.sr2_ppm

    def set_sr2_ppm(self, sr2_ppm):
        self.sr2_ppm = sr2_ppm
        self.osmosdr_source_0.set_freq_corr(self.sr2_ppm, 0)

    def get_sr2_freq_offset(self):
        return self.sr2_freq_offset

    def set_sr2_freq_offset(self, sr2_freq_offset):
        self.sr2_freq_offset = sr2_freq_offset
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.sr2_rcv_tun_freq+self.sr2_freq_offset, self.samp_rate_sr2)
        self.osmosdr_source_0.set_center_freq(self.sr2_rcv_tun_freq-self.sr2_freq_offset-self.offset_temp-self.lnb_lo, 0)

    def get_sr1_sq_thres_min(self):
        return self.sr1_sq_thres_min

    def set_sr1_sq_thres_min(self, sr1_sq_thres_min):
        self.sr1_sq_thres_min = sr1_sq_thres_min
        self._sr1_sq_thres_config_config = ConfigParser.ConfigParser()
        self._sr1_sq_thres_config_config.read('default')
        if not self._sr1_sq_thres_config_config.has_section('main'):
        	self._sr1_sq_thres_config_config.add_section('main')
        self._sr1_sq_thres_config_config.set('main', 'Min Squelch Level sr1', str(self.sr1_sq_thres_min))
        self._sr1_sq_thres_config_config.write(open('default', 'w'))
        self.analog_pwr_squelch_xx_0_0_0.set_threshold((self.sr1_sq_thres_min))

    def get_sr1_rit(self):
        return self.sr1_rit

    def set_sr1_rit(self, sr1_rit):
        self.sr1_rit = sr1_rit
        self.uhd_usrp_source_0_0_0.set_center_freq(self.sr1_freq+self.sr1_rit, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.sr1_freq+self.sr1_rit, self.samp_rate_sr1/4)

    def get_sr1_gain(self):
        return self.sr1_gain

    def set_sr1_gain(self, sr1_gain):
        self.sr1_gain = sr1_gain
        self.uhd_usrp_source_0_0_0.set_gain(self.sr1_gain, 0)
        	

    def get_sr1_freq(self):
        return self.sr1_freq

    def set_sr1_freq(self, sr1_freq):
        self.sr1_freq = sr1_freq
        Qt.QMetaObject.invokeMethod(self._sr1_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.sr1_freq)))
        self.uhd_usrp_source_0_0_0.set_center_freq(self.sr1_freq+self.sr1_rit, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.sr1_freq+self.sr1_rit, self.samp_rate_sr1/4)

    def get_sr1_atten_linear(self):
        return self.sr1_atten_linear

    def set_sr1_atten_linear(self, sr1_atten_linear):
        self.sr1_atten_linear = sr1_atten_linear
        self.blocks_multiply_const_vxx_2.set_k((self.sr1_atten_linear, ))

    def get_samp_rate_sr2_0(self):
        return self.samp_rate_sr2_0

    def set_samp_rate_sr2_0(self, samp_rate_sr2_0):
        self.samp_rate_sr2_0 = samp_rate_sr2_0

    def get_samp_rate_sr2(self):
        return self.samp_rate_sr2

    def set_samp_rate_sr2(self, samp_rate_sr2):
        self.samp_rate_sr2 = samp_rate_sr2
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate_sr2)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate_sr2/4/25)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.sr2_rcv_tun_freq+self.sr2_freq_offset, self.samp_rate_sr2)
        self.pseudo_doppler_source_0.set_sampling_freq(self.samp_rate_sr2)
        self.pseudo_doppler_source.set_sampling_freq(self.samp_rate_sr2)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate_sr2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate_sr2/4, 10e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0_0_0_0.set_sampling_freq(self.samp_rate_sr2/4)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate_sr2/4)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate_sr2)

    def get_samp_rate_UHD(self):
        return self.samp_rate_UHD

    def set_samp_rate_UHD(self, samp_rate_UHD):
        self.samp_rate_UHD = samp_rate_UHD

    def get_pseudo_doppler(self):
        return self.pseudo_doppler

    def set_pseudo_doppler(self, pseudo_doppler):
        self.pseudo_doppler = pseudo_doppler
        self._pseudo_doppler_callback(self.pseudo_doppler)
        self.blks2_selector_0_0.set_input_index(int(self.pseudo_doppler))

    def get_probed_det_freq_error_with_old(self):
        return self.probed_det_freq_error_with_old

    def set_probed_det_freq_error_with_old(self, probed_det_freq_error_with_old):
        self.probed_det_freq_error_with_old = probed_det_freq_error_with_old
        self.analog_const_source_x_0_0_0_0.set_offset(self.probed_det_freq_error_with_old)

    def get_probed_det_freq_error(self):
        return self.probed_det_freq_error

    def set_probed_det_freq_error(self, probed_det_freq_error):
        self.probed_det_freq_error = probed_det_freq_error
        self.analog_const_source_x_0_0_1.set_offset(self.probed_det_freq_error)

    def get_offset_tone_freq(self):
        return self.offset_tone_freq

    def set_offset_tone_freq(self, offset_tone_freq):
        self.offset_tone_freq = offset_tone_freq
        self.analog_sig_source_x_0_0_0_0_0.set_frequency(self.offset_tone_freq)
        self.analog_sig_source_x_0_0_0.set_frequency(-self.offset_tone_freq)

    def get_offset_temp(self):
        return self.offset_temp

    def set_offset_temp(self, offset_temp):
        self.offset_temp = offset_temp
        self.osmosdr_source_0.set_center_freq(self.sr2_rcv_tun_freq-self.sr2_freq_offset-self.offset_temp-self.lnb_lo, 0)
        self.analog_sig_source_x_1_1_0.set_frequency(self.offset_temp)

    def get_lpf_taps(self):
        return self.lpf_taps

    def set_lpf_taps(self, lpf_taps):
        self.lpf_taps = lpf_taps
        self.freq_xlating_fft_filter_ccc_0.set_taps((self.lpf_taps))

    def get_lnb_lo(self):
        return self.lnb_lo

    def set_lnb_lo(self, lnb_lo):
        self.lnb_lo = lnb_lo
        self.osmosdr_source_0.set_center_freq(self.sr2_rcv_tun_freq-self.sr2_freq_offset-self.offset_temp-self.lnb_lo, 0)

    def get_gr2_atten_linear(self):
        return self.gr2_atten_linear

    def set_gr2_atten_linear(self, gr2_atten_linear):
        self.gr2_atten_linear = gr2_atten_linear
        self.blocks_multiply_const_vxx_1.set_k((self.gr2_atten_linear, ))

    def get_enable_feedback(self):
        return self.enable_feedback

    def set_enable_feedback(self, enable_feedback):
        self.enable_feedback = enable_feedback
        self._enable_feedback_callback(self.enable_feedback)
        self.blks2_selector_0_1.set_input_index(int(self.enable_feedback))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.low_pass_filter_0_2_0.set_taps(firdes.low_pass(1, self.audio_rate, 5e3, 500, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=ground_test_1, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
