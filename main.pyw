from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from math import *
from mpmath import *

global lang
lang = 'English'


class mainvar:
    shape = 'Area - Square'
    unit = 'Inches'

def is_number(s):
    try:
        float(s)  # Try converting the input to a float
        return True
    except ValueError:
        return False

class _2D:
    def square(sl):
        return float(sl) ** 2
    def rectangle(l, w):
        return float(l) * float(w)
    def circle(r):
        return pi*(float(r) ** 2)
    def isosceles_triangle(b, h):
        return (1/2) * float(b) * float(h)
    def scalene_triangle(a, b, c):
        float(a)
        float(b)
        float(c)
        s = (a + b + c) / 2
        sa = s - a
        sb = s - b
        sc = s - c
        return sqrt(s * sa * sb * sc)
    def equilateral_triangle(sl):
        return ((sqrt(3)) / 4) * (float(sl) ** 2)
    def pentagon(sl):
        n = 5
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def hexagon(sl):
        n = 6
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def heptagon(sl):
        n = 7
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def octagon(sl):
        n = 8
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def nonagon(sl):
        n = 9
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def decagon(sl):
        n = 10
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def undecagon(sl):
        n = 11
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def dodecagon(sl):
        n = 12
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def tridecagon(sl):
        n = 13
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def tetradecagon(sl):
        n = 14
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def pentadecagon(sl):
        n = 15
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def trapezoid(a, b, h):
        return (1 / 2) * (float(a) + float(b)) * float(h)
    def ellipse(a, b):
        return (pi * float(a) * float(b))
    def polyomino(nos, ssl):
        return float(nos) * (float(ssl) ** 2)
    def star(nop, sl):
        return (1 / 4) * float(nop) * (float(sl) ** 2) * cot(pi / float(nop))
    def semicircle(r):
        return (pi * (float(r)) ** 2) / 2
    def squircle(bcttc, rr):
        return (_2D.square(float(bcttc)) - (_2D.square(float(rr)) * 4)) + _2D.circle(float(rr))
    def parallelogram(l, w):
        return float(l) * float(w)
    def annulus(ic, oc):
        return _2D.circle(float(oc)) - _2D.circle(float(ic))
    def kite(d1, d2):
        return (1 / 2) * (float(d1) * float(d2))
    def rhombus(d):
        return (1 / 2) * (float(d) ** 2)
