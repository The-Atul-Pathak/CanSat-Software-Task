from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
import csv


csv_file = open('trial_data.csv', mode='r')
csv_reader = iter(csv.DictReader(csv_file))

def UpdateData():
    try:
        row = next(csv_reader)
        TimeResultLabel.setText(row['TIME_STAMPING'])
        packetCountResultLabel.setText(row['PACKET_COUNT'])
        softwareStateResultLabel.setText(row['FLIGHT_SOFTWARE_STATE'])
        altitudeResultLabel.setText(row['ALTITUDE'])
        pressureResultLabel.setText(row['PRESSURE'])
        tempeResultLabel.setText(row['TEMP'])
        voltageResultLabel.setText(row['VOLTAGE'])
        tvocResultLabel.setText(row['TVOC'])
        eco2ResultLabel.setText(row['eCO2'])
        gnssTimeResultLabel.setText(row['GNSS_TIME'])
        gnssLatitudeResultLabel.setText(row['GNSS_LATITUDE'])
        gnssLongitudeResultLabel.setText(row['GNSS_LONGITUDE'])
        gnssAltitudeResultLabel.setText(row['GNSS_ALTITUDE'])
        gnssSatsResultLabel.setText(row['GNSS_SATS'])
        accrResultLabel.setText(row['ACC_R'])
        accpResultLabel.setText(row['ACC_P'])
        accyResultLabel.setText(row['ACC_Y'])
        gyrorResultLabel.setText(row['GYRO_R'])
        gyropResultLabel.setText(row['GYRO_P'])
        gyroyResultLabel.setText(row['GYRO_Y'])
    except StopIteration:
        timer.stop()
        csv_file.close()


app = QApplication([])
window = QMainWindow()
window.setWindowTitle("PyQt6 Layouts Example")
window.setGeometry(100, 100, 1024, 537)
window.setStyleSheet("""
    QMainWindow {
        background: qlineargradient(
            x1:0, y1:0, x2:1, y2:0,
            stop:0 #000000,
            stop:1 #9884cf
        );
    }
""")


# Create layouts
ParentLayout = QVBoxLayout()
header = QGridLayout()
telemetry = QGridLayout()
telemetry.setContentsMargins(0, 0, 0, 0)
graphsLayout = QVBoxLayout()
locationLayout = QVBoxLayout()
liveLayout = QVBoxLayout()

footer = QHBoxLayout()

# Header Layout
softwareStateLabel = QLabel("SOFTWARE STATE", alignment=Qt.AlignmentFlag.AlignCenter)
softwareStateLabel.setStyleSheet("font-size: 14px; color: white;")
softwareStateResultLabel = QLabel("LAUNCH_PAD", alignment=Qt.AlignmentFlag.AlignCenter)
softwareStateResultLabel.setFixedWidth(140)
softwareStateResultLabel.setFixedHeight(30)
softwareStateResultLabel.setStyleSheet("border-radius: 15px; border: 2px solid #9e2133; background: #fffffe; color: black; font-size: 14px;")

