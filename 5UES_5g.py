#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: 5UE_flowchart
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import zeromq
from gnuradio.qtgui import Range, RangeWidget
from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "5UE_flowchart")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("5UE_flowchart")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 23.04e6
        self.gain4 = gain4 = 0.05
        self.gain3 = gain3 = 0.04
        self.gain2 = gain2 = 0.06
        self.gain1 = gain1 = 0.03
        self.gain0 = gain0 = 0.05

        ##################################################
        # Blocks
        ##################################################
        self._gain4_range = Range(0.001, 0.999, 0.001, 0.05, 200)
        self._gain4_win = RangeWidget(self._gain4_range, self.set_gain4, 'gain4', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain4_win)
        self._gain3_range = Range(0.001, 0.999, 0.001, 0.04, 200)
        self._gain3_win = RangeWidget(self._gain3_range, self.set_gain3, 'gain3', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain3_win)
        self._gain2_range = Range(0.001, 0.999, 0.001, 0.06, 200)
        self._gain2_win = RangeWidget(self._gain2_range, self.set_gain2, 'gain2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain2_win)
        self._gain1_range = Range(0.001, 0.999, 0.001, 0.03, 200)
        self._gain1_win = RangeWidget(self._gain1_range, self.set_gain1, 'gain1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain1_win)
        self._gain0_range = Range(0.001, 0.999, 0.001, 0.05, 200)
        self._gain0_win = RangeWidget(self._gain0_range, self.set_gain0, 'gain0', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain0_win)
        self.zeromq_req_source_3_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2100', 100, False, -1)
        self.zeromq_req_source_3 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2000', 100, False, -1)
        self.zeromq_req_source_1_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2102', 100, False, -1)
        self.zeromq_req_source_1 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2002', 100, False, -1)
        self.zeromq_req_source_0_1_0_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2005', 100, False, -1)
        self.zeromq_req_source_0_1_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2006', 100, False, -1)
        self.zeromq_req_source_0_1 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2004', 100, False, -1)
        self.zeromq_req_source_0_0_0_0_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2106', 100, False, -1)
        self.zeromq_req_source_0_0_0_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2105', 100, False, -1)
        self.zeromq_req_source_0_0_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2104', 100, False, -1)
        self.zeromq_req_source_0_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2103', 100, False, -1)
        self.zeromq_req_source_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2003', 100, False, -1)
        self.zeromq_rep_sink_2_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2152', 100, False, -1)
        self.zeromq_rep_sink_2 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2052', 100, False, -1)
        self.zeromq_rep_sink_1_1_0_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2056', 100, False, -1)
        self.zeromq_rep_sink_1_1_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2055', 100, False, -1)
        self.zeromq_rep_sink_1_1 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2054', 100, False, -1)
        self.zeromq_rep_sink_1_0_0_0_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2156', 100, False, -1)
        self.zeromq_rep_sink_1_0_0_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2155', 100, False, -1)
        self.zeromq_rep_sink_1_0_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2154', 100, False, -1)
        self.zeromq_rep_sink_1_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2153', 100, False, -1)
        self.zeromq_rep_sink_1 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2053', 100, False, -1)
        self.zeromq_rep_sink_0_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2101', 100, False, -1)
        self.zeromq_rep_sink_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2001', 100, False, -1)
        self.blocks_throttle_0_0_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0_3_0 = blocks.multiply_const_cc(gain0)
        self.blocks_multiply_const_vxx_0_3 = blocks.multiply_const_cc(gain0)
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_cc(gain0)
        self.blocks_multiply_const_vxx_0_1_2_2 = blocks.multiply_const_cc(gain3)
        self.blocks_multiply_const_vxx_0_1_2_1_0_0 = blocks.multiply_const_cc(gain4)
        self.blocks_multiply_const_vxx_0_1_2_1_0 = blocks.multiply_const_cc(gain3)
        self.blocks_multiply_const_vxx_0_1_2_1 = blocks.multiply_const_cc(gain3)
        self.blocks_multiply_const_vxx_0_1_2_0_1 = blocks.multiply_const_cc(gain4)
        self.blocks_multiply_const_vxx_0_1_2_0_0 = blocks.multiply_const_cc(gain4)
        self.blocks_multiply_const_vxx_0_1_2_0 = blocks.multiply_const_cc(gain4)
        self.blocks_multiply_const_vxx_0_1_2 = blocks.multiply_const_cc(gain3)
        self.blocks_multiply_const_vxx_0_1_1_0 = blocks.multiply_const_cc(gain2)
        self.blocks_multiply_const_vxx_0_1_1 = blocks.multiply_const_cc(gain2)
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_cc(gain2)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_cc(gain2)
        self.blocks_multiply_const_vxx_0_0_1_0 = blocks.multiply_const_cc(gain1)
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_cc(gain1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_cc(gain1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(gain1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(gain0)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.zeromq_rep_sink_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_1_0, 0), (self.zeromq_rep_sink_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blocks_add_xx_0_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_1_1, 0), (self.zeromq_rep_sink_1_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1_1_0, 0), (self.zeromq_rep_sink_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_0_0, 0), (self.zeromq_rep_sink_1_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_0_1, 0), (self.blocks_add_xx_0_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_1, 0), (self.zeromq_rep_sink_1_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_1_0, 0), (self.zeromq_rep_sink_1_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_1_0_0, 0), (self.zeromq_rep_sink_1_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_2, 0), (self.blocks_add_xx_0_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_3, 0), (self.zeromq_rep_sink_2, 0))
        self.connect((self.blocks_multiply_const_vxx_0_3_0, 0), (self.zeromq_rep_sink_2_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.zeromq_rep_sink_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.zeromq_rep_sink_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_1, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_1, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_2_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_2_1, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_multiply_const_vxx_0_3, 0))
        self.connect((self.blocks_throttle_0_0_1, 0), (self.blocks_multiply_const_vxx_0_0_1_0, 0))
        self.connect((self.blocks_throttle_0_0_1, 0), (self.blocks_multiply_const_vxx_0_1_1_0, 0))
        self.connect((self.blocks_throttle_0_0_1, 0), (self.blocks_multiply_const_vxx_0_1_2_1_0, 0))
        self.connect((self.blocks_throttle_0_0_1, 0), (self.blocks_multiply_const_vxx_0_1_2_1_0_0, 0))
        self.connect((self.blocks_throttle_0_0_1, 0), (self.blocks_multiply_const_vxx_0_3_0, 0))
        self.connect((self.zeromq_req_source_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.zeromq_req_source_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.zeromq_req_source_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))
        self.connect((self.zeromq_req_source_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_2_2, 0))
        self.connect((self.zeromq_req_source_0_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_2_0_1, 0))
        self.connect((self.zeromq_req_source_0_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.zeromq_req_source_0_1_0, 0), (self.blocks_multiply_const_vxx_0_1_2_0, 0))
        self.connect((self.zeromq_req_source_0_1_0_0, 0), (self.blocks_multiply_const_vxx_0_1_2, 0))
        self.connect((self.zeromq_req_source_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.zeromq_req_source_1_0, 0), (self.blocks_multiply_const_vxx_0_2, 0))
        self.connect((self.zeromq_req_source_3, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.zeromq_req_source_3_0, 0), (self.blocks_throttle_0_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_1.set_sample_rate(self.samp_rate)

    def get_gain4(self):
        return self.gain4

    def set_gain4(self, gain4):
        self.gain4 = gain4
        self.blocks_multiply_const_vxx_0_1_2_0.set_k(self.gain4)
        self.blocks_multiply_const_vxx_0_1_2_0_0.set_k(self.gain4)
        self.blocks_multiply_const_vxx_0_1_2_0_1.set_k(self.gain4)
        self.blocks_multiply_const_vxx_0_1_2_1_0_0.set_k(self.gain4)

    def get_gain3(self):
        return self.gain3

    def set_gain3(self, gain3):
        self.gain3 = gain3
        self.blocks_multiply_const_vxx_0_1_2.set_k(self.gain3)
        self.blocks_multiply_const_vxx_0_1_2_1.set_k(self.gain3)
        self.blocks_multiply_const_vxx_0_1_2_1_0.set_k(self.gain3)
        self.blocks_multiply_const_vxx_0_1_2_2.set_k(self.gain3)

    def get_gain2(self):
        return self.gain2

    def set_gain2(self, gain2):
        self.gain2 = gain2
        self.blocks_multiply_const_vxx_0_1.set_k(self.gain2)
        self.blocks_multiply_const_vxx_0_1_0.set_k(self.gain2)
        self.blocks_multiply_const_vxx_0_1_1.set_k(self.gain2)
        self.blocks_multiply_const_vxx_0_1_1_0.set_k(self.gain2)

    def get_gain1(self):
        return self.gain1

    def set_gain1(self, gain1):
        self.gain1 = gain1
        self.blocks_multiply_const_vxx_0_0.set_k(self.gain1)
        self.blocks_multiply_const_vxx_0_0_0.set_k(self.gain1)
        self.blocks_multiply_const_vxx_0_0_1.set_k(self.gain1)
        self.blocks_multiply_const_vxx_0_0_1_0.set_k(self.gain1)

    def get_gain0(self):
        return self.gain0

    def set_gain0(self, gain0):
        self.gain0 = gain0
        self.blocks_multiply_const_vxx_0.set_k(self.gain0)
        self.blocks_multiply_const_vxx_0_2.set_k(self.gain0)
        self.blocks_multiply_const_vxx_0_3.set_k(self.gain0)
        self.blocks_multiply_const_vxx_0_3_0.set_k(self.gain0)



def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
