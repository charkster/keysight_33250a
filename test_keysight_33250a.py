import pyvisa

rm = pyvisa.ResourceManager()
# print(rm.list_resources())
arb = keysight_33250a(rm.open_resource('USB0::0x0917::0x0428::MY440474A5::INSTR'))
#arb.k33250a.write('*RST')
time.sleep(2)
# get_unique_scpi_list is a list of SCPI commands which are different from Power-On values
print(arb.get_unique_scpi_list())