kalpanaLabel = QLabel("TEAM KALPANA : 2024-CANSAT-ASI-023", alignment=Qt.AlignmentFlag.AlignCenter)
kalpanaLabel.setStyleSheet("font-size: 18px; color: white;")
kalpanaLogo = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
kalpanaLogo.setPixmap(QPixmap("image.png").scaled(50, 45, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

TimeLable = QLabel("TIME", alignment=Qt.AlignmentFlag.AlignCenter)
TimeLable.setStyleSheet("font-size: 14px; color: white;")
TimeResultLabel = QLabel("00:05:37", alignment=Qt.AlignmentFlag.AlignCenter)
TimeResultLabel.setFixedWidth(120)
TimeResultLabel.setFixedHeight(30)
TimeResultLabel.setStyleSheet("border-radius: 15px; border: 2px solid #9e2133; background: #fffffe; color: black; font-size: 14px;")

packetCountLabel = QLabel("PACKET COUNT", alignment=Qt.AlignmentFlag.AlignCenter)
packetCountLabel.setStyleSheet("font-size: 14px; color: white;")
packetCountResultLabel = QLabel("335", alignment=Qt.AlignmentFlag.AlignCenter)
packetCountResultLabel.setFixedWidth(120)
packetCountResultLabel.setFixedHeight(30)
packetCountResultLabel.setStyleSheet("border-radius: 15px; border: 2px solid #9e2133; background: #fffffe; color: black; font-size: 14px;")

header.addWidget(softwareStateLabel, 0, 0, 1, 2)
header.addWidget(softwareStateResultLabel, 1, 0, 1, 2)
header.addWidget(kalpanaLabel, 0, 2, 1, 3)
header.addWidget(kalpanaLogo, 1, 2, 1, 3)
header.addWidget(TimeLable, 0, 5, 1, 1)
header.addWidget(TimeResultLabel, 1, 5, 1, 1)
header.addWidget(packetCountLabel, 0, 6, 1, 1)
header.addWidget(packetCountResultLabel, 1, 6, 1, 1)

header.setAlignment(softwareStateResultLabel, Qt.AlignmentFlag.AlignCenter)
header.setAlignment(softwareStateLabel, Qt.AlignmentFlag.AlignCenter)
header.setAlignment(kalpanaLabel, Qt.AlignmentFlag.AlignCenter)
header.setAlignment(kalpanaLogo, Qt.AlignmentFlag.AlignCenter)
header.setAlignment(TimeLable, Qt.AlignmentFlag.AlignCenter)
header.setAlignment(TimeResultLabel, Qt.AlignmentFlag.AlignCenter)
header.setAlignment(packetCountLabel, Qt.AlignmentFlag.AlignCenter)
header.setAlignment(packetCountResultLabel, Qt.AlignmentFlag.AlignCenter)


headerWidget = QWidget()
headerWidget.setMaximumHeight(100)
headerWidget.setLayout(header)
headerWidget.setStyleSheet("background-color: #150d4f;")


# telemetry Page Layout
l1 = QGridLayout()
l2 = QGridLayout()
l3 = QGridLayout()
l4 = QGridLayout()
l5 = QGridLayout()

## l1
gnssStatsLabel = QLabel("GNSS STATS", alignment=Qt.AlignmentFlag.AlignCenter)
gnssStatsLabel.setMaximumHeight(10)
gnssStatsLabel.setStyleSheet("color: #cfe4cb;")
gnssTimeLabel = QLabel("gnss_time")
gnssTimeResultLabel = QLabel("13:04:59", alignment=Qt.AlignmentFlag.AlignCenter)
gnssTimeResultLabel.setFixedWidth(120)
gnssTimeResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")

gnssLatitudeLabel = QLabel("gnss_latitude")
gnssLatitudeResultLabel = QLabel("13:04:59", alignment=Qt.AlignmentFlag.AlignCenter)
gnssLatitudeResultLabel.setFixedWidth(120)
gnssLatitudeResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")

gnssLongitudeLabel = QLabel("gnss_longitude")
gnssLongitudeResultLabel = QLabel("13:04:59", alignment=Qt.AlignmentFlag.AlignCenter)
gnssLongitudeResultLabel.setFixedWidth(120)
gnssLongitudeResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")

gnssAltitudeLabel = QLabel("gnss_altitude")
gnssAltitudeResultLabel = QLabel("13:04:59", alignment=Qt.AlignmentFlag.AlignCenter)
gnssAltitudeResultLabel.setFixedWidth(120)
gnssAltitudeResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")

gnssSatsLabel = QLabel("gnss_sats")
gnssSatsResultLabel = QLabel("13:04:59", alignment=Qt.AlignmentFlag.AlignCenter)
gnssSatsResultLabel.setFixedWidth(120)
gnssSatsResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")

l1.addWidget(gnssStatsLabel, 0, 0, 1, 2)
l1.addWidget(gnssTimeLabel, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l1.addWidget(gnssTimeResultLabel, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l1.addWidget(gnssLatitudeLabel, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l1.addWidget(gnssLatitudeResultLabel, 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l1.addWidget(gnssLongitudeLabel, 3, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l1.addWidget(gnssLongitudeResultLabel, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l1.addWidget(gnssAltitudeLabel, 4, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l1.addWidget(gnssAltitudeResultLabel, 4, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l1.addWidget(gnssSatsLabel, 5, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l1.addWidget(gnssSatsResultLabel, 5, 1, alignment=Qt.AlignmentFlag.AlignCenter)

l1_widget = QWidget()
l1_widget.setLayout(l1)
l1_widget.setStyleSheet("QWidget { border: 2px solid #0b5a06; border-radius: 10px; } QLabel { border: none; }")

## l2
electricalStatsLabel = QLabel("ELECTRICAL STATS", alignment=Qt.AlignmentFlag.AlignCenter)
electricalStatsLabel.setMaximumHeight(10)
electricalStatsLabel.setStyleSheet("color: #cfe4cb;")
voltageLabel = QLabel("voltage")
voltageResultLabel = QLabel("13:04:59", alignment=Qt.AlignmentFlag.AlignCenter)
voltageResultLabel.setFixedWidth(120)
voltageResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")

l2.addWidget(electricalStatsLabel, 0, 0, 1, 2)
l2.addWidget(voltageLabel, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l2.addWidget(voltageResultLabel, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)

l2_widget = QWidget()
l2_widget.setLayout(l2)
l2_widget.setStyleSheet("QWidget { border: 2px solid #0b5a06; border-radius: 10px; } QLabel { border: none; }")

## l3
environmentalStatsLabel = QLabel("ENVIRONMENTAL STATS", alignment=Qt.AlignmentFlag.AlignCenter)
environmentalStatsLabel.setMaximumHeight(10)
environmentalStatsLabel.setStyleSheet("color: #cfe4cb;")
altitudeLabel = QLabel("altitude")
altitudeResultLabel = QLabel("305.41", alignment=Qt.AlignmentFlag.AlignCenter)
altitudeResultLabel.setFixedWidth(120)
altitudeResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")
pressureLabel = QLabel("pressure")
pressureResultLabel = QLabel("97710.08", alignment=Qt.AlignmentFlag.AlignCenter)
pressureResultLabel.setFixedWidth(120)
pressureResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")
tempeLabel = QLabel("temp")
tempeResultLabel = QLabel("32.42", alignment=Qt.AlignmentFlag.AlignCenter)
tempeResultLabel.setFixedWidth(120)
tempeResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")
tvocLabel = QLabel("tvoc")
tvocResultLabel = QLabel("0.00", alignment=Qt.AlignmentFlag.AlignCenter)
tvocResultLabel.setFixedWidth(120)
tvocResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")
eco2Label = QLabel("eco2")
eco2ResultLabel = QLabel("400.00", alignment=Qt.AlignmentFlag.AlignCenter)
eco2ResultLabel.setFixedWidth(120)
eco2ResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")

l3.addWidget(environmentalStatsLabel, 0, 0, 1, 2)
l3.addWidget(altitudeLabel, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l3.addWidget(altitudeResultLabel, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l3.addWidget(pressureLabel, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l3.addWidget(pressureResultLabel, 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l3.addWidget(tempeLabel, 3, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l3.addWidget(tempeResultLabel, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l3.addWidget(tvocLabel, 4, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l3.addWidget(tvocResultLabel, 4, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l3.addWidget(eco2Label, 5, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l3.addWidget(eco2ResultLabel, 5, 1, alignment=Qt.AlignmentFlag.AlignCenter)

l3_widget = QWidget()
l3_widget.setLayout(l3)
l3_widget.setStyleSheet("QWidget { border: 2px solid #0b5a06; border-radius: 10px; } QLabel { border: none; }")

## l4
accelerometerStatsLabel = QLabel("ACCELEROMETER STATS", alignment=Qt.AlignmentFlag.AlignCenter)
accelerometerStatsLabel.setMaximumHeight(10)
accelerometerStatsLabel.setStyleSheet("color: #cfe4cb;")
accrLabel = QLabel("accr")
accrResultLabel = QLabel("0.00", alignment=Qt.AlignmentFlag.AlignCenter)
accrResultLabel.setFixedWidth(120)
accrResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")
accpLabel = QLabel("accp")
accpResultLabel = QLabel("0.00", alignment=Qt.AlignmentFlag.AlignCenter)
accpResultLabel.setFixedWidth(120)
accpResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")
accyLabel = QLabel("accy")
accyResultLabel = QLabel("0.00", alignment=Qt.AlignmentFlag.AlignCenter)
accyResultLabel.setFixedWidth(120)
accyResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")

l4.addWidget(accelerometerStatsLabel, 0, 0, 1, 2)
l4.addWidget(accrLabel, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l4.addWidget(accrResultLabel, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l4.addWidget(accpLabel, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l4.addWidget(accpResultLabel, 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l4.addWidget(accyLabel, 3, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l4.addWidget(accyResultLabel, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)

l4_widget = QWidget()
l4_widget.setLayout(l4)
l4_widget.setStyleSheet("QWidget { border: 2px solid #0b5a06; border-radius: 10px; } QLabel { border: none; }")

## l5
gyroscopeStatsLabel = QLabel("GYROSCOPE STATS", alignment=Qt.AlignmentFlag.AlignCenter)
gyroscopeStatsLabel.setMaximumHeight(10)
gyroscopeStatsLabel.setStyleSheet("color: #cfe4cb;")
gyrorLabel = QLabel("gyror")
gyrorResultLabel = QLabel("0.00", alignment=Qt.AlignmentFlag.AlignCenter)
gyrorResultLabel.setFixedWidth(120)
gyrorResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")
gyropLabel = QLabel("gyrop")
gyropResultLabel = QLabel("0.00", alignment=Qt.AlignmentFlag.AlignCenter)
gyropResultLabel.setFixedWidth(120)
gyropResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")
gyroyLabel = QLabel("gyroy")
gyroyResultLabel = QLabel("0.00", alignment=Qt.AlignmentFlag.AlignCenter)
gyroyResultLabel.setFixedWidth(120)
gyroyResultLabel.setStyleSheet("border-radius: 5px; border: 1px solid #9e2133; background: #fffffe; color: black; font-size: 14px; padding: 2px;")

l5.addWidget(gyroscopeStatsLabel, 0, 0, 1, 2)
l5.addWidget(gyrorLabel, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l5.addWidget(gyrorResultLabel, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l5.addWidget(gyropLabel, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l5.addWidget(gyropResultLabel, 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)
l5.addWidget(gyroyLabel, 3, 0, alignment=Qt.AlignmentFlag.AlignLeft)
l5.addWidget(gyroyResultLabel, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)

l5_widget = QWidget()
l5_widget.setLayout(l5)
l5_widget.setStyleSheet("QWidget { border: 2px solid #0b5a06; border-radius: 10px; } QLabel { border: none; }")

telemetry.addWidget(l1_widget, 0, 0, 3, 1)
telemetry.addWidget(l2_widget, 3, 0)
telemetry.addWidget(l3_widget, 0, 1, 4, 1)
telemetry.addWidget(l4_widget, 0, 2, 2, 1)
telemetry.addWidget(l5_widget, 2, 2, 2, 1)

telemetryPage = QWidget()
telemetryPage.setContentsMargins(0, 0, 0, 0)
telemetryPage.setLayout(telemetry)

# Graphs Page Layout
graphsPage = QWidget()
graphsLabel = QLabel("Empty Page : Graphs", alignment=Qt.AlignmentFlag.AlignCenter)
graphsLabel.setStyleSheet("color: white; font-size: 20px;")
graphsLayout.addWidget(graphsLabel)
graphsPage.setLayout(graphsLayout)

# Location Page Layout
locationPage = QWidget()
locationLabel = QLabel("Empty Page : Location and 3D Plotting", alignment=Qt.AlignmentFlag.AlignCenter)
locationLabel.setStyleSheet("color: white; font-size: 20px;")
locationLayout.addWidget(locationLabel)
locationPage.setLayout(locationLayout)

# Live Telecast Page Layout
livePage = QWidget()
liveLabel = QLabel("Empty Page : Live Telecast", alignment=Qt.AlignmentFlag.AlignCenter)
liveLabel.setStyleSheet("color: white; font-size: 20px;")
liveLayout.addWidget(liveLabel)
livePage.setLayout(liveLayout)



stack = QStackedWidget()
stack.addWidget(telemetryPage)
stack.addWidget(graphsPage)
stack.addWidget(locationPage)
stack.addWidget(livePage)

tab_active = "background: #8f9a99; color: white; height: 30px; border-radius: 10px; font-size: 14px; font-weight: bold;"
tab_inactive = "background: #bddfe1; color: white; height: 30px; border-radius: 10px; font-size: 14px; font-weight: bold;"

tabTelemetry = QPushButton("Telemetry Data")
tabGraphs = QPushButton("Graphs")
tabLocation = QPushButton("Location and 3D Plotting")
tabLive = QPushButton("Live Telecast")

tabTelemetry.setStyleSheet(tab_active)
tabGraphs.setStyleSheet(tab_inactive)
tabLocation.setStyleSheet(tab_inactive)
tabLive.setStyleSheet(tab_inactive)

def switchTab(index):
    stack.setCurrentIndex(index)
    for i, btn in enumerate([tabTelemetry, tabGraphs, tabLocation, tabLive]):
        btn.setStyleSheet(tab_active if i == index else tab_inactive)

tabTelemetry.clicked.connect(lambda: switchTab(0))
tabGraphs.clicked.connect(lambda: switchTab(1))
tabLocation.clicked.connect(lambda: switchTab(2))
tabLive.clicked.connect(lambda: switchTab(3))

tabBar = QHBoxLayout()
tabBar.setSpacing(3)
tabBar.setContentsMargins(0, 0, 0, 0)
tabBar.addWidget(tabTelemetry)
tabBar.addWidget(tabGraphs)
tabBar.addWidget(tabLocation)
tabBar.addWidget(tabLive)

















# Footer Layout
boot = QPushButton("BOOT")
boot.clicked.connect(lambda: print("BOOT"))
boot.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1f103f, stop:1 #0effea); color: #c2a834; border-radius: 8px; height: 40px; font-size: 11px; width: 80px; border: 2px solid black;")

setTime = QPushButton("Set Time")
setTime.clicked.connect(lambda: print("Set Time"))
setTime.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1f103f, stop:1 #0effea); color: #c2a834; border-radius: 8px; height: 40px; font-size: 11px; width: 80px; border: 2px solid black;")

Calibrate = QPushButton("Calibrate")
Calibrate.clicked.connect(lambda: print("Calibrate"))
Calibrate.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1f103f, stop:1 #0effea); color: #c2a834; border-radius: 8px; height: 40px; font-size: 11px; width: 80px; border: 2px solid black;")

onOff = QPushButton("ON/OFF")
onOff.clicked.connect(lambda: print("ON/OFF"))
onOff.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1f103f, stop:1 #0effea); color: #c2a834; border-radius: 8px; height: 40px; font-size: 11px; width: 80px; border: 2px solid black;")

cx = QPushButton("CX")
cx.clicked.connect(lambda: print("CX"))
cx.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1f103f, stop:1 #0effea); color: #c2a834; border-radius: 8px; height: 40px; font-size: 11px; width: 80px; border: 2px solid black;")

simEnable = QPushButton("SIM Enable")
simEnable.clicked.connect(lambda: print("SIM Enable"))
simEnable.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1f103f, stop:1 #0effea); color: #c2a834; border-radius: 8px; height: 40px; font-size: 11px; width: 80px; border: 2px solid black;")

simActivate = QPushButton("SIM Activate")
simActivate.clicked.connect(lambda: print("SIM Activate"))
simActivate.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1f103f, stop:1 #0effea); color: #c2a834; border-radius: 8px; height: 40px; font-size: 11px; width: 80px; border: 2px solid black;")

simDisable = QPushButton("SIM Disable")
simDisable.clicked.connect(lambda: print("SIM Disable"))
simDisable.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1f103f, stop:1 #0effea); color: #c2a834; border-radius: 8px; height: 40px; font-size: 11px; width: 80px; border: 2px solid black;")

footer.addWidget(boot, alignment=Qt.AlignmentFlag.AlignCenter)
footer.addWidget(setTime, alignment=Qt.AlignmentFlag.AlignCenter)
footer.addWidget(Calibrate, alignment=Qt.AlignmentFlag.AlignCenter)
footer.addWidget(onOff, alignment=Qt.AlignmentFlag.AlignCenter)
footer.addWidget(cx, alignment=Qt.AlignmentFlag.AlignCenter)
footer.addWidget(simEnable, alignment=Qt.AlignmentFlag.AlignCenter)
footer.addWidget(simActivate, alignment=Qt.AlignmentFlag.AlignCenter)
footer.addWidget(simDisable, alignment=Qt.AlignmentFlag.AlignCenter)

footerWidget = QWidget()
footerWidget.setMaximumHeight(50)
footerWidget.setLayout(footer)



# Adding Layouts and Widgets
ParentLayout.addWidget(headerWidget)
ParentLayout.addLayout(tabBar)
ParentLayout.addWidget(stack)
ParentLayout.addWidget(footerWidget)




centerWidgit = QWidget()
centerWidgit.setLayout(ParentLayout)

window.setCentralWidget(centerWidgit)
timer = QTimer()
timer.setInterval(1000)
timer.timeout.connect(UpdateData)
timer.start()

window.show()
app.exec()