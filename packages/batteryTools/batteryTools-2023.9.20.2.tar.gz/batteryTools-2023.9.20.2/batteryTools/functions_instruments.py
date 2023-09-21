__update__ = '2023.09.20'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

'''
NOTES:
    -
TASK:
    - Implementar la comunicación por RS-232
WARNINGS
    - al usar "sleep" crashea desde una app con PyQt, estar atento (19.09.2023)
'''

''' SYSTEM LIBRARIES '''
# from time import sleep

''' VISA INSTRUMENT
--------------------------------------------------------  '''

class VISA_INSTRUMENT:
    '''
    visa_resource: GPIB0::17::INSTR" / USB0::0x0AAD::0x014E::101060::INSTR / PXI1Slot2\n
    timeout (seconds) = 10 seconds default
    '''
    def __init__(self, visa_resource: str, timeout: int = 10):
        import pyvisa
        RM = pyvisa.ResourceManager()
        RM.list_resources()
        self.DEVICE = RM.open_resource(visa_resource)
        self.DEVICE.timeout = timeout * 1000 # miliseconds
    
    def CLOSE(self):
        self.DEVICE.close()
    
    def WR(self, SENTENCE: str):
        '''
        Write
        '''
        self.DEVICE.write(SENTENCE)
    
    def RD(self, SENTENCE: str, FLOAT: bool = False) -> str | float:
        '''
        Query
        '''
        VALUE = self.DEVICE.query(SENTENCE)
        if FLOAT:
            VALUE = float(VALUE)
        return VALUE

    def READ(self, FLOAT: bool = False) -> str | float:
        '''
        Read
        '''
        VALUE = self.DEVICE.read()
        if FLOAT:
            VALUE = float(VALUE)
        return VALUE
    
    def OPC(self) -> None:
        self.DEVICE.write("*CLS")
        self.DEVICE.write("ESE 1")
        self.DEVICE.write("SRE 32")
        self.DEVICE.write("*OPC?")
        self.DEVICE.read()


''' RS232 INSTRUMENT
--------------------------------------------------------  '''

class RS232_INSTRUMENT:
    '''
    INCOMPLETE:
        - Not tested yet 
    '''
    def __init__(self, port: str = "COM1", baudrate: int = 9600, timeout: float = 1) -> None:
        import serial
        self.DEVICE = serial.Serial(port, baudrate, timeout)

    def CLOSE(self):
        self.DEVICE.close()

    def WR(self, SENTENCE: str):
        '''
        Write
        '''
        bytes_value = SENTENCE.encode('utf-8')
        self.DEVICE.write(bytes_value)

    def RD(self, SENTENCE: str, FLOAT: bool = False) -> str | float:
        '''
        Query
        '''
        bytes_value = SENTENCE.encode('utf-8')
        self.DEVICE.write(bytes_value)
        VALUE = self.DEVICE.readline().decode('utf-8')
        if FLOAT:
            VALUE = float(VALUE)
        return VALUE


''' PXI INSTRUMENT
--------------------------------------------------------  '''

''' NI MODULES
NI-DCPower (Python module: nidcpower)
NI-Digital Pattern Driver (Python module: nidigital)
NI-DMM (Python module: nidmm)
NI-FGEN (Python module: nifgen)
NI-ModInst (Python module: nimodinst)
NI-SCOPE (Python module: niscope)
NI Switch Executive (Python module: nise)
NI-SWITCH (Python module: niswitch)
NI-TClk (Python module: nitclk)
'''

class PXI_DMM:
    '''
    INCOMPLETE:
    - En caso de error hay que devolver un false
    - Hay que cerrar session con self.session.close
    - Al usar range=-1 lo configuramos en AUTO
    - Hay que buscar las opciones de NULL
    - Añadir espera o indicación al terminar el self test y el self cal
    '''
    def __init__(self, resource: str = ""):
        import nidmm
        self.session = nidmm.Session(resource)
        self.NMB_FUNCTIONS: tuple = (
            self.MEAS,
            self.CONFIG_VDC,
            self.CONFIG_VAC,
            self.CONFIG_RES_2W,
            self.CONFIG_RES_4W,
            self.CONFIG_IDC,
            self.CONFIG_IAC,
            self.CONFIG_FREQ,
            self.CONFIG_TEMP
        )
    
    def CLOSE(self) -> None:
        self.session.close()

    def DEVICE_INFO(self) -> str:
        '''
        Get info (Manufacturer, Model, Serial Id) about device
        '''
        MANUFACTURER = self.session.instrument_manufacturer
        MODEL = self.session.instrument_model
        SERIAL_NUMBER = self.session.serial_number
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn

    def SELF_TEST(self) -> None:
        self.session.self_test()

    def SELF_CAL(self) -> None:
        self.session.self_cal()

    def MEAS_INFO(self) -> str:
        '''
        Get info (Measure Function, Range, Digits) about config
        '''
        FUNCTION = self.session.function
        RANGE = self.session.range
        DIGITS = self.session.resolution_digits
        config = f"{FUNCTION}, {RANGE}, {DIGITS}"
        return config

    def MEAS(self, *args) -> float:
        measure = self.session.read()
        try:
            measure = float(measure)
            return measure
        except:
            print("MEAS ERROR / Float value")
            return 0.0  

    def CONFIG_VDC(self, *args) -> None:
        '''
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.DC_VOLTS,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )
    
    def CONFIG_VAC(self, *args) -> None:
        '''
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.AC_VOLTS,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )
    
    def CONFIG_RES_2W(self, *args) -> None:
        '''
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.TWO_WIRE_RES,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def CONFIG_RES_4W(self, *args) -> None:
        '''
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.FOUR_WIRE_RES,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def CONFIG_IDC(self, *args) -> None:
        '''
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.DC_CURRENT,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def CONFIG_IAC(self, *args) -> None:
        '''
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.AC_CURRENT,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def CONFIG_FREQ(self, *args) -> None:
        '''
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.FREQ,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def CONFIG_TEMP(self, *args) -> None:
        '''
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.TEMPERATURE,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

