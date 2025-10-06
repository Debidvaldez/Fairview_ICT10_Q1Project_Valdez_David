from js import document

def calculate_total(e):
    name = document.getElementById("name").value

    # prices
    chawan_price = 1700
    chasen_price = 650
    chashaku_price = 310
    sifter_price = 60
    stand_price = 700
    matcha_price = 800

    # checkboxes
    chawan_box = document.getElementById("chawan")
    chasen_box = document.getElementById("chasen")
    chashaku_box = document.getElementById("chashaku")
    sifter_box = document.getElementById("sifter")
    stand_box = document.getElementById("stand")
    matcha_box = document.getElementById("matcha")

    # quantities
    chawan_qty = int(document.getElementById("chawan_qty").value)
    chasen_qty = int(document.getElementById("chasen_qty").value)
    chashaku_qty = int(document.getElementById("chashaku_qty").value)
    sifter_qty = int(document.getElementById("sifter_qty").value)
    stand_qty = int(document.getElementById("stand_qty").value)
    matcha_qty = int(document.getElementById("matcha_qty").value)

    # total math
    total = (
        chawan_price * chawan_qty * int(chawan_box.checked) +
        chasen_price * chasen_qty * int(chasen_box.checked) +
        chashaku_price * chashaku_qty * int(chashaku_box.checked) +
        sifter_price * sifter_qty * int(sifter_box.checked) +
        stand_price * stand_qty * int(stand_box.checked) +
        matcha_price * matcha_qty * int(matcha_box.checked)
    )

    message = "Thank you " + (name or "Customer") + "! Your total is ₱" + str(total)
    document.getElementById("summary").innerText = message