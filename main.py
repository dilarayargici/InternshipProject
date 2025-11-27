from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pymodbus.client import ModbusTcpClient
import struct
import random

app = FastAPI()

# CORS - JS için gerekli
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Statik dosya (HTML, JS, CSS) sun
app.mount("/static", StaticFiles(directory="static"), name="static")

# Anasayfa
@app.get("/")
def get_index():
    return FileResponse("static/index.html")

def registers_to_float_cdab(registers):
    raw = struct.pack('>HH', registers[0], registers[1])
    return struct.unpack('>f', raw)[0]

# Örnek: Modbus’tan veri al (senin IP'ye bağlanmak için düzenlenebilir)
def get_modbus_value(register):
    try:
        client = ModbusTcpClient("78.187.240.91", port=6666)
        client.connect()
        rsp = client.read_holding_registers(address=register, count=2, slave=1)
        client.close()
        if rsp.isError():
            return None
        return round(registers_to_float_cdab(rsp.registers), 2)
    except:
        return None

# API endpoint
@app.get("/api/veri")
def get_veri():
    # Şu anda test verileriyle
    santraller = {
        "daghan": {
            "tip": "RES",
            "anlik_guc": get_modbus_value(1112) or random.uniform(-10, 0),
            "gunluk_uretim": random.uniform(0.6, 0.8),
        },
        "yatmahan": {
            "tip": "RES",
            "anlik_guc": get_modbus_value(1012) or random.uniform(-20, 0),
            "gunluk_uretim": random.uniform(0.8, 1.0),
        },
        "turkmenhan": {
            "tip": "GES",
            "anlik_guc": get_modbus_value(1062) or random.uniform(-500, -300),
            "gunluk_uretim": random.uniform(0.5, 0.7),
        },
        "yasemin": {
            "tip": "GES",
            "anlik_guc": get_modbus_value(1162) or random.uniform(-300, -100),
            "gunluk_uretim": random.uniform(0.4, 0.6),
        },
    }

    toplam_guc = sum([s["anlik_guc"] for s in santraller.values()])
    toplam_uretim = sum([s["gunluk_uretim"] for s in santraller.values()])

    return {
        "toplam_aktif_guc": round(toplam_guc, 1),
        "toplam_uretim": round(toplam_uretim, 2),
        "santraller": santraller
    }
