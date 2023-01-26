from numpy import *

"""global constants"""
PI = pi                  # 3.1415926
G = 9.81                    # gravitational acceleration m/s/s
R = 8.314                   # J/mol/K
M_air = 28.97e-3            # air molecular weight in kg/mol
UiMPa = 10e6                # MPa to Pa

"""global variables"""
# plunger parameters
m_plunger = 5               # plunger mass in kg
L_plunger = 0.4             # plunger length in m
d_plunger = 1.9 * 0.0254    # plunger diameter in
Cd_plunger = 0.1019         # plunger fall drag coefficient
Epsilon_plunger = 0.0457    # plunger rise

A_plunger = 0.25*PI*d_plunger**2   # plunger cross sectional area in m2

# well parameters
H_well = 10000 * 0.3048     # well depth in m
ID_tubing = 1.995 * 0.0254  # tubing ID in m
OD_tubing = 2.125 * 0.0254  # tubing OD in m
ID_casing = 4.85 * 0.0254   # casing ID in m
ED = 2.5e-4                 # tubing roughness

A_tubing = 0.25*PI*(ID_tubing**2)                   # tubing cross sectional area in m2
A_casing = 0.25*PI*(ID_casing**2 - OD_tubing**2)    # annulus cross section area in m2
AB = 0.25*PI*ID_casing**2                           # cross-sectional area of casing
Ann = 0.25*PI*(ID_tubing**2 - d_plunger**2)         # cross section area between plunger and tubing in m2

# reservoir IPR
P_res = 6e6                 # reservoir pressure in Pa
C_res = 2.58e-15            # reservoir coefficient for gas flow rate in Vogel model
n = 1                       # reservoir index for gas flow rate in Vogel model
GLR = 10                    # gas-liquid-ratio 
Rsl = 0.1                   # average gas solubility in liquid at average T and P, m3/m3
Tgrd = 0.03                 # formation temperature gradient 30K/km

# fluid properties
den_liquid_relative = 0.85  # relative density of liquid
den_gas_relative = 0.7      # relative density of gas
vis_liquid = 4e-4           # liquid viscosity in Pa.s
denl = den_liquid_relative * 1000
M_gas = M_air * den_gas_relative
fluid_type = 2                   # 1: black oil model, 2 compositional model
# surface parameters
Cv = 0.5e-7                 # coefficient of motor valve
T_wellhead = 288            # temperature at well head in K

# wellbore section
LB = 1500 * 0.3048          # deviated section of the wellbore
VB = AB * LB                # horizontal section volume in m3
ANG = 1                     # inclination angle of the deviated section
DB = ID_casing              # assume inner diameter the same as casing ID

"""initial variables"""
Pc = 1.6e6                  # casing pressure
Pt = 1.57e6                 # tubing pressure
Pl = 1.1e6                  # production line pressure - fixed if no surface line or separator considered
Ltt = 5.                    # initial liquid column length above plunger (m)
Ltb = 0.                    # initial liquid column length below plunger (m)
dt_H=0.5                    # time step for horizontal section
dt_U=5.                     # time step for plunger upward section
dt_D=10.0                   # time step for plunger downward section
cycles=4.                   # Plunger lift cycles to be computed
Period=30.*60.              # Plunger lift period (s to min)
T_open=12.*60.              # Surface valve open time (s to min)

# define state parameters
mga = 0.                    # mass of gas in annulus (kg)
mla = 0.                    # mass of liquid in annulus (kg)
mgtt = 0.                   # mass of gas in tubing top (kg)
mltt = 0.                   # mass of liquid in tubing top (kg)
mgtb = 0.                   # mass of gas in tubing bottom (kg)
mltb = 0.                   # mass of liquid in tubing bottom (kg)
Xp = 0.                     # plunger position from tubing shoe (m), initially at the bottom
Vp = 0.                     # plunger velocity (m/s)
Ar = 0.                     # plunger arrival time (s)
v = 0                       # motor valve open or close: 0 - close, 1 - open

# intermediate variables
La = 0.                     # ASSUME initial liquid column length in annulus (m)
Pcb = Pc                    # annular pressure right above liquid level
Ptb = Pt                    # tubing gas pressure right above plunger
Pwf = 0                     # bottom pressure at tubing shoe
PwfB = 0.                   # bottom pressure at wellbore
Fgout = 0.                  # surface gas mass flow rate (kg/s)
Flout = 0.                  # surface liquid mass flow rate (kg/s)
t = 0.                      # calculation time
dt = 0.01                   # delta t in s
PGT = 0.                    # total pressure gradient in horizontal well (pa/m)
Ppb = 0.                    # pressure on the bottom of plunger
Ppt = 0.                    # pressure on top of the plunger
Acc = -1                    # plunger acceleration in m/s2
Fgres = 0.                  # gas flow from horizontal well kg/s
Flres = 0.                  # liquid flow from horizontal well kg/s
FgresB = 0.                 # gas flow from reservoir kg/s
FlresB = 0.                 # liquid flow from reservoir kg/s
Fgtub = 0.                  # gas flow into tubing kg/s
Fltub = 0.                  # liquid flow into tubing kg/s
Fgann = 0.                  # gas flow into annulus kg/s
Flann = 0.                  # liquid flow into annulus kg/s
Ltt0 = Ltt                  # initial liquid height in tubing for each plunger cycle
HLB = 1                     # liquid holdup in the inclined or horizontal section of wellbore
