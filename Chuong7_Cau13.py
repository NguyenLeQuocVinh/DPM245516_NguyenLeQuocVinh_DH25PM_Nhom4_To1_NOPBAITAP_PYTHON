import xml.etree.ElementTree as ET

# ============================================
# ĐỌC DANH SÁCH NHÓM THIẾT BỊ
# ============================================
def load_groups(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    groups = []
    for nhom in root.findall("nhom"):
        ma = nhom.find("ma").text
        ten = nhom.find("ten").text
        groups.append({"ma": ma, "ten": ten})

    return groups


# ============================================
# ĐỌC DANH SÁCH THIẾT BỊ
# ============================================
def load_devices(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    devices = []
    for tb in root.findall("thietbi"):
        manhom = tb.attrib.get("manhom")
        ma = tb.find("ma").text
        ten = tb.find("ten").text
        devices.append({"ma": ma, "ten": ten, "manhom": manhom})

    return devices


# ============================================
# LƯU LẠI FILE THIẾT BỊ
# ============================================
def save_devices(filename, devices):
    root = ET.Element("thietbis")

    for d in devices:
        tb = ET.SubElement(root, "thietbi")
        tb.set("manhom", d["manhom"])

        ma = ET.SubElement(tb, "ma")
        ma.text = d["ma"]

        ten = ET.SubElement(tb, "ten")
        ten.text = d["ten"]

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


# ============================================
# HIỂN THỊ DANH SÁCH THIẾT BỊ
# ============================================
def list_devices(devices):
    print("\n=== DANH SÁCH THIẾT BỊ ===")
    for d in devices:
        print(f"Mã: {d['ma']} - Tên: {d['ten']} - Nhóm: {d['manhom']}")


# ============================================
# THÊM THIẾT BỊ
# ============================================
def add_device(devices, ma, ten, manhom):
    devices.append({"ma": ma, "ten": ten, "manhom": manhom})


# ============================================
# SỬA THIẾT BỊ
# ============================================
def update_device(devices, ma, new_ten=None, new_manhom=None):
    for d in devices:
        if d["ma"] == ma:
            if new_ten:
                d["ten"] = new_ten
            if new_manhom:
                d["manhom"] = new_manhom
            return True
    return False


# ============================================
# XÓA THIẾT BỊ
# ============================================
def remove_device(devices, ma):
    for d in devices:
        if d["ma"] == ma:
            devices.remove(d)
            return True
    return False


# ============================================
# CHẠY THỬ
# ============================================
if __name__ == "__main__":
    groups = load_groups("nhomthietbi.xml")
    devices = load_devices("ThietBi.xml")

    print("Danh sách nhóm:")
    print(groups)

    list_devices(devices)

    print("\n--- Thêm thiết bị mới ---")
    add_device(devices, "tb10", "Thiết bị 10", "n2")

    print("\n--- Cập nhật thiết bị tb2 ---")
    update_device(devices, "tb2", new_ten="Thiết bị 2 (Updated)", new_manhom="n3")

    print("\n--- Xóa thiết bị tb4 ---")
    remove_device(devices, "tb4")

    list_devices(devices)

    save_devices("ThietBi.xml", devices)
