import pyvisa

rm = pyvisa.ResourceManager("@py")      # force pure-Python backend
# print("Back-end:", rm)
# print("Resources:", rm.list_resources())

for res in rm.list_resources():
    inst = rm.open_resource(res)
    inst.timeout = 5000
    inst.write_termination = '\n'
    inst.read_termination  = '\n'
    print(f"{res} → {inst.query('*IDN?').strip()}")

