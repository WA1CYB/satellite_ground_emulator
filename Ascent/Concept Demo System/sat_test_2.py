#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Sat Test 2
# Author: WA1CYB
# Description: Sat Test 2 Linear with Doppler,Lock Tone & ID+ dual nbfm
# Generated: Wed Oct 11 09:04:22 2017
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
import sip
import sys
import time


class sat_test_2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Sat Test 2")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Sat Test 2")
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

        self.settings = Qt.QSettings("GNU Radio", "sat_test_2")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_sr1 = samp_rate_sr1 = 100.e6/100
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
        self.samp_rate_sr2 = samp_rate_sr2 = samp_rate_sr1
        self.wpm_0 = wpm_0 = 15
        self.wpm = wpm = 10
        
        self.wide_xlate_filter_taps_0 = wide_xlate_filter_taps_0 = firdes.low_pass(1.0, samp_rate_sr2, (256*.95)*1e3/4, 0.05*(256e3), firdes.WIN_HAMMING, 6.76)
          
        self.temp_atten_all_channels = temp_atten_all_channels = 1
        self.st1_gain = st1_gain = 25.0
        self.st1_freq = st1_freq = 446.3e6
        self.sr2_sq_thres_min = sr2_sq_thres_min = sr2_sq_thres_config
        self.sr2_rcv_tun_freq = sr2_rcv_tun_freq = 146.52e6
        self.sr2_rcv_rf_tun_gain_if = sr2_rcv_rf_tun_gain_if = 20.0
        self.sr2_rcv_rf_tun_gain = sr2_rcv_rf_tun_gain = 30
        self.sr2_ppm = sr2_ppm = 18.0
        self.sr2_freq_offset = sr2_freq_offset = 0
        self.sr1_sq_thres_min = sr1_sq_thres_min = sr1_sq_thres_config
        self.sr1_rit = sr1_rit = 0
        self.sr1_gain = sr1_gain = 25.0
        self.sr1_freq = sr1_freq = 1265e6
        
        self.sb_xlate_filter_taps_0 = sb_xlate_filter_taps_0 = firdes.low_pass(1.0, samp_rate_sr2/16, 3.8e3/4, 70, firdes.WIN_HAMMING, 6.76)
          
        self.samp_rate_UHD = samp_rate_UHD = samp_rate_sr1
        self.samp_rate = samp_rate = 32000
        
        self.psk31_xlate_filter_taps_0 = psk31_xlate_filter_taps_0 = firdes.low_pass(1.0, samp_rate_sr2/16, .7e3, 300, firdes.WIN_HAMMING, 6.76)
          
        self.pseudo_doppler = pseudo_doppler = 0
        self.offset_temp = offset_temp = 0
        
        self.nbfm_xlate_filter_taps_0 = nbfm_xlate_filter_taps_0 = firdes.low_pass(1.0, samp_rate_sr1/2, 3.8e3*4, 1600, firdes.WIN_HAMMING, 6.76)
          
        
        self.low_pass_filter_taps_output = low_pass_filter_taps_output = firdes.low_pass(1.0, samp_rate_sr2, 128e3/2, (0.1)*128e3, firdes.WIN_HAMMING, 6.76)
          
        
        self.half_band_xlate_filter_taps_0 = half_band_xlate_filter_taps_0 = firdes.low_pass(1.0, samp_rate_sr1/2, 64e3/2, 5e3, firdes.WIN_HAMMING, 6.76)
          
        
        self.cw_xlate_filter_taps_0 = cw_xlate_filter_taps_0 = firdes.low_pass(1.0, samp_rate_sr2/16, .4e3, 100, firdes.WIN_HAMMING, 6.76)
          
        
        self.band_xlate_filter_taps_0 = band_xlate_filter_taps_0 = firdes.low_pass(1.0, samp_rate_sr1, 256e3/4, 0.1*(128e3)/2, firdes.WIN_HAMMING, 6.76)
          
        self.audio_rate = audio_rate = 48000
        self.LO = LO = 2**16
        
        self.D9600_xlate_filter_taps_0 = D9600_xlate_filter_taps_0 = firdes.low_pass(1.0, samp_rate_sr2/16, 9.6e3/2, 100, firdes.WIN_HAMMING, 6.76)
          

        ##################################################
        # Blocks
        ##################################################
        self.sdr_st1_controls = Qt.QTabWidget()
        self.sdr_st1_controls_widget_0 = Qt.QWidget()
        self.sdr_st1_controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_st1_controls_widget_0)
        self.sdr_st1_controls_grid_layout_0 = Qt.QGridLayout()
        self.sdr_st1_controls_layout_0.addLayout(self.sdr_st1_controls_grid_layout_0)
        self.sdr_st1_controls.addTab(self.sdr_st1_controls_widget_0, 'ST1 Transmit Frequency')
        self.sdr_st1_controls_widget_1 = Qt.QWidget()
        self.sdr_st1_controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_st1_controls_widget_1)
        self.sdr_st1_controls_grid_layout_1 = Qt.QGridLayout()
        self.sdr_st1_controls_layout_1.addLayout(self.sdr_st1_controls_grid_layout_1)
        self.sdr_st1_controls.addTab(self.sdr_st1_controls_widget_1, 'ST1 Transmit Gain')
        self.sdr_st1_controls_widget_2 = Qt.QWidget()
        self.sdr_st1_controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_st1_controls_widget_2)
        self.sdr_st1_controls_grid_layout_2 = Qt.QGridLayout()
        self.sdr_st1_controls_layout_2.addLayout(self.sdr_st1_controls_grid_layout_2)
        self.sdr_st1_controls.addTab(self.sdr_st1_controls_widget_2, 'Pseudo Doppler')
        self.top_grid_layout.addWidget(self.sdr_st1_controls, 0,3,2,1)
        self.sdr_sr1_controls = Qt.QTabWidget()
        self.sdr_sr1_controls_widget_0 = Qt.QWidget()
        self.sdr_sr1_controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_sr1_controls_widget_0)
        self.sdr_sr1_controls_grid_layout_0 = Qt.QGridLayout()
        self.sdr_sr1_controls_layout_0.addLayout(self.sdr_sr1_controls_grid_layout_0)
        self.sdr_sr1_controls.addTab(self.sdr_sr1_controls_widget_0, 'SR1 Receiver Frequency')
        self.sdr_sr1_controls_widget_1 = Qt.QWidget()
        self.sdr_sr1_controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_sr1_controls_widget_1)
        self.sdr_sr1_controls_grid_layout_1 = Qt.QGridLayout()
        self.sdr_sr1_controls_layout_1.addLayout(self.sdr_sr1_controls_grid_layout_1)
        self.sdr_sr1_controls.addTab(self.sdr_sr1_controls_widget_1, 'SR1 Receiver RIT')
        self.sdr_sr1_controls_widget_2 = Qt.QWidget()
        self.sdr_sr1_controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_sr1_controls_widget_2)
        self.sdr_sr1_controls_grid_layout_2 = Qt.QGridLayout()
        self.sdr_sr1_controls_layout_2.addLayout(self.sdr_sr1_controls_grid_layout_2)
        self.sdr_sr1_controls.addTab(self.sdr_sr1_controls_widget_2, 'SR1 Receiver Gain')
        self.sdr_sr1_controls_widget_3 = Qt.QWidget()
        self.sdr_sr1_controls_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.sdr_sr1_controls_widget_3)
        self.sdr_sr1_controls_grid_layout_3 = Qt.QGridLayout()
        self.sdr_sr1_controls_layout_3.addLayout(self.sdr_sr1_controls_grid_layout_3)
        self.sdr_sr1_controls.addTab(self.sdr_sr1_controls_widget_3, 'SR1 Squelch')
        self.top_grid_layout.addWidget(self.sdr_sr1_controls, 0,0,2,1)
        self._temp_atten_all_channels_range = Range(.0001, 1, .0001, 1, 200)
        self._temp_atten_all_channels_win = RangeWidget(self._temp_atten_all_channels_range, self.set_temp_atten_all_channels, "temp_atten_all_channels", "counter_slider", float)
        self.top_layout.addWidget(self._temp_atten_all_channels_win)
        self._st1_freq_tool_bar = Qt.QToolBar(self)
        self._st1_freq_tool_bar.addWidget(Qt.QLabel('Frequency'+": "))
        self._st1_freq_line_edit = Qt.QLineEdit(str(self.st1_freq))
        self._st1_freq_tool_bar.addWidget(self._st1_freq_line_edit)
        self._st1_freq_line_edit.returnPressed.connect(
        	lambda: self.set_st1_freq(eng_notation.str_to_num(str(self._st1_freq_line_edit.text().toAscii()))))
        self.sdr_st1_controls_grid_layout_0.addWidget(self._st1_freq_tool_bar,  0,0,1,1)
        self._sr1_sq_thres_min_range = Range(-100, 0, 1, sr1_sq_thres_config, 200)
        self._sr1_sq_thres_min_win = RangeWidget(self._sr1_sq_thres_min_range, self.set_sr1_sq_thres_min, 'SR1 min SQ in dB', "counter_slider", float)
        self.sdr_sr1_controls_grid_layout_3.addWidget(self._sr1_sq_thres_min_win,  0,0,1,1)
        self._sr1_rit_range = Range(-30000, 30000, 5.0, 0, 200)
        self._sr1_rit_win = RangeWidget(self._sr1_rit_range, self.set_sr1_rit, "SR1 Receiver RIT", "counter_slider", float)
        self.sdr_sr1_controls_grid_layout_1.addWidget(self._sr1_rit_win,  0,0,1,1)
        self._sr1_gain_range = Range(0.0, 50, 1.0, 25.0, 200)
        self._sr1_gain_win = RangeWidget(self._sr1_gain_range, self.set_sr1_gain, 'RF Gain', "counter_slider", float)
        self.sdr_sr1_controls_grid_layout_2.addWidget(self._sr1_gain_win,  0,0,1,1)
        self._sr1_freq_tool_bar = Qt.QToolBar(self)
        self._sr1_freq_tool_bar.addWidget(Qt.QLabel('Frequency'+": "))
        self._sr1_freq_line_edit = Qt.QLineEdit(str(self.sr1_freq))
        self._sr1_freq_tool_bar.addWidget(self._sr1_freq_line_edit)
        self._sr1_freq_line_edit.returnPressed.connect(
        	lambda: self.set_sr1_freq(eng_notation.str_to_num(str(self._sr1_freq_line_edit.text().toAscii()))))
        self.sdr_sr1_controls_grid_layout_0.addWidget(self._sr1_freq_tool_bar,  0,0,1,1)
        self.rtl_sdr_1_controls = Qt.QTabWidget()
        self.rtl_sdr_1_controls_widget_0 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_0)
        self.rtl_sdr_1_controls_grid_layout_0 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_0.addLayout(self.rtl_sdr_1_controls_grid_layout_0)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_0, 'SR2 Receiver Frequency ')
        self.rtl_sdr_1_controls_widget_1 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_1)
        self.rtl_sdr_1_controls_grid_layout_1 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_1.addLayout(self.rtl_sdr_1_controls_grid_layout_1)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_1, 'SR2 RIT')
        self.rtl_sdr_1_controls_widget_2 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_2)
        self.rtl_sdr_1_controls_grid_layout_2 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_2.addLayout(self.rtl_sdr_1_controls_grid_layout_2)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_2, 'SR2 Receiver Gain')
        self.rtl_sdr_1_controls_widget_3 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_3)
        self.rtl_sdr_1_controls_grid_layout_3 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_3.addLayout(self.rtl_sdr_1_controls_grid_layout_3)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_3, 'SR2 Receiver IF Gain')
        self.rtl_sdr_1_controls_widget_4 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_4)
        self.rtl_sdr_1_controls_grid_layout_4 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_4.addLayout(self.rtl_sdr_1_controls_grid_layout_4)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_4, 'SR2 PPM')
        self.rtl_sdr_1_controls_widget_5 = Qt.QWidget()
        self.rtl_sdr_1_controls_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.rtl_sdr_1_controls_widget_5)
        self.rtl_sdr_1_controls_grid_layout_5 = Qt.QGridLayout()
        self.rtl_sdr_1_controls_layout_5.addLayout(self.rtl_sdr_1_controls_grid_layout_5)
        self.rtl_sdr_1_controls.addTab(self.rtl_sdr_1_controls_widget_5, 'SR2 Squelch')
        self.top_grid_layout.addWidget(self.rtl_sdr_1_controls, 0,2,2,1)
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
        self.uhd_usrp_source_0_0_0.set_center_freq(sr1_freq+sr1_rit-offset_temp, 0)
        self.uhd_usrp_source_0_0_0.set_gain(sr1_gain, 0)
        self.uhd_usrp_source_0_0_0.set_antenna('RX2', 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate_sr1)
        self.uhd_usrp_sink_0.set_center_freq(st1_freq, 0)
        self.uhd_usrp_sink_0.set_gain(20, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self._st1_gain_range = Range(0.0, 50, 1.0, 25.0, 200)
        self._st1_gain_win = RangeWidget(self._st1_gain_range, self.set_st1_gain, 'RF Gain', "counter_slider", float)
        self.sdr_st1_controls_grid_layout_1.addWidget(self._st1_gain_win,  0,0,1,1)
        self._sr2_sq_thres_min_range = Range(-100, 0, 1, sr2_sq_thres_config, 200)
        self._sr2_sq_thres_min_win = RangeWidget(self._sr2_sq_thres_min_range, self.set_sr2_sq_thres_min, 'SR2 min SQ in dB', "counter_slider", float)
        self.rtl_sdr_1_controls_grid_layout_5.addWidget(self._sr2_sq_thres_min_win,  0,0,1,1)
        self._sr2_rcv_tun_freq_range = Range(70e6, 1700.0e6, 1, 146.52e6, 200)
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
        self._sr2_freq_offset_range = Range(-20000, 20000, 1, 0, 200)
        self._sr2_freq_offset_win = RangeWidget(self._sr2_freq_offset_range, self.set_sr2_freq_offset, "SR2 RIT ", "counter_slider", float)
        self.rtl_sdr_1_controls_grid_layout_1.addWidget(self._sr2_freq_offset_win,  0,0,1,1)
        self.sr2_dc_iq_offset_0_2_0_0 = analog.sig_source_c(samp_rate_sr2, analog.GR_CONST_WAVE, 0, 1, 0)
        self.sr2_dc_iq_offset_0_1 = analog.sig_source_c(samp_rate_sr2, analog.GR_COS_WAVE, -9e3, 1, 0)
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, samp_rate_sr2, 5, 0.35, 200))
        self.rational_resampler_xxx_6 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=int(samp_rate_sr1/16)/5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=2,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0_0_0_0_0_0_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate_sr1),
                decimation=int(samp_rate_sr1/4),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0_0_0_0_0_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate_sr1),
                decimation=int(samp_rate_sr1/16),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate_sr1/16),
                decimation=int(samp_rate_sr1/8),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024*4, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate_sr1, #bw
        	"Output- as seen on Gnd", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-30, 0)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 6,3,1,1)
        self.qtgui_freq_sink_x_2_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate_sr1, #bw
        	"Sat Xmtr#1 Input Spectrum", #name
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
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	sr1_freq+sr1_rit, #fc
        	samp_rate_sr1/4, #bw
        	"SR1 Input- Post pseudo Doppler", #name
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 2,0,1,3)
        self.pseudo_doppler_source = analog.sig_source_f(samp_rate_sr2, analog.GR_TRI_WAVE, 10./600, 1, -.5)
        self.low_pass_filter_0_2_0_2_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, int(samp_rate_sr1/16), 7500, 400, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_2 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, int(samp_rate_sr1/16), 3e3, 300, firdes.WIN_HAMMING, 6.76))
        self.blocks_vector_source_x_0 = blocks.vector_source_c((1,0,1,0,1,0,1,1,1, 0,0,0,1,0,1,0,1,0,1,1,1, 0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0, 1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0, 1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1, 0,0,0,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0), True, 1, [])
        self.blocks_vco_c_0_3 = blocks.vco_c(samp_rate_sr2, 2*(22/7)*(2*50e3)*((sr1_freq-offset_temp)/st1_freq), 1)
        self.blocks_vco_c_0_1_0 = blocks.vco_c(samp_rate_sr2, 2*(22/7)*(2*250e3)*((sr1_freq-offset_temp)/st1_freq), 1)
        self.blocks_vco_c_0_1 = blocks.vco_c(samp_rate_sr2, 2*(22/7)*(2*250e3), 1)
        self.blocks_vco_c_0_0_0 = blocks.vco_c(samp_rate_sr2, 2*(22/7)*(2*150e3)*((sr1_freq-offset_temp)/st1_freq), 1)
        self.blocks_vco_c_0_0 = blocks.vco_c(samp_rate_sr2, 2*(22/7)*(2*150e3), 1)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate_sr2, 2*(22/7)*(2*50e3), 1)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, int(1.2 * audio_rate / wpm))
        self.blocks_null_source_1 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_1_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_5 = blocks.multiply_const_vcc((0.07, ))
        self.blocks_multiply_const_vxx_4 = blocks.multiply_const_vff((1, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc((temp_atten_all_channels, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vcc((16*5/100., ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((1, ))
        self.blocks_add_xx_4 = blocks.add_vcc(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blks2_selector_sr1 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=4,
        	num_outputs=1,
        	input_index=pseudo_doppler,
        	output_index=0,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=4,
        	num_outputs=1,
        	input_index=pseudo_doppler,
        	output_index=0,
        )
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_sig_source_x_1_0 = analog.sig_source_c(samp_rate_sr2, analog.GR_COS_WAVE, -30.5e3, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate_sr2, analog.GR_CONST_WAVE, 0, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate_sr2, analog.GR_CONST_WAVE, 0, 1, 0)
        self.analog_pwr_squelch_xx_0_0_1 = analog.pwr_squelch_cc((sr1_sq_thres_min), .001, 1, False)
        self.analog_pwr_squelch_xx_0_0_0 = analog.pwr_squelch_cc((sr1_sq_thres_min), .001, 1, False)
        self.analog_nbfm_tx_0_0 = analog.nbfm_tx(
        	audio_rate=int(samp_rate_sr1/16)/5,
        	quad_rate=int(samp_rate_sr1/16),
        	tau=75e-6,
        	max_dev=8.9e3,
        	fh=-1.0,
                )
        self.analog_nbfm_rx_2_0 = analog.nbfm_rx(
        	audio_rate=int(samp_rate_sr1/16)/5,
        	quad_rate=int(samp_rate_sr1/16),
        	tau=75e-6,
        	max_dev=8.9e3,
          )
        self.analog_agc2_xx_0_0_0_2 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_0_0_2.set_max_gain(16)
        self.analog_agc2_xx_0_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_0.set_max_gain(16)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0_0, 0), (self.analog_pwr_squelch_xx_0_0_0, 0))    
        self.connect((self.analog_agc2_xx_0_0_0_2, 0), (self.analog_pwr_squelch_xx_0_0_1, 0))    
        self.connect((self.analog_nbfm_rx_2_0, 0), (self.low_pass_filter_0_2, 0))    
        self.connect((self.analog_nbfm_rx_2_0, 0), (self.rational_resampler_xxx_6, 0))    
        self.connect((self.analog_nbfm_tx_0_0, 0), (self.low_pass_filter_0_2_0_2_0_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0_0_0, 0), (self.analog_nbfm_rx_2_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0_0_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blks2_selector_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blks2_selector_sr1, 0))    
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.blks2_selector_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.blks2_selector_sr1, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.blocks_add_xx_4, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.rational_resampler_xxx_0_0_0_0_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.rational_resampler_xxx_2, 0))    
        self.connect((self.blocks_multiply_const_vxx_4, 0), (self.blocks_vco_c_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_4, 0), (self.blocks_vco_c_0_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_4, 0), (self.blocks_vco_c_0_3, 0))    
        self.connect((self.blocks_multiply_const_vxx_5, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_const_vxx_5, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.qtgui_freq_sink_x_2_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_1, 1))    
        self.connect((self.blocks_multiply_xx_1_0_0, 0), (self.blocks_add_xx_1, 2))    
        self.connect((self.blocks_null_source_1, 0), (self.blocks_add_xx_4, 1))    
        self.connect((self.blocks_repeat_0, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.blocks_vco_c_0, 0), (self.blks2_selector_0, 1))    
        self.connect((self.blocks_vco_c_0_0, 0), (self.blks2_selector_0, 2))    
        self.connect((self.blocks_vco_c_0_0_0, 0), (self.blks2_selector_sr1, 2))    
        self.connect((self.blocks_vco_c_0_1, 0), (self.blks2_selector_0, 3))    
        self.connect((self.blocks_vco_c_0_1_0, 0), (self.blks2_selector_sr1, 3))    
        self.connect((self.blocks_vco_c_0_3, 0), (self.blks2_selector_sr1, 1))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.low_pass_filter_0_2, 0), (self.analog_nbfm_tx_0_0, 0))    
        self.connect((self.low_pass_filter_0_2_0_2_0_0, 0), (self.rational_resampler_xxx_0_0_0_0_0_0_0, 0))    
        self.connect((self.pseudo_doppler_source, 0), (self.blocks_multiply_const_vxx_4, 0))    
        self.connect((self.pseudo_doppler_source, 0), (self.blocks_vco_c_0, 0))    
        self.connect((self.pseudo_doppler_source, 0), (self.blocks_vco_c_0_0, 0))    
        self.connect((self.pseudo_doppler_source, 0), (self.blocks_vco_c_0_1, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_agc2_xx_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_1_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0_0_0_0_0_0_0, 0), (self.blocks_add_xx_1, 3))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_2, 0), (self.analog_agc2_xx_0_0_0_2, 0))    
        self.connect((self.rational_resampler_xxx_2, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.rational_resampler_xxx_2, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.rational_resampler_xxx_6, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.sr2_dc_iq_offset_0_1, 0), (self.blocks_multiply_xx_1_0_0, 1))    
        self.connect((self.sr2_dc_iq_offset_0_2_0_0, 0), (self.blocks_add_xx_1, 0))    
        self.connect((self.uhd_usrp_source_0_0_0, 0), (self.blocks_add_xx_4, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "sat_test_2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate_sr1(self):
        return self.samp_rate_sr1

    def set_samp_rate_sr1(self, samp_rate_sr1):
        self.samp_rate_sr1 = samp_rate_sr1
        self.set_samp_rate_sr2(self.samp_rate_sr1)
        self.uhd_usrp_source_0_0_0.set_samp_rate(self.samp_rate_sr1)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate_sr1)
        self.set_samp_rate_UHD(self.samp_rate_sr1)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate_sr1)
        self.qtgui_freq_sink_x_2_0.set_frequency_range(0, self.samp_rate_sr1)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.sr1_freq+self.sr1_rit, self.samp_rate_sr1/4)
        self.low_pass_filter_0_2_0_2_0_0.set_taps(firdes.low_pass(1, int(self.samp_rate_sr1/16), 7500, 400, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_2.set_taps(firdes.low_pass(1, int(self.samp_rate_sr1/16), 3e3, 300, firdes.WIN_HAMMING, 6.76))

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

    def get_samp_rate_sr2(self):
        return self.samp_rate_sr2

    def set_samp_rate_sr2(self, samp_rate_sr2):
        self.samp_rate_sr2 = samp_rate_sr2
        self.sr2_dc_iq_offset_0_2_0_0.set_sampling_freq(self.samp_rate_sr2)
        self.sr2_dc_iq_offset_0_1.set_sampling_freq(self.samp_rate_sr2)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate_sr2, 5, 0.35, 200))
        self.pseudo_doppler_source.set_sampling_freq(self.samp_rate_sr2)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate_sr2)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate_sr2)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate_sr2)

    def get_wpm_0(self):
        return self.wpm_0

    def set_wpm_0(self, wpm_0):
        self.wpm_0 = wpm_0

    def get_wpm(self):
        return self.wpm

    def set_wpm(self, wpm):
        self.wpm = wpm
        self.blocks_repeat_0.set_interpolation(int(1.2 * self.audio_rate / self.wpm))

    def get_wide_xlate_filter_taps_0(self):
        return self.wide_xlate_filter_taps_0

    def set_wide_xlate_filter_taps_0(self, wide_xlate_filter_taps_0):
        self.wide_xlate_filter_taps_0 = wide_xlate_filter_taps_0

    def get_temp_atten_all_channels(self):
        return self.temp_atten_all_channels

    def set_temp_atten_all_channels(self, temp_atten_all_channels):
        self.temp_atten_all_channels = temp_atten_all_channels
        self.blocks_multiply_const_vxx_2.set_k((self.temp_atten_all_channels, ))

    def get_st1_gain(self):
        return self.st1_gain

    def set_st1_gain(self, st1_gain):
        self.st1_gain = st1_gain

    def get_st1_freq(self):
        return self.st1_freq

    def set_st1_freq(self, st1_freq):
        self.st1_freq = st1_freq
        Qt.QMetaObject.invokeMethod(self._st1_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.st1_freq)))
        self.uhd_usrp_sink_0.set_center_freq(self.st1_freq, 0)

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

    def get_sr2_rcv_tun_freq(self):
        return self.sr2_rcv_tun_freq

    def set_sr2_rcv_tun_freq(self, sr2_rcv_tun_freq):
        self.sr2_rcv_tun_freq = sr2_rcv_tun_freq

    def get_sr2_rcv_rf_tun_gain_if(self):
        return self.sr2_rcv_rf_tun_gain_if

    def set_sr2_rcv_rf_tun_gain_if(self, sr2_rcv_rf_tun_gain_if):
        self.sr2_rcv_rf_tun_gain_if = sr2_rcv_rf_tun_gain_if

    def get_sr2_rcv_rf_tun_gain(self):
        return self.sr2_rcv_rf_tun_gain

    def set_sr2_rcv_rf_tun_gain(self, sr2_rcv_rf_tun_gain):
        self.sr2_rcv_rf_tun_gain = sr2_rcv_rf_tun_gain

    def get_sr2_ppm(self):
        return self.sr2_ppm

    def set_sr2_ppm(self, sr2_ppm):
        self.sr2_ppm = sr2_ppm

    def get_sr2_freq_offset(self):
        return self.sr2_freq_offset

    def set_sr2_freq_offset(self, sr2_freq_offset):
        self.sr2_freq_offset = sr2_freq_offset

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
        self.analog_pwr_squelch_xx_0_0_1.set_threshold((self.sr1_sq_thres_min))
        self.analog_pwr_squelch_xx_0_0_0.set_threshold((self.sr1_sq_thres_min))

    def get_sr1_rit(self):
        return self.sr1_rit

    def set_sr1_rit(self, sr1_rit):
        self.sr1_rit = sr1_rit
        self.uhd_usrp_source_0_0_0.set_center_freq(self.sr1_freq+self.sr1_rit-self.offset_temp, 0)
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
        self.uhd_usrp_source_0_0_0.set_center_freq(self.sr1_freq+self.sr1_rit-self.offset_temp, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.sr1_freq+self.sr1_rit, self.samp_rate_sr1/4)

    def get_sb_xlate_filter_taps_0(self):
        return self.sb_xlate_filter_taps_0

    def set_sb_xlate_filter_taps_0(self, sb_xlate_filter_taps_0):
        self.sb_xlate_filter_taps_0 = sb_xlate_filter_taps_0

    def get_samp_rate_UHD(self):
        return self.samp_rate_UHD

    def set_samp_rate_UHD(self, samp_rate_UHD):
        self.samp_rate_UHD = samp_rate_UHD

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_psk31_xlate_filter_taps_0(self):
        return self.psk31_xlate_filter_taps_0

    def set_psk31_xlate_filter_taps_0(self, psk31_xlate_filter_taps_0):
        self.psk31_xlate_filter_taps_0 = psk31_xlate_filter_taps_0

    def get_pseudo_doppler(self):
        return self.pseudo_doppler

    def set_pseudo_doppler(self, pseudo_doppler):
        self.pseudo_doppler = pseudo_doppler
        self._pseudo_doppler_callback(self.pseudo_doppler)
        self.blks2_selector_sr1.set_input_index(int(self.pseudo_doppler))
        self.blks2_selector_0.set_input_index(int(self.pseudo_doppler))

    def get_offset_temp(self):
        return self.offset_temp

    def set_offset_temp(self, offset_temp):
        self.offset_temp = offset_temp
        self.uhd_usrp_source_0_0_0.set_center_freq(self.sr1_freq+self.sr1_rit-self.offset_temp, 0)

    def get_nbfm_xlate_filter_taps_0(self):
        return self.nbfm_xlate_filter_taps_0

    def set_nbfm_xlate_filter_taps_0(self, nbfm_xlate_filter_taps_0):
        self.nbfm_xlate_filter_taps_0 = nbfm_xlate_filter_taps_0

    def get_low_pass_filter_taps_output(self):
        return self.low_pass_filter_taps_output

    def set_low_pass_filter_taps_output(self, low_pass_filter_taps_output):
        self.low_pass_filter_taps_output = low_pass_filter_taps_output

    def get_half_band_xlate_filter_taps_0(self):
        return self.half_band_xlate_filter_taps_0

    def set_half_band_xlate_filter_taps_0(self, half_band_xlate_filter_taps_0):
        self.half_band_xlate_filter_taps_0 = half_band_xlate_filter_taps_0

    def get_cw_xlate_filter_taps_0(self):
        return self.cw_xlate_filter_taps_0

    def set_cw_xlate_filter_taps_0(self, cw_xlate_filter_taps_0):
        self.cw_xlate_filter_taps_0 = cw_xlate_filter_taps_0

    def get_band_xlate_filter_taps_0(self):
        return self.band_xlate_filter_taps_0

    def set_band_xlate_filter_taps_0(self, band_xlate_filter_taps_0):
        self.band_xlate_filter_taps_0 = band_xlate_filter_taps_0

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.blocks_repeat_0.set_interpolation(int(1.2 * self.audio_rate / self.wpm))

    def get_LO(self):
        return self.LO

    def set_LO(self, LO):
        self.LO = LO

    def get_D9600_xlate_filter_taps_0(self):
        return self.D9600_xlate_filter_taps_0

    def set_D9600_xlate_filter_taps_0(self, D9600_xlate_filter_taps_0):
        self.D9600_xlate_filter_taps_0 = D9600_xlate_filter_taps_0


def main(top_block_cls=sat_test_2, options=None):

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