class PXI_DCPOWER:
    '''
    INCOMPLETE
    '''
    def __init__(self, resource: str = ""):
        import nidcpower
        self.session = nidcpower.Session(resource)
    
    def CLOSE(self) -> None:
        self.session.close()

    def DEVICE_INFO(self) -> str:
        '''
        Get info (Manufacturer, Model, Serial Id) about device
        '''
        MANUFACTURER = self.session.instrument_manufacturer
        MODEL = self.session.instrument_model
        SERIAL_NUMBER = self.session.serial_number
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn

class NI_VBENCH:
    '''
    INCOMPLETE
    '''
    def __init__(self, resource: str):
        from pyvirtualbench import PyVirtualBench, PyVirtualBenchException, Waveform
        self.virtualbench = PyVirtualBench(resource)
        self.fgen = self.virtualbench.acquire_function_generator()

    def DEVICE_INFO(self) -> str:
        '''
        INCOMPLETE
        '''
        MANUFACTURER = "NATIONAL INSTRUMENTS"
        MODEL = self.virtualbench.device_name
        SERIAL_NUMBER = ""
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn

    # def FGEN_ONOFF(self):
    #     self.fgen.run()
    #     self.fgen.

    def FGEN_SETUP(self,
                waveform_function: str,
                frequency: float, # Hz
                amplitude: float, # Vpp
                dc_offset: float, # V
                duty_cycle: float, # %
                ) -> None:
        '''
        waveform_function: DC / SINE / SQUARE / TRIANGLE
        frequency (Hz) / amplitude (Vpp) / dc_offset (V) / duty_cycle (%)
        '''
        if waveform_function == "DC":
            waveForm = Waveform.DC
        if waveform_function == "SINE":
            waveForm = Waveform.SINE
        if waveform_function == "SQUARE":
            waveForm = Waveform.SQUARE
        if waveform_function == "TRIANGLE":
            waveForm = Waveform.TRIANGLE
        self.fgen.configure_standard_waveform(waveForm, amplitude, dc_offset, frequency, duty_cycle)


''' SPECIAL INSTRUMENT
--------------------------------------------------------  '''

class FLKE_5XXX(VISA_INSTRUMENT):
    '''
    Especial functions for the device:
        - TYPE: CALIBRATOR
        - MANUFACTURER: FLUKE
        - MODEL: 5xxx
    '''
    def __init__(self, visa_resource=str, timeout: int = 10):
        super().__init__(visa_resource, timeout)
        self.WR("*CLS")
        IDN = self.RD("*IDN?; *WAI")
        MODEL = IDN.split(chr(44))[1]
        self.MODEL = None
        if MODEL[0:2] == "57":
            self.MODEL = "5700"
        if MODEL[0:2] == "55":
            self.MODEL = "5500"
        
        ## NMBv3 FUNCTIONS
        self.NMB_FUNCTIONS: tuple = (
            self.OPER,
            self.STBY,
            self.OUT_VPP,
            self.FOUR_WIRES
        )
    
    def DEVICE_INFO(self) -> str:
        self.WR("*CLS")
        IDN = self.RD("*IDN?; *WAI")
        IDNL = IDN.split(chr(44))
        MANUFACTURER = IDNL[0]
        MODEL = IDNL[1]
        SERIAL_NUMBER = IDNL[2]
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn
    
    def OPER(self, VALUE: str, UNIT: str) -> None:
        '''
        '''
        self.WR("*CLS")
        self.WR("ESE 1")
        self.WR("SRE 32")
        self.WR("OPER")
        self.OPC()

    def STBY(self, *args) -> None:
        '''
        '''
        self.WR("*CLS")
        self.WR("ESE 1")
        self.WR("SRE 32")
        self.WR("OUT 0 HZ")
        self.WR("OUT 0 V")
        self.WR("STBY")
        self.OPC()

    def OUT_VPP(self, *args):
        pass

    def FOUR_WIRES(self, *args) -> None:
        pass

class RS_SM(VISA_INSTRUMENT):
    '''
    Especial functions for the device:
        - TYPE: SIGNAL GENERATOR
        - MANUFACTURER: ROHDE & SCHWARZ
        - MODEL: SMx
    '''
    def __init__(self, visa_resource: str, timeout: int = 10):
        super().__init__(visa_resource, timeout)
        
        ## NMBv3 FUNCTIONS
        self.NMB_FUNCTIONS: tuple = (
            self.STBY,
            self.NRP_MEAS,
            self.NRP_ALC
        )
    
    def STBY(self, *args):
        self.WR("*CLS")
        self.WR("ESE 1")
        self.WR("SRE 32")
        self.WR("SOUR:POW -100 DBM")
        self.WR("OUTP:STAT OFF")
        self.OPC()
    
    def NRP_MEAS(self, *args):
        '''
        '''
        pass

    def NRP_ALC(self, *args):
        '''
        Set Power Level to Target Level in NRP
        ** Make sure the generator has a NRP connected and is identified as 1
        INCOMPLETE:
        '''
        # Chekear la sonda
        # Revisar el modelo
        # En caso de fallo llamar STBY
        pass

SPECIAL_INSTRUMENTS: tuple = (FLKE_5XXX, PXI_DMM)


''' TEST
--------------------------------------------------------  '''