class _3D:
    def tribonacci_constant():
        inner_term = 19 + 3 * sqrt(33)
        first_cube_root = inner_term ** (1/3)
        second_cube_root = (19 - 3 * sqrt(33)) ** (1/3)
        tribonacci_const = (1 + first_cube_root + second_cube_root) / 3
        return tribonacci_const
    tc = tribonacci_constant()
    def cube(el):
        return float(el) ** 3
    def rectangular_prism(l, w, h):
        return float(l) * float(w) * float(h)
    def sphere(r):
        return (4/3) * pi * (float(r) ** 3)
    def cylinder(r, h):
        return _2D.circle(float(r)) * float(h)
    def cone(r, h):
        return (1 / 3) * _2D.circle(float(r)) * float(h)
    def dodecahedron(el):
        return ((15 + 7 * sqrt(5)) / 4) * (float(el) ** 3)
    def isosceles_triangular_prism(bb, w, h):
        return _2D.isosceles_triangle(float(bb), float(w)) * float(h)
    def scalene_triangular_prism(ba, bb, bc, h):
        return _2D.scalene_triangle(float(ba), float(bb), float(bc)) * float(h)
    def equlateral_triangular_prism(bel, h):
        return _2D.equilateral_triangle(float(bel)) * float(h)
    def hemisphere(r):
        return _3D.sphere(float(r)) / 2
    def torus(R, r):
        return 2 * (pi ** 2) * (float(r) ** 2) * float(R)
    def rhombicosidodecahedron(el):
        return ((60 + 29 * sqrt(5)) / 3) * (float(el) ** 3)
    def snub_cube(el):
        return (float(el) ** 3) * ((8 * _3D.tc + 6) / (3 * sqrt(2 * ((_3D.tc ** 2) - 3))))
    def capsule(lwre, r):
        return _3D.cylinder(float(r), float(lwre)) + _3D.sphere(float(r))
    def tetrahedron(el):
        return(float(el) ** 3) / (6 * sqrt(2))
    def octahedron(el):
        return ((float(el) ** 3) * sqrt(2)) / 3
    def icosahedron(el):
        return (5 / 12) * (3 + sqrt(5)) * (float(el) ** 3)
    def isosceles_triangular_pyramid(bb, w, h):
        return (1 / 3) * _2D.isosceles_triangle(float(bb), float(w)) * float(h)
    def scalene_triangular_pyramid(ba, bb, bc, h):
        return (1 / 3) * _2D.scalene_triangle(float(ba), float(bb), float(bc)) * float(h)
    def equilateral_triangular_pyramid(bel, h):
        return (1 / 3) * _2D.equilateral_triangle(float(bel)) * float(h)
    def square_pyramid(bel, h):
        return (1 / 3) * _2D.square(float(bel)) * float(h)
    def pentagon_pyramid(bel, h):
        return (1 / 3) * _2D.pentagon(float(bel)) * float(h)
    def hexagon_pyramid(bel, h):
        return (1 / 3) * _2D.hexagon(float(bel)) * float(h)
    def heptagon_pyramid(bel, h):
        return (1 / 3) * _2D.heptagon(float(bel)) * float(h)
    def octagon_pyramid(bel, h):
        return (1 / 3) * _2D.octagon(float(bel)) * float(h)
    def nonagon_pyramid(bel, h):
        return (1 / 3) * _2D.nonagon(float(bel)) * float(h)
    def decagon_pyramid(bel, h):
        return (1 / 3) * _2D.decagon(float(bel)) * float(h)
    def star_prism(bnop, bel, h):
        return _2D.star(float(bnop), float(bel)) * float(h)
    def isosceles_triangular_bipyramid(l, w, h):
        h2 = float(h) / 2
        return 2 * _3D.isosceles_triangular_pyramid(float(l), float(w), h2)
    def equilateral_triangular_bipyramid(lw, h):
        h2 = float(h) / 2
        return 2 * _3D.equilateral_triangular_pyramid(float(lw), h2) 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u'MainWindow')
        MainWindow.resize(360, 640)
        MainWindow.setMinimumSize(QSize(360, 640))
        MainWindow.setMaximumSize(QSize(360, 640))
        icon = QIcon()
        icon.addFile(u'./assets/images/logo.png', QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.actionSolve = QAction(MainWindow)
        self.actionSolve.setObjectName(u'actionSolve')
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u'centralwidget')
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u'title')
        self.title.setGeometry(QRect(0, 0, 361, 21))
        font = QFont()
        font.setFamily(u'MS Shell Dlg 2')
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.title.setFont(font)
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.addItem('')
        self.comboBox_2.setObjectName(u'comboBox_2')
        self.comboBox_2.setGeometry(QRect(0, 40, 361, 61))
        font1 = QFont()
        font1.setPointSize(12)
        self.comboBox_2.setFont(font1)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u'line_2')
        self.line_2.setGeometry(QRect(-10, 100, 391, 20))
        self.line_2.setLineWidth(5)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u'line_3')
        self.line_3.setGeometry(QRect(-20, 20, 391, 20))
        self.line_3.setLineWidth(5)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u'line_4')
        self.line_4.setGeometry(QRect(-10, 160, 391, 20))
        self.line_4.setLineWidth(5)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem('')
        self.comboBox_3.addItem('')
        self.comboBox_3.addItem('')
        self.comboBox_3.addItem('')
        self.comboBox_3.addItem('')
        self.comboBox_3.addItem('')
        self.comboBox_3.addItem('')
        self.comboBox_3.addItem('')
        self.comboBox_3.addItem('')
        self.comboBox_3.setObjectName(u'comboBox_3')
        self.comboBox_3.setGeometry(QRect(0, 181, 361, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.comboBox_3.setFont(font2)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u'pushButton_2')
        self.pushButton_2.setGeometry(QRect(-1, 200, 362, 41))
        font3 = QFont()
        font3.setPointSize(15)
        self.pushButton_2.setFont(font3)

        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.answer = QLabel(self.centralwidget)
        self.answer.setObjectName(u'answer')
        self.answer.setGeometry(QRect(0, 260, 361, 41))
        font4 = QFont()
        font4.setPointSize(10)
        self.answer.setFont(font4)
        self.answer.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.Input1 = QPlainTextEdit(self.centralwidget)
        self.Input1.setObjectName(u'Input1')
        self.Input1.setGeometry(QRect(0, 130, 90, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input1.sizePolicy().hasHeightForWidth())
        self.Input1.setSizePolicy(sizePolicy)
        self.Input1.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.Input2 = QPlainTextEdit(self.centralwidget)
        self.Input2.setObjectName(u'Input2')
        self.Input2.setGeometry(QRect(90, 130, 90, 31))
        sizePolicy.setHeightForWidth(self.Input2.sizePolicy().hasHeightForWidth())
        self.Input2.setSizePolicy(sizePolicy)
        self.Input2.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.Input2.setReadOnly(True)
        self.Input3 = QPlainTextEdit(self.centralwidget)
        self.Input3.setObjectName(u'Input3')
        self.Input3.setGeometry(QRect(180, 130, 90, 31))
        sizePolicy.setHeightForWidth(self.Input3.sizePolicy().hasHeightForWidth())
        self.Input3.setSizePolicy(sizePolicy)
        self.Input3.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.Input3.setReadOnly(True)
        self.Input3Label = QLabel(self.centralwidget)
        self.Input3Label.setObjectName(u'Input3Label')
        self.Input3Label.setGeometry(QRect(180, 110, 91, 20))
        self.Input3Label.setAlignment(Qt.AlignCenter)
        self.Input2Label = QLabel(self.centralwidget)
        self.Input2Label.setObjectName(u'Input2Label')
        self.Input2Label.setGeometry(QRect(90, 110, 91, 20))
        self.Input2Label.setAlignment(Qt.AlignCenter)
        self.Input1Label = QLabel(self.centralwidget)
        self.Input1Label.setObjectName(u'Input1Label')
        self.Input1Label.setGeometry(QRect(0, 110, 91, 20))
        self.Input1Label.setAlignment(Qt.AlignCenter)
        self.Input4 = QPlainTextEdit(self.centralwidget)
        self.Input4.setObjectName(u'Input4')
        self.Input4.setGeometry(QRect(270, 130, 90, 31))
        sizePolicy.setHeightForWidth(self.Input4.sizePolicy().hasHeightForWidth())
        self.Input4.setSizePolicy(sizePolicy)
        self.Input4.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.Input4.setReadOnly(True)
        self.Input4Label = QLabel(self.centralwidget)
        self.Input4Label.setObjectName(u'Input4Label')
        self.Input4Label.setGeometry(QRect(270, 110, 91, 20))
        self.Input4Label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.Input2.setReadOnly(True)
        self.Input3.setReadOnly(True)
        self.Input4.setReadOnly(True)
        self.Input2Label.setText("")
        self.Input3Label.setText("")
        self.Input4Label.setText("")

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate('MainWindow', u'Area and Volume Calculator', None))
        self.title.setText(QCoreApplication.translate('MainWindow', u'Area and Volume Calculator', None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate('MainWindow', u'Area - Square', None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate('MainWindow', u'Area - Rectangle', None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate('MainWindow', u'Area - Circle', None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate('MainWindow', u'Area - Isosceles triangle', None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate('MainWindow', u'Area - Scalene triangle', None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate('MainWindow', u'Area - Equilateral triangle', None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate('MainWindow', u'Area - Pentagon', None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate('MainWindow', u'Area - Hexagon', None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate('MainWindow', u'Area - Heptagon', None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate('MainWindow', u'Area - Octagon', None))
        self.comboBox_2.setItemText(10, QCoreApplication.translate('MainWindow', u'Area - Nonagon', None))
        self.comboBox_2.setItemText(11, QCoreApplication.translate('MainWindow', u'Area - Decagon', None))
        self.comboBox_2.setItemText(12, QCoreApplication.translate('MainWindow', u'Area - Undecagon', None))
        self.comboBox_2.setItemText(13, QCoreApplication.translate('MainWindow', u'Area - Dodecagon', None))
        self.comboBox_2.setItemText(14, QCoreApplication.translate('MainWindow', u'Area - Tridecagon', None))
        self.comboBox_2.setItemText(15, QCoreApplication.translate('MainWindow', u'Area - Tetradecagon', None))
        self.comboBox_2.setItemText(16, QCoreApplication.translate('MainWindow', u'Area - Pentadecagon', None))
        self.comboBox_2.setItemText(17, QCoreApplication.translate('MainWindow', u'Area - Trapezoid', None))
        self.comboBox_2.setItemText(18, QCoreApplication.translate('MainWindow', u'Area - Ellipse', None))
        self.comboBox_2.setItemText(19, QCoreApplication.translate('MainWindow', u'Area - Polyomino', None))
        self.comboBox_2.setItemText(20, QCoreApplication.translate('MainWindow', u'Area - Star', None))
        self.comboBox_2.setItemText(21, QCoreApplication.translate('MainWindow', u'Area - Semicircle', None))
        self.comboBox_2.setItemText(22, QCoreApplication.translate('MainWindow', u'Area - Squircle', None))
        self.comboBox_2.setItemText(23, QCoreApplication.translate('MainWindow', u'Area - Parallelogram', None))
        self.comboBox_2.setItemText(24, QCoreApplication.translate('MainWindow', u'Area - Annulus', None))
        self.comboBox_2.setItemText(25, QCoreApplication.translate('MainWindow', u'Area - Kite', None))
        self.comboBox_2.setItemText(26, QCoreApplication.translate('MainWindow', u'Area - Rhombus', None))
        self.comboBox_2.setItemText(27, QCoreApplication.translate('MainWindow', u'Volume - Cube', None))
        self.comboBox_2.setItemText(28, QCoreApplication.translate('MainWindow', u'Volume - Rectangular prism', None))
        self.comboBox_2.setItemText(29, QCoreApplication.translate('MainWindow', u'Volume - Sphere', None))
        self.comboBox_2.setItemText(30, QCoreApplication.translate('MainWindow', u'Volume - Cylinder', None))
        self.comboBox_2.setItemText(31, QCoreApplication.translate('MainWindow', u'Volume - Cone', None))
        self.comboBox_2.setItemText(32, QCoreApplication.translate('MainWindow', u'Volume - Dodecahedron', None))
        self.comboBox_2.setItemText(33, QCoreApplication.translate('MainWindow', u'Volume - Isosceles triangular prism', None))
        self.comboBox_2.setItemText(34, QCoreApplication.translate('MainWindow', u'Volume - Scalene triangular prism', None))
        self.comboBox_2.setItemText(35, QCoreApplication.translate('MainWindow', u'Volume - Equilateral triangular prism', None))
        self.comboBox_2.setItemText(36, QCoreApplication.translate('MainWindow', u'Volume - Hemisphere', None))
        self.comboBox_2.setItemText(37, QCoreApplication.translate('MainWindow', u'Volume - Torus', None))
        self.comboBox_2.setItemText(38, QCoreApplication.translate('MainWindow', u'Volume - Rhombicosidodecahedron', None))
        self.comboBox_2.setItemText(39, QCoreApplication.translate('MainWindow', u'Volume - Snub cube', None))
        self.comboBox_2.setItemText(40, QCoreApplication.translate('MainWindow', u'Volume - Capsule', None))
        self.comboBox_2.setItemText(41, QCoreApplication.translate('MainWindow', u'Volume - Tetrahedron', None))
        self.comboBox_2.setItemText(42, QCoreApplication.translate('MainWindow', u'Volume - Octahedron', None))
        self.comboBox_2.setItemText(43, QCoreApplication.translate('MainWindow', u'Volume - Icosahedron', None))
        self.comboBox_2.setItemText(44, QCoreApplication.translate('MainWindow', u'Volume - Isosceles triangular pyramid', None))
        self.comboBox_2.setItemText(45, QCoreApplication.translate('MainWindow', u'Volume - Scalene triangular pyramid', None))
        self.comboBox_2.setItemText(46, QCoreApplication.translate('MainWindow', u'Volume - Equilateral triangular pyramid', None))
        self.comboBox_2.setItemText(47, QCoreApplication.translate('MainWindow', u'Volume - Square pyramid', None))
        self.comboBox_2.setItemText(48, QCoreApplication.translate('MainWindow', u'Volume - Pentagonal pyramid', None))
        self.comboBox_2.setItemText(49, QCoreApplication.translate('MainWindow', u'Volume - Hexagonal pyramid', None))
        self.comboBox_2.setItemText(50, QCoreApplication.translate('MainWindow', u'Volume - Heptagonal pyramid', None))
        self.comboBox_2.setItemText(51, QCoreApplication.translate('MainWindow', u'Volume - Octagonal pyramid', None))
        self.comboBox_2.setItemText(52, QCoreApplication.translate('MainWindow', u'Volume - Nonagonal pyramid', None))
        self.comboBox_2.setItemText(53, QCoreApplication.translate('MainWindow', u'Volume - Decagonal pyramid', None))
        self.comboBox_2.setItemText(54, QCoreApplication.translate('MainWindow', u'Volume - Star prism', None))
        self.comboBox_2.setItemText(55, QCoreApplication.translate('MainWindow', u'Volume - Isosceles triangular bipyramid', None))
        self.comboBox_2.setItemText(56, QCoreApplication.translate('MainWindow', u'Volume - Equilateral triangular bipyramid', None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate('MainWindow', u'Inches', None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate('MainWindow', u'Feet', None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate('MainWindow', u'Yards', None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate('MainWindow', u'Miles', None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate('MainWindow', u'Millimeters', None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate('MainWindow', u'Centimeters', None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate('MainWindow', u'Meters', None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate('MainWindow', u'Kilometers', None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate('MainWindow', u'None', None))

        self.pushButton_2.setText(QCoreApplication.translate('MainWindow', u'Solve', ))
        self.answer.setText(QCoreApplication.translate('MainWindow', u'Answer', None))
        self.Input3Label.setText(QCoreApplication.translate('MainWindow', u'', None))
        self.Input4Label.setText(QCoreApplication.translate('MainWindow', u'', None))
        self.Input2Label.setText(QCoreApplication.translate('MainWindow', u'', None))
        self.Input1Label.setText(QCoreApplication.translate('MainWindow', u'Side length:', None))




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Instantiate your existing UI class
        self.ui.setupUi(self)  # Setup your UI

        # Connect signals to slots here if needed
        self.ui.comboBox_3.currentTextChanged.connect(self.update_units)
        self.ui.comboBox_2.currentTextChanged.connect(self.update_shape)
        self.ui.pushButton_2.clicked.connect(self.solve)
        # Add any additional setup or functionality here

    def solve(self):
        if mainvar.shape == u'Area - Square':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.square(float(a))
                    self.ui.answer.setText("Square area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.square(float(a))
                    self.ui.answer.setText("Square area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.square(float(a))
                    self.ui.answer.setText("Square area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.square(float(a))
                    self.ui.answer.setText("Square area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.square(float(a))
                    self.ui.answer.setText("Square area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.square(float(a))
                    self.ui.answer.setText("Square area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.square(float(a))
                    self.ui.answer.setText("Square area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.square(float(a))
                    self.ui.answer.setText("Square area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.square(float(a))
                    self.ui.answer.setText("Square area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Rectangle':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.rectangle(float(a), float(b))
                    self.ui.answer.setText("Rectangle area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.rectangle(float(a), float(b))
                    self.ui.answer.setText("Rectangle area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.rectangle(float(a), float(b))
                    self.ui.answer.setText("Rectangle area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.rectangle(float(a), float(b))
                    self.ui.answer.setText("Rectangle area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.rectangle(float(a), float(b))
                    self.ui.answer.setText("Rectangle area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.rectangle(float(a), float(b))
                    self.ui.answer.setText("Rectangle area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.rectangle(float(a), float(b))
                    self.ui.answer.setText("Rectangle area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.rectangle(float(a), float(b))
                    self.ui.answer.setText("Rectangle area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.rectangle(float(a), float(b))
                    self.ui.answer.setText("Rectangle area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Circle':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.circle(float(a))
                    self.ui.answer.setText("Circle area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.circle(float(a))
                    self.ui.answer.setText("Circle area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.circle(float(a))
                    self.ui.answer.setText("Circle area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.circle(float(a))
                    self.ui.answer.setText("Circle area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.circle(float(a))
                    self.ui.answer.setText("Circle area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.circle(float(a))
                    self.ui.answer.setText("Circle area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.circle(float(a))
                    self.ui.answer.setText("Circle area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.circle(float(a))
                    self.ui.answer.setText("Circle area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.circle(float(a))
                    self.ui.answer.setText("Circle area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Isosceles triangle':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.isosceles_triangle(float(a), float(b))
                    self.ui.answer.setText("Isosceles triangle area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.isosceles_triangle(float(a), float(b))
                    self.ui.answer.setText("Isosceles triangle area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.isosceles_triangle(float(a), float(b))
                    self.ui.answer.setText("Isosceles triangle area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.isosceles_triangle(float(a), float(b))
                    self.ui.answer.setText("Isosceles triangle area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.isosceles_triangle(float(a), float(b))
                    self.ui.answer.setText("Isosceles triangle area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.isosceles_triangle(float(a), float(b))
                    self.ui.answer.setText("Isosceles triangle area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.isosceles_triangle(float(a), float(b))
                    self.ui.answer.setText("Isosceles triangle area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.isosceles_triangle(float(a), float(b))
                    self.ui.answer.setText("Isosceles triangle area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.isosceles_triangle(float(a), float(b))
                    self.ui.answer.setText("Isosceles triangle area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Scalene triangle':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            c = is_number(self.ui.Input3.toPlainText())
            if a == True and b == True and c == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.scalene_triangle(float(a), float(b), float(c))
                    self.ui.answer.setText("Scalene triangle area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.scalene_triangle(float(a), float(b), float(c))
                    self.ui.answer.setText("Scalene triangle area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.scalene_triangle(float(a), float(b), float(c))
                    self.ui.answer.setText("Scalene triangle area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.scalene_triangle(float(a), float(b), float(c))
                    self.ui.answer.setText("Scalene triangle area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.scalene_triangle(float(a), float(b), float(c))
                    self.ui.answer.setText("Scalene triangle area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.scalene_triangle(float(a), float(b), float(c))
                    self.ui.answer.setText("Scalene triangle area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.scalene_triangle(float(a), float(b), float(c))
                    self.ui.answer.setText("Scalene triangle area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.scalene_triangle(float(a), float(b), float(c))
                    self.ui.answer.setText("Scalene triangle area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.scalene_triangle(float(a), float(b), float(c))
                    self.ui.answer.setText("Scalene triangle area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Equilateral triangle':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.equilateral_triangle(float(a))
                    self.ui.answer.setText("Equilateral triangle area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.equilateral_triangle(float(a))
                    self.ui.answer.setText("Equilateral triangle area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.equilateral_triangle(float(a))
                    self.ui.answer.setText("Equilateral triangle area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.equilateral_triangle(float(a))
                    self.ui.answer.setText("Equilateral triangle area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.equilateral_triangle(float(a))
                    self.ui.answer.setText("Equilateral triangle area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.equilateral_triangle(float(a))
                    self.ui.answer.setText("Equilateral triangle area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.equilateral_triangle(float(a))
                    self.ui.answer.setText("Equilateral triangle area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.equilateral_triangle(float(a))
                    self.ui.answer.setText("Equilateral triangle area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.equilateral_triangle(float(a))
                    self.ui.answer.setText("Equilateral triangle area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Pentagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.pentagon(float(a))
                    self.ui.answer.setText("Pentagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.pentagon(float(a))
                    self.ui.answer.setText("Pentagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.pentagon(float(a))
                    self.ui.answer.setText("Pentagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.pentagon(float(a))
                    self.ui.answer.setText("Pentagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.pentagon(float(a))
                    self.ui.answer.setText("Pentagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.pentagon(float(a))
                    self.ui.answer.setText("Pentagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.pentagon(float(a))
                    self.ui.answer.setText("Pentagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.pentagon(float(a))
                    self.ui.answer.setText("Pentagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.pentagon(float(a))
                    self.ui.answer.setText("Pentagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Hexagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.hexagon(float(a))
                    self.ui.answer.setText("Hexagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.hexagon(float(a))
                    self.ui.answer.setText("Hexagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.hexagon(float(a))
                    self.ui.answer.setText("Hexagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.hexagon(float(a))
                    self.ui.answer.setText("Hexagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.hexagon(float(a))
                    self.ui.answer.setText("Hexagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.hexagon(float(a))
                    self.ui.answer.setText("Hexagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.hexagon(float(a))
                    self.ui.answer.setText("Hexagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.hexagon(float(a))
                    self.ui.answer.setText("Hexagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.hexagon(float(a))
                    self.ui.answer.setText("Hexagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Heptagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.heptagon(float(a))
                    self.ui.answer.setText("Heptagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.heptagon(float(a))
                    self.ui.answer.setText("Heptagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.heptagon(float(a))
                    self.ui.answer.setText("Heptagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.heptagon(float(a))
                    self.ui.answer.setText("Heptagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.heptagon(float(a))
                    self.ui.answer.setText("Heptagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.heptagon(float(a))
                    self.ui.answer.setText("Heptagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.heptagon(float(a))
                    self.ui.answer.setText("Heptagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.heptagon(float(a))
                    self.ui.answer.setText("Heptagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.heptagon(float(a))
                    self.ui.answer.setText("Heptagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Octagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.octagon(float(a))
                    self.ui.answer.setText("Octagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.octagon(float(a))
                    self.ui.answer.setText("Octagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.octagon(float(a))
                    self.ui.answer.setText("Octagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.octagon(float(a))
                    self.ui.answer.setText("Octagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.octagon(float(a))
                    self.ui.answer.setText("Octagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.octagon(float(a))
                    self.ui.answer.setText("Octagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.octagon(float(a))
                    self.ui.answer.setText("Octagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.octagon(float(a))
                    self.ui.answer.setText("Octagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.octagon(float(a))
                    self.ui.answer.setText("Octagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Nonagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.nonagon(float(a))
                    self.ui.answer.setText("Nonagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.nonagon(float(a))
                    self.ui.answer.setText("Nonagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.nonagon(float(a))
                    self.ui.answer.setText("Nonagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.nonagon(float(a))
                    self.ui.answer.setText("Nonagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.nonagon(float(a))
                    self.ui.answer.setText("Nonagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.nonagon(float(a))
                    self.ui.answer.setText("Nonagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.nonagon(float(a))
                    self.ui.answer.setText("Nonagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.nonagon(float(a))
                    self.ui.answer.setText("Nonagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.nonagon(float(a))
                    self.ui.answer.setText("Nonagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Decagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.decagon(float(a))
                    self.ui.answer.setText("Decagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.decagon(float(a))
                    self.ui.answer.setText("Decagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.decagon(float(a))
                    self.ui.answer.setText("Decagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.decagon(float(a))
                    self.ui.answer.setText("Decagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.decagon(float(a))
                    self.ui.answer.setText("Decagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.decagon(float(a))
                    self.ui.answer.setText("Decagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.decagon(float(a))
                    self.ui.answer.setText("Decagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.decagon(float(a))
                    self.ui.answer.setText("Decagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.decagon(float(a))
                    self.ui.answer.setText("Decagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Undecagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.undecagon(float(a))
                    self.ui.answer.setText("Undecagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.undecagon(float(a))
                    self.ui.answer.setText("Undecagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.undecagon(float(a))
                    self.ui.answer.setText("Undecagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.undecagon(float(a))
                    self.ui.answer.setText("Undecagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.undecagon(float(a))
                    self.ui.answer.setText("Undecagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.undecagon(float(a))
                    self.ui.answer.setText("Undecagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.undecagon(float(a))
                    self.ui.answer.setText("Undecagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.undecagon(float(a))
                    self.ui.answer.setText("Undecagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.undecagon(float(a))
                    self.ui.answer.setText("Undecagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Dodecagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.dodecagon(float(a))
                    self.ui.answer.setText("Dodecagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.dodecagon(float(a))
                    self.ui.answer.setText("Dodecagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.dodecagon(float(a))
                    self.ui.answer.setText("Dodecagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.dodecagon(float(a))
                    self.ui.answer.setText("Dodecagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.dodecagon(float(a))
                    self.ui.answer.setText("Dodecagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.dodecagon(float(a))
                    self.ui.answer.setText("Dodecagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.dodecagon(float(a))
                    self.ui.answer.setText("Dodecagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.dodecagon(float(a))
                    self.ui.answer.setText("Dodecagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.dodecagon(float(a))
                    self.ui.answer.setText("Dodecagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Tridecagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.tridecagon(float(a))
                    self.ui.answer.setText("Tridecagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.tridecagon(float(a))
                    self.ui.answer.setText("Tridecagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.tridecagon(float(a))
                    self.ui.answer.setText("Tridecagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.tridecagon(float(a))
                    self.ui.answer.setText("Tridecagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.tridecagon(float(a))
                    self.ui.answer.setText("Tridecagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.tridecagon(float(a))
                    self.ui.answer.setText("Tridecagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.tridecagon(float(a))
                    self.ui.answer.setText("Tridecagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.tridecagon(float(a))
                    self.ui.answer.setText("Tridecagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.tridecagon(float(a))
                    self.ui.answer.setText("Tridecagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Tetradecagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.tetradecagon(float(a))
                    self.ui.answer.setText("Tetradecagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.tetradecagon(float(a))
                    self.ui.answer.setText("Tetradecagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.tetradecagon(float(a))
                    self.ui.answer.setText("Tetradecagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.tetradecagon(float(a))
                    self.ui.answer.setText("Tetradecagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.tetradecagon(float(a))
                    self.ui.answer.setText("Tetradecagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.tetradecagon(float(a))
                    self.ui.answer.setText("Tetradecagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.tetradecagon(float(a))
                    self.ui.answer.setText("Tetradecagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.tetradecagon(float(a))
                    self.ui.answer.setText("Tetradecagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.tetradecagon(float(a))
                    self.ui.answer.setText("Tetradecagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Pentadecagon':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.pentadecagon(float(a))
                    self.ui.answer.setText("Pentadecagon area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.pentadecagon(float(a))
                    self.ui.answer.setText("Pentadecagon area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.pentadecagon(float(a))
                    self.ui.answer.setText("Pentadecagon area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.pentadecagon(float(a))
                    self.ui.answer.setText("Pentadecagon area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.pentadecagon(float(a))
                    self.ui.answer.setText("Pentadecagon area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.pentadecagon(float(a))
                    self.ui.answer.setText("Pentadecagon area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.pentadecagon(float(a))
                    self.ui.answer.setText("Pentadecagon area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.pentadecagon(float(a))
                    self.ui.answer.setText("Pentadecagon area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.pentadecagon(float(a))
                    self.ui.answer.setText("Pentadecagon area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Trapezoid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            c = is_number(self.ui.Input3.toPlainText())
            if a == True and b == True and c == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.trapezoid(float(a), float(b), float(c))
                    self.ui.answer.setText("Trapezoid area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.trapezoid(float(a), float(b), float(c))
                    self.ui.answer.setText("Trapezoid area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.trapezoid(float(a), float(b), float(c))
                    self.ui.answer.setText("Trapezoid area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.trapezoid(float(a), float(b), float(c))
                    self.ui.answer.setText("Trapezoid area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.trapezoid(float(a), float(b), float(c))
                    self.ui.answer.setText("Trapezoid area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.trapezoid(float(a), float(b), float(c))
                    self.ui.answer.setText("Trapezoid area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.trapezoid(float(a), float(b), float(c))
                    self.ui.answer.setText("Trapezoid area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.trapezoid(float(a), float(b), float(c))
                    self.ui.answer.setText("Trapezoid area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.trapezoid(float(a), float(b), float(c))
                    self.ui.answer.setText("Trapezoid area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Ellipse':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.ellipse(float(a), float(b))
                    self.ui.answer.setText("Ellipse area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.ellipse(float(a), float(b))
                    self.ui.answer.setText("Ellipse area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.ellipse(float(a), float(b))
                    self.ui.answer.setText("Ellipse area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.ellipse(float(a), float(b))
                    self.ui.answer.setText("Ellipse area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.ellipse(float(a), float(b))
                    self.ui.answer.setText("Ellipse area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.ellipse(float(a), float(b))
                    self.ui.answer.setText("Ellipse area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.ellipse(float(a), float(b))
                    self.ui.answer.setText("Ellipse area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.ellipse(float(a), float(b))
                    self.ui.answer.setText("Ellipse area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.ellipse(float(a), float(b))
                    self.ui.answer.setText("Ellipse area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Polyomino':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.polyomino(float(a), float(b))
                    self.ui.answer.setText("Polyomino area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.polyomino(float(a), float(b))
                    self.ui.answer.setText("Polyomino area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.polyomino(float(a), float(b))
                    self.ui.answer.setText("Polyomino area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.polyomino(float(a), float(b))
                    self.ui.answer.setText("Polyomino area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.polyomino(float(a), float(b))
                    self.ui.answer.setText("Polyomino area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.polyomino(float(a), float(b))
                    self.ui.answer.setText("Polyomino area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.polyomino(float(a), float(b))
                    self.ui.answer.setText("Polyomino area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.polyomino(float(a), float(b))
                    self.ui.answer.setText("Polyomino area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.polyomino(float(a), float(b))
                    self.ui.answer.setText("Polyomino area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Star':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.star(float(a), float(b))
                    self.ui.answer.setText("Star area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.star(float(a), float(b))
                    self.ui.answer.setText("Star area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.star(float(a), float(b))
                    self.ui.answer.setText("Star area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.star(float(a), float(b))
                    self.ui.answer.setText("Star area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.star(float(a), float(b))
                    self.ui.answer.setText("Star area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.star(float(a), float(b))
                    self.ui.answer.setText("Star area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.star(float(a), float(b))
                    self.ui.answer.setText("Star area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.star(float(a), float(b))
                    self.ui.answer.setText("Star area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.star(float(a), float(b))
                    self.ui.answer.setText("Star area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Semicircle':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.semicircle(float(a))
                    self.ui.answer.setText("Semicircle area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.semicircle(float(a))
                    self.ui.answer.setText("Semicircle area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.semicircle(float(a))
                    self.ui.answer.setText("Semicircle area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.semicircle(float(a))
                    self.ui.answer.setText("Semicircle area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.semicircle(float(a))
                    self.ui.answer.setText("Semicircle area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.semicircle(float(a))
                    self.ui.answer.setText("Semicircle area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.semicircle(float(a))
                    self.ui.answer.setText("Semicircle area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.semicircle(float(a))
                    self.ui.answer.setText("Semicircle area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.semicircle(float(a))
                    self.ui.answer.setText("Semicircle area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Squircle':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.squircle(float(a), float(b))
                    self.ui.answer.setText("Squircle area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.squircle(float(a), float(b))
                    self.ui.answer.setText("Squircle area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.squircle(float(a), float(b))
                    self.ui.answer.setText("Squircle area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.squircle(float(a), float(b))
                    self.ui.answer.setText("Squircle area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.squircle(float(a), float(b))
                    self.ui.answer.setText("Squircle area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.squircle(float(a), float(b))
                    self.ui.answer.setText("Squircle area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.squircle(float(a), float(b))
                    self.ui.answer.setText("Squircle area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.squircle(float(a), float(b))
                    self.ui.answer.setText("Squircle area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.squircle(float(a), float(b))
                    self.ui.answer.setText("Squircle area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Parallelogram':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.parallelogram(float(a), float(b))
                    self.ui.answer.setText("Parallelogram area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.parallelogram(float(a), float(b))
                    self.ui.answer.setText("Parallelogram area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.parallelogram(float(a), float(b))
                    self.ui.answer.setText("Parallelogram area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.parallelogram(float(a), float(b))
                    self.ui.answer.setText("Parallelogram area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.parallelogram(float(a), float(b))
                    self.ui.answer.setText("Parallelogram area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.parallelogram(float(a), float(b))
                    self.ui.answer.setText("Parallelogram area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.parallelogram(float(a), float(b))
                    self.ui.answer.setText("Parallelogram area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.parallelogram(float(a), float(b))
                    self.ui.answer.setText("Parallelogram area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.parallelogram(float(a), float(b))
                    self.ui.answer.setText("Parallelogram area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Annulus':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.annulus(float(a), float(b))
                    self.ui.answer.setText("Annulus area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.annulus(float(a), float(b))
                    self.ui.answer.setText("Annulus area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.annulus(float(a), float(b))
                    self.ui.answer.setText("Annulus area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.annulus(float(a), float(b))
                    self.ui.answer.setText("Annulus area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.annulus(float(a), float(b))
                    self.ui.answer.setText("Annulus area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.annulus(float(a), float(b))
                    self.ui.answer.setText("Annulus area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.annulus(float(a), float(b))
                    self.ui.answer.setText("Annulus area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.annulus(float(a), float(b))
                    self.ui.answer.setText("Annulus area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.annulus(float(a), float(b))
                    self.ui.answer.setText("Annulus area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Kite':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.kite(float(a), float(b))
                    self.ui.answer.setText("Kite area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.kite(float(a), float(b))
                    self.ui.answer.setText("Kite area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.kite(float(a), float(b))
                    self.ui.answer.setText("Kite area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.kite(float(a), float(b))
                    self.ui.answer.setText("Kite area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.kite(float(a), float(b))
                    self.ui.answer.setText("Kite area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.kite(float(a), float(b))
                    self.ui.answer.setText("Kite area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.kite(float(a), float(b))
                    self.ui.answer.setText("Kite area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.kite(float(a), float(b))
                    self.ui.answer.setText("Kite area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.kite(float(a), float(b))
                    self.ui.answer.setText("Kite area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Area - Rhombus':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _2D.rhombus(float(a))
                    self.ui.answer.setText("Rhombus area: " + str(ans) + u" in²")
                if mainvar.unit == u'Feet':
                    ans = _2D.rhombus(float(a))
                    self.ui.answer.setText("Rhombus area: " + str(ans) + u" ft²")
                if mainvar.unit == u'Yards':
                    ans = _2D.rhombus(float(a))
                    self.ui.answer.setText("Rhombus area: " + str(ans) + u" yd²")
                if mainvar.unit == u'Miles':
                    ans = _2D.rhombus(float(a))
                    self.ui.answer.setText("Rhombus area: " + str(ans) + u" mi²")
                if mainvar.unit == u'Millimeters':
                    ans = _2D.rhombus(float(a))
                    self.ui.answer.setText("Rhombus area: " + str(ans) + u" mm²")
                if mainvar.unit == u'Centimeters':
                    ans = _2D.rhombus(float(a))
                    self.ui.answer.setText("Rhombus area: " + str(ans) + u" cm²")
                if mainvar.unit == u'Meters':
                    ans = _2D.rhombus(float(a))
                    self.ui.answer.setText("Rhombus area: " + str(ans) + u" m²")
                if mainvar.unit == u'Kilometers':
                    ans = _2D.rhombus(float(a))
                    self.ui.answer.setText("Rhombus area: " + str(ans) + u" km²")
                if mainvar.unit == u'None':
                    ans = _2D.rhombus(float(a))
                    self.ui.answer.setText("Rhombus area: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Cube':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.cube(float(a))
                    self.ui.answer.setText("Cube volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.cube(float(a))
                    self.ui.answer.setText("Cube volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.cube(float(a))
                    self.ui.answer.setText("Cube volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.cube(float(a))
                    self.ui.answer.setText("Cube volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.cube(float(a))
                    self.ui.answer.setText("Cube volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.cube(float(a))
                    self.ui.answer.setText("Cube volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.cube(float(a))
                    self.ui.answer.setText("Cube volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.cube(float(a))
                    self.ui.answer.setText("Cube volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.cube(float(a))
                    self.ui.answer.setText("Cube volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Rectangular prism':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            c = is_number(self.ui.Input3.toPlainText())
            if a == True and b == True and c == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.rectangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Rectangular prism volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.rectangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Rectangular prism volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.rectangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Rectangular prism volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.rectangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Rectangular prism volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.rectangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Rectangular prism volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.rectangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Rectangular prism volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.rectangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Rectangular prism volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.rectangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Rectangular prism volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.rectangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Rectangular prism volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
           
        elif mainvar.shape == u'Volume - Sphere':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.sphere(float(a))
                    self.ui.answer.setText("Sphere volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.sphere(float(a))
                    self.ui.answer.setText("Sphere volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.sphere(float(a))
                    self.ui.answer.setText("Sphere volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.sphere(float(a))
                    self.ui.answer.setText("Sphere volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.sphere(float(a))
                    self.ui.answer.setText("Sphere volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.sphere(float(a))
                    self.ui.answer.setText("Sphere volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.sphere(float(a))
                    self.ui.answer.setText("Sphere volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.sphere(float(a))
                    self.ui.answer.setText("Sphere volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.sphere(float(a))
                    self.ui.answer.setText("Sphere volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Cylinder':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.cylinder(float(a), float(b))
                    self.ui.answer.setText("Cylinder volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.cylinder(float(a), float(b))
                    self.ui.answer.setText("Cylinder volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.cylinder(float(a), float(b))
                    self.ui.answer.setText("Cylinder volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.cylinder(float(a), float(b))
                    self.ui.answer.setText("Cylinder volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.cylinder(float(a), float(b))
                    self.ui.answer.setText("Cylinder volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.cylinder(float(a), float(b))
                    self.ui.answer.setText("Cylinder volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.cylinder(float(a), float(b))
                    self.ui.answer.setText("Cylinder volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.cylinder(float(a), float(b))
                    self.ui.answer.setText("Cylinder volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.cylinder(float(a), float(b))
                    self.ui.answer.setText("Cylinder volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Cone':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.cone(float(a), float(b))
                    self.ui.answer.setText("Cone volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.cone(float(a), float(b))
                    self.ui.answer.setText("Cone volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.cone(float(a), float(b))
                    self.ui.answer.setText("Cone volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.cone(float(a), float(b))
                    self.ui.answer.setText("Cone volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.cone(float(a), float(b))
                    self.ui.answer.setText("Cone volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.cone(float(a), float(b))
                    self.ui.answer.setText("Cone volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.cone(float(a), float(b))
                    self.ui.answer.setText("Cone volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.cone(float(a), float(b))
                    self.ui.answer.setText("Cone volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.cone(float(a), float(b))
                    self.ui.answer.setText("Cone volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Dodecahedron':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.dodecahedron(float(a))
                    self.ui.answer.setText("Dodecahedron volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.dodecahedron(float(a))
                    self.ui.answer.setText("Dodecahedron volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.dodecahedron(float(a))
                    self.ui.answer.setText("Dodecahedron volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.dodecahedron(float(a))
                    self.ui.answer.setText("Dodecahedron volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.dodecahedron(float(a))
                    self.ui.answer.setText("Dodecahedron volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.dodecahedron(float(a))
                    self.ui.answer.setText("Dodecahedron volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.dodecahedron(float(a))
                    self.ui.answer.setText("Dodecahedron volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.dodecahedron(float(a))
                    self.ui.answer.setText("Dodecahedron volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.dodecahedron(float(a))
                    self.ui.answer.setText("Dodecahedron volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Isosceles triangular prism':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            c = is_number(self.ui.Input3.toPlainText())
            if a == True and b == True and c == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.isosceles_triangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular prism volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.isosceles_triangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular prism volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.isosceles_triangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular prism volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.isosceles_triangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular prism volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.isosceles_triangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular prism volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.isosceles_triangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular prism volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.isosceles_triangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular prism volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.isosceles_triangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular prism volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.isosceles_triangular_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular prism volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Scalene triangular prism':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            c = is_number(self.ui.Input3.toPlainText())
            d = is_number(self.ui.Input4.toPlainText())
            if a == True and b == True and c == True and d == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.scalene_triangular_prism(float(a), float(b), float(c), float(d))
                    self.ui.answer.setText("Scalene triangular prism volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.scalene_triangular_prism(float(a), float(b), float(c), float(d))
                    self.ui.answer.setText("Scalene triangular prism volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.scalene_triangular_prism(float(a), float(b), float(c), float(d))
                    self.ui.answer.setText("Scalene triangular prism volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.scalene_triangular_prism(float(a), float(b), float(c), float(d))
                    self.ui.answer.setText("Scalene triangular prism volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.scalene_triangular_prism(float(a), float(b), float(c), float(d))
                    self.ui.answer.setText("Scalene triangular prism volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.scalene_triangular_prism(float(a), float(b), float(c), float(d))
                    self.ui.answer.setText("Scalene triangular prism volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.scalene_triangular_prism(float(a), float(b), float(c), float(d))
                    self.ui.answer.setText("Scalene triangular prism volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.scalene_triangular_prism(float(a), float(b), float(c), float(d))
                    self.ui.answer.setText("Scalene triangular prism volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.scalene_triangular_prism(float(a), float(b), float(c), float(d))
                    self.ui.answer.setText("Scalene triangular prism volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Equilateral triangular prism':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.equlateral_triangular_prism(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular prism volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.equlateral_triangular_prism(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular prism volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.equlateral_triangular_prism(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular prism volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.equlateral_triangular_prism(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular prism volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.equlateral_triangular_prism(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular prism volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.equlateral_triangular_prism(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular prism volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.equlateral_triangular_prism(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular prism volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.equlateral_triangular_prism(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular prism volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.equlateral_triangular_prism(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular prism volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Hemisphere':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.hemisphere(float(a))
                    self.ui.answer.setText("Hemisphere volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.hemisphere(float(a))
                    self.ui.answer.setText("Hemisphere volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.hemisphere(float(a))
                    self.ui.answer.setText("Hemisphere volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.hemisphere(float(a))
                    self.ui.answer.setText("Hemisphere volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.hemisphere(float(a))
                    self.ui.answer.setText("Hemisphere volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.hemisphere(float(a))
                    self.ui.answer.setText("Hemisphere volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.hemisphere(float(a))
                    self.ui.answer.setText("Hemisphere volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.hemisphere(float(a))
                    self.ui.answer.setText("Hemisphere volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.hemisphere(float(a))
                    self.ui.answer.setText("Hemisphere volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Torus':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.torus(float(a), float(b))
                    self.ui.answer.setText("Torus volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.torus(float(a), float(b))
                    self.ui.answer.setText("Torus volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.torus(float(a), float(b))
                    self.ui.answer.setText("Torus volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.torus(float(a), float(b))
                    self.ui.answer.setText("Torus volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.torus(float(a), float(b))
                    self.ui.answer.setText("Torus volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.torus(float(a), float(b))
                    self.ui.answer.setText("Torus volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.torus(float(a), float(b))
                    self.ui.answer.setText("Torus volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.torus(float(a), float(b))
                    self.ui.answer.setText("Torus volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.torus(float(a), float(b))
                    self.ui.answer.setText("Torus volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Rhombicosidodecahedron':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.rhombicosidodecahedron(float(a))
                    self.ui.answer.setText("Rhombicosidodecahedron volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.rhombicosidodecahedron(float(a))
                    self.ui.answer.setText("Rhombicosidodecahedron volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.rhombicosidodecahedron(float(a))
                    self.ui.answer.setText("Rhombicosidodecahedron volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.rhombicosidodecahedron(float(a))
                    self.ui.answer.setText("Rhombicosidodecahedron volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.rhombicosidodecahedron(float(a))
                    self.ui.answer.setText("Rhombicosidodecahedron volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.rhombicosidodecahedron(float(a))
                    self.ui.answer.setText("Rhombicosidodecahedron volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.rhombicosidodecahedron(float(a))
                    self.ui.answer.setText("Rhombicosidodecahedron volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.rhombicosidodecahedron(float(a))
                    self.ui.answer.setText("Rhombicosidodecahedron volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.rhombicosidodecahedron(float(a))
                    self.ui.answer.setText("Rhombicosidodecahedron volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Snub cube':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.snub_cube(float(a))
                    self.ui.answer.setText("Snub cube volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.snub_cube(float(a))
                    self.ui.answer.setText("Snub cube volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.snub_cube(float(a))
                    self.ui.answer.setText("Snub cube volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.snub_cube(float(a))
                    self.ui.answer.setText("Snub cube volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.snub_cube(float(a))
                    self.ui.answer.setText("Snub cube volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.snub_cube(float(a))
                    self.ui.answer.setText("Snub cube volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.snub_cube(float(a))
                    self.ui.answer.setText("Snub cube volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.snub_cube(float(a))
                    self.ui.answer.setText("Snub cube volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.snub_cube(float(a))
                    self.ui.answer.setText("Snub cube volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            

        elif mainvar.shape == u'Volume - Capsule':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.capsule(float(a), float(b))
                    self.ui.answer.setText("Capsule volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.capsule(float(a), float(b))
                    self.ui.answer.setText("Capsule volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.capsule(float(a), float(b))
                    self.ui.answer.setText("Capsule volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.capsule(float(a), float(b))
                    self.ui.answer.setText("Capsule volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.capsule(float(a), float(b))
                    self.ui.answer.setText("Capsule volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.capsule(float(a), float(b))
                    self.ui.answer.setText("Capsule volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.capsule(float(a), float(b))
                    self.ui.answer.setText("Capsule volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.capsule(float(a), float(b))
                    self.ui.answer.setText("Capsule volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.capsule(float(a), float(b))
                    self.ui.answer.setText("Capsule volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Tetrahedron':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.octahedron(float(a))
                    self.ui.answer.setText("Tetrahedron volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.octahedron(float(a))
                    self.ui.answer.setText("Tetrahedron volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.octahedron(float(a))
                    self.ui.answer.setText("Tetrahedron volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.octahedron(float(a))
                    self.ui.answer.setText("Tetrahedron volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.octahedron(float(a))
                    self.ui.answer.setText("Tetrahedron volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.octahedron(float(a))
                    self.ui.answer.setText("Tetrahedron volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.octahedron(float(a))
                    self.ui.answer.setText("Tetrahedron volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.octahedron(float(a))
                    self.ui.answer.setText("Tetrahedron volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.octahedron(float(a))
                    self.ui.answer.setText("Tetrahedron volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Octahedron':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.octrahedron(float(a))
                    self.ui.answer.setText("Octahedron volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.tetrahedron(float(a))
                    self.ui.answer.setText("Octahedron volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.tetrahedron(float(a))
                    self.ui.answer.setText("Octahedron volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.tetrahedron(float(a))
                    self.ui.answer.setText("Octahedron volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.tetrahedron(float(a))
                    self.ui.answer.setText("Octahedron volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.tetrahedron(float(a))
                    self.ui.answer.setText("Octahedron volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.tetrahedron(float(a))
                    self.ui.answer.setText("Octahedron volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.tetrahedron(float(a))
                    self.ui.answer.setText("Octahedron volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.tetrahedron(float(a))
                    self.ui.answer.setText("Octahedron volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Icosahedron':
            a = is_number(self.ui.Input1.toPlainText())
            if a == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.icosahedron(float(a))
                    self.ui.answer.setText("Icosahedron volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.icosahedron(float(a))
                    self.ui.answer.setText("Icosahedron volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.icosahedron(float(a))
                    self.ui.answer.setText("Icosahedron volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.icosahedron(float(a))
                    self.ui.answer.setText("Icosahedron volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.icosahedron(float(a))
                    self.ui.answer.setText("Icosahedron volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.icosahedron(float(a))
                    self.ui.answer.setText("Icosahedron volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.icosahedron(float(a))
                    self.ui.answer.setText("Icosahedron volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.icosahedron(float(a))
                    self.ui.answer.setText("Icosahedron volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.icosahedron(float(a))
                    self.ui.answer.setText("Icosahedron volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Isosceles triangular pyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            c = is_number(self.ui.Input3.toPlainText())
            if a == True and b == True and c == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.isosceles_triangular_pyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular pyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.isosceles_triangular_pyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular pyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.isosceles_triangular_pyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular pyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.isosceles_triangular_pyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular pyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.isosceles_triangular_pyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular pyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.isosceles_triangular_pyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular pyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.isosceles_triangular_pyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular pyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.isosceles_triangular_pyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular pyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.isosceles_triangular_pyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular pyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
           
        elif mainvar.shape == u'Volume - Scalene triangular pyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            c = is_number(self.ui.Input3.toPlainText())
            d = is_number(self.ui.Input4.toPlainText())
            if a == True and b == True and c == True and d == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.scalene_triangular_pyramid(float(a), float(b), float(c), float(b))
                    self.ui.answer.setText("Scalene triangular pyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.scalene_triangular_pyramid(float(a), float(b), float(c), float(b))
                    self.ui.answer.setText("Scalene triangular pyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.scalene_triangular_pyramid(float(a), float(b), float(c), float(b))
                    self.ui.answer.setText("Scalene triangular pyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.scalene_triangular_pyramid(float(a), float(b), float(c), float(b))
                    self.ui.answer.setText("Scalene triangular pyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.scalene_triangular_pyramid(float(a), float(b), float(c), float(b))
                    self.ui.answer.setText("Scalene triangular pyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.scalene_triangular_pyramid(float(a), float(b), float(c), float(b))
                    self.ui.answer.setText("Scalene triangular pyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.scalene_triangular_pyramid(float(a), float(b), float(c), float(b))
                    self.ui.answer.setText("Scalene triangular pyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.scalene_triangular_pyramid(float(a), float(b), float(c), float(b))
                    self.ui.answer.setText("Scalene triangular pyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.scalene_triangular_pyramid(float(a), float(b), float(c), float(b))
                    self.ui.answer.setText("Scalene triangular pyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Equilateral triangular pyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.equlateral_triangular_pyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular pyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.equlateral_triangular_pyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular pyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.equlateral_triangular_pyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular pyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.equlateral_triangular_pyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular pyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.equlateral_triangular_pyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular pyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.equlateral_triangular_pyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular pyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.equlateral_triangular_pyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular pyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.equlateral_triangular_pyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular pyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.equlateral_triangular_pyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular pyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Square pyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.square_pyramid(float(a), float(b))
                    self.ui.answer.setText("Square pyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.square_pyramid(float(a), float(b))
                    self.ui.answer.setText("Square pyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.square_pyramid(float(a), float(b))
                    self.ui.answer.setText("Square pyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.square_pyramid(float(a), float(b))
                    self.ui.answer.setText("Square pyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.square_pyramid(float(a), float(b))
                    self.ui.answer.setText("Square pyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.square_pyramid(float(a), float(b))
                    self.ui.answer.setText("Square pyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.square_pyramid(float(a), float(b))
                    self.ui.answer.setText("Square pyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.square_pyramid(float(a), float(b))
                    self.ui.answer.setText("Square pyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.square_pyramid(float(a), float(b))
                    self.ui.answer.setText("Square pyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Pentagonal pyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.pentagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Pentagonal pyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.pentagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Pentagonal pyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.pentagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Pentagonal pyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.pentagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Pentagonal pyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.pentagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Pentagonal pyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.pentagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Pentagonal pyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.pentagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Pentagonal pyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.pentagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Pentagonal pyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.pentagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Pentagonal pyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Hexagonal pyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.hexagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Hexagonal pyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.hexagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Hexagonal pyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.hexagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Hexagonal pyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.hexagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Hexagonal pyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.hexagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Hexagonal pyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.hexagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Hexagonal pyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.hexagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Hexagonal pyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.hexagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Hexagonal pyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.hexagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Hexagonal pyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Heptagonal pyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.heptagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Heptagonal pyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.heptagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Heptagonal pyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.heptagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Heptagonal pyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.heptagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Heptagonal pyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.heptagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Heptagonal pyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.heptagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Heptagonal pyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.heptagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Heptagonal pyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.heptagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Heptagonal pyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.heptagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Heptagonal pyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Octagonal pyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.octagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Octagonal pyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.octagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Octagonal pyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.octagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Octagonal pyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.octagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Octagonal pyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.octagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Octagonal pyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.octagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Octagonal pyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.octagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Octagonal pyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.octagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Octagonal pyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.octagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Octagonal pyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Nonagonal pyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.nonagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Nonagonal pyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.nonagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Nonagonal pyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.nonagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Nonagonal pyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.nonagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Nonagonal pyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.nonagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Nonagonal pyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.nonagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Nonagonal pyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.nonagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Nonagonal pyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.nonagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Nonagonal pyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.nonagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Nonagonal pyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Decagonal pyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.decagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Decagonal pyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.decagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Decagonal pyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.decagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Decagonal pyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.decagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Decagonal pyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.decagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Decagonal pyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.decagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Decagonal pyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.decagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Decagonal pyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.decagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Decagonal pyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.decagon_pyramid(float(a), float(b))
                    self.ui.answer.setText("Decagonal pyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Star prism':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            c = is_number(self.ui.Input3.toPlainText())
            if a == True and b == True and c == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.star_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Star prism volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.star_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Star prism volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.star_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Star prism volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.star_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Star prism volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.star_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Star prism volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.star_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Star prism volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.star_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Star prism volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.star_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Star prism volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.star_prism(float(a), float(b), float(c))
                    self.ui.answer.setText("Star prism volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
           
        elif mainvar.shape == u'Volume - Isosceles triangular bipyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            c = is_number(self.ui.Input3.toPlainText())
            if a == True and b == True and c == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.isosceles_triangular_bipyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular bipyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.isosceles_triangular_bipyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular bipyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.isosceles_triangular_bipyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular bipyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.isosceles_triangular_bipyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular bipyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.isosceles_triangular_bipyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular bipyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.isosceles_triangular_bipyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular bipyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.isosceles_triangular_bipyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular bipyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.isosceles_triangular_bipyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular bipyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.isosceles_triangular_bipyramid(float(a), float(b), float(c))
                    self.ui.answer.setText("Isosceles triangular bipyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        elif mainvar.shape == u'Volume - Equilateral triangular bipyramid':
            a = is_number(self.ui.Input1.toPlainText())
            b = is_number(self.ui.Input2.toPlainText())
            if a == True and b == True:
                a = self.ui.Input1.toPlainText()
                b = self.ui.Input2.toPlainText()
                c = self.ui.Input3.toPlainText()
                d = self.ui.Input4.toPlainText()
                if mainvar.unit == u'Inches':
                    ans = _3D.equilateral_triangular_bipyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular bipyramid volume: " + str(ans) + u" in³")
                if mainvar.unit == u'Feet':
                    ans = _3D.equilateral_triangular_bipyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular bipyramid volume: " + str(ans) + u" ft³")
                if mainvar.unit == u'Yards':
                    ans = _3D.equilateral_triangular_bipyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular bipyramid volume: " + str(ans) + u" yd³")
                if mainvar.unit == u'Miles':
                    ans = _3D.equilateral_triangular_bipyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular bipyramid volume: " + str(ans) + u" mi³")
                if mainvar.unit == u'Millimeters':
                    ans = _3D.equilateral_triangular_bipyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular bipyramid volume: " + str(ans) + u" mm³")
                if mainvar.unit == u'Centimeters':
                    ans = _3D.equilateral_triangular_bipyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular bipyramid volume: " + str(ans) + u" cm³")
                if mainvar.unit == u'Meters':
                    ans = _3D.equilateral_triangular_bipyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular bipyramid volume: " + str(ans) + u" m³")
                if mainvar.unit == u'Kilometers':
                    ans = _3D.equilateral_triangular_bipyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular bipyramid volume: " + str(ans) + u" km³")
                if mainvar.unit == u'None':
                    ans = _3D.equilateral_triangular_bipyramid(float(a), float(b))
                    self.ui.answer.setText("Equilateral triangular bipyramid volume: " + str(ans))
            else:
                self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'One or more inputs are not a number', None))
            
        else:
            self.ui.answer.setText(QCoreApplication.translate('MainWindow', u'Error. Please report to help.areavolumecalc@gmail.com', None))
        
    def update_shape(self, shape):
        Curr_shape = shape
        mainvar.shape = Curr_shape
        if mainvar.shape == u'Area - Square':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Rectangle':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Length:")
            self.ui.Input2Label.setText("Width:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Circle':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Radius:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Isosceles triangle':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Base length:")
            self.ui.Input2Label.setText("Height:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Scalene triangle':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(False)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side A length:")
            self.ui.Input2Label.setText("Side B length:")
            self.ui.Input3Label.setText("Side C length:")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Equilateral triangle':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Pentagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Hexagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Heptagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Octagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Nonagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Decagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Undecagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Dodecagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Tridecagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Tetradecagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Pentadecagon':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Side length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Trapezoid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(False)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Left side length:")
            self.ui.Input2Label.setText("Right side length:")
            self.ui.Input3Label.setText("Height")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Ellipse':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Radius A:")
            self.ui.Input2Label.setText("Radius B:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Polyomino':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Amount of squares:")
            self.ui.Input2Label.setText("Square side length:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Star':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Amount of points:")
            self.ui.Input2Label.setText("Side length:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Semicircle':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Radius:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Squircle':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Length/width:")
            self.ui.Input2Label.setText("Rounding radius:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Parallelogram':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Length:")
            self.ui.Input2Label.setText("Height")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Annulus':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Inner circle radius:")
            self.ui.Input2Label.setText("Full radius:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Kite':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Diagonal:")
            self.ui.Input2Label.setText("Other diagonal:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Area - Rhombus':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Diagonal:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Cube':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Edge length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Rectangular prism':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(False)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Length:")
            self.ui.Input2Label.setText("Width:")
            self.ui.Input3Label.setText("Height:")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Sphere':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Radius:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Cylinder':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Base radius:")
            self.ui.Input2Label.setText("Height")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Cone':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Base radius:")
            self.ui.Input2Label.setText("Height")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Dodecahedron':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Edge length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Isosceles triangular prism':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(False)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Length:")
            self.ui.Input2Label.setText("Width:")
            self.ui.Input3Label.setText("Height:")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Scalene triangular prism':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(False)
            self.ui.Input4.setReadOnly(False)
            self.ui.Input1Label.setText("Base side A length:")
            self.ui.Input2Label.setText("Base side B length:")
            self.ui.Input3Label.setText("Base side C length:")
            self.ui.Input4Label.setText("Height")
        elif mainvar.shape == u'Volume - Equilateral triangular prism':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Length/width:")
            self.ui.Input2Label.setText("Height:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Hemisphere':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Radius:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Torus':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Major radius:")
            self.ui.Input2Label.setText("Minor radius")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Rhombicosidodecahedron':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Edge length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Snub cube':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Edge length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Capsule':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Main cylinder length:")
            self.ui.Input2Label.setText("Main cylinder radius")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Tetrahedron':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Edge length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Octahedron':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Edge length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Icosahedron':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(True)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Edge length:")
            self.ui.Input2Label.setText("")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Isosceles triangular pyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(False)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Length:")
            self.ui.Input2Label.setText("Width:")
            self.ui.Input3Label.setText("Height:")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Scalene triangular pyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(False)
            self.ui.Input4.setReadOnly(False)
            self.ui.Input1Label.setText("Base side A length:")
            self.ui.Input2Label.setText("Base side B length:")
            self.ui.Input3Label.setText("Base side C length:")
            self.ui.Input4Label.setText("Height")
        elif mainvar.shape == u'Volume - Equilateral triangular pyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Length/width:")
            self.ui.Input2Label.setText("Height:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Square pyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Base side length:")
            self.ui.Input2Label.setText("Height")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Pentagonal pyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Base side length:")
            self.ui.Input2Label.setText("Height")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Hexagonal pyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Base side length:")
            self.ui.Input2Label.setText("Height")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Heptagonal pyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Base side length:")
            self.ui.Input2Label.setText("Height")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Octagonal pyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Base side length:")
            self.ui.Input2Label.setText("Height")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Nonagonal pyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Base side length:")
            self.ui.Input2Label.setText("Height")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Decagonal pyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Base side length:")
            self.ui.Input2Label.setText("Height")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Star prism':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(False)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Amount of points on base:")
            self.ui.Input2Label.setText("Base side length")
            self.ui.Input3Label.setText("Height")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Isosceles triangular bipyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(False)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Length:")
            self.ui.Input2Label.setText("Width:")
            self.ui.Input3Label.setText("Height:")
            self.ui.Input4Label.setText("")
        elif mainvar.shape == u'Volume - Equilateral triangular bipyramid':
            self.ui.Input1.setReadOnly(False)
            self.ui.Input2.setReadOnly(False)
            self.ui.Input3.setReadOnly(True)
            self.ui.Input4.setReadOnly(True)
            self.ui.Input1Label.setText("Length/width:")
            self.ui.Input2Label.setText("Height:")
            self.ui.Input3Label.setText("")
            self.ui.Input4Label.setText("")

    def update_units(self, text):
        # Update the variable mainvar.units_ans with the selected mainvar.units
        mainvar.unit = text

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())